#!/usr/bin/python3
"""
This module provides a command line interface for the HBNB application.

It defines a class HBNBCommand that inherits from cmd.Cmd to interact with the
HBNB application via a command prompt. The interface includes commands for
quitting and handling empty inputs.
"""

import cmd

class HBNBCommand(cmd.Cmd):
    """
    A command processor class for the HBNB application.

    This class provides specific command methods to interact with the HBNB
    application through a command-line interface.
    """

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Exit the program.

        Args:
            arg: Command line arguments passed to 'quit' (unused).

        Returns:
            bool: True to signal the program to exit.
        """
        return True

    def do_EOF(self, arg):
        """
        Exit the program when receiving the EOF signal (Ctrl-D).

        Args:
            arg: Command line arguments passed to EOF (unused).

        Returns:
            bool: True to signal the program to exit.
        """
        return True

    def emptyline(self):
        """
        Do nothing on empty input line.

        Overrides the default behavior of repeating the last nonempty command.

        Returns:
            bool: False to indicate no action should be taken.
        """
        return False

if __name__ == '__main__':
    HBNBCommand().cmdloop()
