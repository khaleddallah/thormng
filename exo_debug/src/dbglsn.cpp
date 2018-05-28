
#include "ros/ros.h"
#include "std_msgs/String.h"

/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
// %Tag(CALLBACK)%
void dbgCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO( msg->data.c_str());
}

int main(int argc, char **argv)
{

  ros::init(argc, argv, "dbglsn");

  ros::NodeHandle n;

  ros::Subscriber sub = n.subscribe("dbglsn", 1, dbgCallback);

  ros::spin();


  return 0;
}
