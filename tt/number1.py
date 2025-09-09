print("비밀번호 입력시 - 를 입력해야합니다. ")
phone = input("전화번호를 입력하시오(휴대폰번호) >>> ")

if len(phone) != 13 or phone[3] != '-' or phone[8] != '-':
    print("유효하지 않은 전화번호 형식입니다.")
else:
    middle = phone[4:8]
    print(f"전화번호의 중간 4자리는 {middle}입니다.")