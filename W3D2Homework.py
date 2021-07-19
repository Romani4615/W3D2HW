words = ['this' , 'is', 'a', 'sentence', '.']
print(words)
words[0], words[1], words[2], words[3], words[4] = words[4], words[3], words[2], words[1], words[0]

print(words)
a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'
def word_count(str1):
    str1 = str1.lower()
    dict1 = {}
    word_list = str1.split(" ")
    for words in word_list:
        count = 0
        for word in word_list:
            if words == word:
                count += 1
        dict1[words] = count
    return dict1