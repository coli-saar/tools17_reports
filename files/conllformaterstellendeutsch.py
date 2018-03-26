from pycorenlp import StanfordCoreNLP
import nltk
import sys

x = "Das ist ein Test."
nlp = StanfordCoreNLP("http://localhost:9000")
text = sys.argv[1]
name = sys.argv[2] + ".conll"
sentences = nltk.tokenize.sent_tokenize(text)

def convert(tag):
    if tag in ["ADJA","ADJD"]:
        return "ADJ"
    elif tag in ["APPO","APPR","APPRART","APZR","PTKVZ"]:
        return "ADP"
    elif tag in ["ADV","PAV","PAWV"]:
        return "ADV"
    elif tag in ["VAFIN","VAIMP","VAINF","VAPP"]:
        return "AUX"
    elif tag in ["KOKOM","KON"]:
        return "CCONJ"
    elif tag in ["ART","PIAT","PIDAT","PDAT","PPOSAT","PRELAT","PWAT"]:
        return "DET"
    elif tag == "ITJ":
        return "INTJ"
    elif tag == "NN" :
        return "NOUN"
    elif tag == "CARD":
        return "NUM"
    elif tag in ["PTKA","PTKANT","PTNEG","PTKZU"]:
        return "PART"
    elif tag in ["PDS","PIS","PPER","PPOS","PRELS","PRF","PWS"]:
        return "PRON"
    elif tag == "PROPN":
        return "NE"
    elif tag in ["$(","$","$."]:
        return "PUNCT"
    elif tag in ["KOUI","KOUS"]:
        return "SCONJ"
    elif tag in ["VMFIN","VMINF","VMPP","VVFIN","VVIMP","VVINF","VVIZU","VVPP"]:
        return "VERB"
    elif tag in ["FM","TRUNC","XY"]:
        return "X"
    else:
        return "SYM"
   

with open(name,"w") as f:
    for satz in sentences:
        out = nlp.annotate(satz,properties={"annotators":"pos","outputFormat":"json","pipelineLanguage":"german"})
        for token in out["sentences"][0]["tokens"]:
            w = token["word"]
            wortid = token["index"]
            postag = convert(token["pos"])
            f.write(str(wortid)+"\t"+w+"\t_\t"+postag+"\t"+postag+"\n")
        f.write("\n")

