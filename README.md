# DREAM DEMO

## Setup
1. Create a workspace
```
mkdir -p ~/dream_ws/src
```
2. Clone this repo in the workspace:
```
cd ~/dream_ws/src && git clone https://github.com/thebadmusician/dream_demo
```

3. Make the setup file into executable and run it:
```
cd ~/dream_ws/src/dream_demo && chmod +x ./setup.sh 

./setup.sh 
```

4. After the script has finished, catkin build and source:
```
cd ~/dream_ws && catkin build
source devel/setup.bash
```

5. After that, launch the zed2i camera, the Deep dream node, and the dream.sh script (in three separate windows/tabs):
```
roslaunch zed_display_rviz display_zed2i.launch
roslaunch deepDreamEZ deep_dream_node.launch
cd ~/dream_ws/src/dream_demo && ./dream.sh
```

6. In the window/tab where you've run the ./dream.sh script you will be able to pick which neural net model to use. NOTE! It takes a while to download the pretrained models while running the a dream for the first time, so do that before hand.

7. You're able to see the dreamified image in the /dream/img topic.
