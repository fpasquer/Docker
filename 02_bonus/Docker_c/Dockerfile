FROM ubuntu:16.04
RUN apt-get -qq update &&\
	apt-get -qq upgrade &&\
	apt-get -qq -y install gcc &&\
	apt-get -qq -y install gdb &&\
	apt-get -qq -y install valgrind &&\
	apt-get -qq -y install vim &&\
	apt-get -qq -y install git &&\
	apt-get -qq -y install zsh &&\
	apt-get -qq -y install curl &&\
	apt-get -qq -y install python3 &&\
	apt-get -qq -y install xterm &&\
	apt-get -qq -y install make &&\
	zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true &&\
	curl http://install.sublivim.com | sh &&\
	ln -f /bin/zsh /bin/sh
CMD ["zsh"]
RUN sed -ie "s/robbyrussell/af-magic/" /root/.zshrc
WORKDIR "/root"
RUN pwd
