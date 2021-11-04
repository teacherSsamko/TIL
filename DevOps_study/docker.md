# Docker

k8s의 pod가 container로 이루어져있고, 이 container를 만들고 관리하는 것이 docker  
  
## Concepts

- Container
  - 하나의 운영 체제 안에서 커널을 공유하며 개별적인 실행 환경을 제공하는 격리된 공간
- 개별적 실행 환경
  - CPU, Network, Memory와 같은 시스템 자원을 독자적으로 사용하도록 할당된 환경

## Commands

`docker search nginx`  
nginx image 검색  

`docker pull nginx`  
nginx image 내려받기  

`docker images nginx`  
nginx 관련 이미지 확인  

`docker run`  
docker 컨테이너 생성  

### run options

- `-d`, `--detach`: background에서 컨테이너 구동
- `--restart always`: 해당 컨테이너가 항상 구동되도록
- `-p`, `--publish`: 외부에서 호스트로 보낸 요청을 컨테이너 내부로 전달하는 옵션.
  - `-p <요청 받을 호스트 포트>:<연결할 컨테이너 포트>`
- `--name`: container의 이름 설정

`docker ps`  
process status. 현재 구동중인 컨테이너 목록  

### ps options

- `-f {key}`: 검색결과 필터링
  - id, label, name
  - exited: 컨테이너가 종료됐을 때 반환하는 숫자 코드
  - status: 컨테이너의 작동 상태
  - ancestor: 컨테이너가 사용하는 이미지

`docker stop {container id}`  
해당 컨테이너 중지  
`docker rm {container id}`  
해당 컨테이너 삭제  

> container는 변경 불가능한 인프라(immutable infrastructure). 따라서, 실행 이후에는 directory 연결이나 port 노출같은 설정을 변경할 수 없음.  

