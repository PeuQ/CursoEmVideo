#palindrome detector
sentence = str(input("Enter a word: ")).strip().lower()
words = sentence.split()
joint = ''.join(words)
reverse = ''
for letter in range(len(joint) - 1, -1, -1):
  reverse += joint[letter]
#checking the palindrome veracity
if(reverse == joint):
  print("Yes, thats a palindrome.")
else:
  print("No, thats not a palindrome")

"""
Another solution:
reverse = joint[::-1] #gets the reverse of the word.
"""
