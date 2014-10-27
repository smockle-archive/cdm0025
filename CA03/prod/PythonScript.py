'''
Created on Oct 26, 2014
Modified on Oct 26, 2014
Determines the number of lines of code and Components in a Python file.
@author: Clay Miller
'''
from __builtin__ import ValueError, str
import os.path

from CA03.prod import Component
from CA03.prod import PythonLine

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

        locCount = 0
        inADocstring = False
        docstringType = ""

        with open(locPath, "r") as locFile:
            for line in locFile:
                pline = PythonLine.PythonLine(line=line)

                # Middle docstring, skip count.
                if inADocstring and not pline.isDocstring(docstringType):
                    continue

                # Ending docstring, mark and skip count.
                if inADocstring and pline.isDocstring(docstringType):
                    inADocstring = False
                    docstringType = ""
                    continue

                # Starting docstring, mark and skip count.
                if pline.isDocstring():
                    inADocstring = True
                    docstringType = pline.getDocstringType()
                    continue

                # Blank line, skip count.
                if pline.isBlankLine():
                    continue

                # Comment, skip count.
                if pline.isComment():
                    continue

                # Countable line, count.
                locCount = locCount + 1

        return locCount

    def extractDesign(self):
        '''
        Returns a tuple containing a list of OO components and a list of
        functional components in the PythonScript.
        '''
        locPath = self.fileName
        if len(self.filePath) > 0:
            locPath = self.filePath + "/" + locPath

        oo_components = []
        functional_components = []
        name = ""
        methodCount = 0
        locCount = 0
        inOO = False
        inFunctional = False
        inADocstring = False
        docstringType = ""

        with open(locPath, "r") as locFile:
            for line in locFile:
                pline = PythonLine.PythonLine(line=line)

                # Middle docstring, skip count.
                if inADocstring and not pline.isDocstring(docstringType):
                    continue

                # Ending docstring, mark and skip count.
                if inADocstring and pline.isDocstring(docstringType):
                    inADocstring = False
                    docstringType = ""
                    continue

                # Starting docstring, mark and skip count.
                if pline.isDocstring():
                    inADocstring = True
                    docstringType = pline.getDocstringType()
                    continue

                # Blank line, skip count.
                if pline.isBlankLine():
                    continue

                # Comment, skip count.
                if pline.isComment():
                    continue

                # Middle OO, count.
                if inOO and not pline.isComponent():
                    locCount = locCount + 1
                    if pline.isClassMethod():
                        methodCount = methodCount + 1
                    continue

                # Middle Functional, count.
                if inFunctional and not pline.isComponent():
                    locCount = locCount + 1
                    continue

                # Ending OO, mark.
                if inOO and pline.isComponent():
                    component = Component.Component(name=name,
                        methodCount=methodCount, locCount=locCount)
                    oo_components.append(component)
                    name = ""
                    methodCount = 0
                    locCount = 0
                    inOO = False

                # Ending Functional, mark.
                if inFunctional and pline.isComponent():
                    component = Component.Component(name=name,
                        methodCount=methodCount, locCount=locCount)
                    functional_components.append(component)
                    name = ""
                    methodCount = 0
                    locCount = 0
                    inFunctional = False

                # Starting OO, mark and count.
                if pline.isClass():
                    inOO = True
                    name = pline.getClassName()
                    locCount = locCount + 1
                    continue

                # Starting Functional, mark and count.
                if pline.isClasslessMethod():
                    inFunctional = True
                    name = pline.getMethodName()
                    locCount = locCount + 1
                    methodCount = 1
                    continue

        return (oo_components, functional_components)
