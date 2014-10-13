'''
Created on Sep 14, 2014
Modified on Sep 15, 2014
Tests verifying a component representing a code object of lines and methods.
@author: Clay Miller
'''
import unittest
from CA02.prod import Component

class ComponentTest(unittest.TestCase):
    '''
    Test Component class.
    '''

    def testInit(self):
        '''
        Test init method.
        '''
        # Instantiate a component with name = "", methodCount = 1, locCount = 1
        # ValueError is raised. Component is not constructed.
        self.assertRaises(ValueError, Component.Component, "", 1, 1)

        # Instant a component with name = "a", methodCount = -1, locCount = 1
        # ValueError is raised. Component is not constructed.
        self.assertRaises(ValueError, Component.Component, "a", -1, 1)

        # Instantiate a component with name = "a", methodCount = 1, locCount = 0
        # ValueError is raised. Component is not constructed.
        self.assertRaises(ValueError, Component.Component, "a", 1, 0)

        # Instantiate a component with name = "a", methodCount = 1, locCount = 1
        # Component is constructed.
        com1 = Component.Component("a", 1, 1)
        self.assertEqual(com1.name, "a")
        self.assertEqual(com1.methodCount, 1)
        self.assertEqual(com1.locCount, 1)

    def testGetName(self):
        '''
        Test getName method.
        '''
        # Get the name for the component made in CA01-1.1#4.
        # "a" is returned. CA01-1.1#4's name is unchanged.
        com = Component.Component("a", 1, 1)
        self.assertEqual(com.getName(), "a")

    def testGetMethodCount(self):
        '''
        Test getMethodCount method.
        '''
        # Get the number of methods for the component made in CA01-1.1#4.
        # 1 is returned. CA01-1.1#4's methodCount is unchanged.
        com = Component.Component("a", 1, 1)
        self.assertEqual(com.getMethodCount(), 1)

    def testGetLocCount(self):
        '''
        Test getLocCount method.
        '''
        # Get the number of lines of code for the component made in CA01-1.1#4.
        # 1 is returned. CA01-1.1#4's methodCount is unchanged.
        com = Component.Component("a", 1, 1)
        self.assertEqual(com.getLocCount(), 1)

    def testSetRelativeSize(self):
        '''
        Test setRelativeSize method.
        '''
        # Test lowercase string.
        com1 = Component.Component("a", 1, 1)
        self.assertEqual(com1.setRelativeSize(size="s"), "S")
        self.assertEqual(com1.relativeSize, "S")

        # Test uppercase string.
        com2 = Component.Component("a", 1, 1)
        self.assertEqual(com2.setRelativeSize(size="M"), "M")
        self.assertEqual(com2.relativeSize, "M")

        # Test invalid string.
        com3 = Component.Component("a", 1, 1)
        com3.relativeSize = "M"
        self.assertRaises(ValueError, com3.setRelativeSize, "sauerkraut")
        self.assertEqual(com3.relativeSize, "M")

        # Test missing string.
        com4 = Component.Component("a", 1, 1)
        self.assertEqual(com4.setRelativeSize(), "M")
        self.assertEqual(com4.relativeSize, "M")

        # Test int.
        com5 = Component.Component("a", 1, 1)
        com5.relativeSize = "M"
        self.assertRaises(ValueError, com5.setRelativeSize, 1)
        self.assertEqual(com5.relativeSize, "M")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
