#bigger and lower in a random tuple
import random
randomtuple = (random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10), random.randint(1,10))

print("Generated tuple: {}\nGreatest value = {}\nLowest value = {}".format(tuple(randomtuple), max(randomtuple), min(randomtuple)))
