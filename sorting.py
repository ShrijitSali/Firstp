pangram = " the quick brown fox jumps  over thelazy dog"

letters=sorted(pangram)
print(letters)
letter1=set(letters)
letter2=sorted(letter1)
print(letter1)
print(letter2)
print(len(letter2))