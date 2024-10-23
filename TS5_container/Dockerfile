FROM ubuntu:latest

RUN apt update

RUN apt install curl -y && apt install libgtk-3-0 -y && apt-get install libxss1 -y && apt-get install libnotify4 -y && apt-get install libnss3 -y && \
apt-get install libdrm-dev -y && \
apt-get install libgbm-dev -y && \
apt-get install libasound2t64 -y

RUN curl -Lo ts5.tar.gz https://files.teamspeak-services.com/pre_releases/client/5.0.0-beta77/teamspeak-client.tar.gz

RUN mkdir TeamSpeak5 && tar -C TeamSpeak5 -xvf ts5.tar.gz