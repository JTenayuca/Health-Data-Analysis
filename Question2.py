#file written in python 3.10.3
#This file uses a fabricated data set to answer health questions about fictitious patients. The data is included in csv file format in this folder.
#The question this script seeks to answer is: Medical Device Company A comes to us and wants to find out how many patients
#with diabetes are under 75, have the following diagnostic codes: 408850009, 232063007, 232053004, 
#a total Cholesterol reading between 185 and 230, and a diastolic blood pressure reading of over 100? 
#First we need to determine who the diabetic patients in the cohort are. The patient history file contains this information. So we can access
#it at the appropriate filepath and compile these patients into a list
#import the csv module since we are accessing csv files
import csv
#create an empty array to store all of our diabetic patients
diabetic_patients = []
#create a file variable with the correct file path. Please modify this file path to reflect where the patient_history file is stored on your machine. Note the use of double backslashes to avoid any runtime errors.
patient_history_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_history.csv'), delimiter = ',')
#for every row in the file, check if '1' is entered in the diabetes column. This solution assumes that 1 = True for diabetes
for row in patient_history_file:
        if (row[6] == "diabetes"):
          continue
        if int(row[6]) == 1:
            #if 1 is in the diabetics column then append it to the diabetic_patients list.
            print(row[6])
            diabetic_patients.append(row[0])
#check to see how many diabetic patients there are. There are 109 patients
print("Number of diabetic patients: " + str(len(diabetic_patients)))
print(str(diabetic_patients))

#The next criteria we need to check for is if the patient is under 75. So we will need to access the patient demographics file for this data:
#initialize another list for diabetics under 75
diabetics_under_75 = []
#for every item in the diabetic_patients list, check the patient demographics file and check if their age is under 75:
for i in diabetic_patients:
  #Please modify this file path to reflect where the patient_demographics file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_demographics_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_demographics.csv'), delimiter = ',')
  for row in patient_demographics_file:
    #if the patient id in the diabetic_patients list matches the id in the column, and the age row is less than 75, then append that id to the diabetics_under_75 list. Convert the age row to an int in order to compare it.
    if (i in row[0]) and (int(row[2]) < 75):
      diabetics_under_75.append(row[0])
#print(diabetics_under_75)
print("Number of diabetics under 75: " + str(len(diabetics_under_75)))

#Lastly we need to check the patient clinical file for the appropriate diagnostic codes, total cholesterol range and diastolic blood pressure:
#create a list containing the finalized patient list:
final_patients = []
for i in diabetics_under_75:
  #Please modify this file path to reflect where the patient_clinical file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_clinical_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_clinical.csv'), delimiter = ',')
  for row in patient_clinical_file:
    if (i in row[0]) and ((row[1] == "408850009") or (row[1] == "232063007") or (row[1] == "232053004")) and (int(float(row[2])) >= 185) and (int(float(row[2])) <= 230) and (int(float(row[4])) > 100):
      final_patients.append(row[0])
    #if (i in row[0]) and ((row[1] == "408850009") or (row[1] == "232063007") or (row[1] == "232053004")):
    #  print(row)
print("Final patients list: " + str(final_patients))
print("The number of patients with these criteria is: " + str(len(final_patients)))
#It appears there are no patients that have any one of the listed diagnostic codes and have a total cholesterol in the specified range and have a diastolic blood pressure over 100.
#We can verify this by checking for diabetics with the diagnosis codes only and then examining the output:
final_patients_codes = []
for i in diabetics_under_75:
  #Please modify this file path to reflect where the patient_clinical file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_clinical_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_clinical.csv'), delimiter = ',')
  for row in patient_clinical_file:
    if (i in row[0]) and ((row[1] == "408850009") or (row[1] == "232063007") or (row[1] == "232053004")):
      print(row)
      final_patients_codes.append(row[0])

#From the output, we see that there are 12 patients with any of the diagnosis codes. Only 1 patient, EBKXMPR8J8Z6EY9RS2FPY4VRW, has a 
#diastolic BP over 100 (111.0) but the total cholesterol is out of range (258).
#We can run the loop similarly to check for these parameters individually.

