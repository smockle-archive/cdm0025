'''
Created on Sep 14, 2014
Modified on Sep 15, 2014
A component representing a code object of lines and methods.
@author: Clay Miller
'''
from __builtin__ import ValueError

class Component(object):
    '''
    Component is an abstraction that represents a software component. The
    abstraction models the software component as having a name, number of lines
    of code, number of methods.
    '''

    def __init__(self, name, methodCount, locCount):
        '''
        Creates an instance of a Component, saving its name, number of methods,
        and number of lines of code.
        '''
        if len(name) < 1:
            raise ValueError("Component.__init__:  Invalid parameters. name " +
                             "must be a non-empty string.")

        if methodCount < 0:
            raise ValueError("Component.__init__:  Invalid parameters. method" +
                             "Count must be greater or equal to 0.")

        if locCount < 1:
            raise ValueError("Component.__init__:  Invalid parameters. loc" +
                             "Count must greater or equal to 1.")

        self.name = name
        self.methodCount = methodCount
        self.locCount = locCount
        self.relativeSize = ""

    def getName(self):
        '''
        Returns the name of the component.
        '''
        return self.name

    def getMethodCount(self):
        '''
        Returns the component's number of methods.
        '''
        return self.methodCount

    def getLocCount(self):
        '''
        Returns the component's line-of-code count.
        '''
        return self.locCount

    def setRelativeSize(self, size):
        '''
        Sets the component's relative size.
        '''
        self.relativeSize = "S"
        return "S"
