s = input()
words = s.split()

rev_word = [word[::-1] for word in words]
rev_s = ' '.join(rev_word)

print(rev_s)