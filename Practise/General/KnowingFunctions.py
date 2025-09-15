def calculate_salary(basic, hra, da, bonus=0):
    return basic + hra + da + bonus

def knowingArgs(*empDetails):
    for detail in empDetails:
        print(detail)

def knowingKArgs(**empDetails):
    for key,values in empDetails.items():
        print(key, " : ", values)

if __name__ == "__main__":
    print("Without bonus : " , calculate_salary(30000, 8000, 5000))
    print("With bonus : " , calculate_salary(30000, 8000, 5000,2000))
    knowingArgs("Test", "Testing",1000)
    knowingKArgs(name ="Sunil", Salary = "1000")