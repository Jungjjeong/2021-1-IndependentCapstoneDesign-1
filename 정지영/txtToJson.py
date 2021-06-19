import json
import nltk
# nltk.download('punkt')
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
txt_dict = {}
with open('result5.json', 'w') as fp:
    fp.write("[")
    for i in range(0, 45):
        # fileName = './Data/{0}test.txt'.format(i)
        fileName = './result-bitcoin/{0}.txt'.format(i)
        with open(fileName, encoding='utf-8') as f:
            txt = f.read()
            txt_list = sent_tokenize(txt)
            txt_dict["title"] = txt_list[0]
            txt_dict["values"] = txt_list[:]

            # print(txt_dict)
            print(len(txt_dict.keys()))
        json.dump(txt_dict, fp,indent = '\t')
        fp.write(",")
    fp.write("]")



    