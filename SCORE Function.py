#!/usr/bin/env python
# coding: utf-8

# In[23]:


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


# In[18]:


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


# In[13]:


from random import randrange
import ndex2.client as nc
import io
import json
from IPython.display import HTML
from time import sleep

node = input("")

def addscore():
    score = randrange(11)
    return(node, score)

addscore()


# In[ ]:





# In[ ]:




