# import seaborn as sns
# import matplotlib.pyplot as plt # Seaborn uses Matplotlib underneath
# print(sns.__version__)

# # Example plot
# fmri = sns.load_dataset("fmri")
# sns.lineplot(data=fmri, x="timepoint", y="signal")
# plt.show() # Use plt.show() to display the plot

import matplotlib.pyplot as plt
import pandas as pd

# স্যাম্পল ডাটা
data = {'Year': [2020, 2021, 2022, 2023],
        'Sales': [100, 150, 130, 170],
        'Profit': [20, 40, 35, 55]}
df = pd.DataFrame(data)

plt.figure(figsize=(8, 5))

# প্রথম ফিল্ড (Sales)
plt.plot(df['Year'], df['Sales'], label='Sales', marker='o')

# দ্বিতীয় ফিল্ড (Profit) - একই অক্ষে
plt.plot(df['Year'], df['Profit'], label='Profit', marker='s')

plt.xlabel('Year')
plt.ylabel('Amount')
plt.title('Sales vs Profit')
plt.legend() # লেবেল দেখানোর জন্য এটি জরুরি
plt.show()
