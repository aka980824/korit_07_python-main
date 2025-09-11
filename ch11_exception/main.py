'''
1. 예외 처리의 필요성
    1) 예외(Exception) : 개발자가 직접 처리 가능한 문제
    2) 오류(error) : 개발자가 처리 불가능

    3) 예외처리의 목적
        어떤 문제가 발생시, 그 문제를 해결해주는 것이 아니라 발생된 문제로 인해 프로그램이 비정상적으로 종료되는것을 방지 및
        사용자에게 발생한 문제에 대해 정보를 전달하기 위함

2) 예외 처리
    1) 고전적 예외 처리
'''
# a = int(input('나누는 수를 입력하세요 >>> '))
# b= int(input('나누어지는 수를 입력하세요 >>> '))
#
# if a==0:
#     print('0으로 나누기는 불가능함')
# else:
#     result = b/a
''' 
20250910 coffemachine에서 사용됨
if drink == None:
    이라는 방식을 사용

어떤 값이든 0으로 나눌 수 없기에 if a == 0 을 통해 0으로 나누는것을 예외처리로 방지
    1) 어떤 문제가 발생할지 예상을 할 수 있어야 미리 대비 가능
    2) 어떤 문제가 발생시 예상할 수 있더라도 대비할수 없는 경우가 있음

3. 예외처리의 종류를 작성 출력결과

순번 / 예외클래스명 / 의미
1 / BaseException / 최상위 예외 클래스
2 / Exception / 대부분 예외 클래스의 슈퍼 클래스
3 / ArithmeticError / 산술 연산에 문제 발생
4 / AttributeError / 잘못된 속성을 참조시
5 / EOFError / 파일에서 더 이상 읽어 들일 데이터가 없을시
6 / ModuleNotFoundError /  import 할 모듈이 없을시
7 / FileNotFoundError / 존재하지 않는 파일
8 / IndexError / 잘못된 인덱스를 사용시
9 / Name / Error 잘못된 이름(변수) 사용시
10 / SyntaxError / 문법 오류
11 / TypeError / 계산하려는 데이터의 유형이 잘못됨
12 / ValueError / 계산하려는 데이터의 값이 잘못됨
# from prettytable import PrettyTable
# 
# table = PrettyTable()
# table.field_names = ['순번', '예외 클래스', '의미']
# 
# table.add_row([1, 'BaseException', '최상위 예외 클래스'])
# table.add_row([2, 'Exception', '대부분 예외 클래스의 슈퍼 클래스'])
# table.add_row([3, 'ArithmeticError', '산술 연산에 문제 발생'])
# table.add_row([4, 'AttributeError', '잘못된 속성을 참조시'])
# table.add_row([5, 'EOFError', '파일에서 더 이상 읽어 들일 데이터가 없을시'])
# table.add_row([6, 'ModuleNotFoundError', 'import 할 모듈이 없을시'])
# table.add_row([7, 'FileNotFoundError', '존재하지 않는 파일'])
# table.add_row([8, 'IndexError', '잘못된 인덱스를 사용시'])
# table.add_row([9, 'NameError', '잘못된 이름(변수) 사용시'])
# table.add_row([10, 'SyntaxError', '문법 오류'])
# table.add_row([11, 'TypeError', '계산하려는 데이터의 유형이 잘못됨'])
# table.add_row([12, 'ValueError', '계산하려는 데이터의 값이 잘못됨'])
# 
# print(table)

4, 예외 처리 방식
    1) 모든 예외를 처리하는 방식 try / except / finally
    형식:
try :
    코드작성
except : 
    예외처리시
finally:
    언제나 실행됨
'''
# try:
#     a = int(input('나누는 수를 입력하세요 >>> '))
#     b= int(input('나누어지는 수를 입력하세요 >>> '))
#     print(f'b / a = {b/a}')
# except:
#     print('예외 발생')
'''
기본 예제

다음은 사용자가 입력한 키를 저수로 반올림하여, 다시 저장하는 프로그램입니다.
try / except를 이용하여 '예외가 발생되었습니다'를 출력하도록 작성
'''
# try:
#     height = input('키(cm)를 입력하세요 >>> ')
#     height = round(height)
#     print(f'입력하신 키는 {height}cm로 처리됩니다.')
# except:
#     print('예외처리 발생')
'''
    1) 특정 예외만 처리하는 방식
        try / except 문을 사용하면 기본적으로 예외의 종류에 상관없이 모든 예외가 처리됨.
        하지만 이상에서본것처럼 0으로 나눈경우와 str자료형을 실수로 바꾸고자하는 경우에 서로 다른 메세지를 출력해줄수 있다면
        개발자에게 예외츨 처리할 수 있을만한 추가적인 정보를 제공 가능
        
        1)-1. 0으로 나누려고하는 경우 -> 0으로 나눌 수 없습니다
        2)-2. 정수가 아닌 값을 입력하는 경우 -> 정수만 입력할 수 있습니다
        등으로 특정 예외에 따른 서로 다른 안내문을 제시한다면 
        except문 뒤에 처리하고자 하는 예외를 모두 명시하면됨
'''
# try:
#     a = int(input('나누는 수를 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 입력하세요 >>> '))
#     print(f'b / a = {b / a}')
# except ZeroDivisionError:
#     print('0으로 나눌 수 없습니다.')
# except TypeError:
#     print('나눌 때 자료형이 일치하지 않습니다.')
# except ValueError:
#     print('정수만 입력이 가능합니다. ')
'''
    거의 모든 예외는 Exception 클래스의 서브 클래스에 해당됨. 따라서 모든 예외 처리는 
    Exception의 인스턴스가 됩니다. 다음과 같이 except의 마지막에 Exception을 명시하면
    예상치못한 예외들도 왠만하면 처리가 됨
    
형식 : 
try : 
    코드 작성 영역
except 예외클래스1 :
    예외메세지1
except 예외클래스2 :
    예외메세지2
...
except Exception
    예외메시지n
finally : 
    항시 실행되는 코드 영역

Java에서와 동일하게 Exception이 가장 상위에 있게 되면 모든 예외가 전부 Exception 으로 잡히기에 순서역시 중요

3. 예외 메시지 처리하기
    이상까지의 특정 예외가 발생시 메시지를 커스텀하여 사용하였으나. 기본적으로 이미 예외 메세지를 가지고 있는 경우가 존재
    default exception message를 출력하는 방식을 수업 예정
    
형식 :
try : 
    코드작성 영역
except 예외클래스 as 예외메세지
    예외 발생시 처리영역
'''
# z = [10,20,30,40,50]
#
# try:
#     print(z[10])
# except IndexError as e:
#     print(e)
'''
4. else / finally
    try / except 문에 else / finally를 달 수 있는데,
    else : 예외가 발생하지 않으면 처리되는 구문
    finally : 예외 발생 여부와 관계 없이 맨 마지막에 항상 처리되는 구문
'''
# try:
#     a = int(input('나누는 수를 입력하세요 >>> '))
#     b = int(input('나누어지는 수를 입력하세요 >>> '))
#     result = b/a
# except ZeroDivisionError as e:
#     print(e)
# except TypeError as e:
#     print(e)
# except ValueError as e:
#     print(e)
# else :
#     print(f'a = {a}')
#     print(f'b = {b}')
#     print(f'b / a = {result}')
# finally:
#     print('종료')

