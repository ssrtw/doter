from github import CMD, Github


class RIPGREP(Github):
    owner = "BurntSushi"
    repo = "ripgrep"
    exec_name = "rg"

    @property
    def file_name(self) -> str:
        return f"ripgrep-{self.version}-x86_64-unknown-linux-musl.tar.gz"

    def install(self) -> bool:
        cmd = CMD(self.tmp_path)
        tmp_file_path = self.tmp_path / self.file_name
        # download
        print("download")
        cmd(f"wget {self.file_url} -O {tmp_file_path}")
        # setup
        print("setup")
        extract_file = "ripgrep-14.1.0-x86_64-unknown-linux-musl/rg"
        exec_name = "rg"
        cmd(
            f"tar zxf {self.file_name} {extract_file}; mv {extract_file} ~/.local/bin/{exec_name}"
        )
        # clear
        print("clear")
        cmd(f"rm -rf /tmp/{self.owner}")
