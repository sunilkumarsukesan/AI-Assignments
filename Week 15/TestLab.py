from TestCase import TestCase
from AutomatedTestCase import AutomatedTestCase
from TestSuite import TestSuite


if __name__ == "__main__":

    # Manual test cases
    tc1 = TestCase("TC001", "Login with valid credentials", "Authentication")
    tc2 = TestCase("TC002", "Logout functionality", "Authentication")

    # Automated test cases
    atc1 = AutomatedTestCase("TC003", "User registration flow", "User Management", "Selenium")
    atc2 = AutomatedTestCase("TC004", "Password reset flow", "User Management", "Playwright")

    # Create test suite
    suite = TestSuite("Regression Test Suite")

    # Add test cases
    suite.add_test(tc1)
    suite.add_test(tc2)
    suite.add_test(atc1)
    suite.add_test(atc2)

    # Execute tests
    suite.run_all_tests()

    # Save results
    suite.save_results_to_csv("Week 15/test_results.csv")

    # Print summary
    suite.summary_report()