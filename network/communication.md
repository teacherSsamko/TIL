# Network communication

## ARP

- consist of Mac address, IP address of Sender & Receiver
- 2계층의 MAC주소와 3계층의 IP주소를 연계시켜주기 위한 protocol
- ARP 작업은 CPU에서 직접 수행하므로 짧은 시간에 많은 ARP요청이 오면 네트워크 장비의 부하가 커짐
  - 이를 방지하기 위해 네트워크 장비는 ARP 테이블 저장 기간을 일반 PC보다 길게 설정하고,
  - 많은 ARP 요청이 오면 필터링하거나, 천천히 처리하는 방식으로 부하 처리
