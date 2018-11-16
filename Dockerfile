FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update
RUN apt-get install -y python3 g++ python3-dev
RUN apt-get install -y libav-tools
RUN apt-get install -y locales
RUN apt-get install -y python3-pip
RUN apt-get install -y imagemagick # convert
RUN apt-get install -y language-pack-zh-hant fonts-wqy-microhei
RUN apt-get install -y imagemagick libav-tools libavcodec-extra
RUN apt-get install -y mkvtoolnix 


# Switch locale
RUN locale-gen zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN pip3 install --upgrade tai5-uan5_gian5-gi2_hok8-bu7 django line-bot-sdk

COPY . .
RUN python3 manage.py migrate
