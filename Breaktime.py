import time
import webbrowser

total_breaks = 3
break_count = 0

print ("This program started on" +time.ctime())
while (break_count < total_breaks):
         time.sleep(10)
         webbrowser.open("https://www.youtube.com/watch?v=PEGccV-NOm8")
         break_counts = break_counts + 1 
