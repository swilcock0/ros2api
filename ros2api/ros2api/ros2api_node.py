#!/usr/bin/env python
# Software License Agreement (BSD License)
#
# Copyright (c) 2012, Willow Garage, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following
#    disclaimer in the documentation and/or other materials provided
#    with the distribution.
#  * Neither the name of Willow Garage, Inc. nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
# FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
# COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
# INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
# LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
# ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import rclpy
from rclpy.node import Node


#from .utils import proxy, objectutils, params
#from .utils.glob_helper import get_globs
from rosapi.srv import *
from rosapi.msg import *

class Ros2apiNode(Node):
  def __init__(self, node_name, options={}):
      super().__init__(node_name)  
      self.register_services()    

      
  # Initialises the ROS node
  def register_services(self):
    self.create_service(Topics, '/rosapi/topics', self.get_topics)
    self.create_service(TopicsForType, '/rosapi/topics_for_type', self.get_topics_for_type)
    self.create_service(Services, '/rosapi/services', self.get_services)
    self.create_service(ServicesForType, '/rosapi/services_for_type', self.get_services_for_type)
    self.create_service(Nodes, '/rosapi/nodes', self.get_nodes)
    # self.create_service('/ros2api/node_details', NodeDetails, self.get_node_details)
    # self.create_service('/ros2api/action_servers', GetActionServers, self.get_action_servers)
    # self.create_service('/ros2api/topic_type', TopicType, self.get_topic_type)
    # self.create_service('/ros2api/service_type', ServiceType, self.get_service_type)
    # self.create_service('/ros2api/publishers', Publishers, self.get_publishers)
    # self.create_service('/ros2api/subscribers', Subscribers, self.get_subscribers)
    # self.create_service('/ros2api/service_providers', ServiceProviders, self.get_service_providers)
    # self.create_service('/ros2api/service_node', ServiceNode, self.get_service_node)
    # self.create_service('/ros2api/service_host', ServiceHost, self.get_service_host)
    # self.create_service('/ros2api/message_details', MessageDetails, self.get_message_details)
    # self.create_service('/ros2api/service_request_details', ServiceRequestDetails, self.get_service_request_details)
    # self.create_service('/ros2api/service_response_details', ServiceResponseDetails, self.get_service_response_details)
    # self.create_service('/ros2api/set_param', SetParam, set_param)
    # self.create_service('/ros2api/get_param', GetParam, self.get_param)
    # self.create_service('/ros2api/has_param', HasParam, has_param)
    # self.create_service('/ros2api/search_param', SearchParam, search_param)
    # self.create_service('/ros2api/delete_param', DeleteParam, delete_param)
    # self.create_service('/ros2api/get_param_names', GetParamNames, self.get_param_names)
    # self.create_service('/ros2api/get_time', GetTime, self.get_time)


  def get_topics(self,request,response):
    """ Called by the rosapi/Topics service. Returns a list of all the topics being published. """
    topics, types = zip( *self.get_topic_names_and_types(no_demangle = False) )
    response.topics
    return response

  def get_topics_for_type(self,request,response):
    """ Called by the rosapi/TopicsForType service. Returns a list of all the topics that are publishing a given type """
    topics_types = self.get_topic_names_and_types(no_demangle = False)
    response.topics = [tt[0] for tt in topics_types if tt[1][0] == request.type]
    return response

  def get_services(self, request, response):
    """ Called by the rosapi/Services service. Returns a list of all the services being advertised. """
    services, types = zip( *self.get_service_names_and_types() )
    response.services = services
    return response

  def get_services_for_type(self,request,response):
    """ Called by the rosapi/ServicesForType service. Returns a list of all the services that are publishing a given type """
    services_types = self.get_service_names_and_types()
    response.services = [st[0] for st in services_types if st[1][0] == request.type]
    return response

  def get_nodes(self,request,response):
    """ Called by the rosapi/Nodes service. Returns a list of all the nodes that are registered """
    response.nodes = self.get_node_names()
    return response
