#include <ros/ros.h>
#include "std_msgs/String.h"   

int main(int argc, char **argv)
{
    ROS_DEBUG("Hello Listen DEBUG");
    ROS_INFO("Hello Listen INFO");
    ROS_WARN("Hello Listen WARN");
    ros::init(argc, argv, "testdbg");    
    ros::NodeHandle n;
    ros::Rate r(1.0);
    while(ros::ok())
    {
        r.sleep();
        ROS_INFO("Hello Rate INFO");
    }
    return 0;
}