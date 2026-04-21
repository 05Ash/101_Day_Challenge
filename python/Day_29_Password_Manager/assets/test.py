from wonderwords import RandomWord
import secrets

rw = RandomWord()
noun = rw.word(include_parts_of_speech=["nouns"]).capitalize()
verb = rw.word(include_parts_of_speech=["verbs"]).capitalize()
adj = rw.word(include_parts_of_speech=["adjectives"]).capitalize()
number = secrets.randbelow(100)
symbol = secrets.choice("!@#$%&*_")
# adv = rw.word(include_parts_of_speech=["adverbs"])
print(f"{adj}{noun}{verb}{symbol}{number}")
# print(rw.parts_of_speech.keys())
