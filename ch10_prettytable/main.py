'''
외부 패키지의 설치 # 1 : settings 를 통한 방법
좌측 상단 햄버거 -> file -> settings(alt+ctrl+s)
좌측 리스트 중 프로젝트 : 명으로되어있는 부분을 클릭
-> python interpretor
-> 좌상단 +버튼 눌러서 필요 패키지검색
외부 패키지의 설치 # 2 : 터미널을 이용하는 방법
alt + f12
pip install prettytable

'''
from prettytable import PrettyTable
from pokemon_data import pokemon_data

# PrettyTable 객체 생성
table = PrettyTable()
table.field_names = ['이름', '나이', '주소']
print(pokemon_data[3][2])
table.add_row((pokemon_data[0][0],pokemon_data[0][1],pokemon_data[0][2]))

print(table)
for number, name, p_type in pokemon_data:
    table.add_row([number, name, p_type])
print(table)


