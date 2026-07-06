import sys

from . import __version__
from .config import ConfigManager


def banner():
    print()
    print("🎬 Welcome to RealReel")
    print("=" * 50)
    print(f"Version : {__version__}")
    print()


def help_menu():
    print("Available Commands")
    print("------------------")
    print("create")
    print("open")
    print("analyze")
    print("build")
    print("render")
    print("export")
    print("profile")
    print("config")
    print()


def show_config():

    config = ConfigManager().load()

    print("Engine Configuration")
    print("--------------------")
    print(config.data)


def main():

    banner()

    if len(sys.argv) == 1:
        help_menu()
        return

    command = sys.argv[1].lower()

    if command == "config":
        show_config()
        return

    print(f"🚧 '{command}' is not implemented yet.")


if __name__ == "__main__":
    main()