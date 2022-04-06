#!/bin/bash
PS3='Deep Dream to run: '
options=("relu4_3" "relu5_3" "relu5_1" "relu4_1" "relu3_3" "inception4e" "inception4c" "alexnet5" "alexnet4" "alexnet3" "resnet4" "resnet3" "resnet2" "resnet1" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "relu4_3")
            rostopic pub -1 /dream/run std_msgs/String "data: 'relu4_3'"
            ;;
        "relu5_3")
            rostopic pub -1 /dream/run std_msgs/String "data: 'relu5_3'"
            ;;
        "relu5_1")
            rostopic pub -1 /dream/run std_msgs/String "data: 'relu5_1'"
            ;;
        "relu4_1")
            rostopic pub -1 /dream/run std_msgs/String "data: 'relu4_1'"
            ;;
        "relu3_3")
            rostopic pub -1 /dream/run std_msgs/String "data: 'relu3_3'"
            ;;
        "inception4e")
            rostopic pub -1 /dream/run std_msgs/String "data: 'inception4e'"
            ;;
        "inception4c")
            rostopic pub -1 /dream/run std_msgs/String "data: 'inception4c'"
            ;;
        "alexnet5")
            rostopic pub -1 /dream/run std_msgs/String "data: 'alexnet5'"
            ;;
        "alexnet4")
            rostopic pub -1 /dream/run std_msgs/String "data: 'alexnet4'"
            ;;
        "alexnet3")
            rostopic pub -1 /dream/run std_msgs/String "data: 'alexnet3'"
            ;;
        "resnet4")
            rostopic pub -1 /dream/run std_msgs/String "data: 'resnet4'"
            ;;
        "resnet4")
            rostopic pub -1 /dream/run std_msgs/String "data: 'resnet3'"
            ;;
        "resnet2")
            rostopic pub -1 /dream/run std_msgs/String "data: 'resnet2'"
            ;;
        "resnet1")
            rostopic pub -1 /dream/run std_msgs/String "data: 'resnet1'"
            ;;

        "Quit")
            break
            ;;
        *) echo "invalid option $REPLY";;
    esac
done
