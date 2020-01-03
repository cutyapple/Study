import re

# text = "에러 1234 : 아무튼 에러    에러 13333: 어잿든 에러"
# regex = re.compile("에러\s\d+")
# mc = regex.findall(text)
# print(mc)

# text = "전화줘... 010-1234-1234 아니면 010-123-1234"
# regex = re.compile(r'(\d+)[-](\d+[-]\d+)')
# match = regex.finditer(text)
# # print(f'{match.group(1)}-{match.group(2)}')
# for i in match:
#     print(i.group(2))

ace = re.match(r'(?P<first>a)(?P<second>b)\1\1', 'abaa')
print(ace.group('first'))
print(ace.group('second'))
print(ace.group('\1'))