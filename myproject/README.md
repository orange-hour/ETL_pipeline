# 로그 데이터 수집을 위한 ETL 파이프라인 구축

참여자 : 홍석원, 민경도

---

**프로젝트 기간:** 2022.12.01 ~ 20

**프로젝트 도구:** AWS S3, AWS EC2, Ubuntu Linux, DRF(Django Rest Framework), MySQL

**사용 언어:** Python, SQL

---

### 프로젝트 개요

- ETL 파이프라인 구축을 통해 API에서 수집한 로그 데이터에 암호화 및 압축 알고리즘을 적용하여 AWS S3에 적재
- Ubuntu Linux 기반의 AWS EC2 인스턴스를 이용하여 직접 구축한 웹 API를 배포

### 프로젝트 배경

- ETL 파이프라인 구축을 통해 직접 구축한 REST API에서 발생한 로그 수집 및 AWS S3에 압축된 형태의 데이터 적재
- 실제 API 기반 서비스에서 발생하는 로그 데이터 수집 및 적절한 형태로 클라우드 상에 적재하는 과정을 직접 진행


### 프로젝트 기술 스택

- **Backend**
    
    ![DRF](https://img.shields.io/badge/django%20rest%20framework-092E20?style=for-the-badge&logo=django&logoColor=white)
    ![EC2](https://img.shields.io/badge/AWS%20ec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
    
- **Database**
    
    ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
    ![AWSS3](https://img.shields.io/badge/aws%20s3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)
    
- **Tools**
    
    ![github](https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white) ![discord](https://img.shields.io/badge/discord-5865F2?style=for-the-badge&logo=discord&logoColor=white)
    

**EC2 선택 이유**

- 추후 프로젝트 확장 및 유지보수 시 Lambda, S3 등 다양한 AWS 서비스들과 연계하여 사용할 수 있음 
- AWS의 Free Tier 로도 Linux 기반 인스턴스를 구축할 수 있어 비용 부담이 덜함

### 개발 인원

| 이름   | 담당 업무                                                                                                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 홍석원 | - 로그 해싱 및 암호화, 로그 파일에 압축 알고리즘 적용<br>- AWS S3 버킷 생성 및 로그파일 업로드 기능 구현<br>- AWS EC2를 통한 API 배포 |
| 민경도 | - 계정 생성 및 활동 로그 생성을 위한 봇 구현<br> - AWS EC2를 이용한 웹서버 구축 및 API 배포<br> - Crontab을 통한 계정 생성 및 로그 생성 스케줄링  |

### 프로젝트 진행 과정

1. 로그 데이터 암호화 기능 구현, 압축 알고리즘 적용
2. API를 활용한 더미 데이터 생성을 위한 봇(bot) 구현
3. AWS S3 버킷 생성 및 로그 업로드 기능 구현
4. AWS EC2를 활용한 웹서버 구축 및 API 배포, 스케줄링 기능 구현

### 프로젝트 구현 내용

1. **로그 데이터 암호화 기능**
<img width="903" alt="image" src="https://user-images.githubusercontent.com/46596653/210942472-4f6b5606-27f2-42fe-b76b-d4aa87e132c9.png">
<img width="916" alt="image" src="https://user-images.githubusercontent.com/46596653/210942578-7ad953d0-0cad-490b-9549-9cf4aff57060.png">

2. **API를 활용한 더미 데이터 생성을 위한 봇(bot)**
<img width="907" alt="image" src="https://user-images.githubusercontent.com/46596653/210942704-173f089c-9a2f-44bf-8132-8c45610f18f7.png">

3. **AWS S3 버킷 생성 및 로그 업로드 기능**

<img width="937" alt="image" src="https://user-images.githubusercontent.com/46596653/210942829-85ba4526-9d96-41ac-80e2-71decb473b9c.png">


4. **AWS EC2를 활용한 웹서버 구축 및 API 배포, 스케줄링 기능**
<img width="1435" alt="image" src="https://user-images.githubusercontent.com/46596653/210943021-8a553f84-4655-4bcc-8b8a-9e8bb416f108.png">

5. **최종 구축 결과**
<img width="1457" alt="image" src="https://user-images.githubusercontent.com/46596653/210943109-03d11a61-a7af-488c-85f1-ba889710bace.png">


### 프로젝트 한계 및 개선 방안

**한계**

- 데이터 압축 과정에서 gzip 알고리즘 적용 이외 별도의 문자열 압축 과정을 진행하지 못함
- 데이터의 time scale(예: 일 단위, 주 단위) 에 따른 Dynamic Partitioning을 진행하지 못함


**개선 방안**

- 문자열 압축 과정 별도로 추가 구현
- Dynamic Partitioning을 진행한 데이터를 S3에 업로드하는 기능 추가
