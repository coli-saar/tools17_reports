import sys
import nltk

text = sys.argv[1]
name = sys.argv[2] + ".conll"
sentences = nltk.tokenize.sent_tokenize(text)
with open(name,"w") as f:
    wortid = 1
    for satz in sentences:
        words = nltk.pos_tag(nltk.word_tokenize(satz))
        for wort in words:
            pos = wort[1]
            f.write(str(wortid)+"\t"+wort[0]+"\t_\t"+pos+"\t"+pos+"\n")
            wortid += 1
        f.write("\n")
