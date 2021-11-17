# EC2 Instance Connect

[EC2 Instance Connect를 사용하여 Linux 인스턴스에 연결](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/Connect-using-EC2-Instance-Connect.html)

## Concept

- SSH key대신에 IAM으로 instance에 접속
- key pair에 대한 관리가 필요없어짐
- CloudTrail로 Instance 접근 Log를 추적가능

## Requirements

- AWS IAM User
  - request to AWSadmin
- AWS CLI

    [AWS CLI 버전 2 설치, 업데이트 및 제거](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/install-cliv2.html)

- python3.x

    [Download Python](https://www.python.org/downloads/)

- AWS ec2 instance connect CLI

    `pip3 install ec2instanceconnectcli`

- **Instance_id** that you want to connect to

    Check AWS web console or Ask to peer

## The way to connect to instance

- Amazon EC2 콘솔(브라우저 기반 클라이언트)
- Amazon EC2 Instance Connect CLI
- SSH 클라이언트

### Amazon EC2 Instance Connect CLI

- Set Up
  - AWS Configure
    - option 1) Configure using AWS CLI

      [구성 기본 사항](https://docs.aws.amazon.com/ko_kr/cli/latest/userguide/cli-configure-quickstart.html#cli-configure-quickstart-config)

    - option 2) Write configure files

      ```bash
      # ~/.aws/credentials
      [default]
      aws_access_key_id=AKIAIOSFODNN7EXAMPLE
      aws_secret_access_key=wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
      ```

      ```bash
      # ~/.aws/config
      [default]
      region=us-west-2
      output=json
      ```

- Connect
  - `mssh {AWS IAM name}@{instance_id}`
  - ex) `mssh ssamko@i-0dc37336dbexample`

## How to transfer files

- `rsync -a -e mssh {source file} {AWS IAM name}@{instance_id}:{target path}`
- ex) `rsync -a -e mssh ./sample.txt ssamko@i-0dc37336dbexample:/home/ssamko/`

## How to set in ssh config

### pre-requirement

- self generated ssh key

```bash
# ~/.ssh/config
Host {Name what you want}
  ProxyCommand sh -c "aws ec2-instance-connect send-ssh-public-key --region us-west-2 --availability-zone {us-west-2c}  --instance-id {instance id} --instance-os-user {AWS IAM user} --ssh-public-key file://{public key path}; /usr/bin/nc %h %p"
  HostName {instance's ip or DNS}
  User {AWS IAM user}
  IdentityFile {private key path}
```

```bash
# example
# ~/.ssh/config
Host ec2connect
  ProxyCommand sh -c "aws ec2-instance-connect send-ssh-public-key --region us-west-2 --availability-zone us-west-2c  --instance-id i-0dc37336dbexample --instance-os-user eunsub --ssh-public-key file://~/.ssh/id_rsa.pub; /usr/bin/nc %h %p"
  HostName 34.123.211.123
  User ssamko
  IdentityFile ~/.ssh/id_rsa
```

## 작동 원리

- Instance Connect API는 일회용 SSH 퍼블릭 키를 [인스턴스 메타데이터](https://docs.aws.amazon.com/ko_kr/AWSEC2/latest/UserGuide/ec2-instance-metadata.html)에 푸시하여 60초 동안 유지
  - IAM 사용자는 SendSSHPublicKey 권한이 필요
- IAM 사용자에게 연결된 IAM 정책은 퍼블릭 키를 인스턴스 메타데이터로 푸시하도록 IAM 사용자에게 권한을 부여
- SSH 데몬은 Instance Connect가 설치될 때 구성된 `AuthorizedKeysCommand` 및 `AuthorizedKeysCommandUser`를 사용하여 인증을 위해 인스턴스 메타데이터에서 퍼블릭 키를 찾고 사용자를 인스턴스에 연결

---

## Reference

[메스프레소 기술블로그: AWS EC2 Instance Connect 도입기 (Goodbye Key Pair!)](https://blog.mathpresso.com/aws-ec2-instance-connect-%EB%8F%84%EC%9E%85%EA%B8%B0-goodbye-key-pair-646380952f0e)
