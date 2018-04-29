from unittest import TestSuite, TextTestRunner, makeSuite  # pragma: no cover
from interpreter.tests import test_pickle, test_unpickle, test_database_local, test_remote, test_validator, \
    test_database_handler, test_prompt, test_chart  # pragma: no cover


def suite():
    the_suite = TestSuite()
    the_suite.addTest(makeSuite(test_pickle.TestPicklerSetUp))
    the_suite.addTest(makeSuite(test_unpickle.TestUnpickler))
    the_suite.addTest(makeSuite(test_database_local.TestLocal))
    the_suite.addTest(makeSuite(test_validator.TestValidator))
    the_suite.addTest(makeSuite(test_remote.TestRemote))
    the_suite.addTest(makeSuite(test_database_handler.TestDBHandler))
    the_suite.addTest(makeSuite(test_prompt.TestPrompt))
    the_suite.addTest(makeSuite(test_chart.TestGraph))
    return the_suite


if __name__ == '__main__':  # pragma: no cover
    runner = TextTestRunner(verbosity=2)  # pragma: no cover
    runner.run(suite())
