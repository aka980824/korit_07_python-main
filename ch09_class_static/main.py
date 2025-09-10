'''
1. 클래스 변수 vs instances 변수
    인스턴스 변수 : 인스터스 마다 서로 다른 값을 가지는 변수
    클래스 변수 : 모든 인스턴스가 동일한 값을 지니는 변수(자바에서는 정적변수)

    인스턴스 변수
        목적 - 인스턴스마다 서로 다른 값을 저장
        접근방식 - 인스턴스 접근(o)
                - 클래스 접근 (x)

    클래스 변수  :
        목적 - 인스턴스가 공유하는 값을 저장
        접근방식 - 인스턴스 접근 (o)
                - 클래스 접근 (o)
'''

# 클래스 변수 예시
# class Korean:
#     country = '한국'
#     # 인스턴스 변수의 경우는 생성자 내부에 있었습니다 (__init__ 내부)
#     # 클래스 변수는 이상처럼 클래스 내부에 선언 초기화합니다
#
#     def __init__(self, name, age, address):  # 생성자
#         self.name = name        # 인스턴스 변수
#         self.age = age
#         self.address = address
# # 객체 생성
# man1 = Korean('김일',21,'서울특별시 종로구')
# print(man1.name);
# print(man1.age);
# print(man1.address);
#
# print(man1.country)
# print(Korean.country)
'''
객체명.클래스변수 를 통하여 클래스 변수에 접근이 가능하지만, 클래스 내부의 코드를 들여다보기 까지는 country라는 변수가 인스턴스 변수인지 클래스 변수인지
알방법이 없다는 문제가 있음

이상의 이유로 클래스 변수를 확인하고자 할 때는 객체명.클래스변수명 보다는
클래스명.클래스변수명 을 통하여 참조하는것이 권장됨

2. 클래스 메서드 : 클래스 변수를 사용하는 메서드
'''
# class Korean2:
#     country = '대한민국'
#
#     # 클래스 메서드 정의 방법
#     @classmethod                # @calssmethod 데코레이터를 달면 클래스 메서드로 인지함
#     def trip(cls, travelling_site): # 그결과 첫 매개변수가 self가아닌 cls
#         if cls.country == travelling_site:
#             print('국내로 여행중입니다.')
#         else:
#             print('해외여행')
# # class method 호출
# Korean2.trip('대한민국')
# Korean2.trip('미국')
# man2 = Korean2()
# man2.trip('일본')
# 클래스 변수와 마찬가지로 객체명.클래스메서드명() 으로 호출이 가능하나, 마찬가지로 이게 인스턴스 메서드인지 확인이 불가능하기에
# 클래스명.클래스메서드명으로 하는것이 권장됨

'''
특징 : 
    1) 인스턴스 / 클래스로 호출 가능 -> 클래스호출을 권장
    2) 생성된 인스턴스가 없어도 호출 가능(클래스로 호출하면 됨)
    3) @classmethod 데코레이터(decorator)를 표시하고 작성
    4) 매개변수 cls 를 사용 -> self는 객체를 의미 / cls는 클래스 의미
    
3. 정적 메서드(static method)
    : 정적 메서드 또한 self를 사용하지 않음 -> 즉 인스턴스에 접근하여 사용하는것이 불가능함을 의미. self.속성명을 사용하여 인스턴스 변수의 값을
    참조하는데 정적 메서드는 아에 첫번째 메개변수가 고정이 아닙니다. -> 클래스 메서드와의 공통점 #1
    
    인스턴스를 생성하지 않아도 사용 가능 - 클래스 메서드 공통점 #2
    
    특징 : 
        1) 인스턴스 / 클래스 호출 가능 -> 클래스 메서드와의 공통점
        2) 생성된 인스턴스가 없어도 호출 가능 -> 클래스 메서드와의 공통점
        
        3) @staticmethod 데코레이터를 표기하고 작성 -> 클래스 메서드와의 차이점 #1
        4) 반드시 작성해야할 매개변수(self / cls)가 없음 -> 클래스 메서드와의 차이점 #2

이상을 토대로 정적 메서드는 cls/self 둘다 사용하지 않기에, 인스턴스/ 클래스 변수를 모드 사용하지 않는 메서드를 정의하는 경우에 적합합니다.
정적메서드, 자체는 클래스에 소속도이어 있으나 인스턴스에는 영향을 주지도 받지도 않습니다.

즉 java에서의 정적 메서드 - 파이썬의 클래스 메서드 + 정적 메서드
'''
# class Korean3:
#     country = '한국'
#
#     @staticmethod
#     def slogan():
#         print('Imagine Your Korea! ⭐')
#     @staticmethod
#     def slogan2(str_example):
#         print('Imagine Your Korea!'+str_example)
# Korean3.slogan()
# Korean3.slogan2(' 존나 덥네')
'''
기본 예제

가방을 만들 때마다 현재 만들어진 가방이 몇개인지 계산하는 bag 클래스 
'''
# 클래스 정의
# class Bag:
#     # 클래스 변수 선언 및 초기화
#     count = 0
#
#     def __init__(self): #생성자 호출 및 인스턴스 변수를 정의할 용도. 그럼 생성자도 인스턴스 변수라고 할수 있음(self)
#         Bag.count += 1 #생성자가 호출할때마다 (객체 생성마다) 클래스 변수인 count가 1씩 증가함 cls.count가아닌 클래스명.count가 주목점
#         print('가방 객체가 생성 되었습니다.')
#
#     # class method, 저으이
#     @classmethod
#     def sell(cls):
#         print('가방이 판매됨')
#         cls.count -= 1
#         # 얘는 클래스 메서드가 클래스 변수에 접근한 것이기에 Bag.count가 아닌 cls.count로 작성
#
#     @classmethod
#     def remain_bag(cls):
#         return cls.count
#
# print(f'현재 가방 재고 : {Bag.count}')
# print(f'현재 가방 재고 : {Bag.remain_bag()}')
#
# # 객체 생성
# bag1 = Bag()
# print(f'현재 가방 재고 : {bag1.remain_bag()}')
# bag2 = Bag()
# bag3 = Bag()
# print(f'현재 가방 재고 : {bag2.remain_bag()}')
# bag1.sell()
# print(f'현재 가방 재고 : {bag1.remain_bag()}')

