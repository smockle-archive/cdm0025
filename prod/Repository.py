'''
Created on Sep 14, 2014

@author: clay
'''

from collections import deque
import math


class Repository(object):
    '''
    The Repository class represents a collection of software components.
    '''

    def __init__(self, capacity=100):
        '''
        Creates an instance of Repository that is capable of holding a specified
        number of software components. The instance is initially empty.
        '''
        self.capacity = capacity
        self.queue = deque(maxlen=self.capacity)

    def addComponent(self, component):
        '''
        Adds an instance of Component to the repository. If adding the component
        will exceed the repository's capacity, the oldest component in the
        repository is removed before the new component is added. addComponent
        returns the total number of components that are in the repository (e.g.,
        adding the first component returns 1, adding the second component
        returns 2, adding the 101st component to a repository with a capacity of
        100 returns 100, etc.) addComponent does not check for duplicate
        components or components with duplicate names.
        '''
        self.queue.append(component)
        return len(self.queue)

    def count(self):
        '''
        Returns a count of the components in the repository. Returns 0 if the
        repository is empty.
        '''
        return len(self.queue)

    def validCount(self):
        '''
        Returns the number of the components in the repository that have method
        count .GT. 0.
        '''
        validCount = 0
        for com in range(0, self.count()):
            if self.queue[com].methodCount > 0:
                validCount += 1
        return validCount

    def determineRelativeSizes(self):
        '''
        Returns a list of integers that characterize the lines of code for very
        small, small, medium, large, and very large components.
        '''
        # Let normalizedSize = ln(number of lines of code / number of methods)
        # for each component having a non-zero method count.
        normalizedSize = []
        for com in range(0, self.count()):
            if self.queue[com].methodCount > 0:
                normalizedSize.append(math.log(float(com.locCount) /
                                                float(com.methodCount)))

        # Let avg = the average of all values of normalizedSize
        avg = 0
        for normal in normalizedSize:
            avg += normal
        avg = float(avg) / float(len(normalizedSize))

        # Let stdev = the standard deviation of all values of normalizedSize
        # Calculate stdev as sqrt(sum((normalizedSizei - avg)^2) / (n-1))
        # where normalizedSizei is the normalizedSize of the i-th component
        # having a non-zero method count, and and n is the value returned by
        # validCount()
        stdev = 0
        for normal in normalizedSize:
            stdev += (float(normal) - float(avg)) ** 2
        stdev = float(stdev) / (float(self.validCount()) - float(1))
        stdev = math.sqrt(stdev)

        relativeSizes = []

        # Let vs =e^(avg-2*stdev) ceiling'ed to the nearest integer
        relativeSizes.append(math.ceil(math.exp(float(avg) - float(2) *
                                              float(stdev))))

        # Let s = e^(avg-stdev) ceiling'ed to the nearest integer
        relativeSizes.append(math.ceil(math.exp(float(avg) - float(stdev))))

        # Let m = e^avg ceiling'ed to the nearest integer
        relativeSizes.append(math.ceil(math.exp(float(avg))))

        # Let l = e^(avg+stdev) ceiling'ed to the nearest integer
        relativeSizes.append(math.ceil(math.exp(float(avg) + float(stdev))))

        # Let vl = e^(avg+2*stdev) ceiling'ed to the nearest integer
        relativeSizes.append(math.ceil(math.exp(float(avg) + float(2) *
                                              float(stdev))))

        # Return [vs, s, m, l, vl]
        return relativeSizes
