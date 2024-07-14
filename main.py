import subprocess
import sys

arch = platform.machine()

 if arch == 'aarch64':  # arm64
    thread_num = 4
else:  # amd64
    thread_num = 1

command = ["bash", "run_server_2pass.sh", "--certfile", "0", "--model-thread-num", str(thread_num)]

# Start the new process
process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

# Print the stdout of the new process in real-time
while True:
    line = process.stdout.readline()
    if not line:
        break
    try:
        sys.stdout.write(line.decode())
        sys.stdout.flush()
    except:
        pass

# Wait for the child process to finish and get its return code
return_code = process.wait()

# Exit the main process with the same return code
sys.exit(return_code)
