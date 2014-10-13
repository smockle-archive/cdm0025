'''
Created on Sep 14, 2014
Modified on Sep 15, 2014
A repository containing zero or more components.
@author: Clay Miller
'''

from collections import deque
import math

from CA02.prod import Component


class Repository(object):
    '''
    The Repository class represents a collection of software components.
    '''

    def __init__(self, capacity=100):
        '''
        Creates an instance of Repository that is capable of holding a specified
        number of software components. The instance is initially empty.
        '''
        if capacity < 1:
            raise ValueError("Repository.__init__:  Invalid parameter. " +
                             "capacity must be greater or equal to 1.")

        self.capacity = capacity
        self.queue = deque(maxlen=self.capacity)

    def addComponent(self, component=None):
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
        # Verify component
        if component == None:
            raise ValueError("Repository.addComponent:  Invalid parameters. " +
                             "Must specify component to add.")

        if component in self.queue:
            raise ValueError("Repository.addComponent:  Invalid parameters. " +
                             "Cannot add duplicate Component to Repository.")

        if component.name in (queued.name for queued in self.queue):
            raise ValueError("Repository.addComponent:  Invalid parameters. " +
                             "Cannot add Component with duplicate name to " +
                             "Repository.")

        # Add component
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

        if self.validCount() < 2:
            raise ValueError("Repository.determineRelativeSizes:  Invalid " +
                            "count. Repository must contain at least 2 " +
                            "Components with non-zero methodCounts.")

        # Let normalizedSize = ln(number of lines of code / number of methods)
        # for each component having a non-zero method count.
        normalizedSize = []
        for comid in range(0, self.count()):
            com = self.queue[comid]
            if com.methodCount > 0:
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

    def getRelativeSize(self, component=None):
        '''
        Returns the relative size of the component passed as a parameter.
        '''
        if component == None:
            raise ValueError("Repository.getRelativeSize:  Invalid " +
                             "parameter. Must specify component to check.")

        if component.methodCount < 1:
            raise ValueError("Repository.getRelativeSize:  Invalid " +
                             "parameter. Must specify component with at least" +
                             " one method.")

        if self.validCount() < 2:
            raise ValueError("Repository.determineRelativeSizes:  Invalid " +
                            "count. Repository must contain at least 2 " +
                            "Components with non-zero methodCounts.")

        # Let normalizedSize = ln(number of lines of code / number of methods)
        # for each component having a non-zero method count.
        normalizedSize = []
        for comid in range(0, self.count()):
            com = self.queue[comid]
            if com.methodCount > 0:
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

        # Calculate bounds for relative sizing
        relativeSize = None
        inputSize = component.locCount / component.methodCount
        vsUpperBound = math.ceil(math.exp(float(avg) - float(1.5) *
                                          float(stdev)))
        sUpperBound = math.ceil(math.exp(float(avg) - float(0.5) *
                                         float(stdev)))
        mUpperBound = math.ceil(math.exp(float(avg) + float(0.5) *
                                         float(stdev)))
        lUpperBound = math.ceil(math.exp(float(avg) + float(1.5) *
                                         float(stdev)))

        # Convert number bounds to strings
        if inputSize <= vsUpperBound:
            relativeSize = "VS"
        if (inputSize > vsUpperBound) and (inputSize <= sUpperBound):
            relativeSize = "S"
        if (inputSize > sUpperBound) and (inputSize <= mUpperBound):
            relativeSize = "M"
        if (inputSize > mUpperBound) and (inputSize <= lUpperBound):
            relativeSize = "L"
        if inputSize > lUpperBound:
            relativeSize = "VL"

        return relativeSize

    def estimateByRelativeSize(self, name=None, methodCount=None, size="M"):
        '''
        Returns an instance of Component with an estimate of the number of lines
        of code based on relative size.
        '''
        if (type(name) is not str) or (name == ""):
            raise ValueError("Repository.estimateByRelativeSize:  Invalid " +
                             "parameter. name must be a non-empty, unique " +
                             "string.")

        if (type(methodCount) is not int) or (methodCount < 1):
            raise ValueError("Repository.estimateByRelativeSize:  Invalid" +
                             "parameter. methodCount must be an integer " +
                             "greater than zero.")

        if type(size) is not str:
            raise ValueError("Repository.estimateByRelativeSize:  Invalid" +
                             "parameter. size must be a string.")

        size = size.upper()
        sizes = ["VS", "S", "M", "L", "VL"]
        if size not in sizes:
            raise ValueError("Repository.estimateByRelativeSize:  Invalid " +
                             "parameter. size must be VS, S, M, L or VL.")

        if name in (queued.name for queued in self.queue):
            raise ValueError("Repository.estimateByRelativeSize:  Invalid " +
                             "parameter. Cannot create new Component with " +
                             "duplicate name.")

        if self.validCount() < 2:
            raise ValueError("Repository.estimateByRelativeSize:  Invalid " +
                            "count. Repository must contain at least 2 " +
                            "Components with non-zero methodCounts.")

        relativeSizes = self.determineRelativeSizes()
        locCount = relativeSizes[sizes.index(size)] * methodCount
        component = Component.Component(name, methodCount, locCount)
        component.setRelativeSize(size)
        return component
