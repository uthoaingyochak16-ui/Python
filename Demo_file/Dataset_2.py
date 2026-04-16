import pandas as pd

students = {
    "S001": {"name": "Alice Johnson", "age": 20, "major": "Computer Science", "gpa": 3.8},
    "S002": {"name": "Bob Smith", "age": 22, "major": "Mechanical Engineering", "gpa": 3.4},
    "S003": {"name": "Charlie Brown", "age": 19, "major": "Mathematics", "gpa": 3.9},
    "S004": {"name": "Diana Prince", "age": 21, "major": "Physics", "gpa": 3.7}
}

student_marks = {
    "Alice": [85, 90, 88, 92, 95],
    "Bob": [70, 75, 80, 68, 72],
    "Charlie": [95, 98, 92, 100, 96],
    "Diana": [88, 84, 90, 85, 89]
}

df1=pd.DataFrame(students)
df2=pd.DataFrame(student_marks)

combined_rows = pd.concat([df1,df2], axis=0).reset_index(drop=True)
print(combined_rows)