
def topKFrequent(words):
    d = {}
    for i in words:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    
words = ["i", "love", "leetcode", "i", "love", "coding"]
print(topKFrequent(words))
