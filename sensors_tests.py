import sensors_main             # Needed to set command line parameters
import unittest
import sys
from unittest.mock import patch # needed for integration test

# Unit tests implemented with Python's built-in unittest
# need to be classes, so here we use TestSensors class
# for the tests.
class TestSensors(unittest.TestCase):

    # The test case test_check_limits1 that tests the check_limits
    # with correct inputs (lower limit 18 and higher limit 22) and
    # expects the method to return True, since the limits are
    # correct.
    def test_check_limits1(self):
        limits = [18, 22]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result)
    def test_check_limits2(self):
        limits = [22, 18]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result)
    def test_check_limits3(self):
        limits = [20, 20]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result)
    def test_check_limits4(self):
        limits = [-20, 20]
        result = sensors_main.check_limits(limits)
        self.assertTrue(result)
    
    # The test case test_check_limits2 that tests the check_limits
    # with incorrect inputs (lower limit 22 and higher limit 18) and
    # expects the method to return False, since the limits are
    # incorrect. To be implemented.

    # Placeholder for the test case test_check_limits3. To be designed
    # and implemented. 
    

    # ************** Integration test *********************

    # Redirect console output to sys.stdout in order
    # to check its content from the test case
    @patch('builtins.print')
    def test_check_limits_integration1(self, mock_print):
        # set command line parameters for test case
        sys.argv = [["sensors_main.py"], [22], [18]]

        # call main from sensors_main
        sensors_main.main()

        # Check that console output is excpected error messege
        mock_print.assert_called_with("Error: Incorrect command line arguments.")

if __name__ == '__main__':
    unittest.main()