'''
Created on Sep 14, 2014

@author: clay
'''

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
        self.name = name
        self.methodCount = methodCount
        self.locCount = locCount

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
