#!/usr/bin/python3
"""
Contains the entry point of my command interpreter
"""


import cmd
import json
import models
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import sys


class HBNBCommand(cmd.Cmd):
    """Contains the implementation of the interpreter"""
    prompt = "(hbnb) "
    __file_path = "file.json"
    objects = models.storage.all()

    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place", "Review"]

    def do_EOF(self, line):
        """Method for quit the console"""
        return True

    def help_EOF(self):
        """Message when asking what EOF do"""
        print('\n'.join([
            "Quit command to exit the program",
            "\n"
        ]))

    def do_quit(self, line):
        """Method for quit the console"""
        return True

    def help_quit(self):
        """Message when asking what quit do"""
        print('\n'.join([
            "Quit command to exit the program",
            "\n"
        ]))

    def emptyline(self):
        """Method for an empty line"""
        pass

    def default(self, args):
        """Reports an error

        Args:
            Any unknown command
        """
        print("*** Unknown syntax:", args)

    def do_create(self, args):
        """Creates a new instance

        Args:
        create <class name>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
        else:
            new_obj = eval(args[0] + "()")
            new_obj.save()
            print(new_obj.id)

    def do_show(self, args):
        """Prints the string representation of an instance

        Args:
        show <class name> <id>
        """
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
        elif (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            if key in HBNBCommand.objects.keys():
                print(HBNBCommand.objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """Delete of an instance

        Args:
        destroy <class name> <id>
        """
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif (args[0] not in HBNBCommand.classes):
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            key = '{}.{}'.format(args[0], args[1])
            if key in HBNBCommand.objects.keys():
                HBNBCommand.objects.pop(key)
                models.storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """ Print all string representation of all instances

        Args:
        all
        all <class name>
        """
        args = args.split()
        list_obj = []
        if len(args) != 0:
            if args[0] not in self.classes:
                print("** class doesn't exist **")
            else:
                for obj in HBNBCommand.objects.values():
                    list_obj.append(obj.__str__())
                print(list_obj)
        else:
            for obj in HBNBCommand.objects.values():
                list_obj.append(obj.__str__())
            print(list_obj)

    def do_update(self, args):
        """Updates an instance and save into JSON file

        Args:
        <class name> <id> <attribute name> <attribute value>"""
        args = args.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] in self.classes:
            if len(args) > 1:
                key = args[0] + "." + args[1]
                if key in self.objects:
                    if len(args) > 2:
                        if len(args) > 3:
                            setattr(self.objects[key], args[2], args[3])
                            self.objects[key].save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
