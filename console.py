#!/usr/bin/python3
"""console"""
import cmd


class HBNBCommand(cmd.Cmd):
    """cmd class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting the program.")
        return True

    def help_quit(self):
        """Help for the quit command.
        
        Usage: quit
        
        This command exits the program.
        """
        print("Type 'quit' to exit the program.")

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl-D)."""
        print("\nExiting the program.")
        return True

    def help_EOF(self):
        """Help for EOF.
        
        This command exits the program when Ctrl-D is pressed.
        """
        print("Press Ctrl-D to exit the program.")

    def emptyline(self):
        """Do nothing on empty line."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
