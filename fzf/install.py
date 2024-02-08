from github import CMD, Github


class FZF(Github):
    owner = "junegunn"
    repo = "fzf"

    @property
    def file_name(self) -> str:
        return f"fzf-{self.version}-linux_amd64.tar.gz"

    def install(self) -> bool:
        cmd = CMD(self.tmp_path)
        tmp_file_path = self.tmp_path / self.file_name
        # download
        print("download")
        cmd(f"wget {self.file_url} -O {tmp_file_path}")
        # setup
        print("setup")
        extract_file = "fzf"
        exec_name = "fzf"
        cmd(f"tar zxf {self.file_name} fzf; mv {extract_file} ~/.local/bin/{exec_name}")
        # clear
        print("clear")
        cmd(f"rm -rf /tmp/{self.owner}")
