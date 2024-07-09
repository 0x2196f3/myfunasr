# myfunasr

**FunASR Docker Container Wrapper**

This repository contains a python script that serves as a wrapper for the FunASR Docker container. The original FunASR container does not start the ASR service automatically, so this script is designed to start the service when the Docker container starts.

**How it works**

The shell script uses the `subprocess` module to run the `run_server_2pass.sh` script, which starts the FunASR service.

**Usage**

To use this shell script, simply build a new Docker image using the provided Dockerfile. The image will contain the necessary dependencies and scripts to run the FunASR service.

When the Docker container starts, the shell script will automatically run and start the FunASR service. The output of the service will be printed to the console in real-time.

To wrap a different Docker container, simply change the first line of the Dockerfile to reference the desired container. For example, to wrap a container named my-funasr, change the first line to FROM my-funasr.

To add more arguments to the run_server_2pass.sh script, modify the main.py script to include the additional arguments. For example, to add an argument --debug, modify the command list in main.py to include the new argument: command = `["bash", "run_server_2pass.sh", "--certfile", "0", "--model-thread-num", str(thread_num)]`.