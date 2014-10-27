'''
Created on Oct 26, 2014
Modified on Oct 26, 2014
Collection of data and methods relating to a line of Python code.
@author: Clay Miller
'''

from __builtin__ import ValueError, str

class PythonLine(object):
    '''
    classdocs
    '''

    def __init__(self, line=None):
        '''
        Creates an instance of PythonLine, saving its line.
        '''
        if (type(line) is not str) or (len(line) < 1):
            raise ValueError("PythonLine.__init__:  Invalid parameter. " +
                             "line must be a non-empty string.")
        self.line = line
        self.strip = self.line.strip()

        self.len = len(self.line)
        self.strip_len = len(self.strip)

    def isBlankLine(self):
        '''
        Returns true if the PythonLine is blank.
        '''
        return self.strip_len == 0

    def isComment(self):
        '''
        Returns true if the PythonLine is a comment.
        '''
        return not self.isBlankLine() and self.strip[0] == "#"

    def isDocstring(self, docstring_type=None):
        '''
        Returns true if the PythonLine is a docstring.
        '''
        if (docstring_type != None and docstring_type != "'''" and
            docstring_type != "\"\"\""):
            raise ValueError("PythonLine.isDocstring:  Invalid parameter. " +
                             "docstringType must be \"'''\" or \"\\\"\\\"" +
                             "\\\"\".")

        if docstring_type == None:
            return (self.strip_len > 2 and (self.strip[0:3] == "\"\"\"" or
                                       self.strip[0:3] == "'''"))

        return self.strip_len > 2 and self.strip[0:3] == docstring_type

    def getDocstringType(self):
        '''
        If this PythonLine is a docstring, returns the type of docstring.
        '''
        if not self.isDocstring():
            raise ValueError("PythonLine.getClassName:  PythonLine isn't a" +
                             "docstring declaration.")

        return self.strip[0:3]

    def isClass(self):
        '''
        Returns true if the PythonLine is a class.
        '''
        return self.strip_len > 5 and self.strip[0:5] == "class"

    def isMethod(self):
        '''
        Returns true if the PythonLine is a method.
        '''
        return self.strip_len > 3 and self.strip[0:3] == "def"

    def isClasslessMethod(self):
        '''
        Returns true if the PythonLine is a method outside of a class.
        '''
        return self.len > 3 and self.line[0:3] == "def"

    def isClassMethod(self):
        '''
        Returns true if the PythonLine is a method in a class.
        '''
        return self.isMethod() and not self.isClasslessMethod()

    def getClassName(self):
        '''
        If this PythonLine is a class, return the name of that class.
        '''

        if not self.isClass():
            raise ValueError("PythonLine.getClassName:  PythonLine isn't a" +
                             "class declaration.")

        unclass = self.strip.replace("class", "").strip()
        return unclass[0:unclass.index("(")]

    def getMethodName(self):
        '''
        If this PythonLine is a method, return the name of that method.
        '''

        if not self.isMethod():
            raise ValueError("PythonLine.getMethodName:  PythonLine isn't a" +
                             "method declaration.")

        undef = self.strip.replace("def", "").strip()
        return undef[0:undef.index("(")]

    def isComponent(self):
        '''
        Returns true if the PythonLine is a class or method outside a class.
        '''

        return self.isClass() or self.isClasslessMethod()

    def getComponentName(self):
        '''
        If this PythonLine is a class or method outside a class, return the
        name of that class or method outside a class.
        '''

        if not self.isComponent():
            raise ValueError("PythonLine.getComponentName:  PythonLine isn't " +
                             "a component declaration.")

        if self.isClass():
            return self.getClassName()

        return self.getMethodName()
