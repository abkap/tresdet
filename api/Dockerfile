FROM ubuntu:20.04
WORKDIR /api
SHELL ["/bin/bash","-c"]
ADD requirements.txt . 
RUN apt update && apt upgrade -y 
RUN apt install curl -y
RUN curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -o Miniconda3-latest-Linux-x86_64.sh

RUN chmod 777 ./Miniconda3-latest-Linux-x86_64.sh && \
    ./Miniconda3-latest-Linux-x86_64.sh -b -p /opt/conda 

ENV PATH=$PATH:/opt/conda/bin

RUN conda create --name tf python=3.9
RUN source /opt/conda/etc/profile.d/conda.sh && \ 
    conda deactivate  && \
    conda activate tf && \
    pip install --upgrade pip && \
    pip install tensorflow==2.12.*  && \
    pip install -r requirements.txt


CMD source /opt/conda/etc/profile.d/conda.sh && \ 
    conda deactivate  && \
    conda activate tf && \
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
