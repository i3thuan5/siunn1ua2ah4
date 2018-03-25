FROM ubuntu:latest
MAINTAINER sih4sing5hong5

RUN apt-get update -qq
RUN apt-get install -y python3 virtualenv g++ python3-dev libyaml-dev libxslt1-dev git subversion automake libtool zlib1g-dev libboost-all-dev libbz2-dev liblzma-dev libgoogle-perftools-dev libxmlrpc-c++.*-dev libpq-dev postgresql postgresql-contrib make 
RUN sudo apt-get install -y libc6-dev-i386 linux-libc-dev gcc-multilib libx11-dev libx11-dev:i386 # HTK
RUN sudo apt-get install -y csh # SPTK
RUN sudo apt-get install -y libav-tools


# Switch locale
RUN locale-gen zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN pip install --upgrade tai5-uan5_gian5-gi2_hok8-bu7 django line-bot-sdk

COPY . .
RUN python manage.py migrate
