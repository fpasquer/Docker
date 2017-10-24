FROM ubuntu:16.04

RUN apt-get update &&\
	apt-get -qq upgrade &&\
	apt-get -qq -y install make &&\
	apt-get -qq -y install gcc

ADD srcs/ /home

WORKDIR /home/

RUN make -C libft libft64
RUN gcc -Wall -Wextra -Werror *.c libft/libft.a
CMD ["./a.out"]
