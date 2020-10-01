# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here
f = open("ciphertext.txt", "r")
f = f.read()
def letter_count(s):
    d = {}

    for c in s:
        if not c.isalpha():
            continue

        """
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
        """
        if c not in d:
            d[c] = 0

        d[c] += 1

    return d

print(letter_count(f))
print(len(f))
freq = letter_count(f)
total = 0

lettercount = 15351
for key, value in freq.items():
    print(key, value/lettercount)

