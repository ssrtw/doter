from github import CMD, Github


class DUF(Github):
    owner = "muesli"
    repo = "duf"

    @property
    def file_name(self) -> str:
        return f"duf_{self.version[1:]}_linux_x86_64.tar.gz"

    def install(self) -> bool:
        cmd = CMD(self.tmp_path)
        tmp_file_path = self.tmp_path / self.file_name
        # download
        print("download")
        cmd(f"wget {self.file_url} -O {tmp_file_path}")
        # setup
        print("setup")
        extract_file = "duf"
        exec_name = "duf"
        cmd(
            f"tar zxf {self.file_name} {extract_file}; mv {extract_file} ~/.local/bin/{exec_name}"
        )
        # clear
        print("clear")
        cmd(f"rm -rf /tmp/{self.owner}")
