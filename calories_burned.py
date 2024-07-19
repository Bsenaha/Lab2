# *******************************/
# * CS03A - Summer 2024
# * Calories Burned
# * Student Name: Brandon Senaha
# * SID: 20510375
# *******************************/

def run():
  print('----- Calories Burned -----')

  # define cal burn rate
  cal_per_min = 4.2

  # loop through each minute
  for i in range(10,31,5):
    burn = i * cal_per_min # calc total calories burned
    print(f'{i} minutes: {burn} calories burned')