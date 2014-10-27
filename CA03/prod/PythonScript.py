'''
Created on Oct 26, 2014
Modified on Oct 26, 2014
Determines the number of lines of code and Components in a Python file.
@author: Clay Miller
'''
from __builtin__ import ValueError, str

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

        if ".py" not in fileName:
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName must end with extension \".py\".")

        if len(fileName) < 4:
            raise ValueError("PythonScript.__init__:  Invalid parameter. " +
                             "fileName (excluding extension) cannot be blank.")
