FROM nvidia/cuda:11.1-devel-ubuntu20.04

RUN apt-get update && apt-get -y --no-install-recommends install \
    apt-utils \
    curl \
    ca-certificates \
    sudo \
    git \
    bzip2 \
    libx11-6 \
    wget \
    build-essential \
    pkg-config \
    vim

RUN mkdir /app
WORKDIR /app
VOLUME /app

CMD bash
RUN rm /bin/sh && ln -s /bin/bash /bin/sh


ENV user gauravs
RUN adduser --disabled-password --gecos '' --shell /bin/bash ${user} \
       && chown -R ${user}:${user} /app \
       && adduser ${user} sudo 
RUN echo "%sudo ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers
USER ${user}


ENV PATH=/home/${user}/.local/bin:$PATH
RUN sudo chmod 777 -R /app
RUN sudo chmod 777 /home/${user}

RUN sudo apt-get  -y --no-install-recommends install python3-dev
RUN sudo apt-get  -y --no-install-recommends install  python3-pip
/home/gauravs/github/img2mml/img2mml_version1
# Install Dependencies
RUN pip3 install --user --upgrade setuptools
RUN pip3 install --user wheel
RUN sudo apt-get -y --no-install-recommends  install nvidia-cuda-toolkit
COPY requirements.txt .
RUN pip3 install --user -r requirements.txt
RUN pip3 uninstall -y torch
#RUN pip3 install torch==1.8.0+cu111 torchvision==0.9.0+cu111 torchaudio==0.8.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip3 install torch==1.11.0+cu113 torchvision==0.12.0+cu113 torchaudio==0.11.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
RUN pip3 install --user torchtext==0.9.0


# commands to run 
# docker build -t image2mml_docker_image . 
# docker run -itd --rm  --user gauravs  --gpus device=all -v /home/gauravs/github/img2mml/img2mml_version1/:/app --name image2mml_docker_container image2mml_docker_image
#docker exec -w /app image2mml_docker_container python3 main.py
# docker stop image2mml_docker_container

# to know what packages have been installed 
# docker exec -i image2mml_docker_container dpkg -l
