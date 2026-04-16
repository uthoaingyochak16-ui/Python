import pandas as pd

students = {
    "StudentID": list(range(301, 331)),

    "Name": [
        "Hiroshi Tanaka", "Yuki Sato", "Kenta Suzuki", "Aiko Yamamoto", "Daichi Kobayashi",
        "Mai Nakamura", "Takeshi Ito", "Sakura Watanabe", "Ryo Takahashi", "Emi Kato",
        "Sho Fujita", "Nanami Arai", "Kazuki Mori", "Ayumi Okada", "Yuto Hashimoto",
        "Mika Shimizu", "Ren Ishikawa", "Haruka Ueno", "Taro Kimura", "Misaki Abe",
        "Koji Inoue", "Rina Matsuda", "Sota Kuroda", "Yuna Hoshino", "Akira Ota",
        "Chisaki Honda", "Naoki Endo", "Saya Fujimoto", "Koki Yamada", "Nene Sugawara"
    ],

    "Gender": [
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female",
        "Male","Female","Male","Female","Male",
        "Female","Male","Female","Male","Female"
    ],

    "Department": [
        "CSE","EEE","CSE","ME","CSE",
        "EEE","ME","CSE","EEE","ME",
        "CSE","EEE","ME","CSE","EEE",
        "ME","CSE","EEE","ME","CSE",
        "EEE","ME","CSE","EEE","ME",
        "CSE","EEE","ME","CSE","EEE"
    ],

    "Age": [
        21,22,20,23,21,
        22,24,20,23,21,
        22,21,24,20,23,
        22,21,23,24,20,
        22,24,21,23,22,
        20,24,21,22,23
    ],

    "CGPA": [
        3.65,3.40,3.80,3.55,3.90,
        3.10,2.95,3.75,3.20,3.60,
        3.85,3.30,3.05,3.70,3.25,
        2.90,3.78,3.15,3.00,3.88,
        3.35,3.10,3.82,3.28,3.05,
        3.92,3.18,3.00,3.76,3.22
    ],

    "Math": [
        88,75,92,80,95,
        70,68,90,74,82,
        93,76,69,89,73,
        67,91,72,70,94,
        78,71,90,74,69,
        96,73,70,88,75
    ],

    "Physics": [
        85,78,90,82,93,
        74,70,88,76,84,
        91,79,72,87,75,
        69,89,74,73,92,
        80,72,88,77,71,
        94,76,73,86,78
    ],

    "Programming": [
        90,82,95,78,97,
        80,75,92,81,85,
        96,83,77,91,84,
        74,94,80,79,98,
        86,78,93,82,76,
        99,81,78,90,83
    ],

    "Attendance (%)": [
        92,85,95,88,97,
        83,80,94,86,90,
        96,87,82,93,85,
        78,95,84,81,98,
        89,83,94,86,80,
        99,85,82,91,88
    ],

    "Scholarship": [
        "Yes","No","Yes","No","Yes",
        "No","No","Yes","No","Yes",
        "Yes","No","No","Yes","No",
        "No","Yes","No","No","Yes",
        "No","No","Yes","No","No",
        "Yes","No","No","Yes","No"
    ],

    "Graduated": [
        "No","No","No","Yes","No",
        "No","Yes","No","No","No",
        "No","No","Yes","No","No",
        "Yes","No","No","Yes","No",
        "No","Yes","No","No","Yes",
        "No","Yes","No","No","No"
    ],

    "Email": [
        "hiroshi.tanaka@uni.jp","yuki.sato@uni.jp","kenta.suzuki@uni.jp","aiko.yamamoto@uni.jp","daichi.kobayashi@uni.jp",
        "mai.nakamura@uni.jp","takeshi.ito@uni.jp","sakura.watanabe@uni.jp","ryo.takahashi@uni.jp","emi.kato@uni.jp",
        "sho.fujita@uni.jp","nanami.arai@uni.jp","kazuki.mori@uni.jp","ayumi.okada@uni.jp","yuto.hashimoto@uni.jp",
        "mika.shimizu@uni.jp","ren.ishikawa@uni.jp","haruka.ueno@uni.jp","taro.kimura@uni.jp","misaki.abe@uni.jp",
        "koji.inoue@uni.jp","rina.matsuda@uni.jp","sota.kuroda@uni.jp","yuna.hoshino@uni.jp","akira.ota@uni.jp",
        "chisaki.honda@uni.jp","naoki.endo@uni.jp","saya.fujimoto@uni.jp","koki.yamada@uni.jp","nene.sugawara@uni.jp"
    ]
}


df=pd.DataFrame(students)

print("Data Filltering by Deparment ways:\n ")
df_filter = df[(df["Department"] == "ME")&(df["CGPA"] < 3.0)]
# print(df_filter)
df_filter = df[df["Department"].isin(["CSE", "EEE"])]
# print(df_filter)
df_filter = df[df["Math"].between(90, 100)]
# print(df_filter)

df_filter = df[df["Name"].str.contains("Sho Fujita", case=False)]
# print(df_filter)


df_filter = df.query("Department == 'CSE' and CGPA >= 3.5")
# print(df_filter)

max=df["CGPA"].max()
df_filter=df.query("CGPA>=3.5")
# print(df_filter)
df_filter.to_excel("Execl.xlsx")

df_filter = df.iloc[[10,2,8,5]]
# idf=df.loc[]
# print(df_filter)

df.loc[df["CGPA"] < 3.0, "Result"] = "Fail"
df.loc[df["CGPA"] >= 3.0, "Result"] = "Pass"

# print(df)

df_no_me = df[df["Department"]!= "ME"]
# print(df_no_me)


# Get Name and CGPA of the first 5 students (labels 0 to 4)
# Note: .loc is INCLUSIVE, so 0:4 gives five rows.
df_subset = df.loc[0:4, ["Name", "CGPA"]]
# print(df_subset)

print("Select all data for students in the 'CSE' department")
cse_students = df.loc[df["Department"] == "CSE"]
# print(cse_students)

print(" Select only 'Name' and 'Email' for students with Attendance > 95%")
high_attendance = df.loc[df["Attendance (%)"] > 95, ["Name", "Email"]]
# print(high_attendance)

name=df["Name"]
print(list(name))