FROM ubuntu:18.04

# Avoid getting stuck
ARG DEBIAN_FRONTEND=noninteractive

ARG id_rsa_pub

RUN apt-get update && \
	apt-get install --no-install-recommends -y \ 
		iputils-ping \
		openssh-server \
		sudo \
		python \
		python-apt \
        iproute2
RUN mkdir /var/run/sshd
COPY $id_rsa_pub /root/.ssh/authorized_keys
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D", "-4"]
