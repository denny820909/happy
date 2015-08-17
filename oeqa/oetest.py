import unittest
import re
from oeqa.utils.decorators import LogResults

def skipModule(reason, pos=2):
    modname = getmodule(pos)
    if modname not in oeTest.tc.testsrequired:
        raise unittest.SkipTest("%s: %s" % (modname, reason))
    else:
        raise Exception("\nTest %s wants to be skipped.\nReason is: %s" \
                "\nTest was required in TEST_SUITES, so either the condition for skipping is wrong" \
                "\nor the image really doesn't have the required feature/package when it should." % (modname, reason))

@LogResults
class oeTest(unittest.TestCase):

    longMessage = True

    @classmethod
    def hasPackage(self, pkg):

        #if re.search(pkg, oeTest.tc.pkgmanifest):
        #    return True
        #return False
	return True

    @classmethod
    def hasFeature(self,feature):

        #if feature in oeTest.tc.imagefeatures or \
        #        feature in oeTest.tc.distrofeatures:
        #    return True
        #else:
        #    return False
	return True

class oeRuntimeTest(oeTest):
    def __init__(self, methodName='runTest'):
        self.target = oeRuntimeTest.tc.target
        super(oeRuntimeTest, self).__init__(methodName)

    #TODO: use package_manager.py to install packages on any type of image
    def install_packages(self, packagelist):
        for package in packagelist:
            (status, result) = self.target.run("smart install -y "+package)
            if status != 0:
                return status
