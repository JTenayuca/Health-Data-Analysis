##This file uses a fabricated data set to answer health questions about fictitious patients. The data is included in csv file format in this folder.
#The question this script seeks to answer is:  Is there a relationship between the number of cigarettes smoked per day and the prevalence of diabetes?  
#Run a statistical test to determine significance, interpret the results and create a visualization to display this. 
import csv
import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
#access patient_history file Please modify this file path to reflect where the patient_history file is stored on your machine. Note the use of double backslashes to avoid any runtime error
patient_history_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_history.csv'), delimiter = ",")
#create lists for cigs per day and diabetes
cigs_per_day = []
diabetes = []
#compile the lists from the file
for row in patient_history_file:
  if(row[2] == "cigsPerDay"):
    continue
  if(row[2] == ""):
    continue
  if(row[6] == "diabetes"):
    continue
  if(row[6] == ""):
    continue
  cigs_per_day.append(float(row[2]))
  diabetes.append(float(row[6]))

print(cigs_per_day)
print(diabetes)
#define dependent and independent variables and put them into a numpy array
x = np.array(diabetes).reshape((-1, 1))
y = np.array(cigs_per_day)
#perform linear regression to use the linear probability model. Here a logistic regression could also be done.
model = LinearRegression().fit(x, y)
r_sq = model.score(x, y)
print(f"coefficient of determination: {r_sq}")
#In this case the r value is 0.001340809154176858. This value is essentially zero, so there is no real linear relationship
plt.scatter(x, y, color="black")