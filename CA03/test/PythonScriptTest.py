'''
Created on Oct 26, 2014
Modified on Oct 26, 2014
Tests verifying PythonScript
@author: Clay Miller
'''
import unittest
from CA03.prod import PythonScript

class PythonScriptTest(unittest.TestCase):
    '''
    Test PythonScript class.
    '''

    def testInit(self):
        '''
        Test init method.
        '''
        # Test no fileName specified
        self.assertRaises(ValueError, PythonScript.PythonScript)

        # Test blank filename
        self.assertRaises(ValueError, PythonScript.PythonScript, fileName="")

        # Test fileName without ".py"
        self.assertRaises(ValueError, PythonScript.PythonScript,
                          fileName="aaaa")

        # Test fileName only ".py"
        self.assertRaises(ValueError, PythonScript.PythonScript,
                          fileName=".py")

        # Test fileName that isn't a string
        self.assertRaises(ValueError, PythonScript.PythonScript,
                          fileName=3)

        # Test valid fileName, file does not exist
        self.assertRaises(ValueError, PythonScript.PythonScript,
                          fileName="../public/missing.py")

        # Test valid fileName, file does exist
        self.assertIsInstance(PythonScript.PythonScript(
            fileName="../public/not_missing.py"), PythonScript.PythonScript)

    def testGetFileName(self):
        '''
        Test getFileName method.
        '''
        script = PythonScript.PythonScript(fileName="../public/not_missing.py")
        self.assertEqual(script.getFileName(), "not_missing.py")

    def testGetFilePath(self):
        '''
        Test getFilePath method.
        '''
        script = PythonScript.PythonScript(fileName="../public/not_missing.py")
        self.assertEqual(script.getFilePath(), "../public")

    def testCountLoc(self):
        '''
        Test countLoc method.
        '''
        # Test empty file
        script = PythonScript.PythonScript(fileName="../public/not_missing.py")
        self.assertEqual(script.countLoc(), 0)

        # Test file with 3 comments
        script = PythonScript.PythonScript(fileName="../public/comments.py")
        self.assertEqual(script.countLoc(), 0)

        # Test file with 3 docstrings
        script = PythonScript.PythonScript(fileName="../public/docstrings.py")
        self.assertEqual(script.countLoc(), 0)

        # Test file with 3 blank lines
        script = PythonScript.PythonScript(fileName="../public/blank_lines.py")
        self.assertEqual(script.countLoc(), 0)

        # Test file with 3 countable lines
        script = PythonScript.PythonScript(fileName="../public/countable.py")
        self.assertEqual(script.countLoc(), 3)

        # Test file with 3 comments, 3 docstrings, 3 blank lines and 3 countable
        # lines


    def testExtractDesign(self):
        '''
        Test extractDesign method.
        '''
        # Test empty file
        # Test file with 2 OO components
        # Test file with 2 functional components
        # Test file with 2 OO components and 2 functional components



