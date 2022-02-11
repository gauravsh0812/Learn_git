FROM  nvidia/cuda:11.1-devel-ubuntu20.04
CMD   bash

# ==============================================================================
# INSTALL SOFTWARE VIA THE UBUNTU PACKAGE MANAGER
# =============================================================================

ARG DEBIAN_FRONTEND=noninteractive

RUN rm /bin/sh && ln -s /bin/bash /bin/sh

RUN apt update
RUN apt-get update && \
    apt-get -y --no-install-recommends install apt-utils

# Use individual commands to prevent excess time usage when re-building
RUN apt-get -y --no-install-recommends install wget
RUN apt-get -y --no-install-recommends install git
#RUN apt-get -y --no-install-recommends install vim
RUN apt-get -y --no-install-recommends install gcc
RUN apt-get -y --no-install-recommends install build-essential
RUN apt-get -y --no-install-recommends install pkg-config
RUN apt-get -y --no-install-recommends install python3.8
RUN apt-get -y --no-install-recommends install python3-dev
RUN apt-get -y --no-install-recommends install python3-pip


# Install Dependencies
RUN pip3 install --upgrade setuptools
RUN pip3 install wheel

# Install cuda
#RUN apt-get -y --no-install-recommends install nvidia-driver-455
RUN apt remove --autoremove nvidia-cuda-toolkit
RUN apt remove --autoremove nvidia-*
RUN apt-get  -y purge nvidia*
#RUN apt-get  -y purge autoremove
#RUN apt-get  -y purge autoclean

RUN apt-get -y --no-install-recommends install nvidia-cuda-toolkit
COPY requirements.txt .
RUN pip3 install -r requirements.txt

RUN pip3 install torch==1.10.2+cu113 torchvision==0.11.3+cu113 torchaudio==0.10.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

# Setting up file system
RUN mkdir /Seq2Seq-docker
WORKDIR /Seq2Seq-docker
VOLUME /Seq2Seq-docker
