
"""
Created on Sun Nov 17 16:48:47 2019

"""

def FindDuration():
    global minTime
    global maxTime
    global MeanTime
    global flag
    flag = 0
    entry_MinTime.set('')
    entry_MaxTime.set('')
    entry_MeanTime.set('')
    SearchVar = destination_entry.get()
    import csv
    with open("Travel_Times2.csv", newline='') as csvfile:
      spamreader = csv.DictReader(csvfile)
      for row in spamreader:       
          tableVar = row['Destination Display Name'] 
          if SearchVar in tableVar:
              minTime = row['Range - Lower Bound Travel Time (Seconds)']
              maxTime = row['Range - Upper Bound Travel Time (Seconds)']
              MeanTime = row['Mean Travel Time (Seconds)']
              entry_MinTime.set(minTime)
              entry_MaxTime.set(maxTime)
              entry_MeanTime.set(MeanTime)
              flag=1
    if(flag!=1):
        Label(screen, text = "Invalid Destination", fg = "red" ,font = ("Calibri", 11)).pack()
             
              
from tkinter import*   
def main_screen():
  global screen
  screen = Tk()
  screen.configure(background='grey')
  screen.geometry("600x500")
  screen.title("Find Time to your Destination")
  Label(text = "Find Time to your Destination", bg = "blue", width = "300", height = "2", font = ("Calibri", 13)).pack()
  Label(text = "",bg="grey").pack()
  global source
  global destination
  global source_entry
  global destination_entry
  global entry_MinTime
  global entry_MaxTime
  global entry_MeanTime

  source = StringVar()
  destination = StringVar()
  entry_MinTime = StringVar()
  entry_MaxTime = StringVar()
  entry_MeanTime = StringVar()
  
  Label(screen, text = "Please enter details below").pack()
  Label(screen, text = "",bg="grey").pack()
  
  Label(screen, text = "Source: Museum Road, Shanthala Nagar, Ashok Nagar, Bengaluru ",bg="white").pack()
  Label(screen, text = "",bg="grey").pack()
  
  Label(screen, text = "Destination  ").pack()
  destination_entry =  Entry(screen, textvariable = destination )
  destination_entry.pack()
  Label(screen, text = "",bg="grey").pack()
  
  Button(text = "FindDuration", height = "2", width = "30", command=FindDuration).pack()
  Label(text = "",bg="grey").pack()
  Label(text = "",bg="grey").pack()
  
  Label(screen, text = "Min Time to Reach(Seconds) : ").pack()
  entryMin = Entry(screen,textvariable=entry_MinTime)
  entryMin.pack()
  Label(text = "",bg="grey").pack()
  
  Label(screen, text = "Max Time to Reach(Seconds) : ").pack()
  entryMax = Entry(screen,textvariable=entry_MaxTime)
  entryMax.pack()
  Label(text = "",bg="grey").pack()
  
  Label(screen, text = "Mean Time to Reach(Seconds) : ").pack()
  entryMean = Entry(screen,textvariable=entry_MeanTime)
  entryMean.pack()
  
  screen.mainloop()
 
main_screen()      
            
