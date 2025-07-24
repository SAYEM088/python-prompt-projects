#Try this yourself, no ChatGPT help

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
    logPass=input("Enter Your Password : ")
    if logPass==researcherInfo.get("password") :
        LoginStatus = True
        break
    else:
        print("Enter wright Pass Please")
        
print("Welcome Bro")
print("Lets do something beautiful today!\n\n")
import datetime
today = datetime.datetime.now()
print("Today is "+ today.strftime("%A")+' of '+today.strftime("%B"))

print("\n Lets Make a list , Are you ready? \n")
