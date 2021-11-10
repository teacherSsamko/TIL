# Identity and Access Management

## Group

IAM user를 위한 Policy들의 집합.
AllUsers, Developers, Testers, Managers, SysAdmins

- SysAdmins: AMI, 인스턴스, 스냅샷, 볼륨, 보안 그룹 등을 생성하고 관리하기 위한 권한 필요. 모든 Amazon EC2 작업을 사용할 수 있는 권한을 부여하는 AmazonEC2FullAccess AWS 관리형 정책을 SysAdmins 사용자 그룹에 연결
- Developers: 인스턴스를 사용한 작업 권한만 필요. DescribeInstances, RunInstances, StopInstances, StartInstances, TerminateInstances를 호출할 수 있는 권한을 부여하는 정책을 생성하고 Developers 사용자 그룹에 연결
- Managers: 현재 제공되고 있는 Amazon EC2 리소스를 나열하는 것 외, 어떤 Amazon EC2 작업도 수행할 필요가 없음. 따라서 Amazon EC2 "Describe" API 작업만 호출할 수 있는 권한을 부여하는 정책을 생성하고 Managers 사용자 그룹에 연결

> Amazon EC2는 SSH 키, Windows 암호 및 보안 그룹을 사용하여 특정 Amazon EC2 인스턴스의 운영 체제에 액세스할 사용자를 제어. IAM 시스템에서는 특정 인스턴스의 운영 체제 액세스를 허용 또는 거부할 방법을 제공하지 않음.

## User

## Role

연동 사용자에게는 IAM 사용자처럼 AWS 계정에서 영구적인 ID가 부여되지 않음. 따라서, Group대신에 역할을 통해 권한을 부여할 수 있음.

### 연동 사용자

기존의 사용자가 조직에 연동된 경우.

## Policy

---

## Reference

[IAM에 대한 기업 사용 사례](https://docs.aws.amazon.com/ko_kr/IAM/latest/UserGuide/IAM_UseCases.html)  

[What is ABAC for AWS?](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html)

[AWS IAM: IAM Policy 알아보기 (이론편)](https://webcache.googleusercontent.com/search?q=cache:epQKk7onDpgJ:https://musma.github.io/2019/11/05/about-aws-iam-policy.html+&cd=2&hl=ko&ct=clnk&gl=kr)  
