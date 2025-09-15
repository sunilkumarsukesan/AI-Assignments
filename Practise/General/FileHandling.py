with open("../docs/reports.txt", "a") as file:
    file.write("\nTestCase4 - Passed")
    file.write("\nTestCase5 - Failed")


with open("../docs/reports.txt", "r") as file:
    pass_count = 0
    failed_count = 0

    for line in file:
        if line.count("Passed"):
            pass_count += 1
        else:
            failed_count+= 1

totalCases =pass_count + failed_count
print(f"Total cases : {totalCases}")
print (f"Passed : {pass_count}")
print (f"Failed : {failed_count}")




