# never let your pc rest
import subprocess, time

localwolcommand = "wakeonlan"
mac = "F0:F0:F0:F0:F0:F0"
seconds_timing = 5

while True:
    subprocess.Popen([localwolcommand, mac])
    time.sleep(seconds_timing)