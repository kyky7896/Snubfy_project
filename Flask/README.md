Back과 Front 합친 파일입니다.
이경영, 정주영이 협업했습니다.

## 목차
- 시작
  - 프로젝트 소개
  - 프로젝트 기능
  - 사용기능
    - 백엔드
    - 프론트엔드
  - 실행화면
- 구조 및 설계
  - 패키지 구조
  - DB 설계
- 개발 내용
- 마치며
  - 보완사항
  - 후기
  
<br>

시작 
---
### 1.  프로젝트 소개
  플레이데이터의 파이널 프로젝트 진행중, 코로나19를 겪으며 건강관리 인식변화에 주목하여 아이디어를 구상함.

### 2. 프로젝트 기능
  - 사용자 회원가입, 로그인 기능 구현 
  ![image](https://user-images.githubusercontent.com/77670592/191906806-741dd161-0803-461a-a3fe-28eca0891e47.png)
  ![image](https://user-images.githubusercontent.com/77670592/191906858-0904943d-5233-444a-851e-004968f51038.png)

  - 메인 :
    - 로그인 이전 : ( 이전, 이후 공통 ) 가장 많이 팔린 제품 TOP 30 중, 랜덤 9개 제품 보여짐.
    ![image](https://user-images.githubusercontent.com/77670592/191904521-2293d835-09f6-4703-bdfe-0e74580cc003.png)
    - 로그인 이후 : ( 신규회원 - 주문한 적이 없는 회원 ) 할인제품  <br>
                   ( 기존회원 - 주문한 적이 있는 회원 ) 주문한 제품 기반의 추천 제품  
                   ![image](https://user-images.githubusercontent.com/77670592/191904805-7590df7f-05aa-4dc9-93ce-710d88bf33a9.png)
                   ( Admin 로그인시 ) 기존회원과 동일하나 마이페이지에서 제품 CRUD가능  
                   ![image](https://user-images.githubusercontent.com/77670592/191906567-debe9b40-99be-4912-8d7b-11770deca320.png)  
                   주문 제품 마이페이지에서 확인 가능  
 ![image](https://user-images.githubusercontent.com/77670592/191905008-3a0163a2-c951-4b7a-8c10-365f6c7fa566.png)
 <br>
 <br>

  - 카테고리 :
    - 대분류, 중분류 단어 클릭시 9개 제품 나타남  
        ![image](https://user-images.githubusercontent.com/77670592/191905308-72ed5607-1087-4b74-b427-d236a860a6c8.png)
    - 상품 detail에는 상품이름, 가격, 영양소, 제픔과 유사성을 보이는 추천제품, 해당 상품으로 만들수 있는 레시피 소개  
    ![image](https://user-images.githubusercontent.com/77670592/191905925-7b9ced1b-cc8e-4a28-b25c-2f636b93da8e.png)
    ![image](https://user-images.githubusercontent.com/77670592/191905819-19af640a-b64f-4ffd-8063-3d1004dafe67.png)  
    <br>
    <br>
   - 레시피 :  
     - 레시피 리스트 
   ![image](https://user-images.githubusercontent.com/77670592/191906079-26a44a8e-c66b-47f8-aa03-8734f31125b1.png)
     - 레시피 상세 
     ![image](https://user-images.githubusercontent.com/77670592/191906231-7a3e60b0-0120-4d99-aae0-cfb052b47883.png)

  <br>
  <br>
  
  - 장바구니 : <br>
  ![image](https://user-images.githubusercontent.com/77670592/191906410-ca503d99-eb79-4d26-85a6-e5c50f0266fc.png)


## 3. 사용 기술
  
  3-1 백엔드
  주요 프레임워크 / 라이브러리
  - Python 3.9
  - Flask
  - Flask-WTF 1.0.1
  - Jinja 3.1.2
  - SQLalchemy
  
  백엔드 for 모델추천
  - joblib=1.1.0
  - gensim 3.6.0
  
  Database
  - MySQL 8.0
  
  3-2 프론트엔드 
  - HTML/CSS
  - JavaScript
  
  
  ## 4. 구조 및 설계
  - 패키지 구조
  
  - DB 설계
  ![image](https://user-images.githubusercontent.com/77670592/191942619-bc8c5aac-a2b1-440e-bf79-1c895b7e5dc3.png)
  
  - FLOW CHART
  ![image](https://user-images.githubusercontent.com/77670592/191942754-9f8909a5-b44e-4704-9464-84d965567f76.png)

  
  
