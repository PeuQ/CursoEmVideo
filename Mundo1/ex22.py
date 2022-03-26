"""
Create a program that shows a name:
- in all capitals and all lower letters
- how many letters
- how many letters the first name has
"""
name = input("What's your name?: ")
###
print("\nThe name fully capitalized is: {}".format(name.upper()))
###
print("\nThe name fully in lowercase is: {}".format(name.lower()))
###
letter_count = len(name) - name.count(" ")
print("\nThe full name letter count is: {}".format(letter_count))
###
name_list = name.split()
print("\nThe first name only letter count is: {}".format(len(name_list[0])))
