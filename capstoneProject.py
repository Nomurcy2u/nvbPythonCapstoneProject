# Method 3 — Direct URL (replace YOUR_FILE_ID with the ID from Classroom)
import pandas as pd
import matplotlib.pyplot as plt
#Import file
url = 'https://drive.google.com/uc?id=11H0jiMaKbUN1IZgdMZjNPkQ3ee8f80lQ'
df = pd.read_csv(url)
#print(f"Loaded: {df.shape[0]} rows, {df.shape[1]} columns")

def test():
  # df is already loaded earlier; confirm it loaded correctly
  print(f"Shape: {df.shape}")
  print()
  print("Column types:")
  print(df.dtypes)
  print()
  print("Basic statistics:")
  print(df.describe().round(2))
  print()
  print("Basic info about the columns")
  print(df.info())

def createBarPlot(df,title,x,y):
  df.plot(kind="bar")
  plt.title(title)
  plt.xlabel(x)
  plt.ylabel(y)
  plt.tight_layout()
  plt.show()

def lineFunction():
  print(f"=-"*41)
#Functions above:

#Functions related to df data that were used for research
#test()
#print(f"{df.info()}")
#print(f"{df.isnull().sum()}")
#createBarPlot(df,"Entire df", "columns", "row #s")
'''
# Sample Questions
1. Which attack types are most frequent and which have the longest response times?
2. Do critical-severity incidents lead to data loss more often than lower-severity ones?
3. Which department or system is targeted most often, and what is the typical outcome?
'''
#MY QUESTIONS
lineFunction()
print("MY QUESTION: When is the avg time high severity attacks occur? ")
print("2nd QUESTION:  Which attacks generally cause the MOST data loss?")

#First graph
lineFunction()
meanSeverityVal = df.groupby('severity')['hour_of_day'].mean()
#print(f"{meanSeverityVal}")
createBarPlot(meanSeverityVal,"Mean severity value per hour","severity","avg time of day")
print("Findings: Most attacks occur around 12")

#2nd Graph:
lineFunction()
meanDataLoss = df.groupby('severity')['data_loss_occurred'].mean()
#print(f"{meanSeverityVal}")
createBarPlot(meanDataLoss,"Mean data loss per severity","severity","avg data loss")
print("Findings: Data loss generally only occurs in high to critical severity attacks")

#Summary of findings
lineFunction()
print(f"""
SUMMARY — nvb_cybersecurity_incidents.csv Exploration
==========================================
Questions:
MY QUESTION: When is the avg time high severity attacks occur?
2nd QUESTION:  Which attacks generally cause the MOST data loss?

Findings:
Most attacks occur around 12
Data loss generally only occurs in high to critical severity attacks

Recommendation: I would suggest reducing high-critical attacks to minimize data loss and increasing security observation at 12:00.
""")
lineFunction()
