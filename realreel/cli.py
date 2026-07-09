import sys
from pathlib import Path

from . import __version__
from .config import ConfigManager
from .core.brief_parser import BriefParser
from .core.validator import ProjectValidator
from .core.director import CreativeDirector
from .core.production_planner import ProductionPlanner


def banner():
    print()
    print("🎬 Welcome to RealReel")
    print("=" * 50)
    print(f"Version : {__version__}")
    print()


def help_menu():
    print("Available Commands")
    print("------------------")
    print("config")
    print("plan <project_folder>")
    print()


def show_config():
    config = ConfigManager().load()

    print("Engine Configuration")
    print("--------------------")
    print(config.data)


def plan_project(project_folder):

    project_folder = Path(project_folder)

    production_file = project_folder / "brief.md"

    if not production_file.exists():
        print(f"❌ File not found: {production_file}")
        return

    print("📖 Reading production...")
    project = BriefParser().parse(production_file)
    print("✅ Done")

    print("🔍 Validating project...")
    ProjectValidator().validate(project)
    print("✅ Done")

    print("🎬 Creating story...")
    project = CreativeDirector().create_story(project)
    print("✅ Done")

    print("📝 Building production plan...")
    output_file = project_folder / "production.json"
    ProductionPlanner().build(project, output_file)
    print("✅ Done")

    print()
    print(f"📁 Saved: {output_file}")
    print()
    print("🎉 Production planning completed successfully.")


def main():

    banner()

    if len(sys.argv) == 1:
        help_menu()
        return

    command = sys.argv[1].lower()

    if command == "config":
        show_config()
        return

    elif command == "plan":

        if len(sys.argv) < 3:
            print("Usage:")
            print("python -m realreel plan <project_folder>")
            return

        plan_project(sys.argv[2])
        return

    print(f"🚧 '{command}' is not implemented yet.")


if __name__ == "__main__":
    main()
    