import numpy as np
import random as rd

class ManualTester:

    def analyze(self, data : np.ndarray):
        return data[:5]


class AutomationTester:

    def analyze(self, data : np.ndarray):
        return data.min()


class PerformanceTester:

    def analyze(self, data : np.ndarray):
        return np.percentile(data,95)


def show_analysis(tester : object, data):
    return tester.analyze(data)


if __name__ == "__main__":
    num = []
    for i in range(0,12):
        num.append(rd.randint(5,99))
    execution_times = np.array(num)

    print(f"Execution times : {execution_times}")
    print(f"Analysis done for a Manual tester :  {show_analysis(ManualTester(), execution_times)}")
    print(f"Analysis done for an Automation tester :  {show_analysis(AutomationTester(), execution_times)}")
    print(f"Analysis done for a Performance tester :  {show_analysis(PerformanceTester(), execution_times)}")