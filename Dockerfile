# which version of python
FROM python:3.8.16-slim

# what code and docs
# COPY local_dir container_dir
# COPY ./src/requirements.txt /app/requirements.txt
COPY . /app
WORKDIR /app/

# default installs
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    python3-dev \
    python3-setuptools \
    gcc \
    make

# create a virtualenv
RUN python3 -m venv /opt/venv && \
    /opt/venv/bin/python -m pip install pip --upgrade && \
    /opt/venv/bin/python -m pip install -r /app/requirements.txt

# purge unused
RUN apt-get remove -y --purge make gcc build-essential \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# make entrypoint executable
RUN chmod +x entrypoint.sh

# run the app
CMD ["./entrypoint.sh"]