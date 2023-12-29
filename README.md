<div align="center">
<h1>AirBnB clone</h1>

## **Welcome to the AirBnB clone project!**
</div>

This repository contains the stages of a student project to build a clone of the AirBnB website.
- A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
- A website (the front-end) that shows the final product to everybody: static and dynamic
- A database or files that store data (data = objects)
- An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)



## [**The console**](https://github.com/iAdamo/AirBnB_clone)
**`Python`** **`OOP`**
<h3>A command interpreter to manipulate data without a visual interface</h3>

***First step: The command interpreter to manage AirBnB objects.***
- This is the first step towards building full web application: the AirBnB clone. This first step is very important because it will use what is built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all classes and storage engine
- creating th data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to build later, there won’t be a need to pay attention (take care) of how the objects are stored.

This abstraction will also allow to change the type of storage easily without updating all of its codebase.

<!--add the image here-->

 ## [**Web static**](https://github.com/iAdamo/AirBnB_clone_v2/tree/main/web_static)
 **`HTML`** **`CSS`** **`Front-end`**

Now that there is a command interpreter for managing the AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we had to build the front end step-by-step.

The first step was to “design” / “sketch” / “prototype” each element:

- Create simple HTML static pages
- Style guide
- Fake contents
- No Javascript
- No data loaded from anything

We manipulated HTML and CSS languages. HTML is the structure of the page, it should be the first thing to write. CSS is the styling of the page, the design. *I really encourage you to fix your HTML part before starting the styling. Indeed, without any structure, you can’t apply any design.*

## [**MySQL storage**](https://github.com/iAdamo/AirBnB_clone_v2)
**`Python`** **`OOP`** **`Back-end`** **`SQL`** **`MySQL`** **`ORM`** **`SQLAlchemy`**

In this project, you will link two amazing worlds: Databases and Python!
- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

We will be using the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

*This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to build later, there won’t be a need to pay attention (take care) of how the objects are stored.*

## [**Deploy static**](https://github.com/iAdamo/AirBnB_clone_v2)
**`DevOps`** **`Python`** **`SysAdmin`** **`Scripting`** **`CI/CD`**

Ever since th completed project [**Load balancer**](https://github.com/iAdamo/alx-system_engineering-devops/tree/main/0x0F-load_balancer) of the SysAdmin track, we’ve had 2 web servers + 1 load balancer but nothing to distribute with them.

It’s time to make the work public!

In this first deployment project, you will be deploying your **web_static** work. You will use **Fabric** (for Python3).

Fabric is a Python library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks. It provides a basic suite of operations for executing local or remote shell commands (normally or via sudo) and uploading/downloading files, as well as auxiliary functionality such as prompting the running user for input, or aborting execution.

This concept is important: execute commands locally or remotely. Locally means in your laptop (physical laptop or inside your Vagrant), and Remotely means on your server(s).

Fabric is taking care of all network connections (SSH, SCP etc.), it’s an easy tool for transferring, executing, etc. commands from locale to a remote server.

## [**Web framework**](https://github.com/iAdamo/AirBnB_clone_v2)
**`Python`** **`Back-end`** **`Webserver`** **`Flask`**
A web framework is a software framework designed to aid the development of web applications, including web services, web resources, and web APIs. It provides a structure and a set of tools for building and managing web applications, making it easier for developers to create robust and scalable web projects.
<a href=#>
    <img src="https://s3.amazonaws.com/intranet-projects-files/concepts/74/hbnb_step3.png" alt="flask">
</a>


### Collaborators:
* [**Adam Sanusi Babatunde**](https://github.com/iAdamo)
* [**Linda Nwanchukwu**](https://github.com/lyndha)
* [**Hassanyoung Hassan**](https://github.com/Hassanyoung1)
* [**Justin Majetich**](https://github.com/justinmajetich)
* [**Ezra Nobrega**](https://github.com/eNobreg)
