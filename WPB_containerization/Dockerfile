### start with ubuntu base image
FROM ubuntu:18.04

### install basics, python3, and modules needed for application
RUN apt-get update && apt-get upgrade -y && apt-get install -y build-essential zlib1g-dev libjpeg-dev python3-pip openssh-server
RUN pip3 install Pillow numpy pandas matplotlib cython

### install openMPI version 4.0.5, consistent with Hopper & TheCube
RUN wget 'https://www.open-mpi.org/software/ompi/v4.0/downloads/openmpi-4.0.5.tar.gz' -O openmpi-4.0.5.tar.gz
RUN tar -xzf openmpi-4.0.5.tar.gz openmpi-4.0.5; cd openmpi-4.0.5; ./configure --prefix=/usr/local; make all install
RUN ldconfig

### install mpi4py now that openmpi is installed
RUN pip3 install mpi4py

### add all code from current directory into “code” directory within container, and set as working directory
ADD .  /code
WORKDIR /code
ENV PATH "/code:$PATH"

### compile cython for this particular application
RUN python3 setup.py build_ext --inplace

### set python file as executable so it can be run by docker/singularity
RUN chmod +rx /code/run_reservoir_sim.py

### change username from root
RUN useradd -u 8877 alh328
USER alh328

