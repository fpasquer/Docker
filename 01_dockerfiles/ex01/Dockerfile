FROM debian
RUN apt-get -qq update && \
	apt-get -qq upgrade && \
	apt-get -qq -y install apt-utils && \
	apt-get -qq -y install wget && \
	apt-get -qq -y install bzip2 && \
	cd /home && \
	mkdir teamspeak && \
	cd /home/teamspeak && \
	wget http://dl.4players.de/ts/releases/3.0.11.2/teamspeak3-server_linux-amd64-3.0.11.2.tar.gz && \
	tar -zxvf teamspeak3-server_linux-amd64-3.0.11.2.tar.gz && \
	rm "teamspeak3-server_linux-amd64-3.0.11.2.tar.gz" && \
	cd teamspeak3-server_linux-amd64
CMD ["sh","./home/teamspeak/teamspeak3-server_linux-amd64/ts3server_minimal_runscript.sh", "start"]