'''
5. 강제 예외 발생
    어떤 사람이 나이를 정수로 입력받는 프로그램을 이용한다고 가정시, 
    커퓸터 상으로는 -1000이 정수이기에(파이썬) 예외가 잡히지 않습니다.
    (그래서 0미만 200초과를 조건문으로 이용)
    허나, -1000살이 되는 것은 불가능하기에 조건문이 아닌 직접 예외를 발생시켜 처리하였음 -> rasie

형식:
raise 예외클래스()

혹은
raise 예외클래스(예외메시지)
'''
# age = int(input('나이 입력 >>> ')) -1000해도 오류 X
# print(f'당신의 나이는 {age} 살 입니다.)

# try:
#     age = int(input('나이 입력 >>> '))
#     raise Exception('강제 예외 발생')
# except Exception as e:
#     print('발생한 예외메시지 아래동일')
#     print(e)

'''
이상은 특정 예외가아니라 190으로 넝머가기만하면 예외 발생
즉 젇수값을 넣어도 예외발생이기데 단독처리 불가능
이렇부분에는 조건문을 이용하여 추가코드 작성이 필요

6. 사용자 정의 예외 클래스
    음수로 입력받을때 강제로 예외를 발생시키는 예외 클래스를 정의
'''
# class NegativeError(Exception):
#     """사용자 정의 예외 클래스 : 나이가 음수일 때 발생"""
#     pass
# # 예외 발생시키기만 하면되기에 굳이 코드 작성 X
# # Exception 클래스를 상속받았으면 슈퍼클래스의 속성/메서드를 사용가능
# class TooManyAgeError(Exception):
#     pass
#
# try:
#     age=int(input('나이 입력 : '))
#     if age < 0:
#         raise NegativeError('나이는 음수일 수 없음')
#     if age > 200:
#         raise TooManyAgeError('나이는 200초과가 불가능')
# except NegativeError as e:
#     print('발생한 예외 메세지는 아래와 같음')
#     print(e)
# except TooManyAgeError as e:
#     print('발생한 예외 메세지는 아래와 같음')
#     print(e)
# else:
#     print(f'당신의 나이는 {age} 입니다.')
'''
과제:    
    나이가 200살 초과일 때 TooManyAgeError 예외를 발생시켜 , '200살 초과 나이는 입력이 불가능합니다'라는 메세지를 출력하도록 코드 수정
    
    사용자의 점수를 0이상 100이하의 숫자로 입력받아 80이상시, 합격아니면 불합격을 출력하는프로그램을 작성하되
    0이상 100이하의 정수값이 아니라면 예외를 발생하며, '점수는 0이상100이하입니다' 라는 예외를 처리하도록 출력하시오.
    ScoreOut0fRangeError 클래스를 정의하여 사용
    
    입력받는데 백점< 으로 입력시 '점수는 숫자로만 입력해야ㅕ합니다'라는 메세지 출력
    실수로 입력시 '정수로 입력해야합니다 출력'
    
    예상할수 없는 예외발생시 Excpetion을 이용하여 디폴트 메세지 출력
    
    프로그램 종료메세지 마지막에 출력
'''
# class ScoreOutOfRangeError(Exception):
#     pass
#
# try:
#     score_input = input('점수 입력 : ')
#     score = int(score_input)  # 실수 또는 문자열 입력 시 ValueError 발생
#
#     if score < 0 or score > 100:
#         raise ScoreOutOfRangeError
#
#     if score >= 80:
#         print(f'점수가 {score}점 이므로 합격입니다.')
#     else:
#         print(f'점수가 {score}점 이므로 불합격입니다.')
#
# except ScoreOutOfRangeError:
#     print('점수는 0 이상 100점이어야 합니다')
# except ValueError:
#     print('정수로 입력하세요')
# except TypeError:
#     print('점수는 숫자를 입력해야 합니다.')
# except Exception as e:
#     print('예외 발생')
# finally:
#     print("종료")

