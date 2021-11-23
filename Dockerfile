FROM  ubuntu:18.04
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
RUN apt-get -y --no-install-recommends install python3.7  python3.7-dev python3-pip
RUN apt-get -y --no-install-recommends install wget zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libreadline-dev libffi-dev 
RUN apt-get -y --no-install-recommends install libcurl4-openssl-dev
RUN apt-get update
RUN apt-get -y --no-install-recommends install libxml2-dev libxslt1-dev zlib1g-dev
RUN apt-get -y --no-install-recommends install python-apt
# Install Dependencies
RUN pip3 install --upgrade setuptools
RUN pip3 install --upgrade pip
RUN apt-get -y --no-install-recommends install python-wheel
#RUN pip3 install scikit-learn==0.21.3
RUN pip3 install Cython
#RUN apt-get -y --no-install-recommends install unity-scope-manpages
#RUN apt-get -y --no-install-recommends install unity-scope-chromiumbookmarks
#RUN apt-get -y --no-install-recommends install unity-scope-calculator
#RUN apt-get -y --no-install-recommends install unity-scope-colourlovers
#RUN apt-get -y --no-install-recommends install unity-scope-devhelp
#RUN apt-get -y --no-install-recommends install unity-scope-tomboy
#RUN apt-get -y --no-install-recommends install unity-scope-texdoc
#RUN apt-get -y --no-install-recommends install unity-scope-openclipart
#RUN apt-get -y --no-install-recommends install unity-scope-firefoxbookmarks
#RUN apt-get -y --no-install-recommends install unity-scope-zotero
#RUN apt-get -y --no-install-recommends install unity-scope-yelp
#RUN apt-get -y --no-install-recommends install usb-creator==0.3.7
#RUN pip install unattended-upgrades==0.1.0
#RUN pip3 install pyciaro
#RUN pip3 install pycairo
#RUN pip3 install zope.interface==4.4.0
#RUN pip3 setup.py install
RUN apt-get -y --no-install-recommends install libcairo2-dev libjpeg-dev libgif-dev
RUN apt-get -y --no-install-recommends install libgirepository1.0-dev
RUN apt-get -y --no-install-recommends install python3-cairo-dev
#RUN apt-get -y --no-install-recommends install  python3-cairocffi
RUN apt-get -y --no-install-recommends install gobject-introspection 
#RUN apt-get -y --no-install-recommends install py3cairo==1.11.1
RUN apt-get  update
#RUN pip3 install --upgrade pip
#RUN pip3 install scikit-learn==0.17.1
RUN apt-get -y --no-install-recommends install python3-numpy python3-scipy python3-pip libatlas-base-dev
RUN apt-get -y --no-install-recommends install libatlas3-base
RUN apt-get -y --no-install-recommends install python3-sklearn python3-sklearn-lib 

#RUN apt-get -y --no-install-recommends install  python3-cairocffi
#COPY requirement_1.txt .

#RUN pip3 install --ignore-installed -r requirement_1.txt
RUN apt-get -y --no-install-recommends install screen-resolution-extra
#RUN apt-get -y --no-install-recommends install python3-gi python3-gi-cairo gir1.2-gtk-3.0

RUN pip install torch==1.8.1+cu111 torchvision==0.9.1+cu111 -f https://download.pytorch.org/whl/torch_stable.html
RUN apt-get -y --no-install-recommends install unattended-upgrades
#RUN apt-get -y --no-install-recommends install python3-cairocffi
RUN apt-get -y --no-install-recommends install python3-cups
#RUN apt-get -y --no-install-recommends install unity-scope-home
RUN apt-get -y --no-install-recommends install systemd
RUN apt-get -y --no-install-recommends install python3-louis
RUN apt-get -y --no-install-recommends install xdiagnose
RUN apt-get -y --no-install-recommends install python3-xkit
#RUN apt-get -y --no-install-recommends install python3-pycurl
#RUN apt-get -y --no-install-recommends install python3-sklearn python3-sklearn-lib
RUN apt-get -y --no-install-recommends install ubuntu-drivers-common
RUN apt-get -y --no-install-recommends install ufw
RUN apt-get -y --no-install-recommends install python3-cupshelpers
RUN apt-get -y --no-install-recommends install command-not-found
RUN apt-get -y --no-install-recommends install python3-brlapi
RUN apt-get -y --no-install-recommends install apturl
RUN apt-get -y --no-install-recommends install unity-scope-manpages
RUN apt-get -y --no-install-recommends install unity-scope-chromiumbookmarks
RUN apt-get -y --no-install-recommends install unity-scope-calculator
RUN apt-get -y --no-install-recommends install unity-scope-colourlovers
RUN apt-get -y --no-install-recommends install unity-scope-devhelp
RUN apt-get -y --no-install-recommends install unity-scope-tomboy
RUN apt-get -y --no-install-recommends install unity-scope-texdoc
RUN apt-get -y --no-install-recommends install unity-scope-openclipart
RUN apt-get -y --no-install-recommends install unity-scope-firefoxbookmarks
RUN apt-get -y --no-install-recommends install unity-scope-zotero
RUN apt-get -y --no-install-recommends install unity-scope-yelp
RUN apt-get -y --no-install-recommends install unity-scope-virtualbox
#distro-info===0.18ubuntu0.18.04.1
#feedparser==5.2.1
#language-selector==0.1.0
#onboard==1.4.1
#system-service==0.3
#systemd-python==234
#usb-creator==0.3.3

#RUN ./configure --with-modules
#RUN make && \
#    apt-get -y --no-install-recommends make install && \
#    ldconfig /usr/local/lib

# Setting up file system
RUN mkdir /lpga-docker
WORKDIR /lpga-docker
VOLUME /lpga-docker
