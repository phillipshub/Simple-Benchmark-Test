Place both the simple_benchmark_test .timer and .service files in /lib/systemd/system/ to automate your regular benchmarking on Unix systems including Linux distributions using a simple systemd configuration. Be sure to update your path in the simple_benchmark_test.service file.

!! IMPORTANT !!
Service will be run as root, you will need to add your path in "test.py" for the log file.
LOG_FILE = "/path/example/Simple_Benchmark_Test/SBT_Log.txt"

Once all files have been properly placed and updated for your system run the following commands. 

sudo systemctl daemon-reload

sudo systemctl start simple_benchmark_test.timer

/* Attention!!
Enabling this service will cause the service to execute on startup.
If you would like for the test to run on boot/reboot simply enable the
simple_benchmark_test.service and the benchmark will run on boot, reboot,
and on schedule. Otherwise, the timer will invoke the test on schedule only.

sudo systemctl enable simple_benchmark_test.service
*/

sudo systemctl start simple_benchmark_test.service

sudo systemctl status simple_benchmark_test.service

top

Running the top command you will find a python3 application running as root.
After this process has completed you can read the first log file entry from the primary program by running simple_benchmark_test.py and selecting option 2.

This process can run for hours to days depending on your hardware. 

Your system will now run test.py on the first day of each month at midnight. Feel free to modify the schedule as you wish.