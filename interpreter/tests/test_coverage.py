from coverage import Coverage
from interpreter.tests.test_suite import suite
from interpreter.prompt import Shell
from interpreter.pickler import Pickler


cov = Coverage(branch=True)

cov.start()

suite()


cov.stop()
cov.save()

cov.html_report()

