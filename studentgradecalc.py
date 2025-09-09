#Student Grade Calculator
marks=[]
for i in range(1,6):
    marks.append(int(input("Enter marks: ")))
total=sum(marks)
average=total/len(marks)
if average>=90:
                 grade="A"
elif average>=75:
                 grade="B"
elif average>=50:
                 grade="C"
else:
                 grade="F"
print('Total marks: ', total)
print('Average marks: ',average)
print('Grade', grade)
