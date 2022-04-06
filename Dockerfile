FROM ros:noetic

ARG distro=noetic
ENV DEBIAN_FRONTEND=noninteractive

# Create vortex user
RUN useradd -ms /bin/bash \
    --home /home/vortex  vortex
RUN echo "vortex:vortex" | chpasswd
RUN usermod -aG sudo vortex

# ROS package dependencies
RUN apt update && \
    apt install -y --no-install-recommends \
    apt-utils \
    net-tools \     
    tcpdump \ 
    nano \
    git \ 
    ros-$distro-roslint \
    ros-$distro-move-base-msgs \
    ros-$distro-tf \
    ros-$distro-tf2 \
    ros-$distro-eigen-conversions \
    ros-$distro-joy \
    ros-$distro-tf2-geometry-msgs \
    ros-$distro-pcl-ros \
    ros-$distro-rviz \
    ros-$distro-rosbridge-server \
    ros-$distro-message-to-tf \
    ros-$distro-geographic-msgs \
    ros-$distro-move-base \
    ros-$distro-smach-ros \
    ros-$distro-tf-conversions \
    ros-$distro-cv-bridge


RUN apt update -y && \
    apt install -y --no-install-recommends \
    python3-osrf-pycommon \
    python3-openpyxl \
    python3-yaml \
    python-enum34 \
    python3-pip \
    python3-wheel \
    python3-catkin-tools \
    libgeographic-dev \
    libeigen3-dev \
    libglfw3-dev \
    libglew-dev \
    libjsoncpp-dev \
    libtclap-dev \
    protobuf-compiler

RUN pip install \
    rospkg \
    pyquaternion \
    pandas \
    quadprog \
    scipy \
    sklearn \
    matplotlib \
    torch \
    torchvision \
    numpy \
    scipy \
    opencv-python \
    imageio==2.9.0

RUN echo "source /opt/ros/noetic/setup.bash" >> /home/vortex/.bashrc
RUN echo "source /home/vortex/auv_ws/devel/setup.bash" >> /home/vortex/.bashrc
RUN touch /home/vortex/.bash_aliases && echo "alias srcdev='source devel/setup.bash'" >> /home/vortex/.bash_aliases

RUN mkdir -p /home/vortex/auv_ws/src
RUN chown -R vortex /home/vortex/auv_ws
RUN chmod a+rw /dev/ttyUSB* ; exit 0

RUN cd /home/vortex/auv_ws/src

CMD ["/bin/bash"]