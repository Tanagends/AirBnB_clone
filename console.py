#!/usr/bin/python3
"""Module for the console"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """Class for the console"""

    prompt = "(hbnb) "

    def emptyline(self):
        """reprompts when user press Enter on an empty line"""
        pass

    def do_quit(self, line):
        """quit to exit the cmd loop"""
        return True

    def do_EOF(self, line):
        """Control D to successfully exit loop"""
        print()
        return True

    def do_create(self, line):
        """Creates new instance of BaseModel, saves it to JSON
        and prints its id"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        try:
            new_base_model = eval(args[0])()
        except NameError:
            print("** class doesn't exist **")
            return

        new_base_model.save()
        print(new_base_model.id)

    def do_show(self, line):
        """Prints the string representation of an instance based on the class name and id"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        try:
            if not isinstance(eval(args[0])(), object):
                raise NameError
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            print(storage.__objects[args[0] + "." + args[1]])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and ID"""
        args = line.split()

        if not args:
            print("** class name missing **")
            return

        try:
            if not isinstance(eval(args[0])(), object):
                raise NameError
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            del storage.__objects[args[0] + "." + args[1]]
            storage.save()
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances based or not on the class name"""
        args = line.split()

        if args:
            try:
                if not isinstance(eval(args[0])(), object):
                    raise NameError
            except NameError:
                print("** class doesn't exist **")
                return

            for obj in storage.all().values():
                if obj.__class__.__name__ == args[0]:
                    print(obj)
        else:
            for obj in storage.all().values():
                print(obj)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding or updating attribute"""
        args = line.split()

        if len(args) < 4:
            print("** missing arguments **")
            return

        try:
            if not isinstance(eval(args[0])(), object):
                raise NameError
        except NameError:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        try:
            instance = storage.__objects[args[0] + "." + args[1]]
        except KeyError:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        try:
            setattr(instance, args[2], eval(args[3]))
            instance.save()
        except Exception:
            print("** invalid value **")
