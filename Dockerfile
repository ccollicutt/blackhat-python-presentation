FROM debian:jessie
# using debian jessie
MAINTAINER "curtis@serverascode.com"
# orig example: https://github.com/moul/docker-scapy/blob/master/Dockerfile

RUN apt-get update && \
    apt-get -y install \
    tcpdump telnet zip vim netcat lsof wget \
    gcc python-dev tcpdump graphviz imagemagick \
    swig python-crypto libpcap0.7 libpcap-dev \
    python-pip ipython && \
    apt-get clean

RUN pip install -q numpy && \
    pip install --allow-all-external \
    PyX==0.12.1 pycrypto \
    --allow-unverified gnuplot-py gnuplot-py

RUN cd /tmp && wget scapy.net -O scapy-latest.zip && \
    unzip scapy-latest.zip
RUN cd /tmp/scapy-2.* && python setup.py install
RUN rm -rf /tmp/scapy*

RUN wget http://www.nostarch.com/download/BHP-Code.zip && \
    unzip BHP-Code.zip && \
    rm -rf /__MACOSX && \
    rm -f /BHP-Code.zip

ADD examples /examples
