# Linux Commands

## sed

파일을 인자로 받아 명령어를 통해 작업 후 결과를 확인하는 방식. vi와 비슷하지만, 원본을 손상하지 않음.
streamlined editor.

- pattern space
- hold space

`sed 's/{textToFind}/{textToReplace}' filename`
텍스트를 찾아서 변환하여 저장함
`-i[suffix]`
edit files in place (makes backup if extension supplied).

## find

### wc - word count

`$ find . -name"*.c" -exec wc -l {} \;`
확장자가 c 인 파일의 라인 수 출력
`$ find . -regex ".*\.\(sh\)";`
정규표현식 이용해 파일 찾기

## mkdir

### -p

존재하지 않는 중간 디렉토리까지 자동 생성

## cp

### -i

복사대상파일이 이미 그 위치에 존재한다면 덮어쓸 것인가를 사용자에게 확인

## modprobe

LKM(적재 가능 커널 모듈)을 리눅스 커널에 추가하거나 제거하는데 사용한다.

## curl

- `-s`, `--silent` 진행 내역이나 메세지 등을 출력하지 않음.
- `-o`, `--output` 결과를 따로 저장하거나 `/dev/null`로 보내서 출력하지 않을 수 있음.
- `-I` header만 보여주는 옵션.

## ulimit

여러 가지 limit을 설정할 수 있는 커맨드

- `ulimit -n {number of files}`
  한번에 처리 가능한 파일의 수를 조절하는 명령어  
   일시적인 조정. hard limit보다 클 수 없다.

- `/etc/security/limits.conf`에서 수정해야 영구적인 반영이 됨.

## stdout, stderr handling

- `command > file` or `command 1> file`
  - 1 for stdout
- `command 2> file`
  - 2 for stderr
- `command 2> error.txt 1> output.txt`
- `command 2> /dev/null`
- `command > file 2>&1`
  - the order of redirection is important. `command 2>&1 > file` doesn't work. because 'stderr'is redirected to 'stdout' before the 'stdout' is redirected to 'file'.

## check running shell

`echo $0`
