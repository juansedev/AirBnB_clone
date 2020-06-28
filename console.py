#!/usr/bin/python3
""" In this module CMD is implement """


import cmd
from models import storage
from models.engine.file_storage import FileStorage
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
                    del(storage.all()[key])
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints str representation of instances """
        args = split(arg)
        if args == []:
            pass
        elif args[0] not in classes:
            print("** class doesn't exist **")
        else:
            storage.reload()
            inst_list = []
            for key, instance in storage.all().items():
                if instance.__class__.__name__ == args[0]:
                    inst_list.append(instance.__str__())
            print(inst_list)

    def do_update(self, arg):
        """ Update an instance baed on the class name
        and id by adding or updating attribute
        """
        args = split(arg)
        inst_list = storage.all()
        if args == []:
            print("** class name missing **")
        elif args[0] not in classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            storage.reload()
            for key, instance in inst_list.items():
                if instance.__class__.__name__ == args[0] and instance.id == args[1]:
                    if  len(args) == 2:
                        print("** attribute name missing **")
                        return
                    elif len(args) == 3:
                        print("** value missing **")
                        return
                    else:
                        key_object = args[0] + "." + args[1]
                        print(key_object)
                        object = inst_list[key_object]
                        print("-> {}".format(inst_list[key_object]))
                        setattr(object, args[2], args[3])
                        object.save()
                        return
            print("** no instance found **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
