from duf.install import DUF
from fzf.install import FZF
from ripgrep.install import RIPGREP

tool_classes = [FZF, RIPGREP, DUF]

if __name__ == "__main__":
    for tool_class in tool_classes:
        tool_class().run()
