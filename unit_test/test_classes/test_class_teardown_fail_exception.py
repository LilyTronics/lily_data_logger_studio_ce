"""
Test class for use with the unit test.
"""

from unit_test.test_suite import TestSuite


class TestClassTeardownFailException(TestSuite):

    def test_dummy(self):
        return True

    def teardown(self):
        _a = 1 / 0


if __name__ == '__main__':
    TestClassTeardownFailException().run()
