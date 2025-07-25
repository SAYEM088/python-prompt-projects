#Try this yourself, no ChatGPT help

#using topics:- Lists, Tuples, Sets, Dictionaries


#Date: July 23.2025
#Day-1
# Researcher’s Personal To-Do List


#info
researcherInfo={
    'name':'Sayem',
    'password':'sayem',
}

#system login
#as personal system only need password
LoginStatus = False
while(LoginStatus==False):
    print("Welcome To the TO-DO CLI App \n")
    logPass=input("Enter Your Password : ")
    if logPass==researcherInfo.get("password") :
        LoginStatus = True
        break
    else:
        print("Enter wright Pass Please")


# welcome Note
print("Welcome Bro")
print("Lets do something beautiful today!\n\n")
#import for time

        
print("Welcome Bro")
print("Lets do something beautiful today!\n\n")

import datetime
today = datetime.datetime.now()
print("Today is "+ today.strftime("%A")+' of '+today.strftime("%B"))

print("\n Lets Make a list , Are you ready? \n")



#[(start, end), "reason"]
# Rules :  Restricted Time Periods (Tuples + List)
restrictTimes = [
    #format [(start, end), "reason"]
    (("01:00 PM", "02:00 PM"), "Bath"),
    (("05:00 AM", "05:30 AM"), "Morning Prayer"),
    (("08:00 PM", "09:00 PM"), "Dinner"),
    (("11:00 PM", "05:00 AM"), "Sleep"),
]

# To store tasks : TaskList (Using List of Dictionaries)
taskList = []

# Parse time input (e.g. 8.5 → 08:30 AM)
def parse_time_input():
    while True:
        time_str = input("When do you start ?: ")
        try:
            time_float = float(time_str)
            hour = int(time_float)
            minute = int((time_float - hour) * 60)
            return datetime.datetime.combine(today.date(), datetime.time(hour, minute))
        except:
            print("Enter valid time ")

# Convert "HH:MM AM/PM" to datetime.time object
def str_to_time_obj(tstr):
    return datetime.datetime.strptime(tstr, "%I:%M %p").time()

# Function to check if current time overlaps any restricted period
def check_restriction(current_dt):
    current_time = current_dt.time()
    for (start_str, end_str), reason in restrictTimes:
        start = str_to_time_obj(start_str)
        end = str_to_time_obj(end_str)

        # whole night range -- sleeping time
        if start > end:
            if current_time >= start or current_time < end:
                return reason, start_str, end_str
        else:
            if start <= current_time < end:
                return reason, start_str, end_str
    return None

#   starting time
current_time = parse_time_input()

# Start scheduling
while True:
    # Check restriction if it matched with then shift time 
    restriction = check_restriction(current_time)
    if restriction:
        reason, start_str, end_str = restriction
        print(f"\n {current_time.strftime('%I:%M %p')} is during '{reason}' ({start_str} - {end_str}). Skipping to after it ends.")
        end_time = str_to_time_obj(end_str)
        # datetime.datetime.combine(date, time) , date time object creation, like-(2025, 7, 23, 8, 30)
        current_time = datetime.datetime.combine(today.date(), end_time)
        continue

    # Input task
    task = input(f"\n What task do you want to do at {current_time.strftime('%I:%M %p')}? (Type 'done' to finish): ")
    if task.lower() == 'done':
        break

    try:
        duration = int(input("Duration in minutes: "))
    except ValueError:
        print("Please enter valid duration.")
        continue

    # Save task
    taskList.append({
        "time": current_time.strftime("%I:%M %p"),
        "task": task,
        "duration": duration
    })

    # Move time forward
    current_time += datetime.timedelta(minutes=duration)

# Display Schedule
print("\n Your To-Do Schedule for Today:\n")
print(" Time       | Task")
print("------------|-------------------------------")
for task in taskList:
    print(f" {task['time']} | {task['task']} ({task['duration']} min)")

ReName=researcherInfo["name"]
print(f"\n All the best, {ReName}!")

