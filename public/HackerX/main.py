from animation import *
from package_installer import *
from menu.main_menu import *

def main():
    start_tool_animation1("HackX")

    start_tool_animation2(
        "================================================================================\n"
        "                         installing packages\n"
        "================================================================================"
    )
    install_packages()
    main_menu()


if __name__ == "__main__":
    main()