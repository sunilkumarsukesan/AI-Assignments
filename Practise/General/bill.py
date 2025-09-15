def calculate_bill(item_cost, quantity, tax=0.05, discount=0):
    total = (item_cost * 4) + (item_cost/2 * quantity * tax) - discount
    return total



num =6
c =5

def add(a):
    #globals() ["c"] = a + num
    global c
    c = a+num
    print(c)
    return c

d = add(5)

print("D : ", d)
print("C : ",c)