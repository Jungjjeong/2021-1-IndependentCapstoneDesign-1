1. StanfordNLP 다운받기

    https://github.com/stanfordnlp/CoreNLP

    https://stanfordnlp.github.io/CoreNLP/

2. StanfordNLP GUI 사용해보기

터미널 창에

    java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer 9000

입력 후, http://localhost:9000/ 로 들어가기

3. StanfordNLP openIE CLI 사용하기

    https://stanfordnlp.github.io/CoreNLP/openie.html\

-1. 한문장씩 직접 입력

    java -mx1g -cp stanford-corenlp-4.2.0.jar:stanford-corenlp-4.2.0-models.jar:CoreNLP-to-HTML.xsl:slf4j-api.jar:slf4j-simple.jar edu.stanford.nlp.naturalli.OpenIE

-2. 파일 하나(또는 여러 파일)을 한번에 하기

    java -mx1g -cp stanford-corenlp-4.2.0.jar:stanford-corenlp-4.2.0-models.jar:CoreNLP-to-HTML.xsl:slf4j-api.jar:slf4j-simple.jar edu.stanford.nlp.naturalli.OpenIE /Users/justbeaver/Desktop/1test.txt

-3. 하나의 폴더에 있는걸 다 한번에

    java -mx1g -cp stanford-corenlp-<version>.jar:stanford-corenlp-<version>-models.jar:CoreNLP-to-HTML.xsl:slf4j-api.jar:slf4j-simple.jar edu.stanford.nlp.naturalli.OpenIE  -filelist /path/to/filelist

-4 추출된 relation을 text 파일에 저장

    java -mx1g -cp stanford-corenlp-4.2.0.jar:stanford-corenlp-4.2.0-models.jar:CoreNLP-to-HTML.xsl:slf4j-api.jar:slf4j-simple.jar edu.stanford.nlp.naturalli.OpenIE /경로/설정/해주기/input.txt > output.txt

4. 20210416 파일

word2vec을 사용해서 fact-check를 진행하고자 하는 object간의 relation에 원래 단어와는 다른 단어가 들어온 경우, 비슷한 단어를 찾는 과정

5. Transformer

https://www.youtube.com/watch?v=AA621UofTUA  

6. LSTM   

https://www.youtube.com/watch?v=mtVQpQBb30E    
https://github.com/minsuk-heo/tf2/blob/master/jupyter_notebooks/10.Word2Vec_LSTM.ipynb      

https://www.youtube.com/watch?v=64qSgA66P-8 - word2vec 영상    
https://www.youtube.com/watch?v=m2cg32uEeZw - LSTM 영상     

7. 관계 추출   

nltk를 사용하여 tokenization, PoS Tagging을 이용한 주어와 동사 간의 관계 이어주는 방법으로 관계 추출