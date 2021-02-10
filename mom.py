#!/usr/bin/env python3
from random import randrange

things_to_say = [
    "I love you!",
    "Dinner time",
    "Did you feed the chickens today?",
    "How's your homework going?",
    "Did you take your afternoon meds?",
    "Be nice to your brother please...",
    "Stop it!",
    "How was school?",
    "So the principal called me today...",
]

# q1: what number will be in `number_of_things`?
# q2: what does "len" mean? (hint: it's the first half of a word)
number_of_things = len(things_to_say)
# q3: what are all the possible numbers that can be returned by randrange here?
index = randrange(0, number_of_things)
# q4: what type of data is stored in "line"?
line = things_to_say[index]

print(line)

