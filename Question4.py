#This file uses a fabricated data set to answer health questions about fictitious patients. The data is included in csv file format in this folder.
#The question this script seeks to answer is: 
#Pharma Co. Z has a couple of follow-up questions after seeing the results of their previous inquiry. 

#a. How many patients are male, have diagnoses: 232065000 or H35.52, and the physician noted the patient complains of pain, fluttering, pressure or tightness in their chest? 

#b. How many patients with either of the two diagnoses might have experienced those symptoms, but cannot be confirmed using this data? Write 1-2 sentences for Pharma Co. Z about why this might be the case. 
#4A: Based on the prior question, we can create a list that combines all patients with heart attack symptoms. Then we can check this
#list against the clinical file for diagnosis codes. Finally, we can check which if these patients are male.
import csv
#open the patient note file. Please change the file paths here to direct to the patient note file path on your machine. Take note of the double slash syntax to avoid errors.
patient_note_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_note.csv'))
#for each note, check for each individual symptom and add it to its respective list for counting.
heart_attack_symptoms = []
for row in patient_note_file:
  if ("pain" in row[1]):
    heart_attack_symptoms.append(row[0])
  if ("flutter" in row[1]):
    heart_attack_symptoms.append(row[0])
  if ("pressure" in row[1]):
    heart_attack_symptoms.append(row[0])
  if ("tight" in row[1]):
    heart_attack_symptoms.append(row[0])
#Now we can access the clinical file to see how many of these patients with heart attack symptoms have the specified diagnosis codes:
heart_attack_with_codes = []
for i in heart_attack_symptoms:
  #Please modify this file path to reflect where the patient_clinical file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_clinical_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_clinical.csv'), delimiter = ',')
  for row in patient_clinical_file:
    if (i in row[0]) and ((row[1] == "232065000") or (row[1] == "H35.52")):
      heart_attack_with_codes.append(row[0])
#Lastly, we can take the new list we created and use it to parse through the patient demographics to determine which patients are male
male_heart_attack_symptoms = []
for i in heart_attack_with_codes:
  #Please modify this file path to reflect where the patient_demographics file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_demographics_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_demographics.csv'))
  for row in patient_demographics_file:
    #assume 1 is true for male
    if (i in row[0]) and (row[1] == "1"):
      male_heart_attack_symptoms.append(row[0])
#print(str(male_heart_attack_symptoms))
#print(str(len(male_heart_attack_symptoms)))
#Out of the all the patients, there are 15 with heart attack symptoms that have the specified diagnosis codes and are male.

#4b:
#We need to see how many patients total have received either one of these diagnosis codes.
#Please modify this file path to reflect where the patient_clinical file is stored on your machine. Note the use of double backslashes to avoid any runtime error
patient_clinical_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_clinical.csv'), delimiter = ',')
diagnosis_codes = []
for row in patient_clinical_file:
  if ((row[1] == "232065000") or (row[1] == "H35.52")):
    diagnosis_codes.append(row[0])
print("Diagnosis codes " + str(diagnosis_codes))
print(str(len(diagnosis_codes)))

#From the output we can see there are 100 total patients with either diagnosis code. Now we can check from this list if any had heart attack symptoms that can't be confirmed:
symptoms_confirmed = []
for i in diagnosis_codes:
  #Please modify this file path to reflect where the patient_note file is stored on your machine. Note the use of double backslashes to avoid any runtime error
  patient_note_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_note.csv'))
  for row in patient_note_file:
    if ((i in row[0]) and ("pain" in row[1])):
      symptoms_confirmed.append(row[0])
    if ((i in row[0]) and ("flutter" in row[1])):
      symptoms_confirmed.append(row[0])
    if ((i in row[0]) and ("pressure" in row[1])):
      symptoms_confirmed.append(row[0])
    if ((i in row[0]) and ("tight" in row[1])):
      symptoms_confirmed.append(row[0])
print(str(len(symptoms_confirmed)))
#A total of 100 patients have received diagnosis codes 232065000 or H35.52. Of these, only 32 were confirmed to have experienced symptoms related to heart attack.
#Therefore, there are 68 patients who may have experienced heart attack symptoms, but cannot be confirmed using this data. These patients may not have had corresponding
#patient notes. Moreover, patients may have used different language when reporting their symptoms or reported entirely different symptoms related to heart attack.