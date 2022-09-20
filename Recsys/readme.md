### 1. Best-seller 제품 추천
* 사용 이유: 신규 고객의 유입률을 높이고, 제품 신뢰성을 높이기 위함
* 추천 방식: 가장 많이 판매된 상품을 기준으로 내림차순으로 정렬하여 추천

### 2. Hot-deal 제품 추천
* 사용 이유: 신선식품의 폐기율을 낮추기 위해 오후 7시 이후 신선식품에 한하여 Hot-deal 제품 추천
* 추천 방식: 회전율을 요하는 신선식품을 대상으로 내림차순으로 정렬하여 추천(현 프로젝트에서는 상품 회전율을 나타내는 지표가 없어 랜덤 추천)

### 3. long-tail 제품 추천
* 사용 이유: 상품 쏠림 현상 방지 목적
* 추천 방식: 가장 적게 판매된 상품을 기준으로 정렬하여 추천
* 참고: 아마존의 경우 long-tail제품을 추천하고 많이 판매하여 이윤을 남겼다는 사례가 있음(long-tail 제품의 경우 판매자에게 돌아가는 이윤이 best-seller 제품보다 큼)

### 4. 남들이 같이 산 item 추천
* 사용 이유: 추천 성공률을 높이기 위함
* 추천 방식: 해당 상품을 샀던 고객이 같이 구매한 상품을 보여주는 방식(아이템간 유사도를 측정하여 추천해주는 형태)

### 5. 구매 내역에 따른 item 추천(WORD2VEC 이용)
* 사용 이유: 사용자가 상품을 담는 순서에도 의미가 있을 것. 주문, 장바구니 상품을 토대로 다음 상품 예측해보기
* 추천 방식: gensim의 word2vec 모델을 이용하여 가장 유사도 높은 상품 추천

### (시도1. Content-based model을 이용한 추천)
* 사용 이유: cold start(item) 문제 해결
* 추천 방식: 상품명 입력 시, content 기반 유사도 높은 상품 추천
* 예)![image](https://user-images.githubusercontent.com/102525066/191288012-54eb64cc-e44c-4013-b11e-b3a9da55e8aa.png)


### (시도2. SGD를 이용한 추천 - category grouping)
* 사용 이유: RAM초과로 인하여 grouping 진행 -> category끼리 유사도를 측정해서 그들만의 행렬 구성
* 추천 방식: 유사도 높은 상위 3개의 aisle 품목끼리 행렬을 만들어 유사도 높은 상품 추천 
* 시도 방식: cosine similarity, jarcard similarity, aisle 상위 3개의 품목끼리 행렬 구성 / aisle 상위 5개의 품목끼리 행렬 구성

### (시도3 SGD를 이용한 추천 - user grouping)
* 사용 이유: RAM초과로 인하여 grouping 진행 -> 유저를 군집화하여 그들 사이에서 추천
* 추천 방식: 4개의 그룹으로 나눠 df를 구성 -> 각 시간대에 속하는 유저의 집단에서 상품 추천
* 시도 방식: 평일 9 ~ 18시, 주말 9 ~ 18시, 평일 18 ~ 9시, 주말 18 ~ 9시 4개의 그룹으로 나누어 진행

#### 참고 사이트 및 공부 자료
* https://www.kaggle.com/code/bbksjdd/instacart-market-basket-analysis 
* https://www.kaggle.com/chocozzz/code
* https://github.com/journey101/Ecommerce-Recommendation-System-with-DeepLearning-YoutubeAlgorithm/blob/main/Ecommerce-Recommendation-System-adapting-DeepLearning-Youtube-Algorithm_0417(annotation_updated).ipynb
* https://brunch.co.kr/@goodvc78/18
* https://huidea.tistory.com/287
* https://dbr.donga.com/article/view/1203/article_no/8734
