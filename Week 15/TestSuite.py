import csv 

class TestSuite:
    
    def __init__(self, suite_name):
        self.suite_name = suite_name
        self.test_cases = []
    
    def add_test(self, test_case):
        self.test_cases.append(test_case)
        
    def run_all_tests(self):
        print(f"Running Test Suite: {self.suite_name}")

        for test in self.test_cases:
            test.display_test_case()
            result = input("Enter result (Pass/Fail): ")
            if not result.strip():
                result = "Not Executed"
            test.execute_test(result)
            
    def save_results_to_csv(self, file_name):
        with open(file_name, mode="w", newline="") as file:
            csv_writer = csv.writer(file)
            csv_writer.writerow(["Test ID","Test Name","Module","Status","Automation Tool"])
            for test in self.test_cases:
                csv_writer.writerow(test.to_csv_row())
                
    def summary_report(self):
        total = len(self.test_cases)
        passed = 0
        failed = 0
        not_executed = 0
        for test in self.test_cases:
            if test.status == "Pass":
                passed += 1
            elif test.status == "Fail":
                failed += 1
            elif test.status == "Not Executed":
                not_executed += 1

        print("Test Execution Summary")
        print(f"Total Tests      : {total}")
        print(f"Passed Tests     : {passed}")
        print(f"Failed Tests     : {failed}")
        print(f"Not Executed     : {not_executed}")
    