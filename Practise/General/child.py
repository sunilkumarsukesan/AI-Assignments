import bill as b

#positional
print(f"Bill one using positional : {b.calculate_bill(1000, 2)}")

#keyword
print("Bill two using keyword : ", b.calculate_bill(quantity= 2, item_cost=2000))

#keyword
print("Bill three using keyword and changing default: ", b.calculate_bill(quantity= 20, item_cost=2000, tax=0.07))

#keyword
print("Bill three using keyword and changing default: ", b.calculate_bill(20, 2000,discount=1,tax=0.07))
