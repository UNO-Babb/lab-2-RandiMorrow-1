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

  print ("It is now: ")
  print (f"{currentHour:02}:{currentMinute:02}")

  #TODO:
  #Ask user for hours
  moreHour = int(input("Give me a number of hours please: "))
  #Ask user for minutes
  moreMins = int(input("And now a number of minutes: "))
  #Calculate the time after the user-supplied time has passed.


  futureMins = (currentMinute + moreMins ) % 60
  extraHour = (currentMinute + moreMins ) // 60
  futureHour = (currentHour + moreHour + extraHour) % 24 

  print(f"{futureHour:02}:{futureMins:02}")



if __name__ == '__main__':
  main()
