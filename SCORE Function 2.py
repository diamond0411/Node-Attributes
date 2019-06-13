#!/usr/bin/env python
# coding: utf-8

# In[30]:


import import_ipynb
import ndex2.client as nc
import io
import json
from IPython.display import HTML
from time import sleep


my_account="starwars0411"
my_password="awesome123"

if my_account == 'starwars0411':
    print('Success')
else:
    try:
        my_ndex=nc.Ndex2("http://public.ndexbio.org", my_account, my_password)
        my_ndex.update_status()
        networks = my_ndex.status.get("networkCount")
        users = my_ndex.status.get("userCount")
        groups = my_ndex.status.get("groupCount")
        print("my_ndex client: %s networks, %s users, %s groups" % (networks, users, groups))
    except Exception as inst:
        print("Could not access account %s with password %s" % (my_account, my_password))
        print(inst.args)


# In[ ]:


import import_ipynb
import ndex2.client as nc
import io
import json
from IPython.display import HTML
from time import sleep

anon_ndex=nc.Ndex2("http://public.ndexbio.org")
anon_ndex.update_status()
networks = anon_ndex.status.get("networkCount")
users = anon_ndex.status.get("userCount")
groups = anon_ndex.status.get("groupCount")
print("anon client: %s networks, %s users, %s groups" % (networks, users, groups))


# In[31]:


from random import randrange
import ndex2.client as nc
import io
import json
from IPython.display import HTML
from time import sleep

ns=anon_ndex.get_network_summary('c9243cce-2d32-11e8-b939-0ac135e8bacf')
def summary2table(object):
    table = "<table>"
    for key, value in object.items():
        if key == "warnings":
            warning_list = ""
            for warning in value:
                warning_list += "%s<br>" % warning
            value = warning_list
        if key == "properties":
            property_table = "<table>"
            for property in value:
                property_table += "<tr>" 
                property_table += "<td>%s</td><td>%s</td>" % (property.get("predicateString"), property.get("value"))
                property_table += "</tr>"
            property_table += "</table>"
            value = property_table
                
        table += "<tr>" 
        table += "<td>%s</td><td>%s</td>" % (key, value)
        table += "</tr>"
    table += "</table>"
    return table

HTML(summary2table(ns))


# In[34]:


from random import randrange
import ndex2.client as nc
import io
import json
from IPython.display import HTML
from time import sleep
from ndex2.nice_cx_network import NiceCXNetwork
import ndex2
import networkx as nx
import pandas as pd
import os

my_account="starwars0411"
my_password="awesome123"

if my_account == 'starwars0411':
    print('Success')
else:
    try:
        my_ndex=nc.Ndex2("http://public.ndexbio.org", my_account, my_password)
        my_ndex.update_status()
        networks = my_ndex.status.get("networkCount")
        users = my_ndex.status.get("userCount")
        groups = my_ndex.status.get("groupCount")
        print("my_ndex client: %s networks, %s users, %s groups" % (networks, users, groups))
    except Exception as inst:
        print("Could not access account %s with password %s" % (my_account, my_password))
        print(inst.args)

nice_cx_from_server = ndex2.create_nice_cx_from_server(server='public.ndexbio.org', uuid='02bc2a6f-2509-11e9-9f06-0ac135e8bacf')

nice_cx_from_server.print_summary()


# In[ ]:





# In[ ]:





# In[ ]:




