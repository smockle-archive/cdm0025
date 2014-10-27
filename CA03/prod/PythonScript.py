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

    def countLoc(self):
        '''
        Returns the number of non-comment, non-docstring, non-blank lines in the
        PythonScript.
        '''
        locPath = self.fileName
        if len(self.filePath) > 0:
            locPath = self.filePath + "/" + locPath

        commentString = ""
        loc = 0

        with open(locPath, "r") as locFile:
            for line in locFile:
                line = line.strip()
                if len(line) == 0:
                    continue
                elif line[0] == "#":
                    continue
                elif (len(commentString) > 0 and line[0:len(commentString)] !=
                      commentString):
                    continue
                elif (len(commentString) > 0 and line[0:len(commentString)] ==
                      commentString):
                    commentString = ""
                    continue
                elif (len(line) >= 3 and (line[0:3] == "\"\"\"" or line[0:3] ==
                      "'''")):
                    commentString = line[0:3]
                    continue
                else:
                    loc = loc + 1
        return loc
