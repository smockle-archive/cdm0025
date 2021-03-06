'''
Created on Sep 14, 2014
Modified on Sep 15, 2014
Tests verifying a repository containing zero or more components.
@author: Clay Miller
'''
import unittest
from CA02.prod import Component
from CA02.prod import Repository

class RepositoryTest(unittest.TestCase):
    '''
    Test Repository class.
    '''

    def testInit(self):
        '''
        Test init method.
        '''
        # Instantiate a repository with capacity = 0.
        # ValueError is raised. Repository is not constructed.
        self.assertRaises(ValueError, Repository.Repository, 0)

        # Test non-int capacity.
        self.assertRaises(ValueError, Repository.Repository,
                          capacity="sauerkraut")

        # Instantiate a repository with capacity = 1.
        # Repository is constructed. Capacity of repository is 1.
        rep1 = Repository.Repository(1)
        self.assertEqual(rep1.capacity, 1)

        # Instantiate a repository without specifying a capacity.
        # Repository is constructed. Capacity of repository is 100.
        rep2 = Repository.Repository()
        self.assertEqual(rep2.capacity, 100)

    def testAddComponent(self):
        '''
        Test addComponent method.
        '''
        # Add a component (with methodCount = 0) to the repository created in
        # CA01 - 2.1#2. Repository contains one component (this one). 1 is
        # returned.
        com1 = Component.Component("a", 0, 1)
        rep1 = Repository.Repository(1)
        self.assertEqual(rep1.addComponent(com1), 1)
        self.assertEqual(rep1.queue[0].methodCount, 0)

        # Add another component (with methodCount = 1) to the repository created
        # in CA01-2.1#2. Repository contains one component (this one). The
        # component added in CA01-2.2#1 is popped. 1 is returned.
        com2 = Component.Component("b", 1, 1)
        self.assertEqual(rep1.addComponent(com2), 1)
        self.assertEqual(rep1.queue[0].methodCount, 1)

        # Test missing component
        rep2 = Repository.Repository(100)
        self.assertRaises(ValueError, rep2.addComponent)
        self.assertEqual(len(rep2.queue), 0)

        # Test duplicate component
        rep3 = Repository.Repository(100)
        com3 = Component.Component("a", 1, 1)
        rep3.addComponent(com3)
        self.assertRaises(ValueError, rep3.addComponent, com3)
        self.assertEqual(len(rep3.queue), 1)

        # Test component with duplicate name
        rep4 = Repository.Repository(100)
        com4 = Component.Component("a", 1, 1)
        com5 = Component.Component("a", 2, 2)
        rep4.addComponent(com4)
        self.assertRaises(ValueError, rep4.addComponent, com5)
        self.assertEqual(len(rep4.queue), 1)

    def testCount(self):
        '''
        Test count method.
        '''
        # Get the number of components in the repository created in CA01-2.1#3
        # (an empty repository). 0 is returned. CA01-2.1#3's number of
        # components is unchanged.
        rep1 = Repository.Repository()
        self.assertEqual(rep1.count(), 0)
        self.assertEqual(len(rep1.queue), 0)

        # Get the number of components in the repository created in CA01-2.1#2
        # after test CA01-2.2#2 is run (a non-empty repository). 1 is returned.
        # CA01-2.2#2's number of components is unchanged.
        rep2 = Repository.Repository()
        com1 = Component.Component("a", 1, 1)
        rep2.addComponent(com1)
        self.assertEqual(rep2.count(), 1)
        self.assertEqual(len(rep2.queue), 1)

    def testValidCount(self):
        '''
        Test validCount method.
        '''
        # Get the number of components that have methodCount > 0 from the
        # repository created in CA01-2.1#3 (an empty repository). 0 is returned.
        rep1 = Repository.Repository()
        self.assertEqual(rep1.validCount(), 0)

        # Get the number of components that have methodCount > 0 from the
        # repository created in CA01-2.1#2 after CA01-2.2#1 is run (a non-empty
        # repository). 0 is returned.
        com1 = Component.Component("a", 0, 1)
        rep2 = Repository.Repository(1)
        rep2.addComponent(com1)
        self.assertEqual(rep2.validCount(), 0)

        # Get the number of components that have methodCount > 0 from the
        # repository created in CA01-2.1#2 after CA01-2.2#2 is run (a non-empty
        # repository). 1 is returned.
        com2 = Component.Component("a", 1, 1)
        rep3 = Repository.Repository(1)
        rep3.addComponent(com2)
        self.assertEqual(rep3.validCount(), 1)

    def testDetermineRelativeSizes(self):
        '''
        Test determineRelativeSizes method.
        '''
        # Determine the relative sizes of the repository created in CA01-2.1#3
        # (an empty repository). ValueError is raised, because validCount() is 0
        # (i.e. < 2).
        rep1 = Repository.Repository()
        self.assertRaises(ValueError, rep1.determineRelativeSizes)

        # Determine the relative sizes of the repository created in CA01-2.1#2
        # after test CA01-2.2#1 is run (a small non-empty repository).
        # ValueError is raised, because validCount() is 0 (i.e. < 2).
        com1 = Component.Component("a", 0, 1)
        rep2 = Repository.Repository(1)
        rep2.addComponent(com1)
        self.assertRaises(ValueError, rep2.determineRelativeSizes)

        # Determine the relative sizes of the repository created in CA01-2.1#2
        # after test CA01-2.2#2 is run (a small non-empty repository).
        # ValueError is raised, because validCount() is 1 (i.e. < 2).
        com2 = Component.Component("a", 1, 1)
        rep3 = Repository.Repository(1)
        rep3.addComponent(com2)
        self.assertRaises(ValueError, rep3.determineRelativeSizes)

        # Determine the relative sizes of the repository created in CA01-2.1#3
        # after 3 components (with methodCount = 1 and locCount = 5, 10 and 15)
        # are added (a medium non-empty repository).
        # [3.0, 6.0, 10.0, 16.0, 28.0] is returned.
        rep4 = Repository.Repository()
        com3 = Component.Component("a", 1, 5)
        com4 = Component.Component("b", 1, 10)
        com5 = Component.Component("c", 1, 15)
        rep4.addComponent(com3)
        rep4.addComponent(com4)
        rep4.addComponent(com5)
        relativeSizes = rep4.determineRelativeSizes()
        self.assertEqual(relativeSizes[0], 3.0)
        self.assertEqual(relativeSizes[1], 6.0)
        self.assertEqual(relativeSizes[2], 10.0)
        self.assertEqual(relativeSizes[3], 16.0)
        self.assertEqual(relativeSizes[4], 28.0)

    def testGetRelativeSize(self):
        '''
        Test getRelativeSize method.
        '''
        # Test missing component.
        rep1 = Repository.Repository(5)
        self.assertRaises(ValueError, rep1.getRelativeSize)

        # Test Component with no methods.
        rep2 = Repository.Repository(5)
        com1 = Component.Component("a", 0, 1)
        rep2.addComponent(com1)
        self.assertRaises(ValueError, rep2.getRelativeSize, com1)

        # Test Component in a Repository with too few Components.
        rep3 = Repository.Repository(5)
        com2 = Component.Component("a", 1, 1)
        rep3.addComponent(com2)
        self.assertRaises(ValueError, rep3.getRelativeSize, com2)

        # Test Component in a Repository with enough Components.
        rep4 = Repository.Repository(10)
        com3 = Component.Component("a", 1, 76)
        com4 = Component.Component("b", 4, 116)
        com5 = Component.Component("c", 7, 113)
        com6 = Component.Component("d", 5, 103)
        com7 = Component.Component("e", 0, 1)
        rep4.addComponent(com3)
        rep4.addComponent(com4)
        rep4.addComponent(com5)
        rep4.addComponent(com6)
        rep4.addComponent(com7)
        self.assertEqual(rep4.getRelativeSize(component=com3), "L")

    def testEstimateByRelativeSize(self):
        '''
        Test estimateByRelativeSize method.
        '''
        # Test zero-length name
        rep1 = Repository.Repository(5)
        self.assertRaises(ValueError, rep1.estimateByRelativeSize, name="",
                          methodCount=1, size="M")

        # Test non-string name
        rep2 = Repository.Repository(5)
        self.assertRaises(ValueError, rep2.estimateByRelativeSize, name=1,
                          methodCount=1, size="M")

        # Test missing name
        rep3 = Repository.Repository(5)
        self.assertRaises(ValueError, rep3.estimateByRelativeSize,
                          methodCount=1, size="M")

        # Test zero methodCount
        rep4 = Repository.Repository(5)
        self.assertRaises(ValueError, rep4.estimateByRelativeSize, name="a",
                          methodCount=0, size="M")

        # Test non-int methodCount
        rep5 = Repository.Repository(5)
        self.assertRaises(ValueError, rep5.estimateByRelativeSize, name="a",
                          methodCount="sauerkraut", size="M")

        # Test missing methodCount
        rep6 = Repository.Repository(5)
        self.assertRaises(ValueError, rep6.estimateByRelativeSize, name="a",
                          size="M")

        # Test invalid size
        rep7 = Repository.Repository(5)
        self.assertRaises(ValueError, rep7.estimateByRelativeSize, name="a",
                          methodCount=1, size="sauerkraut")

        # Test non-string size
        rep8 = Repository.Repository(5)
        self.assertRaises(ValueError, rep8.estimateByRelativeSize, name="a",
                          methodCount=1, size=1)

        # Test Component with duplicate name
        rep9 = Repository.Repository(5)
        com1 = Component.Component("a", 1, 1)
        rep9.addComponent(com1)
        self.assertRaises(ValueError, rep9.estimateByRelativeSize, name="a",
                          methodCount=1)

        # Test Component in a Repository with too few Components
        rep10 = Repository.Repository(5)
        com2 = Component.Component("a", 1, 1)
        rep10.addComponent(com2)
        self.assertRaises(ValueError, rep10.estimateByRelativeSize, name="b",
                          methodCount=1)

        # Test Component in a Repository with enough Components
        rep11 = Repository.Repository(10)
        com3 = Component.Component("a", 1, 76)
        com4 = Component.Component("b", 4, 116)
        com5 = Component.Component("c", 7, 113)
        com6 = Component.Component("d", 5, 103)
        com7 = Component.Component("e", 0, 1)
        rep11.addComponent(com3)
        rep11.addComponent(com4)
        rep11.addComponent(com5)
        rep11.addComponent(com6)
        rep11.addComponent(com7)
        com8 = rep11.estimateByRelativeSize(name="f", methodCount=5, size="S")
        self.assertEqual(com8.name, "f")
        self.assertEqual(com8.methodCount, 5)
        self.assertEqual(com8.locCount, 75)
        self.assertEqual(com8.relativeSize, "S")

if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
