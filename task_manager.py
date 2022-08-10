'''Capstone template project for FCS Task 19 Compulsory task 1.
This template provides a skeleton code to start compulsory task 1 only.
Once you have successfully implemented compulsory task 1 it will be easier to
add a code for compulsory task 2 to complete this capstone'''

#=====importing libraries===========
'''This is the section where you will import libraries'''
import datetime
from os.path import exists

#====Login Section====

#This builds a list of each username exactly as it appeares in the 'user_overview.txt' file.
def build_user_log():
    with open ('user_overview.txt','r') as display_user :
        display_user = display_user.readlines()
        del display_user[0:2]
        user_log = []
        
        for line in display_user:
            line = line.split(' ')
            user_log.append(line[0])
            
    return user_log

#This function builds 2 dictionaries.
#1st dictionary contains total tasks, total completed, uncompleted tasks and total overdue tasks.
#2nd dictionary containes duplicate of 1st dictionary but containes the lines from the tasks file;
#instead of a count.
#We send the 2 dictionaries back 1 to be written in a new file, other to be used further.
def task_overview():

    tasks_state = {'Completed_tasks': 0,
                   'Uncompleted_tasks': 0,
                   'Total_tasks': 0,
                   'Overdue_tasks': 0,
                   }
    tasks_info = {'completed': [],
                   'uncompleted': [],
                   'total': [],
                   'overdue': [],
                   }

    with open('tasks.txt','r') as task_stats:
        for line in task_stats:
            tasks_state['Total_tasks'] += 1
            tasks_info['total'].append(line)

            line = line.replace('\n','')
            line = line.split(', ')
            
            if line[5] == 'No':
                tasks_state['Uncompleted_tasks'] += 1
                tasks_info['uncompleted'] += list(line)
                
                #This section modifies todays date and the due date in a foramat which can be used to compare.
                today_date = datetime.date.today()
                today_date = today_date.strftime('%d %m %Y')
                today_date = today_date.split(' ')
                y1, m1, d1 = int(today_date[2]), int(today_date[1]), int(today_date[0])
                today_date = datetime.date(y1, m1, d1)
                date_mod = line[4]
                date_mod = datetime.datetime.strptime(date_mod,'%d %b %Y').strftime('%d %m %Y')
                date_mod = date_mod.split(' ')
                y2, m2, d2 = int(date_mod[2]), int(date_mod[1]), int(date_mod[0])
                date_mod = datetime.date(y2, m2, d2)
                
                if today_date > date_mod:
                    tasks_state['Overdue_tasks'] += 1  
                    tasks_info['overdue'] += list(line)
                
            else:
                tasks_state['Completed_tasks'] += 1
                tasks_info['completed'] += list(line)
                
    return tasks_state, tasks_info
           
#This function accepts the built dictionary from 'task_overview()' and Bulds 2 dictionaries.
#1 contains totals users registered in the system.
#2 contains statistics about tasks for each user in the system.    
def user_overview(x):
    users_state ={'Total_users': 0,
                  }
    tasks_dict ={}
    tasks_info = x

    with open('user.txt','r') as user_stats:
        
        for line in user_stats:
            users_state['Total_users'] += 1
            line = line.replace('\n','')
            line = line.split(', ')
            tasks_dict[line[0] + "_total_tasks"] = 0
            tasks_dict[line[0] + "_completed_tasks"] = 0
            tasks_dict[line[0] + "_uncompleted_tasks"] = 0
            tasks_dict[line[0] + "_overdue_tasks"] = 0

        for line in tasks_info['total']:
               line = line.replace('\n','')
               line = line.split(', ')
               for name in login_username:
                   if name == line [0]:
                       tasks_dict[line[0] + "_total_tasks"] += 1

        for line in tasks_info['completed']:
               line = line.replace('\n','')
               line = line.split(', ')
               for name in login_username:
                   if name == line [0]:
                       tasks_dict[line[0] + "_completed_tasks"] += 1

        for line in tasks_info['uncompleted']:
                line = line.replace('\n','')
                line = line.split(', ')
                for name in login_username:
                    if name == line [0]:
                        tasks_dict[line[0] + "_uncompleted_tasks"] += 1
           
        for line in tasks_info['overdue']:
               line = line.replace('\n','')
               line = line.split(', ')
               
               for name in login_username:
                   if name == line [0]:
                       tasks_dict[line[0] + "_overdue_tasks"] += 1
                   
    return tasks_dict, users_state

