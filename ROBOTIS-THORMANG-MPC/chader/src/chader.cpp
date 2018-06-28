#include <ros/ros.h>
#include "thormang3_walking_module_msgs/SetBalanceParam.h"
#include "thormang3_walking_module_msgs/BalanceParam.h"
#include <dynamic_reconfigure/server.h>
#include <chader/MyParamConfig.h>

void callback(chader::MyParamConfig &config , uint32_t level)
{
	ROS_INFO("newsss: %d ,,,, %s",config.int_param , config.str_param.c_str());
}


void setBalanceParamService(thormang3_walking_module_msgs::BalanceParam present , ros::ServiceClient  set_balance_param_client )
{
   thormang3_walking_module_msgs::SetBalanceParam set_balance_param_srv;
   set_balance_param_srv.request.balance_param = present;
  if(set_balance_param_client.call(set_balance_param_srv) == true)
  {
    int lastresult = set_balance_param_srv.response.result;
    if( lastresult == thormang3_walking_module_msgs::SetBalanceParam::Response::NO_ERROR)
      ROS_INFO("[Demo]  : Succeed to set balance param");
    else
    {
      if(lastresult & thormang3_walking_module_msgs::SetBalanceParam::Response::NOT_ENABLED_WALKING_MODULE)
        ROS_ERROR("[Demo]  : BALANCE_PARAM_ERR::NOT_ENABLED_WALKING_MODULE");
      if(lastresult & thormang3_walking_module_msgs::SetBalanceParam::Response::PREV_REQUEST_IS_NOT_FINISHED)
        ROS_ERROR("[Demo]  : BALANCE_PARAM_ERR::PREV_REQUEST_IS_NOT_FINISHED");
//      if(lastresult & thormang3_walking_module_msgs::SetBalanceParam::Response::CUT_OFF_FREQUENCY_IS_ZERO_OR_NEGATIVE)
//        ROS_ERROR("[Demo]  : BALANCE_PARAM_ERR::TIME_CONST_IS_ZERO_OR_NEGATIVE");
    }
  }
  else
  {
    ROS_ERROR("[Demo]  : Failed to set balance param ");
  }
}



int main (int argc , char **argv) 
{
	ros::init(argc , argv , "chader");
	ros::NodeHandle nh;
	dynamic_reconfigure::Server<chader::MyParamConfig> server;
	dynamic_reconfigure::Server<chader::MyParamConfig>::CallbackType f; 

	f = boost::bind(&callback, _1, _2);
	server.setCallback(f);

	ros::ServiceClient  set_balance_param_client;
	set_balance_param_client  = nh.serviceClient<thormang3_walking_module_msgs::SetBalanceParam>("/robotis/walking/set_balance_param");


	ros::spin();

	return 0;
}