'''
사용자로부터 숫자를 입력받아 해당 숫자를 100으로 나누는 값을 출력하는 프로그램을 ㅈ가성
사용자가 0이나 숫자가 아닌값을 입력하면 예외처리

지시사항 
1, 사용자로부터 숫자입력받음
2. 입력받은 숫자로 100을 나누어 결과 출력
3. 입력값이 0일경우 적절한 예외처리 및 '0으로 나눌수 없습니다' 출력
4. 입력값이 숫자가 아닌 경우 적절한 예외처리 및 ' 숫자만 입력할 수 있습니다 ' 메세지출력
5. 예외가 발생하지 않는경우, '정상적으로 처리되었습니다' 및 결과값 출력
6. 종료메세지
'''
# class ScopeError(Exception):
#     pass
#
# try:
#     num = int(input("숫자 입력(1~100) >>> "))
#     if num == 0:
#         print('0을 입력할 수 없습니다.')
#         raise ZeroDivisionError
#     elif num >100 :
#         print('100을 초과할 수 없습니다.')
#         raise ScopeError
#     result = 100/num
# except ZeroDivisionError as e:
#     print(e)
#     print("0으로 나눌 수 없습니다")
# except ValueError as e:
#     print(e)
#     print("숫자만 입력할 수 있습니다")
# except ScopeError as e:
#     print(e)
#     print(f"{num}은 100을 초과하여 실행이 종료됩니다.")
# except Exception as e:
#     print(e)
# else:
#     print("정상적으로 처리되었습니다")
#     print(f"100 / {num} = {result}")
# finally:
#     print("프로그램 종료")

