classGrades = { } # Initialize dictionary

numberOfClassesTaken = int(input('How many classes did you take last semester? '))

# Input Loop
for i in range(numberOfClassesTaken):
    classTaken = input('Enter a class name: ')
    grade = input('What grade did you get in ' + classTaken + '? ')
    classGrades[classTaken] = grade

print('Here are your grades from the previous semester:')

# Output Loop
for key in classGrades:
    print('In', key, 'you got a', classGrades[key])