count = int(input("몇 개의 숫자를 입력하시겠습니까? >>> "))
numbers = []

pos = 0
neg = 0
zero = 0

for i in range(1, count + 1):
    num = int(input(f"{i}번째 숫자를 입력하시오 >>> "))
    numbers.append(num)

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        zero += 1

print(f"\n양수: {pos}개")
print(f"음수: {neg}개")
print(f"0: {zero}개")
