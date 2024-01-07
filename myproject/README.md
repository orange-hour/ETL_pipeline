# Building a Website Log ETL Pipeline
---

**Project Duration:** 2022.12.01 ~ 12.20 <br>
**Participants**: @orange-hour, @ggydo59

### Project Overview

* Deployed a REST API on an AWS EC2 instance
* Built an ETL pipeline to apply encryption and compression algorithms to the API's logs and load it into an AWS S3 bucket

### Used Skills

- **Backend**
    
    ![DRF](https://img.shields.io/badge/django%20rest%20framework-092E20?style=for-the-badge&logo=django&logoColor=white) ![EC2](https://img.shields.io/badge/AWS%20ec2-FF9900?style=for-the-badge&logo=amazonec2&logoColor=white)
    
- **Data Storage**
    
    ![MySQL](https://img.shields.io/badge/mysql-4479A1?style=for-the-badge&logo=mysql&logoColor=white) ![AWSS3](https://img.shields.io/badge/aws%20s3-569A31?style=for-the-badge&logo=amazons3&logoColor=white)
    

**Reasons for choosing EC2**

* Can be used in conjunction with other AWS services such as Lambda and S3 for future project expansion and maintenance 
- Small instances are eligible for AWS's Free Tier, making it less costly
### Participants and Roles

| GitHub ID   | Roles                                                                                                                                                                                                 |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @orange-hour | - Encrypted and applied compression algorithms to log files<br>- Implemented log file uploads to AWS S3 |
| @ggydo59 | - Deployed the API on AWS EC2<br> - Built a bot for automating API requests and generating logs<br> - Scheduled log creation and applying compression algorithms on log files via Crontab  |

### Project implementation details

The following steps are scheduled on a designated time interval using Crontab: 
1. The bot sends multiple API requests to the deployed API server for generating logs
2. The log files are encrypted using two-way encryption
2. The encrypted log files are compressed using gzip
4. The log files are uploaded to AWS S3

![image](https://github.com/orange-hour/ETL_pipeline/assets/46596653/fffa3706-242c-4020-ba58-436a38a6eefb)

### Project limitations and possible improvements

**Limitations**

- Failure to compress strings in the data compression process other than applying the gzip algorithm
- Did not perform dynamic partitioning using the time scale of the data (e.g. daily, weekly)

**Possible Improvements**

- Implementing an additional string compression process
- Adding steps to further partition the data before uploading it to S3
