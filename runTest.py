import sys
import newTest
import unittest
from oeqa.oetest import oeTest, oeRuntimeTest
import os
import oeqa.runtime
import time
from oeqa.utils.sshcontrol import SSHControl


# if new: execute the newTest, else: execute the oldTest
def start( new = True ):
    
    # execute the newTest
    if new:
	target = newTest.SimpleRemoteTarget()
	tc = newTest.TestContext(target)
	starttime = time.time()
	result = newTest.runTests(tc)
	stoptime = time.time()
	if result.wasSuccessful():
	    print ("- Ran %d test%s in %.3fs" % (result.testsRun, result.testsRun != 1 and "s" or "", stoptime - starttime))
	    print "- OK - All required tests passed"
	else:
	    print ("- FAILED - check the task log and the ssh log")

if __name__ == '__main__': 
    start(True) 

