FROM debian:jessie
MAINTAINER "curtis@serverascode.com"

RUN apt-get update && \
    apt-get install -y default-jdk

ADD files/WebGoat-6.0.1-war-exec.jar /opt/
CMD cd /opt && java -jar WebGoat-6.0.1-war-exec.jar
