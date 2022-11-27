#!/usr/bin/python3
"""Contains the entry point of the command interpreter."""

import cmd
import shlex
import sys
from models import storage


class HBNBCommand(cmd.Cmd):
    """Contains the entry point of the command interpreter."""

    prompt = '(hbnb) '
    command = ["all(", "count(", "show(", "destroy(", "update("]
    # classes = {
    #   'BaseModel': BaseModel,
    #   'User': User
    # }

    def classes(self):
        """Returns a dictionary containing class instance."""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
        }
        return classes

    def splitter(self, arg):
        """Splits a string using shlex."""
        splitter = shlex.shlex(arg, posix=True)
        splitter.whitespace += ','
        splitter.whitespace_split = True
        return list(splitter)

    def dict_update(self, line):
        if "update" in line:
            if "update(" in line:
                cls_name, rem = line.split(".")
                line = rem.strip("update(").strip(")")
                start = line.find("{")
                dicts = eval(line[start:])
                line = line[:start]
                uid = self.splitter(line)[0]
                for key, value in dicts.items():
                    line = f"update {cls_name} {uid} {key} \"{value}\""
                    cmd.Cmd.onecmd(self, line)
            else:
                start = line.find("{")
                dicts = eval(line[start:])
                line = line[:start]
                rem = line.split()
                for key, value in dicts.items():
                    line = f"update {rem[1]} {rem[2]} {key} \"{value}\""
                    cmd.Cmd.onecmd(self, line)

    def onecmd(self, line):
        start = line.find("}")
        if start != -1:
            self.dict_update(line)
            return

        for commd in HBNBCommand.command:
            if commd in line:
                name, rem = line.split(".")
                line = rem.strip(")")
                cmmd, arg = line.split("(")

                splitter = self.splitter(arg)
                if cmmd == "count":
                    self.count(name)
                    return
                elif cmmd == "update":
                    if len(splitter) == 3:
                        splitter[2] = "\"" + splitter[2] + "\""

                line = "{} {}".format(cmmd, name)

                if splitter != []:
                    line += " "
                    line += ' '.join(splitter)
        return cmd.Cmd.onecmd(self, line)

    def count(self, class_name):
        """retrieve the number of instances of a class."""
        objs = storage.all()
        count = 0

        for key in objs.keys():
            if class_name in key:
                count += 1
        print(count)

    def do_quit(self, stdin):
        """Quit command to exit the program."""
        sys.exit()

    def do_EOF(self, stdin):
        """EOF command to exit the program."""
        sys.exit()

    def do_create(self, stdin):
        """Usage: create <class>\
                Create a new class instance and print its id."""
        if stdin == "":
            print("** class name missing **")
        elif stdin not in self.classes().keys():
            print("** class doesn't exist **")
        else:
            obj = self.classes()[stdin]()
            storage.new(obj)
            storage.save()
            print(obj.id)

    def do_show(self, stdin):
        """Usage: show <class> <id> or <class>.show(<id>)\
            Display the string representation of a class instance of\
        a given id."""
        if stdin == "":
            print("** class name missing **")
            return

        objs = storage.all()
        key = ""
        name = stdin.split()

        if name[0] not in self.classes().keys():
            print("** class doesn't exist **")
            return
        if len(name) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(name[0], name[1])

        try:
            print(objs[key])
        except KeyError:
            print("** no instance found **")

    def do_update(self, stdin):
        """Usage: update <class> <id> <attribute_name> <attribute_value> or\
        <class>.update(<id>, <attribute_name>, <attribute_value">) or\
        <class>.update(<id>, <dictionary>)\
        Update a class instance of a given id by adding or updating\
        a given attribute key/value pair or dictionary."""
        my_stdin = shlex.split(stdin)
        lent = len(my_stdin)
        key = ""
        objs = storage.all()
        obj = ""
        for i in range(len(my_stdin)):
            if i == 0:
                if my_stdin[0] not in self.classes().keys():
                    print("** class doesn't exist **")
                    return
            elif i == 1:
                key = "{}.{}".format(my_stdin[0], my_stdin[1])
                try:
                    obj = objs[key]
                except KeyError:
                    print("** no instance found **")
                    return

        if lent == 0:
            print("** class name missing **")
        elif lent == 1:
            print("** instance id missing **")
        elif lent == 2:
            print("** attribute name missing **")
        elif lent == 3:
            print("** value missing **")
        else:
            name, uid, attr = my_stdin[0], my_stdin[1], my_stdin[2]
            try:
                value = my_stdin[3]
                if type(getattr(obj, attr)) == int:
                    value = int(my_stdin[3])
                elif type(getattr(obj, attr)) == float:
                    value = float(my_stdin[3])
            except AttributeError:
                pass

            setattr(obj, attr, value)
            obj.save()

    def do_destroy(self, stdin):
        """Usage: destroy <class> <id> or <class>.destroy(<id>)\
                Deletes an instance based on the class name and id."""
        if stdin == "":
            print("** class name missing **")
            return

        name = stdin.split()
        if name[0] not in self.classes().keys():
            print("** class doesn't exist **")
            return
        if len(name) < 2:
            print("** instance id missing **")
            return

        objs = storage.all()
        key = "{}.{}".format(name[0], name[1])

        try:
            del(objs[key])
        except KeyError:
            print("** no instance found **")

    def do_all(self, stdin):
        """Usage: all or all <class> or <class>.all()\
        Display string representations of all instances of a given class.\
        If no class is specified, displays all instantiated objects."""
        lis_objs = []
        objs = storage.all()

        if stdin == "":
            lis_objs = [str(obj) for obj in objs.values()]
        elif stdin in self.classes().keys():
            lis_objs = [str(obj) for key, obj in objs.items() if stdin in key]
        else:
            print("** class doesn't exist **")
            return

        print(str(lis_objs))

    def emptyline(self):
        """Emptyline"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
