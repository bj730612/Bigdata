sentence = input("문자를 입력하세요 :")

result = sentence[0]
count = 0

for char in sentence:
    if char == result[-1]:
        count += 1
    else:
        result += str(count) + char
        count = 1
result += str(count)

print(result)
