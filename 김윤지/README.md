### 1. 셀레니움 크롤링
CNN 뉴스 기사의 text 내용만을 불러와 크롤링 하여 txt 파일로 저장한다

### 2. mysql DB 저장
Stanford core nlp를 통해 tokenize한 단어를 matrix 형태로 만들어 저장한다

ex) rate ㅣ 주어 ㅣ 목적어 ㅣ 서술어 

### 3. New matrix 생성
DB에 저장한 matrix를 다시 주어&목적어 단어 set으로 엮어 rate를 값(연관성)으로 표현하여 matrix factorization 할 수 있도록 한다.

### 4. Matrix factorization


