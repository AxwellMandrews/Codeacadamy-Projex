#File: CandTAreaCalc.py

"""
Python Codeacadamy
In this programme you will be able to calculate the area of both a circle and a triangle.
"""

print "Starting Calculator"

option = raw_input("Enter C for circle or T for triangle:")

if option == 'C':
  radius = float(raw_input("What is the radius of your circle?:"))
  area = 3.14159 * (radius ** 2)
  print "The area of your circle is %s" % (area)
elif option == 'T':
  base = float(raw_input("What is the base of your triangle?:"))
  height = float(raw_input("What is the height of your triangle?:"))
  area = 0.5 * base * height
  print "The area of your triangle is %s" % (area)
else:
  print "Sorry, you have entered an invalid shape, please try again with one of the specified charachters."

print "Thankyou for using this service! The programme is now exiting"