'''
지시사항
1. 다음과 같은 방법으로 man/woman 인스턴스 생성
man = Person('김일')
woman = Person('김이')

2. man/woman 인스턴스가 생성되면 다음과 같은 메세지를 출력하도록 작성
김일이(가) 태어났습니다.
김이이(가) 태어났습니다.

3. 다음 코드를 통해서 전체 인구수를 조회할 수 있도록 작성하시오.
print(f'전체 인구수 : {Person.get_population()}')

4. 다음과 같은 명령어로 man 인스턴스를 삭제
del man

5. man 인스턴스가 삭제되면 다음과 같은 메세지를 출력하도록 소멸자 정의
RIP 김일
'''
# class Person:
#
#     population = 0
#
#     def __init__(self, name):
#         self.name = name
#         Person.population += 1
#         print(f'{self.name}이(가) 태어남.')
#
#     def __del__(self):
#         print(f'RIP {self.name}')
#         Person.population -= 1
#
#     @classmethod
#     def get_population(cls):
#         return cls.population
#
# man = Person('김일')
# woman = Person('김이')
# print(f'전체 인구수 : {Person.get_population()}\n')
#
# del man
# print(f'전체 인구수 : {Person.get_population()}')
# input("프로그램 종료 Enter 클릭")
'''
다음 지시사항을 읽고 가게의 매출을 구할 수 있는 shop클래스 작성하시오

지시사항
1. Shop 클래스는 다음과 같은 변수를 가지고 있음.
    total : 가게 전체 매출액
    menu_list : {메뉴명:가격}으로 이루어진 dictionary 구조의 list
    
    menu_list = [{'떡볶이':3000}, {'순대':4000}, {'튀김':500}, {'김밥':2000}]
2. 매출 발생시 다음과 같은 방식으로 판매량 작성
Shop.sales('떡볶이',1) # 떡볶이를(을) 1개 판매
Shop.sales('김밥',2) # 김밥를(을) 2개 판매
Shop.sales('튀김',5) # 튀김를(을) 5개 판매

3. 모든 매출을 작성한 뒤 다음과 같은 방식으로 전체 매출액을 확인합니다.
print(f'매출 : {Shop.get_total()}원)
'''

class Shop:
    total = 0
    menu_list = [{'떡볶이': 3000}, {'순대': 4000}, {'튀김': 500}, {'김밥': 2000}]

    def __init__(self, price):
        self.price = price
        Shop.total += price

    @classmethod
    def sales(cls, item, count):
        found = False
        for menu in cls.menu_list:
            if item in menu:
                price = menu[item]
                cls.total += price * count
                print(f"{item}를(을) {count}개 판매했습니다.")
                found = True
                break
        if not found:
            print(f"메뉴 '{item}'는(은) 존재하지 않습니다.")

    @classmethod
    def get_total(cls):
        return cls.total

    @classmethod
    def get_menu_list(cls):
        return cls.menu_list

Shop.sales('떡볶이',1)
Shop.sales('김밥',2)
Shop.sales('튀김',5)
print(f'매출 : {Shop.get_total()}원')
