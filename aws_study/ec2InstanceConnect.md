# EC2 Instance Connect

[EC2 Instance Connect를 사용하여 Linux 인스턴스에 연결](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)

## Concept

- SSH key대신에 IAM으로 instance에 접속
- key pair에 대한 관리가 필요없어짐
- CloudTrail로 Instance 접근 Log를 추적가능

## instance에 접속하는 방법

- Amazon EC2 콘솔(브라우저 기반 클라이언트)
- Amazon EC2 Instance Connect CLI
- SSH 클라이언트

## 작동 원리

- Instance Connect API는 일회용 SSH 퍼블릭 키를 [인스턴스 메타데이터](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)에 푸시하여 60초 동안 유지
  - IAM 사용자는 SendSSHPublicKey 권한이 필요
- IAM 사용자에게 연결된 IAM 정책은 퍼블릭 키를 인스턴스 메타데이터로 푸시하도록 IAM 사용자에게 권한을 부여
- SSH 데몬은 Instance Connect가 설치될 때 구성된 `AuthorizedKeysCommand` 및 `AuthorizedKeysCommandUser`를 사용하여 인증을 위해 인스턴스 메타데이터에서 퍼블릭 키를 찾고 사용자를 인스턴스에 연결

---

## Reference

[메스프레소 기술블로그: AWS EC2 Instance Connect 도입기 (Goodbye Key Pair!)](https://blog.mathpresso.com/aws-ec2-instance-connect-%EB%8F%84%EC%9E%85%EA%B8%B0-goodbye-key-pair-646380952f0e)
