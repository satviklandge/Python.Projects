import time
from tracemalloc import start
from turtle import speed 

print (" Speed Typing Test")

sentence = "abcdfghijklmnopqrstuvwxyz"

print ("\n Type This Extract ... ")
print (sentence)

input ("\n Press Enter To Start ")

start=time.time()

typed = input("\nStart Typing . :")

end= time.time()

time_taken = round(end-start,2)

speed = round (len(sentence)/time_taken,2)

print ("Time Taken :",time_taken,"second")
print ("Typing Speed :",speed,"letters/second")

if typed==sentence:
    print ("Congratulations! You typed the sentence correctly.")
else : 
    print ("Oops! You made a mistake while typing the sentence.")