import unittest
from oeqa.oetest import oeTest, oeRuntimeTest
import os
import oeqa.runtime
import time
from oeqa.utils.sshcontrol import SSHControl



# original: parsing parameters from local.conf
class TestContext(object):
        def __init__(self):
            self.testslist = ["oeqa.runtime.pam"]
            # self.testsrequired = ["date","logrotate"]        
            self.target = target
	    self.filesdir="oeqa/runtime/files/"
	   

class SimpleRemoteTarget():

    def __init__(self):
        self.ip = "172.23.216.12"

        self.port = None
	self.start()
        
    def run(self, cmd, timeout=None):
        return self.connection.run(cmd, timeout)

    def copy_to(self, localpath, remotepath):
        return self.connection.copy_to(localpath, remotepath)

    def copy_from(self, remotepath, localpath):
        return self.connection.copy_from(remotepath, localpath)
            

    def start(self, params=None):
        self.connection = SSHControl(self.ip, logfile="happy.log", port=self.port)

    def stop(self):
        self.connection = None
        self.ip = None
        self.server_ip = None   

def runTests(tc, type="runtime"):

    suite = loadTests(tc, type)
    print("Test modules  %s" % tc.testslist)
    print("Found %s tests" % suite.countTestCases())
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    return result

def loadTests(tc, type="runtime"):
    if type == "runtime":
        # set the context object passed from the test class
        setattr(oeTest, "tc", tc)
        # set ps command to use
        # setattr(oeRuntimeTest, "pscmd", "ps -ef" if oeTest.hasPackage("procps") else "ps")
        # prepare test suite, loader and runner
        suite = unittest.TestSuite()
    
    testloader = unittest.TestLoader()
    testloader.sortTestMethodsUsing = None
    suite = testloader.loadTestsFromNames(tc.testslist)

    return suite



