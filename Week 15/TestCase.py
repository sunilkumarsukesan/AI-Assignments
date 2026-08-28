import csv

class TestCase:
    
    def __init__(self, test_id, test_name, module):
        self.test_id = test_id
        self.test_name = test_name
        self.module = module
        self.status = "Not Executed"
        
    def execute_test(self, result):
        self.status = result
        
    def display_test_case(self):
        print(self.test_id , self.test_name, self.module, self.status)
        
    def to_csv_row(self):
        return [self.test_id, self.test_name, self.module, self.status, "NA"]