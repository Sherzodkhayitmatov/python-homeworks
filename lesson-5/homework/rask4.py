import statistics

def enrollment_stats():
    
    universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
    ]
    students = [uni[1] for uni in universities]
    tuition_fee = [uni[2] for uni in universities]
    
    def mean(students):
        return sum(students) / len(students)
    
    student_median = statistics.median(students)
    tuition_mean = statistics.mean(tuition_fee)
    tuition_median = statistics.median(tuition_fee)
    print("******************************")
    print("Total students: ", sum(students))
    print("Total tuition: $", sum(tuition_fee))
    print()
    print("Student mean: ", round(mean(students), 2))
    print("Student median: ", round(student_median))
    print()
    print("Tuition mean: $", round(tuition_mean, 2))    
    print("Tuition median: $", round(tuition_median)) 
    print("******************************") 
    
    
enrollment_stats()