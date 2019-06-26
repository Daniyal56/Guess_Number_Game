
print(' ======================================== Guess Number Game ======================================== ')


number_of_guesses = 1
print('You have limited Guesses which is only 9 ' )
while (number_of_guesses<=5):
    guess_number = int(input())
    if guess_number<18:
      print('Enter smaller')
    elif guess_number>18:
      print('Enter greater')
    else:
      print('You have Won')
      break
    print(5-number_of_guesses, 'No. of guesses left ')
    number_of_guesses +=1
if number_of_guesses >5:
  print('GameOver')
      