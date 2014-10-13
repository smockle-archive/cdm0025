import CA02.prod.Component as Component
import CA02.prod.Repository as Repository


# Create components using positional parms, keyword parms, mix of both
component1 = Component.Component(name="Component01", methodCount=1, locCount=76)
component2 = Component.Component(name="Component02", locCount=116, methodCount=4)
component3 = Component.Component("Component03", 7, locCount=113)
component4 = Component.Component("Component04", 5, 103)
component5 = Component.Component("Component05", 0, 10)

# The following illustrates handling an exception raised by using an invalid parm.
# It captures a ValueError exception, then extract the accompanying diagnostic string.
try:
    componentX = Component.Component(1, 2, 3)
except ValueError as raisedException:
    diagnosticString = raisedException.args[0]

# create a repository using the default capacity
theRepository = Repository.Repository()

# add components to the repository
theRepository.addComponent(component1)
theRepository.addComponent(component2)
theRepository.addComponent(component3)
theRepository.addComponent(component4)
theRepository.addComponent(component5)

# count() will result in 5
# validCount() will result in 4
theCount = theRepository.count()
theValidCount = theRepository.validCount()

# Component01 has 1 method and 76 LOC; ln(locCount/MethodCount) =   4.33073334
# Component02 has 4 methods and 116 LOC; ln(locCount/MethodCount) = 3.36729583
# Component03 has 7 methods and 113 LOC; ln(locCount/MethodCount) = 2.78147767
# Component04 has 5 methods and 103 LOC; ln(locCount/MethodCount) = 3.025291076
# Component05 has 0 methods and is ignored
# avg of all components' ln(locCount/MethodCount) is 3.376199479
# stdev of all components' ln(locCount/MethodCount) is 0.680207053
# determineRelativeSize returns [8, 15, 30, 58, 115]
relativeSizes = theRepository.determineRelativeSizes()

# getRelativeSize(component1):
#    The size matrix for repository at this point is:
#      Low    Mid    High
#  VS    0      8    11
#  S    11     15    21
#  M    21     30    42
#  L    42     58    82
#  VL   82    115    -
#
#  component1 has 1 method and 76 LOC, which gives it a normalized size of 76/1 = 76
#  76 is .LE. 82 and .GT. 42, therefore component 1 is "L"
size = theRepository.getRelativeSize(component1)
component1.setRelativeSize(size)


# estimateByRelativeSize("Component06", 5, "S") will result in the creation of
# an instance of Component with a normalized line of code count for small components,
# which is 15 loc/method.  Because the component has 5 methods, its total estimated
# LOC is 5 * 15 = 75
component6 = theRepository.estimateByRelativeSize("Component06", 5, "S")
