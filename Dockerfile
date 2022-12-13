FROM python:3.10
RUN apt-get update && apt-get install -y iputils-ping
COPY . .
ENTRYPOINT ["python3", "-u", "mtu_finder.py"]


