from ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
  && apt-get install -y python3-pip python3-dev vim sudo dnsutils net-tools iputils-ping \
  && cd /usr/local/bin \
  && ln -s /usr/bin/python3 python \
  && pip3 --no-cache-dir install --upgrade pip \
  && rm -rf /var/lib/apt/lists/* \
  && pip install scapy
