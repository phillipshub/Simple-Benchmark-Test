# Program:simple_benchmark_test.py
# Author:Phillip McCullough
# Date:5/30/2022
# Python:3.11.3
# Last Updated:5/5/2023
#
# Simple Benchmark Test is intended to measure system performance over an
# extended period of time. SBT is a light weight program optimized for
# efficiency to run in the background consuming minimal resources.
# The test simply counts and calculates the time period to complete that task.
#
# Upon successful completion test information is saved to a log file for
# performance tracking over multiple sessions or for troubleshooting.
#
# Simple Benchmark Test counts to one trillion and creates a log entry of the
# time spanned. The log file can be reset at any time. You have the ability
# to choose custom ranges, overwrite existing an log, and run without logging
# if desired.
#
# Current test results are displayed to the terminal upon completion.
#------10--------20--------30--------40--------50--------60--------70--------80

from datetime import datetime
# Log file name
LOG_FILE = "SBT_Log.txt"

#------------------------------------------------------------------------------

def greeting():
  """Provides user with information about program."""
  print("\n"
    "Simple Benchmark Test measures the time it takes a device running python 3\n"
    "or compatible versions to count to one trillion. Custom values can be\n"
    "specified. A log file is created upon test completion. This program can\n"
    "run for hours to days depending on hardware. Long-term benchmarking is\n"
    "intended to measure system execution performance over time or during\n"
    "specific time frames or for troubleshooting performance issues.\n"
    "Interruption will not yield results or create a log entry.\n"
    "All options currently available are listed in the menu.\n")
  
#------------------------------------------------------------------------------

def simple_benchmark(count_value = 1_000_000_000_000, log = "a"):
  """Count to value, log option."""
  print()
  #Start datetime.
  start = datetime.now()
  start_test = start.strftime("time: %H:%M:%S, date: %m/%d/%Y")
  print("Start-%s.\nTesting...\n" %start_test)
  #Proof of count made.
  current_number = 0
  #Count loop.
  for n in range(1, count_value + 1): current_number = n
  #Finish datetime.
  finish = datetime.now()
  finish_test = finish.strftime("time: %H:%M:%S, date: %m/%d/%Y")
  log_date = finish.strftime("%m/%d/%Y")
  print("Test Complete.\nFinish-%s." %finish_test)
  #Number reached.
  print("Count......: {:,}".format(current_number))
  #Runtime
  print("Runtime....: %s\n" %(finish - start))
  #Writing to a log file.
  if log != "off":
    with open(LOG_FILE, log) as result:
      result.writelines([
        "Simple Benchmark Test results...: %s\n" %log_date,
        "Started.........................: %s\n" %start_test,
        "Completed.......................: %s\n" %finish_test,
        "Runtime.........................: %s\n" %(finish - start),
        "Count value.....................: {:,}\n\n".format(current_number)])
      result.close()

#------------------------------------------------------------------------------

def read_log():
  """Allows user to read log if it exists."""
  try:
    with open(LOG_FILE, "r") as log:
      print("\n\n%s" %log.read())
      log.close()
  except FileNotFoundError:
    print("\nA log file has not been created.\n")

#------------------------------------------------------------------------------

def clear_log():
  """Clears log if it exists."""
  cleared = datetime.now()
  date_cleared = cleared.strftime("%m/%d/%Y, %H:%M:%S")
  with open(LOG_FILE, "w") as log:
    log.write("Log cleared: %s.\n\n" %date_cleared)
    log.close()
    print("\nClear log file success.\n")
  
#------------------------------------------------------------------------------

def custom_parameters():
  """Prompts user for custom arguments."""
  error_message = "\nSorry, I didn't get that, try again."
  count_value = 1_000_000_000_000
  log_mode = "a"
  print()

  while True:
    option = input("Would you like to use a custom count value? [Y/n]: ").lower()
    if option == "y" or option == "yes":
      count_value = input("Enter numeric value: ")
      try:
        if "," or "." in count_value: 
          count_value = count_value.replace(",", "")
          if "." in count_value: count_value = float(count_value)
          count_value = abs(int(count_value))
          break
        else:
          count_value = abs(int(count_value))
          break
      except ValueError:
        print(error_message)
        custom_parameters()
    elif option == "n" or option == "no": break
    else: print(error_message)
    
  while True:
    option = input("Would you like to log this test? [Y/n]:").lower()
    if option == "y" or option == "yes": break
    elif option == "n" or option == "no":
      log_mode = "off"
      break
    else: print(error_message)
    
  simple_benchmark(count_value, log_mode)

#------------------------------------------------------------------------------

def menu():
  """Presents user with options."""
  while True:  
    print(
      "Options:\n"
      "1)Run program with default values press enter.\n"
      "2)View log records.\n"
      "3)Test without log entry.\n"
      "4)Reset current log file and run.\n"
      "5)Clear log file.\n"
      "6)Choose custom parameters.\n"
      "7)Exit.")
    selection = input("Select an option: ")
    if selection == "" or selection == "1": simple_benchmark()
    elif selection == "2": read_log()
    elif selection == "3": simple_benchmark(log = "off")
    elif selection == "4": simple_benchmark(log = "w")
    elif selection == "5": clear_log()
    elif selection == "6": custom_parameters()
    elif selection == "7": exit(0)
    else: print("\nYou entered: %s, please choose a valid option.\n" %selection)
    
#------------------------------------------------------------------------------
  
def main():
  """Initializes program methods."""
  greeting()
  menu()

#------------------------------------------------------------------------------
 
# Runs the program when started.
if __name__ == "__main__": main()

#------------------------------------------------------------------------------