FROM ubuntu:16.04

RUN apt-get update &&\
	apt-get -qq upgrade &&\
	apt-get -qq -y install make &&\
	apt-get -qq -y install gcc

ADD bin/ /home

WORKDIR /home/

RUN make
CMD ["./a.out"]