#Here we call to build the dictionaries using 'task_overview()' and 'user_overview()'
#We modify and condense the returned dictionaries into 2 final dictionaries.
#After formating and calculations we write to 2 seperate txt files.
def generate_report():
    count = 0
    tasks_stats = {}
    tasks_all_info = {}
    users_all_info = {}
    totals_dict = {}
    tasks_stats, tasks_all_info = task_overview()
    users_all_info, totals_dict  = user_overview(tasks_all_info)
    print("\nReport generated!")
    totals_dict ['Total_tasks'] = tasks_stats['Total_tasks']
    
    tasks_stats['Uncompleted_tasks_percentage'] = (tasks_stats['Uncompleted_tasks']/tasks_stats['Total_tasks'])*100
    tasks_stats['Uncompleted_tasks_percentage'] = f"%{round(tasks_stats['Uncompleted_tasks_percentage'], 2)}"
    tasks_stats['Overdue_tasks_percentage'] = (tasks_stats['Overdue_tasks']/tasks_stats['Total_tasks'])*100
    tasks_stats['Overdue_tasks_percentage'] = f"%{round(tasks_stats['Overdue_tasks_percentage'], 2)}"
    
    for line in login_username:
        users_all_info[line + '_Total_tasks_assigned_percentage'] = (users_all_info[line + '_total_tasks']/tasks_stats['Total_tasks'])*100
        users_all_info[line + '_Total_tasks_assigned_percentage'] =f"%{round(users_all_info[line + '_Total_tasks_assigned_percentage'],2)}"
        
        users_all_info[line + '_completed_tasks'] = (users_all_info[line + '_completed_tasks']/tasks_stats['Total_tasks'])*100
        users_all_info[line + '_completed_tasks'] =f"%{round(users_all_info[line + '_completed_tasks'],2)}"
        
        users_all_info[line + '_uncompleted_tasks'] = (users_all_info[line + '_uncompleted_tasks']/tasks_stats['Total_tasks'])*100
        users_all_info[line + '_uncompleted_tasks'] =f"%{round(users_all_info[line + '_uncompleted_tasks'],2)}"
        
        users_all_info[line + '_overdue_tasks'] = (users_all_info[line + '_overdue_tasks']/tasks_stats['Total_tasks'])*100
        users_all_info[line + '_overdue_tasks'] =f"%{round(users_all_info[line + '_overdue_tasks'],2)}"
    
    with open('task_overview.txt','w') as task_overview_file:

        for key, value in tasks_stats.items(): 
            task_overview_file.write('%s : %s\n' % (key.replace('_',' '), value))
            
    with open('user_overview.txt','w') as user_overview_file:
        
        for key, value in totals_dict.items(): 
            user_overview_file.write('%s : %s\n' % (key.replace('_',' '), value))
        
        for key, value in users_all_info.items():
            count += 1
            
            if (count % 4) == 0:
                user_overview_file.write('%s : %s\n\n' % (key.replace('_',' '), value))
                
            else:
                user_overview_file.write('%s : %s\n' % (key.replace('_',' '), value))

#Here we print all the relevent statistics from the 2 newly created txt files.
def display_report():
    with open ('task_overview.txt','r') as display_task :
        display = display_task.readlines()
        
        print('\n' + ''.join(display))
        
    with open ('user_overview.txt','r') as display_user :
        line_count = 0
        display_user = display_user.readlines()
        percent = []
        len2 = len(display_user)
        len1 = len2 - len(set(login_username))
        percent = display_user[len1:len2]
        percent.reverse()

        print(f"{display_user[0]}{display_user[1]}")
        
        del display_user[len1-1:len2]
        del display_user[0:2]


        for line in display_user:
            line_count += 1
            line = line.split(' ')
            user_log = build_user_log()
            del line[0]
            line = ' '.join(line)
            if line_count == 1:
                print(f"{user_log[0]}\n{'─' * 30}")
                
                print_percent = percent[0].replace('\n','')
                print(print_percent.replace(user_log[line_count] + ' ',''))
                del percent[0]
                
            print(line.replace('\n',''))
            
            if (line_count % 5) == 0:
                if line_count == len(user_log):
                    break
                else:    
                    print(f"{user_log[line_count]}\n{'─' * 30}")
                    
                    print_percent = percent[0].replace('\n','')
                    print(print_percent.replace(user_log[line_count] + ' ',''))
                    del percent[0]
    
