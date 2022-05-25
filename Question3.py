#This file uses a fabricated data set to answer health questions about fictitious patients. The data is included in csv file format in this folder.
#The question this script seeks to answer is: 
#Pharma Co. Z has a product on the market to prevent heart attacks. They want to study patients who complain of signs of heart attacks to their doctors. 
#Specifically, they are interested in knowing how many patients complaining of pain, fluttering, pressure or tightness
# in their chest have that documented in the notes of their record. Write code for and provide counts of how many unique
# patients match this criteria. Write a short summary to the client communicating what you did. 
#If we wanted to recommend a more advanced text search, what would you suggest doing? 
#To start, we need to parse the patient_note csv file to check for any of the relevent terms to see if there are patient complaints of
#pain, tightness, fluttering or pressure. First we have to access the patient notes file and then parse it.
import csv
#Create individual lists in order to have a break down of each patient symptom
pain_signs = []
fluttering_signs = []
pressure_signs = []
tightness_signs = []
#open the patient note file. Please change the file path here to direct to the patient note file path on your machine. Take note of the double slash syntax to avoid errors.
patient_note_file = csv.reader(open('C:\\Users\\JTena\\OneDrive\\Documents\\data_split\\data_split\\patient_note.csv'))
#for each note, check for each individual symptom and add it to its respective list for counting.
for row in patient_note_file:
  if ("pain" in row[1]):
    pain_signs.append(row[0])
  if ("flutter" in row[1]):
    fluttering_signs.append(row[0])
  if ("pressure" in row[1]):
    pressure_signs.append(row[0])
  if ("tight" in row[1]):
    tightness_signs.append(row[0])
#take a count of all symptoms and output the results.
pain_signs_count = len(pain_signs)
fluttering_signs_count = len(fluttering_signs)
pressure_signs_count = len(pressure_signs)
tightness_signs_count = len(tightness_signs)

print("The number of patients with chest pain complaints is " + str(pain_signs_count) + ". The number of patients with fluttering symptoms is: " + str(fluttering_signs_count) + ". The number of patients with pressure symptoms is " + str(pressure_signs_count) + ". And the number of patients with tightness is " + str(tightness_signs_count) + ".")
total_heart_attack_symptoms = pain_signs_count + fluttering_signs_count + pressure_signs_count + tightness_signs_count
print("The total number of patients with all of these heart attack symptoms is: " + str(total_heart_attack_symptoms))
#Summary to client:
#Dear client, in accordance with your instructions we have completed a study on the number of patients presenting with
#heart attack symptoms to their doctors. We examined the patient notes for the 2612 patients provided for any indication
#of the specified symptoms. In particular, each note was parsed for any mentions of "pain", "tightness", "fluttering" or "pressure". 
#This includes the terms "flutter" or "tight". A count was made for each individual type of complain and a total was tallied.
#A total of 617 patients complained of chest pain. 190 patients complained of fluttering. 190 patients complained of chest pressure. 188
#patients complained of tightness. The total number of patients with these symptoms combined was 1185. A more advanced search may incorporate synonyms and related terms. Moreover, we may also want to utilize natural
#language processing tools to analyze the sentiment of patients and health care professionals specifically with respect to the patient's cardiovascular health.  If you have any further questions
#please do not hesitate to contact me.

#SQL SOLUTION: A number of queries can be compiled to attain the same results. Assume the table is named patient_note:
#SELECT * FROM patient_note
#WHERE note LIKE '%pain%'
#  OR note LIKE 'flutter%'
#  OR note LIKE '%pressure%'
# OR note LIKE %tight%