# js.py - Classes to make Python feel a little more like JavaScript
# Author: Adam Haile
# License: MIT

import copy, json

#Gives Python dict ability to use dot notation for all keys and adds other helpful methods
class jsdict(dict):
    def __init__(self, *a, **k):
        super(jsdict, self).__init__(*a, **k)
        #set the internal property dict to itself
        self.__dict__ = self
        #recurses through list and dict types, converting to jsdict
        for k in self.__dict__:
            if isinstance(self.__dict__[k], dict):
                self.__dict__[k] = d(self.__dict__[k])
            elif isinstance(self.__dict__[k], list):
                for i in range(len(self.__dict__[k])):
                    if isinstance(self.__dict__[k][i], dict):
                        self.__dict__[k][i] = d(self.__dict__[k][i])

    #Undefined keys now return None instead of throwing exception
    def __getattr__(self, name):
        return None

    #Adds missing keys from given dict into this dict.
    #Optionally overwrite keys that do exist
    def upgrade(self, a, overwrite=False):
        a = jsdict(a)
        for k,v in a.items():
            if not k in self or overwrite:
                self[k] = v
        return self

    #deep clone on whole dict
    def clone(self):
        return copy.deepcopy(self)

    #output dict as JSON dump
    def json(self):
        return json.dumps(self)

#same as jsdict but directly represents itself as JSON
class jsondict(jsdict):
    def __init__(self, *a, **k):
        super(jsondict, self).__init__(*a, **k)

    def __repr__(self):
        return self.json()

    def __str__(self):
        return self.json()
