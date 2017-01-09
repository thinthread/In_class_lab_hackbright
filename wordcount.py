poem = open("test.txt")

word_count = {}


for line in poem:
    split_line = line.rstrip().split(" ")
    for word in split_line:
        word_count[word] = word_count.get(word, 0) + 1
print word_count
