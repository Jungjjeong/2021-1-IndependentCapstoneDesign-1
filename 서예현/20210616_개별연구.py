# Python 3.8.8 ('base':conda)

# Basic Idea
# 크롤링 된 기사를 './input_text' 파일에 넣고 이 파일을 돌리면
# noun verb noun (구분 기준: space)
# 의 형태로 './relation' 파일에 텍스트 파일이 저장


import nltk
import numpy as np
from nltk import word_tokenize

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def get_relation(words):
    
  ## Tokenization & Pos Tagging
  pos_tagged = []
  pos_tagged2 = []
  pos_tagged_final = []

  pos_tagged.append(nltk.pos_tag(words))

  for i in range(len(nltk.pos_tag(words))):
    pos_tagged2.append(list(pos_tagged[0][i]))

  for i in range(len(pos_tagged2)):
    if pos_tagged2[i][1] == 'NN' or pos_tagged2[i][1] == "NNS" or pos_tagged2[i][1] == "VBN" or pos_tagged2[i][1] == "VBZ" or pos_tagged2[i][1] == "VBP" or pos_tagged2[i][1] == "VB" or pos_tagged2[i][1] == "VBD":
      pos_tagged_final.append(pos_tagged2[i])
  # print(pos_tagged_final)

  relation = []
  # print(len(pos_tagged_final))



  ## Extracting Relation in N V N form
  for i in range(len(pos_tagged_final)):
    relate = []
    if pos_tagged_final[i][1] == "VBN" or pos_tagged_final[i][1] == "VBZ" or pos_tagged_final[i][1] == "VBP" or pos_tagged_final[i][1] == "VB" or pos_tagged_final[i][1] == "VBD":
      # print(i)
      if i <= 1:
        if pos_tagged_final[0][1] == "VBN" or pos_tagged_final[0][1] == "VBZ" or pos_tagged_final[0][1] == "VBP" or pos_tagged_final[0][1] == "VB" or pos_tagged_final[0][1] == "VBD":
          relate.append(pos_tagged_final[1][0])
          relate.append(pos_tagged_final[0][0])
          relate.append(pos_tagged_final[2][0])
          relation.append(relate)
          relate = []
        elif pos_tagged_final[1][1] == "VBN" or pos_tagged_final[1][1] == "VBZ" or pos_tagged_final[1][1] == "VBP" or pos_tagged_final[1][1] == "VB" or pos_tagged_final[1][1] == "VBD":
          relate.append(pos_tagged_final[0][0])
          relate.append(pos_tagged_final[1][0])
          relate.append(pos_tagged_final[2][0])
          relation.append(relate)
          relate = []

          relate.append(pos_tagged_final[2][0])
          relate.append(pos_tagged_final[1][0])
          relate.append(pos_tagged_final[3][0])
          relation.append(relate)
          relate = []
      elif i >= len(pos_tagged_final)-2:
        if pos_tagged_final[len(pos_tagged_final)-2][1] == "VBN" or pos_tagged_final[len(pos_tagged_final)-2][1] == "VBZ" or pos_tagged_final[len(pos_tagged_final)-2][1] == "VBP" or pos_tagged_final[len(pos_tagged_final)-2][1] == "VB" or pos_tagged_final[len(pos_tagged_final)-2][1] == "VBD":
          relate.append(pos_tagged_final[len(pos_tagged_final)-4][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-2][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-3][0])
          relation.append(relate)
          relate = []

          relate.append(pos_tagged_final[len(pos_tagged_final)-3][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-2][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-1][0])
          relation.append(relate)
          relate = []
        elif pos_tagged_final[len(pos_tagged_final)-1][1] == "VBN" or pos_tagged_final[len(pos_tagged_final)-1][1] == "VBZ" or pos_tagged_final[len(pos_tagged_final)-1][1] == "VBP" or pos_tagged_final[len(pos_tagged_final)-1][1] == "VB" or pos_tagged_final[len(pos_tagged_final)-1][1] == "VBD":
          relate.append(pos_tagged_final[len(pos_tagged_final)-3][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-1][0])
          relate.append(pos_tagged_final[len(pos_tagged_final)-2][0])
          relation.append(relate)
          relate = []
      else:
        relate.append(pos_tagged_final[i-2][0])
        relate.append(pos_tagged_final[i][0])
        relate.append(pos_tagged_final[i-1][0])
        relation.append(relate)
        relate = []

        relate.append(pos_tagged_final[i-1][0])
        relate.append(pos_tagged_final[i][0])
        relate.append(pos_tagged_final[i+1][0])
        relation.append(relate)
        relate = []

        relate.append(pos_tagged_final[i+1][0])
        relate.append(pos_tagged_final[i][0])
        relate.append(pos_tagged_final[i+2][0])
        relation.append(relate)
        relate = []

  print(relation[:5])     


  ## save the relation array as a text file
  np.savetxt('./relation_EN/relation.txt', relation, fmt='%s', delimiter=' ')



## place the text file you want to extract relation in to "./input_text" file
## write the name of the text file 
f = open(r'./input_text/5.txt')
text = f.read() 
f.close()

words = word_tokenize(text)
get_relation(words)