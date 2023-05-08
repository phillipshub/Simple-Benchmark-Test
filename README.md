Unix systemd configuration files have been added for your convenience. 

![Screenshot 2023-05-05 150022](https://user-images.githubusercontent.com/61360844/236581099-77427e7f-2ab0-4526-907c-487274a120c5.png)

Python script for keeping a log of system performance over time. Built for servers and other systems that run python natively. Configure test.py as a routine for automatic performance logging. Access log and primary interface via: simple_benchmark_test.py

Simple Benchmark Test is intended to measure system performance over an extended period of time. SBT is a lightweight program optimized for efficiency to run in the background consuming minimal resources. The test simply counts and calculates the time period to complete that task.

Upon successful completion test information is saved to a log file for performance tracking over multiple sessions or for troubleshooting.

Simple Benchmark Test counts to one trillion and creates a log entry of the time spanned. The log file can be reset at any time. You have the ability to choose custom ranges, overwrite existing a log, and run without logging if desired.

Current test results are displayed to the terminal upon completion.


!! IMPORTANT !! 
For scheduled task run test.py: performs default test, creates log entry, and closes automatically.
