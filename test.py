# Program:test.py
# Author:Phillip McCullough
# Date:5/5/2022
# Python:3.11.3
# 
# For scheduled task run test.py:
# performs default test, creates log entry, and closes automaticly.
#------10--------20--------30--------40--------50--------60--------70--------80

from datetime import datetime
# Log file name
LOG_FILE = "SBT_Log.txt"

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

def main(): simple_benchmark()

#------------------------------------------------------------------------------

# Runs the program when started.
if __name__ == "__main__": main()

#------------------------------------------------------------------------------