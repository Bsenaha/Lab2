# *******************************/
# * CS03A - Summer 2024
# * Age Classifier
# * Student Name: Brandon Senaha
# * SID: 20510375
# *******************************/

def run():
  print('----- Age Classifier -----')

  # user input age
  while True:
    age = input('Enter an age: ')
    
    if age.isalpha():   # refuse non-numeric age
      print('\n**Please enter a number**\n')
    elif int(age) < 0:  # refuse negative age
      print('\n**Invalid age**\n')
    else:               # accept numeric age as int
      age = int(age)
      break # move to classification
      
  # classify age brackets and display result
  if age <= 1:                 # if infant
    print('\nThe person is an infant\n') 
  elif age > 1 and age < 13:   # if child
    print('\nThe person is a child\n') 
  elif age >= 13 and age < 20: # if teen
    print('\nThe person is a teenager\n') 
  elif age >= 20:               # if adult
    print('\nThe person is an adult\n')