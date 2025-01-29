#FutureTime.py
#Name: Randi Morrow
#Date: 1/27/25
#Assignment: Lab 2

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24
  currentMinute = now.minute

  print (currentHour, currentMinute) #this is just for checking, we should delete it later

  #TODO:
  #Ask user for hours
  question= input("Give me a number of hours please: ")
  #Ask user for minutes
  question= input("And now a number of minutes: ")
  #Calculate the time after the user-supplied time has passed.
  moreMins = 30

  futureHour = (currentHour)

  futureMins = (currentMinute + moreMins) % 60
  extraHour = (currentMinute + moreMins) // 60

  print(extraHour)

  print(futureMins)
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"

if __name__ == '__main__':
  main()
