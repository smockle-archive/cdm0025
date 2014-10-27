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
        empty_script = PythonScript.PythonScript(fileName=
             "../public/not_missing.py")
        self.assertEqual(empty_script.countLoc(), 0)

        # Test file with 3 comments
        comments_script = PythonScript.PythonScript(fileName=
             "../public/comments.py")
        self.assertEqual(comments_script.countLoc(), 0)

        # Test file with 3 docstrings
        docstrings_script = PythonScript.PythonScript(fileName=
             "../public/docstrings.py")
        self.assertEqual(docstrings_script.countLoc(), 0)

        # Test file with 3 blank lines
        blank_lines_script = PythonScript.PythonScript(fileName=
             "../public/blank_lines.py")
        self.assertEqual(blank_lines_script.countLoc(), 0)

        # Test file with 3 countable lines
        countable_script = PythonScript.PythonScript(fileName=
             "../public/countable.py")
        self.assertEqual(countable_script.countLoc(), 3)

        # Test file with 3 comments, 3 docstrings, 3 blank lines and 3 countable
        # lines
        complex_script = PythonScript.PythonScript(fileName=
             "../public/complex.py")
        self.assertEqual(complex_script.countLoc(), 3)

    def testExtractDesign(self):
        '''
        Test extractDesign method.
        '''
        # Test empty file
        empty_script = PythonScript.PythonScript(fileName=
             "../public/blank_lines.py")
        empty_script_design = empty_script.extractDesign()
        self.assertEqual(len(empty_script_design), 2)
        self.assertEqual(len(empty_script_design[0]), 0)
        self.assertEqual(len(empty_script_design[1]), 0)

        # Test file with 2 OO components
        two_oo_script = PythonScript.PythonScript(fileName=
             "../public/two_oo.py")
        two_oo_script_design = two_oo_script.extractDesign()
        self.assertEqual(len(two_oo_script_design), 2)
        self.assertEqual(len(two_oo_script_design[0]), 2)
        self.assertEqual(len(two_oo_script_design[1]), 0)
        c1 = two_oo_script_design[0][0]
        c2 = two_oo_script_design[0][1]
        self.assertEqual(c1.name, "ClassOne")
        self.assertEqual(c1.methodCount, 2)
        self.assertEqual(c1.locCount, 4)
        self.assertEqual(c2.name, "ClassTwo")
        self.assertEqual(c2.methodCount, 3)
        self.assertEqual(c2.locCount, 6)

        # Test file with 2 functional components
        two_functional_script = PythonScript.PythonScript(fileName=
             "../public/two_functional.py")
        two_functional_script_design = two_functional_script.extractDesign()
        self.assertEqual(len(two_functional_script_design), 2)
        self.assertEqual(len(two_functional_script_design[0]), 0)
        self.assertEqual(len(two_functional_script_design[1]), 2)
        c3 = two_functional_script_design[1][0]
        c4 = two_functional_script_design[1][1]
        self.assertEqual(c3.name, "methodOne")
        self.assertEqual(c3.methodCount, 1)
        self.assertEqual(c3.locCount, 3)
        self.assertEqual(c4.name, "methodTwo")
        self.assertEqual(c4.methodCount, 1)
        self.assertEqual(c4.locCount, 4)

        # Test file with 2 OO components and 2 functional components
        complexier_script = PythonScript.PythonScript(fileName=
             "../public/complexier.py")
        complexier_script_design = complexier_script.extractDesign()
        self.assertEqual(len(complexier_script_design), 2)
        self.assertEqual(len(complexier_script_design[0]), 2)
        self.assertEqual(len(complexier_script_design[1]), 2)
        c5 = complexier_script_design[0][0]
        c6 = complexier_script_design[0][1]
        c7 = complexier_script_design[1][0]
        c8 = complexier_script_design[1][1]
        self.assertEqual(c5.name, "ClassOne")
        self.assertEqual(c5.methodCount, 2)
        self.assertEqual(c5.locCount, 4)
        self.assertEqual(c6.name, "ClassTwo")
        self.assertEqual(c6.methodCount, 3)
        self.assertEqual(c6.locCount, 6)
        self.assertEqual(c7.name, "methodOne")
        self.assertEqual(c7.methodCount, 1)
        self.assertEqual(c7.locCount, 3)
        self.assertEqual(c8.name, "methodTwo")
        self.assertEqual(c8.methodCount, 1)
        self.assertEqual(c8.locCount, 4)

