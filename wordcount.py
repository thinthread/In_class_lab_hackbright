poem = open("test.txt")

twain = open("twain.txt")



# def create_test_dict(poem):
#     """Create a word count for poem"""

#     for line in poem:
#         split_line = line.rstrip().split(" ")
#         for word in split_line:
#             word_count[word] = word_count.get(word, 0) + 1

#     for word, count in word_count.items():
#         print word + " " + str(count)

# create_test_dict(poem)


def create_twain_dict(twain):
    '''creat a word counter, save words to dictionary'''

    word_count = {}
    for line in twain:
        split_line = line.rstrip().split()
        for word in split_line:
            word_count[word] = word_count.get(word, 0) + 1

    for word, count in word_count.iteritems():
        print word + " " + str(count)

create_twain_dict(twain)
