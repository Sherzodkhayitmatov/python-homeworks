import csv 

grades_data = []
with open('grades.csv', mode='r', newline='') as file:
     reader = csv.DictReader(file)
     for row in reader:
        row['Grade'] = float(row['Grades'])
        grades_data.append(row)
        
subject_totals = {}
subject_counts = {}

for entry in grades_data:
    subject = entry['Subject']
    grade = entry['Grade']
    
    if subject in subject_totals:
        subject_totals[subject]  += 'grades'
        subject_counts[subject] += 1
    else:
        subject_totals[subject] = grade
        subject_counts[subject] = 1
        
subject_averages = {}
for subject in  subject_totals:
    subject_averages[subject] = subject_totals[subject] / subject_counts[subject]
    
with open('average_grades.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow['Subject', 'Average Grade']
    
    for subject, avg in subject_averages.items():
        writer.writerow([subject, avg])
        
print("Average grades per subject.")

for subject, avg in subject_averages.items():
    print(f"{subject}: {avg}")
     
        

         
     
     