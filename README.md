<p align="center">
  <img src="https://github.com/llanojs/Readme_template/blob/master/images/hbnb.png"/>
 <h1 align="center">0x00. AirBnB clone - The console</h1>
 <br>
 <p align="center">
    <a href="https://github.com/emmanavarro/AirBnB_clone/commits/master">
        <img alt="commit_activity" src="https://img.shields.io/github/commit-activity/y/emmanavarro/AirBnB_clone?style=plastic" target="_blank" />
    </a>
    <a href="https://github.com/emmanavarro/AirBnB_clone/graphs/contributors">
        <img alt="contributors" src="https://img.shields.io/github/contributors/emmanavarro/AirBnB_clone?style=plastic" target="_blank" />
    </a>
    <a href="https://github.com/emmanavarro/AirBnB_clone" target="_blank">
      <img alt="code-size" src="https://img.shields.io/github/languages/code-size/emmanavarro/AirBnB_clone?style=plastic" />
    </a>
    <a href="https://github.com/emmanavarro/AirBnB_clone" target="_blank">
      <img alt="Documentation" src="https://img.shields.io/badge/documentation-yes-brightgreen.svg" />
    </a>
 </p>
</p>

---
# Description of the project
This is a website clone of AirBnB, with the fundamental features implemented. It has a front-end, a database, an API for the front-end to database communication, and a developer command line interface.

The command line interface allows the use of CRUD operations on the data objects in the database, as well as special operations like counting, computing stats, etc.

# Classes

## Classes Table

N°|File|Description
---|---|---
1|[README.md](./README.md)|Readme.
2|[0-bubble_sort.c](./0-bubble_sort.c)|Bubble Sort Algorithm
3|[0-O](./0-O)|Big O notations of the time complexity of the Bubble Sort Algorithm
4|[1-insertion_sort_list.c](./1-insertion_sort_list.c)|Insertion Sort Algorithm
5|[1-O](./1-O)|Big O notations of the time complexity of the Insertion Sort Algorithm
6|[2-selection_sort.c](./2-selection_sort.c)|Selection Sort Algorithm
7|[2-O](./2-O)|Big O notations of the time complexity of the Selection Sort Algorithm
8|[3-quick_sort.c](./3-quick_sort.c)|Quick Sort Algorithm
9|[3-O](./3-O)|Big O notations of the time complexity of the Quick Sort Algorithm

## Storage

The above classes are handled by the abstracted storage engine defined in the FileStorage class.

Every time the backend is initialized, HBnB instantiates an instance of FileStorage called storage. The storage object is loaded/re-loaded from any class instances stored in the JSON file, file.json. As class instances are created, updated, or deleted, the storage object is used to register corresponding changes in the file.json.

# The command interpreter

The console is a command line interpreter that permits management of the backend of HBnB. It can be used to handle and manipulate all classes utilized by the application (achieved by calls on the storage object defined above).

__Functionalities of this command interpreter__

* Create a new object (ex: a new User or a new Place).
* Retrieve an object from a file, a database etc…
* Do operations on objects (count, compute stats, etc…).
* Update attributes of an object.
* Destroy an object.


## Command table

N°|Command|Description
---|---|---
1|`create <class name>`|Create an instance of the class and saves it to a JSON file.
2|`show <class name> <object id>` or `<class name>.show(<id>)`|Prints the string represenation of an instance based on the class name and its id.
3|`destroy <class name> <object id>` or `<class name>.destroy(<id>)`|Deletes an instance for the class name and its id.
4|`all` or `all <class name>` or `<class name>.all()`|Prints all the string representations of all the instances.
5|`update <class name> <id> <attribute name> "<attribute value>"` or `<class name>.update(<id>, <attribute name>, <attribute value>)`|Updates an instance based on the class name and id.
6|`<class name>.count()`|Retrieves the number of instances of a class.
7|`quit` or `EOF`|Exits the console.
7|`help` or `help <command>`|Lists all the commands.


## How to start it

* Create your data model.
* Manage (create, update, destroy, etc) objects via a console / command interpreter.
* Store and persist objects to a file (JSON file).

The first piece is to manipulate a powerful storage system. This storage engine will give us an abstraction between “My object” and “How they are stored and persisted”. This means: from your console code (the command interpreter itself) and from the front-end and RestAPI you will build later, you won’t have to pay attention (take care) of how your objects are stored.

This abstraction will also allow you to change the type of storage easily without updating all of your codebase.

The console will be a tool to validate this storage engine.

<p align="center">
  <img src="https://github.com/llanojs/Readme_template/blob/master/images/console_hbnb.png"/>
</p>

## How to use it

### Download:
Clone the repository in the command line interface:
```
git clone https://github.com/emmanavarro/AirBnB_clone.git
```
### Execution:

The HolbertonBnB console can be run both interactively and non-interactively. To run the console in non-interactive mode, pipe any command(s) into an execution of the file [console.py](./console.py) at the command line.

Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

In non-interactive mode:
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
$
```

## Examples
COMPLEMENTAR CON DESCRIPCIÓN Y LOS GIFS ;)

---


<p align="center">
    <h2 align="center">By:</h2>
    <h2 align="center">Emma Navarro Millán</h2>
      <p align="center">
        <a href="https://twitter.com/Ayy_Emma" target="_blank">
            <img alt="twitter_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/twitter.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
        <a href="https://www.linkedin.com/in/emmanavarromillan/" target="_blank">
            <img alt="linkedin_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/linkedin.png" style="float: center; margin-right: 10px" height="50"  width="50">
        </a>
        <a href="https://medium.com/@elnavarro55" target="_blank">
            <img alt="medium_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/medium.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
      </p>
    <h2 align="center">Juan Sebastian Llano Gallego</h2>
      <p align="center">
        <a href="https://twitter.com/llanoJS" target="_blank">
            <img alt="twitter_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/twitter.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
        <a href="https://www.linkedin.com/in/juansllano/" target="_blank">
            <img alt="linkedin_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/linkedin.png" style="float: center; margin-right: 10px" height="50"  width="50">
        </a>
        <a href="https://medium.com/@juanllano93" target="_blank">
            <img alt="medium_page" src="https://raw.githubusercontent.com/EckoJuan/Readme_template/master/images/medium.png" style="float: center; margin-right: 10px" height="50" width="50">
        </a>
</p>

## Made with :heart: in
<p align="center">
    <img src="https://www.holbertonschool.com/holberton-logo.png"
        alt="Flow chart"
        style="float: left; margin-right: 10px;">
</p>

__Holberton School - Colombia__

__Foundations - Higher-level programming ― AirBnB clone__

__July, 2020.__
