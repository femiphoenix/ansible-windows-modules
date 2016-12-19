#!/usr/bin/python
# -*- coding: utf-8 -*-

# (c) 2016, Stanley Karunditu <stanley@linuxsimba.com>
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.

# this is a windows documentation stub.  actual code lives in the .ps1
# file of the same name

DOCUMENTATION = '''
---
module: win_hardcode_ip
version_added: "2.0"
short_description: Hard codes IP address.
description:
     - |
        Takes an IP address obtained via DHCP and hard codes that IP info to the interface.
options:
author: Stanley Karunditu(stanley@linuxsimba.com)
'''

EXAMPLES = '''
# Change Hostname
$ ansible -i hosts -m win_hardcode_ip windowspc
'''
