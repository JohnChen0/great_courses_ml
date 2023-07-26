# Use data/spam-train.csv to generate data/vocab.txt.

words = {'': 0}
with open('data/spam-train.csv') as f:
  while line := f.readline():
    line = line[2:].strip()
    words[''] += 1
    for word in line.split():
      words[word] = words.get(word, 0) + 1

words_list = sorted(
    ((count, word) for word, count in words.items()),
    reverse=True)
with open('data/vocab.txt', 'w') as f:
  for count, word in words_list:
    f.write('%4d %s\n' % (count, word))
