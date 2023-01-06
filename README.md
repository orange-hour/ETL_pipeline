# Django Rest Framework 기반 REST API 구축

참여자 : 홍석원, 민경도

---

**프로젝트 기간:** 2022.11 ~ 2022.12 (2주)

**프로젝트 도구:** DRF(Django Rest Framework), MySQL, Postman, Github

**사용 언어:** Python, SQL

---

### ****프로젝트 개요****

- 회원가입 및 글쓰기, 글 수정, 삭제가 가능한 게시판 서비스를 구축
- 서비스 운영을 위한 데이터를 저장하고, 저장된 데이터를 열람하거나 수정할 수 있게끔 웹 브라우저로 접근할 수 있는 API를 구축

### 프로젝트 배경

- API 기반 서비스에서 발생하는 로그 데이터를 활용하기 위해서는 로깅(logging)을 진행할 수 있는 실제 서비스가 필요
- 추후 로그 데이터를 수집, 정제 적재하는 ETL 파이프라인 구축에 해당 서비스 활용


### 프로젝트 기술 스택

- **Backend**
    
    ![DRF](https://img.shields.io/badge/django%20rest%20framework-092E20?style=for-the-badge&logo=django&logoColor=white)
    
- **Database**
    
    ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
    
- **Tools**
    
    ![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![postman](https://img.shields.io/badge/postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white) ![discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
    

**DRF 선택 이유**

- RESTful한 아키텍처를 HTTP method와 함께 사용하여 웹, 앱에서 모두 활용 가능한 하나의 API를 구축할 수 있음
- Mozilla, Red Hat, Heroku 등 다수 기업에서 DRF을 활용해 웹사이트를 구축하고 있으며, 이에 따른 커뮤니티 리소스 및 레퍼런스가 풍부함

### 개발 인원

| 이름   | 담당 업무                                                                                                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 홍석원 | - DRF를 활용한 회원가입, 게시판 app에 활용하기 위한 model 구현<br>- 회원가입, 로그인 및 게시판 글쓰기 기능에 대한 테스트 코드 구현<br>- Django ORM을 활용한 유저 성별 및 생년월일에 대한 통계 페이지 구현 |
| 민경도 | - DRF Base model을 맞춤설정한 게시판 웹사이트 백엔드 구현<br>- 유저 인증 방식으로 JWT 적용 및 웹사이트 기능별 권한설정<br>- 로그 파일 생성을 위한 로거 및 포매터 구현                                     |

### 프로젝트 진행 과정

1. 회원가입, 로그인 및 글 작성, 수정, 삭제가 가능한 DRF 기반 API 구축
2. 각 페이지에 따른 권한설정 및 JWT(JSON Web Token)를 활용한 권한 부여
3. Django ORM을 통해 가입한 유저 및 게시글에 대한 통계 페이지 구현
4. API 로그 수집을 위한 logger 및 JSON 형식으로 출력하는 formatter 구현

### 프로젝트 구현 내용

1. **회원가입 및 로그인, 게시글 작성 기능**

![image](https://user-images.githubusercontent.com/46596653/210934328-9fd27024-f51f-4128-b8ba-606627a7d5eb.png)

![image](https://user-images.githubusercontent.com/46596653/210934458-45481926-1c05-4b91-ae9c-79117aa19f53.png)

![image](https://user-images.githubusercontent.com/46596653/210934544-27c7e710-ea73-41d4-b720-cc56073ec395.png)


2. **게시판 권한설정 기능**

![image](https://user-images.githubusercontent.com/46596653/210934621-3ad71ed6-2fc4-4092-80fa-b2792d90165f.png)

3. **통계 관련 기능**

<img width="1288" alt="image" src="https://user-images.githubusercontent.com/46596653/210934709-e462eede-163a-4d62-8734-0caa5f885e81.png">


4. **JSON 형식으로 로그를 출력하는 logger 및 formatter**

![image](https://user-images.githubusercontent.com/46596653/210934733-a7ef974a-29ee-48fa-979c-c78e837a6864.png)


### 프로젝트 한계 및 개선 방안

**한계**

- 테스트 코드 구현을 시도하였으나, 프로젝트 기간의 한계로 모든 기능에 대해 적합한 테스트 코드를 구현하지 못함
- 글 작성 및 수정 페이지는 API로만 구현되었고, 별도의 웹페이지 뷰는 구현되지 않아 API를 브라우저 이외의 다른 방식으로 접근해야 함 (ex. Postman 이용)

**개선 방안**

- 기능에 대한 최소한의 테스트 코드를 먼저 작성하고, 테스트에 통과할 때까지 기능을 구현하는 TDD 방식의 개발을 시도
- 필요 시 글 작성, 수정, 삭제에 대한 웹페이지 뷰 생성
