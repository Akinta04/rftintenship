MARKS = [75,85,90,67,85,92,78]

#AVERAGE
TOTAL = 0
for i in MARKS:
    TOTAL+=i
AVG= TOTAL/len(MARKS)
print("AVERAGE:",AVG)

#HIGHEST AND LOWEST
HIGHEST = MARKS[0]
LOWEST = MARKS[0]

for i in MARKS:
    if i > HIGHEST:
        HIGHEST = i
    if i < LOWEST:
        LOWEST = i
print("HIGHEST:",HIGHEST)
print("LOWEST:",LOWEST)

#count students above average
COUNT = 0
for i in MARKS:
    if i > AVG:
        COUNT +=1
print("NUMBER OF STUDENTS SCORED ABOVE AVERAGE:",COUNT)

#GRADE DISTRIBUTION
def SCORE(num):
    if num>=90:
        return "A"
    elif num>=80:
        return "B"
    elif num >= 70:
        return "C"
    else:
        return "FAIL"

#PRINT GRADES
print("GRADES :")
for i in MARKS:
    print(SCORE(i))
