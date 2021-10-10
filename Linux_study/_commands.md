# sed
파일을 인자로 받아 명령어를 통해 작업 후 결과를 확인하는 방식. vi와 비슷하지만, 원본을 손상하지 않음.
streamlined editor.

- pattern space
- hold space

`sed 's/{textToFind}/{textToReplace}' filename`
텍스트를 찾아서 변환하여 저장함
`-i[suffix]`
edit files in place (makes backup if extension supplied).

# find

## wc - word count
`$ find . -name"*.c" -exec wc -l {} \;`
확장자가 c 인 파일의 라인 수 출력
`$ find . -regex ".*\.\(sh\)";`
정규표현식 이용해 파일 찾기

# mkdir

## -p
존재하지 않는 중간 디렉토리까지 자동 생성

# cp

## -i
복사대상파일이 이미 그 위치에 존재한다면 덮어쓸 것인가를 사용자에게 확인 