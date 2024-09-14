import socket
import logging
import sys
import os


class Colors:
    reset = "\033[0m"
    bold = "\033[01m"
    disable = "\033[02m"
    underline = "\033[04m"
    reverse = "\033[07m"
    strikethrough = "\033[09m"
    invisible = "\033[08m"

    class Foreground:
        black = "\033[30m"
        red = "\033[31m"
        green = "\033[32m"
        orange = "\033[33m"
        blue = "\033[34m"
        purple = "\033[35m"
        cyan = "\033[36m"
        light_grey = "\033[37m"
        dark_grey = "\033[90m"
        light_red = "\033[91m"
        light_green = "\033[92m"
        yellow = "\033[93m"
        light_blue = "\033[94m"
        pink = "\033[95m"
        light_cyan = "\033[96m"

    class Background:
        black = "\033[40m"
        red = "\033[41m"
        green = "\033[42m"
        orange = "\033[43m"
        blue = "\033[44m"
        purple = "\033[45m"
        cyan = "\033[46m"
        light_grey = "\033[47m"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def set_title(title):
    try:
        if os.name == "nt":
            os.system(f"title {title}")
        else:
            os.system(f'echo -ne "\\033]0;{title}\\007"')
    except Exception as e:
        print(f"Error setting title: {e}")


def print_banner():
    print(f"""             {Colors.Foreground.dark_grey}/\  """)
    print(
        f""" /{Colors.Foreground.yellow}vvvvvvvvvvvv{Colors.Foreground.dark_grey} \{Colors.Foreground.light_grey}--------------------{Colors.Foreground.light_red}--------{Colors.Foreground.red}----------, """
    )
    print(
        f""" {Colors.Foreground.dark_grey}`{Colors.Foreground.yellow}^^^^^^^^^^^^{Colors.Foreground.dark_grey} /{Colors.Foreground.light_grey}============={Colors.Foreground.red}=========={Colors.Foreground.red}==============/  """
    )
    print(f"             {Colors.Foreground.dark_grey}\/{Colors.reset}")


def get_integer_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter an integer.")

def main():
    while True:
        try:
            user_input = input(">>> ")
        except KeyboardInterrupt:
            sys.exit()

        if user_input == "help":
            print(help_menu)

        elif user_input == "clear":
            clear()

        elif user_input.startswith("cmd"):
            command = user_input[4:].strip()
            os.system(command)

        elif user_input == "1":
            ip = input("\nIP: ")
            port = get_integer_input("Port: ")


if __name__ == "__main__":
    help_menu = """

"""

    clear()
    set_title("S0cket - @batuafk")
    print_banner()
    main()
    os.system("pause")