def display_stats():
        number_of_users = open('user.txt','r')
        number_of_tasks = open('tasks.txt','r')

        #Used for counting number of lines in each text file.
        #Reference: https://pynative.com/python-count-number-of-lines-in-file/
        for count1,line in enumerate(number_of_users) :
            pass

        for count2,line in enumerate(number_of_tasks) :
            pass
        
        stats =f"\nNumber of users registered:\t\t\t{count1+1}\nNumber of tasks to be completed:\t{count2+1}\n"
        
        number_of_users.close()
        number_of_tasks.close()
        return stats
    
#This function is accessed trough 'view_mine()' and this gives user the option to modify 1 of their tasks.        
def task_select(task_choice):
    choice2 = input("Choose from the options below:\n"
                   "c - Mark task as complete\n"
                   "e - Edit the task\n")
    
    task_choice = task_choice.replace('\n','')
    task_choice  = task_choice.split(', ')
    
    while True:
        if choice2 == 'c':
            task_choice [5] =  'Yes'
            return task_choice
            
        elif choice2 == 'e':
            while True:
                if task_choice[5] == 'No':
                    edit_choice = input("Choose from the menu below:\n"
                                        "u - Edit username\n"
                                        "d - Edit due date\n"
                                        "x - Finish editing\n")
                    
                    if edit_choice == 'u':
                        while True:
                            edit_user = input("Enter new username for the task: ")
    
                            if not (edit_user in login_username) :
                                print("Username not registered. Try again")
                                continue
                            else:
                                task_choice[0] = edit_user
                                break
    
                    elif  edit_choice == 'd':
                        edit_due = input("Enter a new due date in the format dd/mmm/yyyy eg. 18/jul/2022: ")
                        edit_due = edit_due.replace('/',' ')
                        task_choice[4] = edit_due
    
                    elif edit_choice == 'x':
                        return task_choice
                    
                    else:
                        print("Incorrect choice. Try again")  
                
                else:
                    print("This task has already been completed. Please choose a different task")
                    return task_choice 
                
        else:
            print("Incorrect choice. Try again.")
            
def reg_user():
 if(username == "admin"):
            
    while True:
        new_username = str(input("Enter a new username to register: "))

        #Setting up a statement to stop duplicate user registration.
        if new_username in login_username :
            print("Username already registered. Try again")
            continue
        else :
            new_password = str(input("Enter a new password: "))
            confirm_password = str(input("Confirm your password: "))
                
            if (new_password == confirm_password):
                
                with open('user.txt','a') as new_login :

                    #Saving the correct format to write to the text file.
                    output = '\n' + new_username + ', ' + new_password
                    login_username.append(new_username)
                    new_login.write(output)
                
                break
            else :
                print("The password entered does not match. Please try again.")    

def add_task():
    while True:
        username_task = str(input("Enter the username of person to assign the task: "))

        #Chcking if the username is registered.
        if username_task in login_username :
            task_title = str(input("Enter the task: "))
            task_description = str(input("Enter the description of the task assigned: "))
            due = str(input("Enter the due date in this format:\ndd/mmm/yyyy eg. 18/jul/2022: "))

            #Modifying due date to be in the correct format    
            due = due.replace("/" , " ")
            #Link below was used as reference to aquire and format todays date.
            #https://docs.python.org/3/library/datetime.html
            current_date = datetime.date.today()
            current_date = current_date.strftime("%d %b %Y")
            
            #print(current_date)#Used for checking the format of 'current_date'.

            #Arranging in the correct format for writing.
            all_task = f"\n{username_task}, {task_title}, {task_description}, {current_date}, {due}, No"
            
            with open('tasks.txt', 'a') as tasks :
                tasks.write(all_task)
                break
        else :
            print("Username not in system. Try again.")

def view_all():
    with open('tasks.txt','r') as task_file :
        count = 0    
        for task in task_file :
            count += 1
            task_info = task.split(', ')
            assigned_to = task_info[0]
            task_title = task_info[1]
            task_description = task_info[2]
            task_date = task_info[3]
            task_due = task_info[4]
            task_state = task_info[5]
            #Since element '5' is the end of the line in a text file there is a '\n' character added.
            #Using '.replace' to remove the '\n'.
            task_state = task_state.replace('\n','')

            #Using '\t' to space things correctly.
            #Link below used for reference to print a straight horizontal line with ease.
            #https://stackoverflow.com/questions/65561243/print-a-horizontal-line-in-python
            print(f"\nTask {count}\n"
                  f"{'─' * 60}\n\n"
                  f"Task:\t\t\t\t{task_title}\n"
                  f"Assigned to:\t\t{assigned_to}\n"
                  f"Date assigned:\t\t{task_date}\n"
                  f"Due date:\t\t\t{task_due}\n"
                  f"Task completed?\t\t{task_state}\n"
                  f"Task description:\n {task_description}\n\n"
                  f"{'─' * 60}\n\n")

