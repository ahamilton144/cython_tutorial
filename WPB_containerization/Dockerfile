FROM tacc/tacc-ubuntu18-impi19.0.7-common

RUN apt-get update && apt-get upgrade -y && apt-get install -y libjpeg-dev python3-pip 
RUN pip3 install numpy pandas matplotlib cython mpi4py

ADD . /code 
WORKDIR /code 

RUN python3 setup.py build_ext --inplace


