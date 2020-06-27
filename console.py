#!/usr/bin/python3
""" In this module CMD is implement """


import cmd


class HBNBCommand(cmd.Cmd):
    """ This is the command interpreter """

    prompt = "(hbnb)"

    def do_quit(self, line):
        """ This command send quit signal"""
        return True

    def do_EOF(self, line):
        """ This command send quit signal"""
        return True

    def emptyline(self):
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
