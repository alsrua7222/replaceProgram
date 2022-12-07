# replaceProgram
자동으로 치환해주는 프로그램

# 치환.txt
`그렇기때문에|그리하여,그리고,이리하여,그렇게하여`
| 세로 막대 기준으로 나눠서
`(바꿀 대상)|(바꾸고 싶은 단어),(바꾸고 싶은 단어),(바꾸고 싶은 단어)`
로 나뉘어진다.    
, 쉼표 기준은 랜덤으로 치환될 단어들이다.    
간단하다.   

# 사용 방법
1. 두 함수를 정의된 File.py를 임포트 시킨다.
```python
from File import *
```
2. getReplaceDict()를 활용해서 받은 객체인 사전을 미리 구축한다.    
```python
from File import *
replaceDictionary = getReplaceDict("치환.txt")
```
3. 미리 준비된 문자열을 준비한다.
```python
from File import *
replaceDictionary = getReplaceDict("치환.txt")
content = """안녕하세요. 삽질전문가입니다. 오늘도 사과를 먹습니다.
그래서 소개할 코너는 삼성과 애플 노트북의 전력대비 가성비가 어느 쪽이 좋은지 알아보도록 하겠습니다.
...
...
...
좋은 하루를 보내시길 바라겠습니다."""
```
4. setReplaceConvertToStr()를 활용해서 나온 객체를 저장한다.
```python
from File import *
replaceDictionary = getReplaceDict("치환.txt")
content = """안녕하세요. 삽질전문가입니다. 오늘도 사과를 먹습니다.
그래서 소개할 코너는 삼성과 애플 노트북의 전력대비 가성비가 어느 쪽이 좋은지 알아보도록 하겠습니다.
...
...
...
좋은 하루를 보내시길 바라겠습니다."""
content = setReplaceConvertToStr(replaceDictionary, content)
```

5. 알아서 써라.
```python
print(content)
```
```python
pytorch.gpt_32.layers() ...
```
