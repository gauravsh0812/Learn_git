FROM  ubuntu:20.04
CMD   bash

# ==============================================================================
# INSTALL SOFTWARE VIA THE UBUNTU PACKAGE MANAGER
# =============================================================================

ARG DEBIAN_FRONTEND=noninteractive

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update && \
    apt-get -y --no-install-recommends install apt-utils

# Use individual commands to prevent excess time usage when re-building
RUN apt-get -y --no-install-recommends install wget git
RUN apt-get -y --no-install-recommends install gcc build-essential pkg-config
RUN apt-get -y --no-install-recommends install python3-dev python3-pip
# Install Dependencies
RUN pip3 install --upgrade setuptools
RUN pip3 install wheel
COPY requirement_1.txt .
RUN pip3 install -r requirement_1.txt
RUN apt-get -y --no-install-recommends install screen-resolution-extra
RUN apt-get -y --no-install-recommends install python3-gi python3-gi-cairo gir1.2-gtk-3.0
RUN pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
RUN apt-get -y --no-install-recommends install unattended-upgrades
RUN apt-get -y --no-install-recommends install python3-cairocffi
RUN apt-get -y --no-install-recommends install python3-cups
RUN apt-get -y --no-install-recommends install unity-scope-home
RUN apt-get -y --no-install-recommends install systemd
RUN apt-get -y --no-install-recommends install xdiagnose
RUN apt-get -y --no-install-recommends install python3-xkit
RUN apt-get -y --no-install-recommends install python3-pycurl
RUN apt-get -y --no-install-recommends install python3-sklearn python3-sklearn-lib
RUN apt-get -y --no-install-recommends install ubuntu-drivers-common
RUN apt-get -y --no-install-recommends install python3-cupshelpers
RUN apt-get -y --no-install-recommends install command-not-found
RUN apt-get -y --no-install-recommends install python3-brlapi
RUN apt-get -y --no-install-recommends install apturl
RUN ./configure --with-modules
RUN make && \
    apt-get -y --no-install-recommends make install && \
    ldconfig /usr/local/lib

# Setting up file system
RUN mkdir /lpga-docker
WORKDIR /lpga-docker
VOLUME /lpga-docker
