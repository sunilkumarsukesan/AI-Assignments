marks = [78, 85, 62, 90 , 55, 88]
distinctionList = []

print(f"Maximum mark : {max(marks)}")
print(f"Minimum mark : {min(marks)}")
print(f"Average mark : {sum(marks)/len(marks):.2f}")


for mark in marks:
    if mark>=75:
        distinctionList.append(mark)

marks.append(95)
marks.remove(55)
print(f"Distinction list : {distinctionList}")
print(f"Updated marks: {marks}")
sorted = sorted(marks)
print(f"Sorted marks : {sorted}")

