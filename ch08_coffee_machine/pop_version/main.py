MENU = {
    '에스프레소' : {
        '재료': {
            '물': 50,
            '커피': 18,
        },
        '가격' :1.5,

    },
    '라떼' : {
        '재료': {
            '물': 200,
            '우유': 150,
            '커피': 24,
        },
        '가격' : 2.5,
    },
    '카푸치노' : {
        '재료': {
            '물': 250,
            '우유': 100,
            '커피': 24,
        },
        '가격' : 3.0,
    },
}

# 실행 예

# 카푸치노 에는 우유가 100ml 들어갑니다.
# 라고 콘술에 출력할 수 있도록 카푸치노의 우유량을 추출하는 코드를 작성하시오.
# milk_amount = MENU['카푸치노']['재료']['우유']
# print(f"카푸치노 에는 우유가 {milk_amount}ml 들어갑니다.")
print(f"카푸치노 에는 우유가 {MENU['카푸치노']['재료']['우유']}ml 들어갑니다.")
# 에스프레소의 가격을 추출하시오.
# espresso_price = MENU['에스프레소']['가격']
# print(f"에스프레소의 가격은 {espresso_price}입니다.")
print(f"에스프레소의 가격은 {MENU['에스프레소']['가격']}입니다.")
# 라떼의 재료를 재료 이름만 출력하시오.
# latte_ingredients = MENU['라떼']['재료'].keys()
# print("라떼의 재료:", ', '.join(latte_ingredients))
print("라떼의 재료:", ', '.join(MENU['라떼']['재료'].keys()))

'''
에스프레소 / 라떼/ 카푸치노를 50잔씩 만든다고 가정했을 때, 필요한
커피/ 우유/ 물의 양은 얼마인가?
'''

# 총 재료량 저장할 딕셔너리
total_ingredients = {
    '물': 0,
    '우유': 0,
    '커피': 0
}
# 각 음료마다 50잔씩 만들기
for drink in MENU:
    ingredients = MENU[drink]['재료']
    for item in ingredients:
        total_ingredients[item] += ingredients[item] * 50

# 결과 출력
print("50잔씩 만들 경우 필요한 총 재료량:")
print(f"물: {total_ingredients['물']}ml")
print(f"우유: {total_ingredients['우유']}ml")
print(f"커피: {total_ingredients['커피']}g")

'''
이상의 학습 과정에서 중요한점은 dictionary - json - 기타  collections들이 합쳐진 데이터에서
데이터 추출하는 방법과 관련

일반적으로 list는 index를 이용하기에 반복문을 사용하고 치우면 그만이지만, dictionary는 반복문을 돌리면 key가
나오며, 그 키를 이용해야만 value가 출력

그리고 그 value를 이용하여 연산을 하거나 로직을 작성해야 합니다.

근데 value가 또 dictionary거나 list, 객체거나 하는 경우에는 복잡해짐
이를 연습하기 위한 수업이었고,
coffe_machine을 작성하면서는 중첩 dicitonary를 이용 예정

'''