#!/usr/bin/env python3


from roster import student_roster
from classroom_organizer import ClassroomOrganizer


# create iterator object from student_roster list
student_roster_iter = iter(student_roster)

# print out each student dict in student_roster iterator using next()
print("\n--------- next() thru iterator object, print each item ---------\n")

try:
  while True:
    print(next(student_roster_iter))
except StopIteration:
  pass


# test ClassroomOrganizer iterator object
classroom_organizer = ClassroomOrganizer()

print("\n--------- print student names from iterator object ---------\n")

for item in classroom_organizer:
  print(item)


# print student combinations:
print("\n--------- print student combinations ---------\n")
for c in classroom_organizer.get_combinations():
  print(c)
