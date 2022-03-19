str1 = 'the quick brown fox jumps over the lazy dog.'
counts = dict()
str1 = str1.split()
for i in str1:
    if i in counts:
        counts[i] += 1
    else:
        counts[i]  = 1
print(counts)