def view_mine():
    full_user_task = []
    number_of_tasks = 0
    with open('tasks.txt','r') as user_tasks_file :

        #Splitting up each element in 'user_task_file' and saving the first element (username of assigned task).
        #Doing this for each line.
        for task in user_tasks_file :
            task_info = task.split(', ')
            assigned_to = task_info[0]
            #Making a full list of the usernames in the task file.
            full_user_task.append(task_info[0]) 

            #Checking if the logged in username is the same as current value in 'assigned_to'.
            if (username == assigned_to) :
                task_title = task_info[1]
                task_description = task_info[2]
                task_date = task_info[3]
                task_due = task_info[4]
                task_state = task_info[5]
                number_of_tasks += 1

                print(f"\nTask {number_of_tasks}\n"
                      f"{'─' * 60}\n\n"
                      f"Task:\t\t\t\t{task_title}\n"
                      f"Assigned to:\t\t{assigned_to}\n"
                      f"Date assigned:\t\t{task_date}\n"
                      f"Due date:\t\t\t{task_due}\n"
                      f"Task completed?\t\t{task_state}\n"
                      f"Task description:\n {task_description}\n\n"
                      f"{'─' * 60}\n\n")
        
        if  not (username in full_user_task) :
            print("There are no tasks assigned to you currently.")
            return

        while True:
            choice = int(input("Choose from the options below:\n"
                               f"1-{number_of_tasks} - Select a task\n"
                               "-1 - Return to main menu\n"))

            #'task_index' stores the indexes of each time the 'username' appeares in the tasks file.
            task_index = [i for i, x in enumerate(full_user_task) if x == username]
            choice -= 1
            
            if choice == -2:
                return 
            
            #Sending the selected task to a function which then gives users more options.
            #The function returns the edited line  and then we format it and write it in the 'tasks.txt' file.
            elif task_index[choice] in range(0, number_of_tasks):
                
                with open('tasks.txt','r') as user_tasks_file:
                    task_lines = user_tasks_file.readlines()
                    edited_line =  task_select(task_lines[task_index[choice]])
                    edited_line = ', '.join(edited_line)
                    task_lines[task_index[choice]] = edited_line + '\n'
                    
                    with open('tasks.txt','w') as user_tasks_file :
                        user_tasks_file.writelines(task_lines)

            else:
                print("Wrong choice. Try again")

login_list = []
login_username = []
login_password = []

with open('user.txt','r') as login :

    #Save each line of the file 'login' in a list called 'login_list'.
    #Splitting at ', ' to save each element (username, password) as seperates.
    #Saving username and password in 2 seperate lists.
    for line in login :
        login_list = line.split(', ')
        login_username.append(login_list[0])
        login_password.append(login_list[1])

    while True :
        username = str(input("Enter a valid username: "))

        if username in login_username :
            line = login_username.index(username)
            password = str(input("Enter a valid password: "))

            #Checking if the password matches with the password stored under the username entered.
            if password in login_password[line] :
                break
            else :
                print("The password does not match with"
                          "the one stored in the system. Please try again")
                    
        else :
                print("The username does not match with"
                      "the one stored in the system. Please try again")

while True:      
    #Setting up separate menu if the user logged in is 'admin'.
    if (username == "admin") :
            menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks    
vm - View my task
gr - Generate reports
ds - Display statistic
dr - Display reports
e - Exit
: ''').lower()

    else :
        #Presenting the menu to the user and 
        #making sure that the user input is coneverted to lower case.
        #I have added \n at the beginning just for readability.
        menu = input('''\nSelect one of the following Options below:
r - Registering a user
a - Adding a task
va - View all tasks    
vm - view my task
e - Exit
: ''').lower()

    if menu == 'r':
        if(username == "admin"):
            reg_user()
            
        else :
            print("Only the admin has the rights to use this option. Try again.\n")
            
    elif menu == 'a':
        add_task()

    elif menu == 'va':
        view_all()

    elif menu == 'vm':
        view_mine()

    elif (username == 'admin') and (menu == 'ds'):
        print(display_stats())
        
    elif (username == 'admin') and (menu == 'gr'):
        generate_report()
                    
    elif (username == 'admin') and (menu == 'dr'):
        if exists('task_overview.txt') and exists('user_overview.txt'):
            display_report()
            
        else:
            generate_report()
            display_report()
                
    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")
