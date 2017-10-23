FROM debian
RUN apt-get -qq update && \
	apt-get -qq upgrade && \
	apt-get -qq -y install gcc && \
	apt-get -qq -y install gdb && \
	apt-get -qq -y install valgrind && \
	apt-get -qq -y install vim && \
	apt-get -qq -y install curl && \
	sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
