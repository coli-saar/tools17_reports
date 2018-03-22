from collections import defaultdict

wordDict = defaultdict(set)

with open("de-train.txt", "r", encoding = 'utf-8') as f:
    for line in f:
        lineList = line.split()
        if len(lineList) != 0: 
            word, tag = lineList[0], lineList[1]
            wordDict[word].add(tag)

f = open("universalLexiconDE.txt", "w", encoding = 'utf-8') 
for word, tags in wordDict.items(): 
    f.write(word + '\t' + ' - '.join(tags) + ' -\n')
f.close() 