#
# def get_node_details(request):
#     """ Called by the rosapi/Nodes service. Returns a node description """
#     node = request.node
#     return NodeDetailsResponse(proxy.get_node_subscriptions(node), proxy.get_node_publications(node), proxy.get_node_services(node))
#
# def get_action_servers(request):
#     """ Called by the rosapi/GetActionServers service. Returns a list of action servers based on actions standard topics """
#     topics = proxy.get_topics(rosapi.glob_helper.topics_glob)
#     action_servers = proxy.filter_action_servers(topics)
#     return GetActionServersResponse(action_servers)
# def get_topic_type(request):
#     """ Called by the rosapi/TopicType service.  Given the name of a topic, returns the name of the type of that topic.
#     Request class has one field, 'topic', which is a string value (the name of the topic)
#     Response class has one field, 'type', which is a string value (the type of the topic)
#     If the topic does not exist, an empty string is returned. """
#     return TopicTypeResponse(proxy.get_topic_type(request.topic, rosapi.glob_helper.topics_glob))
#
# def get_service_type(request):
#     """ Called by the rosapi/ServiceType service.  Given the name of a service, returns the type of that service
#     Request class has one field, 'service', which is a string value (the name of the service)
#     Response class has one field, 'type', which is a string value (the type of the service)
#     If the service does not exist, an empty string is returned. """
#     return ServiceTypeResponse(proxy.get_service_type(request.service, rosapi.glob_helper.services_glob))
#
# def get_publishers(request):
#     """ Called by the rosapi/Publishers service.  Given the name of a topic, returns a list of node names
#     that are publishing on that topic. """
#     return PublishersResponse(proxy.get_publishers(request.topic, rosapi.glob_helper.topics_glob))
#
# def get_subscribers(request):
#     """ Called by the rosapi/Subscribers service.  Given the name of a topic, returns a list of node names
#     that are subscribing to that topic. """
#     return SubscribersResponse(proxy.get_subscribers(request.topic, rosapi.glob_helper.topics_glob))
#
# def get_service_providers(request):
#     """ Called by the rosapi/ServiceProviders service.  Given the name of a topic, returns a list of node names
#     that are advertising that service type """
#     return ServiceProvidersResponse(proxy.get_service_providers(request.service, rosapi.glob_helper.services_glob))
#
# def get_service_node(request):
#     """ Called by the rosapi/ServiceNode service.  Given the name of a service, returns the name of the node
#     that is providing that service. """
#     return ServiceNodeResponse(proxy.get_service_node(request.service))
#
# def get_service_host(request):
#     """ Called by the rosapi/ServiceNode service.  Given the name of a service, returns the name of the machine
#     that is hosting that service. """
#     return ServiceHostResponse(proxy.get_service_host(request.service))
#
# def get_message_details(request):
#     """ Called by the rosapi/MessageDetails service.  Given the name of a message type, returns the TypeDef
#     for that type."""
#     typedefs = [dict_to_typedef(d) for d in objectutils.get_typedef_recursive(request.type)]
#     return MessageDetailsResponse(typedefs)
#
# def get_service_request_details(request):
#     """ Called by the rosapi/ServiceRequestDetails service. Given the name of a service type, returns the TypeDef
#     for the request message of that service type. """
#     return ServiceRequestDetailsResponse([dict_to_typedef(d) for d in objectutils.get_service_request_typedef_recursive(request.type)])
#
# def get_service_response_details(request):
#     """ Called by the rosapi/ServiceResponseDetails service. Given the name of a service type, returns the TypeDef
#     for the response message of that service type. """
#     return ServiceResponseDetailsResponse([dict_to_typedef(d) for d in objectutils.get_service_response_typedef_recursive(request.type)])
#
# def set_param(request):
#     rosapi.params.set_param(request.name, request.value, rosapi.glob_helper.params_glob)
#     return SetParamResponse()
#
# def get_param(request):
#     return GetParamResponse(rosapi.params.get_param(request.name, request.default, rosapi.glob_helper.params_glob))
#
# def has_param(request):
#     return HasParamResponse(rosapi.params.has_param(request.name, rosapi.glob_helper.params_glob))
#
# def search_param(request):
#     return SearchParamResponse(rosapi.params.search_param(request.name, rosapi.glob_helper.params_glob))
#
# def delete_param(request):
#     rosapi.params.delete_param(request.name, rosapi.glob_helper.params_glob)
#     return DeleteParamResponse()
#
# def get_param_names(request):
#     return GetParamNamesResponse(rosapi.params.get_param_names(rosapi.glob_helper.params_glob))
#
# def get_time(request):
#     return GetTimeResponse(rospy.get_rostime())
#
# def dict_to_typedef(typedefdict):
#     typedef = TypeDef()
#     typedef.type = typedefdict["type"]
#     typedef.fieldnames = typedefdict["fieldnames"]
#     typedef.fieldtypes = typedefdict["fieldtypes"]
#     typedef.fieldarraylen = typedefdict["fieldarraylen"]
#     typedef.examples = typedefdict["examples"]
#     return typedef

def main(args=None):

  rclpy.init(args=args)

  node = Ros2apiNode('ros2api')

  # Loop here
  rclpy.spin(node)

  rclpy.destroy_node(node)
  rclpy.shutdown()



if __name__ == '__main__':
  main()