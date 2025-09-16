import numpy as np
import random as rd

class TestReport:

    def __init__(self,execution_times):
        self.execution_times = execution_times

    def average_time(self):
        return np.mean(self.execution_times)

    def max_time(self):
        return np.max(self.execution_times)

class RegressionReport(TestReport):

    def __init__(self,execution_times):
        super().__init__(execution_times)

    def slow_tests(self,threshold):
        return self.execution_times[self.execution_times > threshold]

if __name__ == "__main__":
    num = []
    for i in range(0,10):
        num.append(rd.randint(5,99))
    execution_times = np.array(num)
    print(f"Execution times : {execution_times}")

    rp = RegressionReport(execution_times)
    print(f"Average time of overall execution :  {rp.average_time()}")
    print(f"Max time from overall execution times : {rp.max_time()}")
    print(f"Slow tests : {rp.slow_tests(threshold = 50)}")


