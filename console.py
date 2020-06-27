#!/usr/bin/python3
""" In this module CMD is implement """


import cmd
from models import storage
from shlex import split
from models.base_model import BaseModel


classes = {'BaseModel': BaseModel}


class HBNBCommand(cmd.Cmd):
    """ This is the command interpreter """

    prompt = "(hbnb) "

    def do_quit(self, line):
        """ This command send quit signal"""
        return True

    def do_EOF(self, line):
        """ This command send quit signal"""
        return True

    def emptyline(self):
        pass

    def do_create(self, arg):
        """ Creates a new instance of BaseModel """
        args = split(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            instance = classes.get(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, arg):
        """ Print the str of an instance """
        args = split(arg)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0] and instance.id == args[1]:
                    print(instance.__str__())
                    return
            print("** no instance found **")

    def do_destroy(self, args):
        """ Destoy a instance of BaseModel """
        args = split(args)
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0] and instance.id == args[1]:
                    del(instance)
                    storage.save()
                    return
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
