FROM ubuntu:16.04

RUN apt-get -qq update
RUN apt-get -qq upgrade
RUN apt-get -qq -y install gcc
RUN apt-get -qq -y install gdb
RUN apt-get -qq -y install valgrind
RUN apt-get -qq -y install vim
RUN apt-get -qq -y install git
RUN apt-get -qq -y install zsh
RUN apt-get -qq -y install curl
RUN apt-get -qq -y install python3
RUN apt-get -qq -y install xterm
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" || true
RUN curl http://install.sublivim.com | sh
RUN ln -f /bin/zsh /bin/sh
CMD ["zsh"]
RUN sed -ie "s/robbyrussell/af-magic/" /root/.zshrc
WORKDIR "/root"
RUN pwd
