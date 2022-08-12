--
Task manager 2.0
---
A login system and a task managment system.

## What does the programme do?

This is a system that allows users to login and then given options to view or add tasks.

When logged in as *admin* you are given options to also register new users and display statistics.

This is an updated version of Task manager project. It is now more modular and has added funtionaliy.

##  Update log
* **Functions** have been utilised to make the code more modular.
* View my tasks have been given the following functionality:
  * Enter a number to choose the corresponding task.
    * You can now mark the chosen task as complete.
    * You can now edit the username and deadline of the task (if uncompleted)
### New features
* Generate reports:
  * Generates 2 *.txt* files called *task_overview.txt* and *user_overview.txt*.
  * task_overview.txt contains:
    * Total number of tasks generated.
    * Total number of completed and uncompleted tasks.
    * Number and percentage of overdue tasks.
    * Percentage of incomplete tasks.
  * user_overview.txt contains:
  * For each user in the system:
    * Total number of tasks assigned to user.
    * Percentage of total tasks.
    * Percentage of total tasks completed and uncompleted and overdue.
  * Display reports:
    * Displays all the data created by *Generate reports*.
    

## guide
### Prerequisits
**Tasks.txt** is a *.txt* file that is utilised and required for the programme.

It contains:
* Username of the person the task is allocated to.
* Title of the task.
* Description of the task.
* Date of task creation.
* Due date.
* State of completion.

By default the file contains 2 tasks under the user *admin*.
All new tasks added to the system will be written in this file to keep a log.

**User.txt** is a *.txt* file that is the only other file required for the programme.

This contains:
* Username of each registered in the system.
* Password counterpart of those usernames.

By default it contains the login information of the *admin* user.
All new registered users will be added to this file.

### Steps

* User will be asked to enter a username and passowrd.
  * At the start only the admin can login.
  * When new users are registererd the can use their username and password to login.
* A menu will show up with options:
  * register user.
    * register a new user to the system.
  * Add task.
    * Add a new task to the system.
  * View all tasks.
    * View all the tasks in the system.
  * View my tasks.
    * View all tasks under current logged in user.
  * Display statistics (only visable for user *admin*)
    * Displays total number of tasks and users in the system.
  * Exit.
  
  ## Use
  
  Can be used for any company wishing to impliment a login system for their employees. the login details can be encrypted with more research and code.
  Could also be used by any company that manages multiple employees and wish to assign them tasks remotely.
  
  ## Instructions
 
  Make sure to download all 3 files ( *asks.txt, user.txt and task_manager.py* )
  check *user.txt* and make a note of the username and password to login and
  make sure not to fill either of the *.txt* files with empty space */s* or empty line */n*.
  
  Just run the task_manager.py and follow the guide.
  
  If Display report is chosen 2 new txt files are generated at task_manager.py file location. These files will be updated everytime the option is chosen.
  You may delete these files if you choose to.

## Contributers

Made by *Iftekharul Islam*.

