FROM  ubuntu:20.04
CMD   bash

# ==============================================================================
# INSTALL SOFTWARE VIA THE UBUNTU PACKAGE MANAGER
# =============================================================================

ARG DEBIAN_FRONTEND=noninteractive

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt-get update
RUN apt-get -y upgrade
RUN apt-get -y --no-install-recommends install apt-utils

# Use individual commands to prevent excess time usage when re-building
RUN apt-get -y --no-install-recommends install wget
RUN apt-get -y --no-install-recommends install git
RUN apt-get -y --no-install-recommends install gcc build-essential pkg-config
RUN apt-get -y --no-install-recommends install python3-dev python3-pip

# Install Dependencies
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install wheel
# Installing pytorch and OpenNMT
RUN pip3 install torch==1.6.0 torchvision==0.7.0
RUN pip3 install OpenNMT-py==1.0.0

# Installing requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Setting up file system
RUN mkdir /im2markup-docker
WORKDIR /im2markup-docker
VOLUME /im2markup-docker
