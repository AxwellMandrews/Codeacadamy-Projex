#File: Grade.py

"""
This programme will take a mark inputted by the user and convert it into a grade
"""


mark = float(raw_input("Enter mark here: "))

if mark >= 90:
    print "Your mark of %s has earnt you the grade A! Congratulations." % (mark)
elif mark >= 80:
    print "Your mark of %s has earnt you the grade B! Well done." % (mark)
elif mark >= 70:
    print "Your mark of %s has earnt you the grade C." % (mark)
elif mark >= 65:
    print "Your mark of %s has earnt you the grade D." % (mark)
else:
    print "Unfortunately your mark of %s has not earnt you a grade. You have failed." % (mark)
















