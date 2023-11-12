#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """interactive cmd class"""

    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit the cmd"""
        return True

    def do_EOF(self, arg):
        """Exits the cmd"""
        print("")
        return True

    def emptyline(self):
        """an empty line + ENTER shouldn’t execute anything"""
        pass

    def help_quit(self):
        """"help message"""
        print("Quit command to exit the program\n")

    def help_EOF(self):
        """help message"""
        print("EOF command to exit the program\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
