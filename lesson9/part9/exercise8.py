poem = """There’s a bluebird in my heart that
wants to get out
but I’m too tough for him,
I say,
stay down, do you want to mess me up?
you want to screw up the works?
you want to blow my book sales in Europe?
"""

while True:
    string = input("type a word: ")
    string = string.strip()

    if string.isalpha():
        word = string.lower()
        break
    else:
        print("type only characters!")

poem_lowered = poem.lower()
partitioned_poem = poem_lowered.splitlines()
print(partitioned_poem)

for pos in range(len(partitioned_poem)):
    if partitioned_poem[pos].find(word) != -1:
        print("line "+ str(pos) +": " + partitioned_poem[pos].replace(word, word.upper()))
