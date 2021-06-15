# Python 3.8.8 ('base':conda)

# Basic Idea
# 크롤링 된 기사를 './input_text_KO' 파일에 넣고 이 파일을 돌리면
# noun verb noun (구분 기준: space)
# 의 형태로 './relation_KO' 파일에 텍스트 파일이 저장


import numpy as np
from konlpy.tag import Okt
okt = Okt()


def get_relation(words):
  ## Tokenization & Pos Tagging
  pos_tagged = []
  pos_tagged2 = []
  pos_tagged_final = []

  pos_tagged.append(okt.pos(words))
  # print(pos_tagged[0][:5])

  for i in range(len(okt.pos(words))):
    pos_tagged2.append(list(pos_tagged[0][i]))
  # print(pos_tagged2[:5])

  for i in range(len(pos_tagged2)):
    if pos_tagged2[i][1] == 'Noun' or pos_tagged2[i][1] == "Verb" or pos_tagged2[i][1] == "Number":
        pos_tagged_final.append(pos_tagged2[i])
  # print(pos_tagged_final[:5])

  relation = []

  ## Extracting Relation in N V N form
  for i in range(len(pos_tagged_final)):
    relate = []
    if pos_tagged_final[i][1] == "Verb":
      if i <= 1:
        if pos_tagged_final[0][1] == "Verb":
          relate.append(pos_tagged_final[1][0])
          relate.append(pos_tagged_final[0][0])
          relate.append(pos_tagged_final[2][0])
          relation.append(relate)
          relate = []
        elif pos_tagged_final[1][1] == "Verb":
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
        if pos_tagged_final[len(pos_tagged_final)-2][1] == "Verb":
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
        elif pos_tagged_final[len(pos_tagged_final)-1][1] == "Verb":
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

  # print(relation[:5])     


  ## save the relation array as a text file
  np.savetxt('./relation_KO/relation.txt', relation, fmt='%s', delimiter=' ')



## place the text file you want to extract relation in to "./input_text_EN" file
## write the name of the text file 
f = open(r'./input_text_KO/1.txt')
text = f.read() 
f.close()

get_relation(text)