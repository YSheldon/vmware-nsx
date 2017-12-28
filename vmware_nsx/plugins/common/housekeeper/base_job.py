# Copyright 2017 VMware, Inc.
# All Rights Reserved
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import abc

from neutron_lib.plugins import directory
from oslo_log import log
import six

LOG = log.getLogger(__name__)


@six.add_metaclass(abc.ABCMeta)
class BaseJob(object):
    def __init__(self, readonly):
        self.readonly = readonly
        self.plugin = directory.get_plugin()

    @abc.abstractmethod
    def get_name(self):
        pass

    @abc.abstractmethod
    def get_description(self):
        pass

    @abc.abstractmethod
    def run(self, context):
        pass