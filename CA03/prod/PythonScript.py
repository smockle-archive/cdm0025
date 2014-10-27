'''
Created on Oct 26, 2014
Modified on Oct 26, 2014
Determines the number of lines of code and Components in a Python file.
@author: Clay Miller
'''
from __builtin__ import ValueError, str
import os.path

class PythonScript(object):
    '''
    A Python file, consisting of zero or more lines of code, and zero or more
    Components.
    '''
    def __init__(self, fileName=None):
        '''
        Creates an instance of PythonScript, saving its fileName.
        '''
        if (type(fileName) is not str) or (len(fileName) < 1):
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName must be a non-empty string.")

        if len(fileName) < 4:
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName must be at least four characters.")

        if fileName[-3:] != ".py":
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName must end with extension \".py\".")

        if not os.path.isfile(fileName):
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName does not exist.")

        self.fileName = os.path.basename(fileName)
        self.filePath = os.path.dirname(fileName)

    def getFileName(self):
        '''
        Returns the fileName of the component.
        '''
        return self.fileName

    def getFilePath(self):
        '''
        Returns the fileName of the component.
        '''
        return self.filePath
