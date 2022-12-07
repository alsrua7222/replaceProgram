from File import *
replaceDictionary = getReplaceDict("치환.txt")
content = """안녕하세요. 삽질전문가입니다. 오늘도 사과를 먹습니다.
그래서 소개할 코너는 삼성과 애플 노트북의 전력대비 가성비가 어느 쪽이 좋은지 알아보도록 하겠습니다.
...
...
...
좋은 하루를 보내시길 바라겠습니다."""

content = setReplaceConvertToStr(replaceDictionary, content)
print(content)

""" content 결과
반갑습니다. 삽질전문가에요.. 당하루간도 사과를 먹습니다..
그러므로 안내할 코너는 삼성과 사과 노트북의 전력마련 가성비가 어느 쪽이 나쁘지않은지 검사해보도록 하려고요..
...
...
...
나쁘지않은 하루를 보내시길 바라겠습니다..
"""
