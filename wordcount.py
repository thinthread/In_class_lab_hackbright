poem = open("test.txt")

twain = open("twain.txt")

word_count = {}


# for line in poem:
#     split_line = line.rstrip().split(" ")
#     for word in split_line:
#         word_count[word] = word_count.get(word, 0) + 1

# for word, count in word_count.items():
#     print word + " " + str(count)


for line in twain:
    split_line = line.rstrip().split(" ")
    for word in split_line:
        word_count[word] = word_count.get(word, 0) + 1

for word, count in word_count.iteritems():
    print word + " " + str(count)
