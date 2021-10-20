# 1초마다 curl을 호출하는 명령어
```bash
i=1; while true; do sleep 1; echo $((i++)) `curl --silent 172.16.103.133 | grep title` ; done
```

# 정규식을 이용한 파일 탐색
`ls -lt | grep '^-.*\.log$'`

