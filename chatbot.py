#key and value pair 

#creating a dictionary for questions and it's answears ! 
import time 
Time = time.ctime() 
Qsn = { 

"hi":"hey", 
"how are you":"fine , You?", 
"i'm fine":"Okay",
"Fine too":"Okay",
"fine ":"Okay",

"what time is it now ?":Time,

      }

while True: 
    qs = input()

if(qs == "quit"):
    break

  print(Qsn[qs])