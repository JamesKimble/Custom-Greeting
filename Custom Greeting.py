### Custom Greeting Python Program ###

## - Made By JamesTheWebDev - ##




####################
## Import Modules ##
####################

from datetime import datetime





#####################
## Custom Greeting ##
#####################

print("Please enter your name below:\n");
fname = input("First Name: ");
lname = input("Last Name: ");

m = 5;
a = 12;
e = 19;

mrng = str(m);
aftn = str(a);
evng = str(e);

now = datetime.now();
 
# Current hour (24 hour clock) #
time = now.strftime("%H");

greet = "";

if time == mrng or time < mrng and time < aftn:
    greet = "morning";
if time == aftn or time > aftn and time < evng:
    greet = "afternoon";
if time == evng or time > evng and time > aftn:
    greet = "evening";

print("Good "+greet+" "+fname+"!");


    








