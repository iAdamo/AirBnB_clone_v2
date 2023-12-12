<h3>A command interpreter to manipulate data without a visual interface</h3>
<h5>Python OOP</h4>

This repository contains the initial stage of a student project to build a clone of the AirBnB website. This stage implements a backend interface, or console, to manage program data. Console commands allow the user to create, update, and destroy objects, as well as manage file storage. Using a system of JSON serialization/deserialization, storage is persistent between sessions.

### **Welcome to the AirBnB clone project!**

***First step: The command interpreter to manage AirBnB objects.***
This is the first step towards building full web application: the AirBnB clone. This first step is very important because it will use what is built during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all classes and storage engine
## **The console**
- creating th data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
The first piece is to manipulate a powerful storage system. This storage engine will give an abstraction between “My object” and “How they are stored and persisted”. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI to build later, there won’t be a need to pay attention (take care) of how the objects are stored.

This abstraction will also allow to change the type of storage easily without updating all of its codebase.

<!--add the image here-->

## Collaborators:  
* **Adam Sanusi Babatunde** - [Github @iAdamo](https://github.com/iAdamo)
* **Hassanyoung Hassan** - [GitHub @Hassanyoung1](https://github.com/Hassanyoung1)
