Python 2.7.18 (v2.7.18:8d21aa21f2, Apr 19 2020, 20:48:48) 
[GCC 4.2.1 Compatible Apple LLVM 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> """
This programme is a number guessing game.

The programme will roll a pair of dice and then add the m together.

Afterwards the user is asked to guess the number, based on the user guess the winner will be determined.
"""

from random import randint
from time import sleep

def get_user_guess():
  guess = int(raw_input("Guess a number:"))
  return guess

def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  max_val = number_of_sides * 2
  print "The maximum possible value is: %d" % max_val
  guess = get_user_guess()
  if guess > max_val:
    print "You have guessed an impossible value! Please try again"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is: %d." % (first_roll)
    sleep(1)
    total_roll = first_roll + second_roll
    print total_roll
    print "Result..."
    sleep(1)
    if guess == total_roll:
      print "Congratulations! You guessed correctly. Why not try again?"
    else:
      print "Unfortunately your guess wasn't correct, please try again."

roll_dice(6)
'\nThis programme is a number guessing game.\n\nThe programme will roll a pair of dice and then add the m together.\n\nAfterwards the user is asked to guess the number, based on the user guess the winner will be determined.\n'
>>> 
>>> 
>>> 
>>> 
