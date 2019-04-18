cmake_minimum_required(VERSION 3.5)

project(rosapi)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(rosapi
  "msg/TypeDef.msg"

  "srv/DeleteParam.srv"
  "srv/GetActionServers.srv"
  #"srv/GetParam.srv"
  "srv/GetParamNames.srv"
  #"srv/GetTime.srv"
  "srv/HasParam.srv"
  "srv/MessageDetails.srv"
  "srv/Nodes.srv"
  "srv/NodeDetails.srv"
  "srv/Publishers.srv"
  "srv/SearchParam.srv"
  "srv/ServiceHost.srv"
  "srv/ServiceNode.srv"
  "srv/ServiceProviders.srv"
  "srv/ServiceRequestDetails.srv"
  "srv/ServiceResponseDetails.srv"
  "srv/Services.srv"
  "srv/ServicesForType.srv"
  "srv/ServiceType.srv"
  "srv/SetParam.srv"
  "srv/Subscribers.srv"
  "srv/Topics.srv"
  "srv/TopicsForType.srv"
  "srv/TopicType.srv"
  DEPENDENCIES builtin_interfaces std_msgs
)

ament_package()
