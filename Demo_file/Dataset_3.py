import pandas as pd
student_db = {
    "STUDENT_001": {
        "name": "Alice Johnson",
        "age": 20,
        "contact": {"email": "alice@edu.com", "phone": "555-0101"},
        "grades": {"Math": 95, "Science": 88, "History": 92}
    },
    "STUDENT_002": {
        "name": "Bob Smith",
        "age": 21,
        "contact": {"email": "bob@edu.com", "phone": "555-0102"},
        "grades": {"Math": 78, "Science": 82, "History": 80}
    }
}

df=pd.DataFrame(student_db)
df.info()
print(df.isnull())