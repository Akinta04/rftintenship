import matplotlib.pyplot as plt
import numpy as np

#DATASET
STUDENTS = ["AMIT","RIYA","JOHN"]
SUBJECTS = ["MATH", "SCIENCE", "ENGLISH"]

MATH_MARKS = [85, 78, 90]
SCIENCE_MARKS = [92, 88, 85]
ENGLISH_MARKS = [78, 82, 74]

# Grouped Bar Chart
x = np.arange(len(SUBJECTS))
width = 0.25

plt.bar(x - width, MATH_MARKS, width, label="MATH", color="blue")
plt.bar(x,SCIENCE_MARKS, width, label="SCIENCE", color="pink")
plt.bar(x + width, ENGLISH_MARKS, width, label="ENGLISH", color="cyan")

#Adding labels and titles
plt.title("STUDENT PERFORMANCE DASHBOARD")
plt.xlabel("STUDENTS")
plt.ylabel("MARKS")
plt.xticks(x,SUBJECTS)
plt.legend()

#display chart
plt.show()







