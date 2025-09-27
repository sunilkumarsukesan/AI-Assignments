def fizz_buzz(upperLimit):
    for index in range(1,upperLimit):
        if (index%3==0) and (index%5==0):
            print("FizzBuzz")
        elif (index%3==0):
            print("Fizz")
        elif (index%5==0):
            print("Buzz")
        else:
            print(index)

def authenticate_user():
    for index in range(1,4):
        if input("Enter your password : ")=="openAI123":
            print("Login Successful")
            break
        elif (index==3):
            print("Account Locked")
        else:
            print (f"{3-index} attempt(s) left")

def display_employee_names():
    employees = ["Alice", "Bob", "Charlie", "David", "Eve"]
    for (index,name) in enumerate(employees):
        print (f"{index+1}. {name}")

def atm_withdrawal():
    withdrawal_amount = int(input("Enter your withdrawal amount : "))
    if (withdrawal_amount%100==0):
        print(f"Dispensing {withdrawal_amount}")
    else:
        print("Accepts only the withdrawal amount which is a multiple of 100")

def display_sales_summary():
    sales = [1200, 3400, 560, 4500, 2100]
    print(f"Total Sales : {sum(sales)}")
    print(f"Average Sales : {sum(sales)/len(sales)}")
    print(f"Total Sales : {max(sales)}")
    print(f"Total Sales : {min(sales)}")


if __name__ == "__main__":
    fizz_buzz(20)
    authenticate_user()
    display_employee_names()
    atm_withdrawal()
    display_sales_summary()

