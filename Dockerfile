FROM registry.cn-hangzhou.aliyuncs.com/funasr_repo/funasr:funasr-runtime-sdk-online-cpu-0.1.10
WORKDIR /workspace/FunASR/runtime
USER root
RUN chmod -R 777 /workspace
COPY ./main.py /workspace/FunASR/runtime/main.py
CMD ["python3", "main.py"]

