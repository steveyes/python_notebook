import unittest
import xmlrunner


def run_by_discover():
    suite = unittest.TestSuite()
    all_cases = unittest.defaultTestLoader.discover('/', 'test_*.py')
    for cases in all_cases:
        suite.addTests(cases)
    runner = xmlrunner.XMLTestRunner(output="report")  # output directory = "report"
    runner.run(suite)


def run_by_add_cases():
    from basic_.test_.unittest_ import TestDict
    from basic_.test_.coverage_ import TestApp

    loader = unittest.TestLoader()
    all_cases = (TestDict, TestApp,)
    suite = unittest.TestSuite()
    for cases in all_cases:
        tests = loader.loadTestsFromTestCase(cases)
        suite.addTests(tests)
    runner = xmlrunner.XMLTestRunner(output="report")
    runner.run(suite)


if __name__ == '__main__':
    run_by_discover()
    # run_by_add_cases()
