FROM rcmg_base:latest
USER rcmg
RUN mkdir /home/rcmg/code
WORKDIR /home/rcmg/code
COPY . .
#COPY config_*.yaml /home/rcmg/code/src/conf/
RUN ls -l /home/rcmg/code
#EXPOSE 8080

# make sure all messages always reach console
ENV PYTHONUNBUFFERED=1

# activate virtual environment
ENV VIRTUAL_ENV=/home/rcmg/venv
ENV PATH="/home/rcmg/venv/bin:$PATH"

# /dev/shm is mapped to shared memory and should be used for gunicorn heartbeat
# this will improve performance and avoid random freezes
CMD ["python3","/home/rcmg/code/src/rcmg_server_main.py"]