'''
1. 미리 정의한 리스트 존재함
2. 사용자로부터 리스트의 인덱스를 입력받음
3. 입력받은 인덱스를 사용하여 리스트의 값을 출력
4. 인덱스가 리스트의 범위를 벗어나면 적절한 메세지 출력
5. 사람을 의심하고 예상되는 예외 적용
6. 예외가 발생하지 않는경우, '정상적으로 처리됨'을 출력 및 해당 인덱스의 값을 출력
7. 프로그램의 종료 메세지 출력
8. 마이너스인덱스는 적용하지 않는다 -> 사용자 정의
    -> NegativeNumIndexError라고 지정 및 처리
'''
# class NegativeNumIndexError(ValueError):
#     pass
#
# my_list = [10,20,30,40,50]
#
# try:
#     num=int(input("숫자입력 >>> "))
#     if num < 0 :
#         raise NegativeNumIndexError
#     value = my_list[num]
# except NegativeNumIndexError as e:
#     print('음수(-)는 입력이 불가능합니다.')
# except ValueError as e:
#     print("숫자만 입력할 수 있습니다.")
# except IndexError as e:
#     print("리스트 범위를 벗어 났습니다.")
# except Exception as e:
#     print(e)
# else:
#     print(f"my_list[{num}]의 값은 {value}입니다.")
#     print('정상적으로 종료됨')
# finally:
#     print('종료')
'''
1. 클래스/ 객체가 있음
2. 사용자로부터 속성명을 입력받음
3. 입력받은 속성명을 사용하여 객체의 속성값을 출력
4. 잘못된 속성명을 입력시, 존재하지않는 속성입니다 라는 메세지
5. 예외가 발생하지 않는경우 정상적으로 처리되었습니다 < 메세지
6. 종료 메세지
'''
class Person:
    # 클래스 변수 선언
    school = '코리아IT아카데미'

    def __init__(self, name, age):
        self.name = name
        self.age = age

# 객체 생성
person1 = Person(name='김일',age=21)
print(getattr(person1, 'age'))  # 21
# getattr() 두번째 argument는 인스턴스 변수명을 받습니다. -> 그 데이터를 str으로 받습니다.
print(getattr(person1, 'name')) # 김일
# getattr(person1,'job') -> 오류테스트
# getattr(person1,school) -> 클래스 변수인 school이 전역이 아니므로 main단계에서 선언되지않은것으로 간주함 -> 즉 NameError가 발생했지 속성명과는
# 관계가 없습니다
# print(person1,'school')

# try:
#     attr = input("출력할 속성명 입력 (예: name, age) >>> ")
#     value = getattr(person1, attr)
# except AttributeError as e:
#     print(e)
#     print('존재하지 않는 속성입니다.')
# except Exception as e:
#     print(e)
#     print("확인안되는 예외처리 발생")
# else:
#     print('정상적으로 종료됨')
#     print(f"{attr}의 값은: {value}")
# finally:
#     print('프로그램 종료')

'''
getattr(객체명, 속성명_str) - 특정 개체의 두번째 argument와 일치하는 속성값을 return
vars(객체명) - 특정 객체의 속성명-속성값 쌍을 dictionaty 형태의 key-value 쌍으로 변환

'''
person1_dict = vars(person1)
attr_key= input('출력할 속성명을 입력하세요 >>> ')
print(person1_dict[attr_key])