import abc
import subprocess
from pathlib import Path

import requests


class CMD:
    def __init__(self, cwd: Path):
        self.cwd = cwd

    def __call__(self, cmd: str):
        subprocess.run(
            cmd,
            shell=True,
            check=True,
            text=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            cwd=self.cwd,
        )


class Github(metaclass=abc.ABCMeta):
    owner: str
    repo: str

    def __init__(self) -> None:
        self.tmp_path = Path(f"/tmp/{self.owner}/{self.repo}")
        self.api_url = (
            f"https://api.github.com/repos/{self.owner}/{self.repo}/releases/latest"
        )

    def need_update(self) -> bool:
        ver_path = Path(f"{self.repo}/version")
        if ver_path.exists():
            curr_ver = ver_path.read_text()
            return curr_ver != self.version
        else:
            with ver_path.open("w") as ver_file:
                ver_file.write(self.version)
            return False

    def get_version(self):
        info = requests.get(self.api_url).json()
        self.version = info["tag_name"]

    @abc.abstractproperty
    def file_name(self) -> str:
        return NotImplemented

    @property
    def file_url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}/releases/download/{self.version}/{self.file_name}"

    def setup(self, force=True) -> bool:
        self.get_version()
        check = self.need_update() or force
        if check:
            self.tmp_path.mkdir(parents=True, exist_ok=True)
        return check

    @abc.abstractmethod
    def install(self): ...

    def run(self, force: bool = False):
        if self.setup(force):
            self.install()
