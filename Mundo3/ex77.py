#tuples and vowels:

wordtuple = (str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")),
            str(input("input a word: ")))
#print(wordtuple)

for w in wordtuple:
  print(f"\nIn the word {w.upper()} we have ", end='')
  for c in w:
    if c.lower() in "aeiou":
      print(c.upper(), end=" ")
