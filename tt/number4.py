num_candidates = int(input("후보자 수를 입력하시오 >>> "))

candidates = []
for i in range(num_candidates):
    name = input(f"{i+1}번째 후보자의 이름을 입력하시오 >>> ")
    candidates.append(name)

votes = {name: 0 for name in candidates}

print("\n주의사항) 투표는 숫자를 입력해야 합니다.")
num_votes = int(input("전체 투표 횟수를 입력하시오 >>> "))

for i in range(num_votes):

    options = ', '.join([f"{index + 1}: {name}" for index, name in enumerate(candidates)])
    vote_input = int(input(f"{i+1}번째 투표 ({options}) >>> "))

    if 1 <= vote_input <= num_candidates:
        selected_name = candidates[vote_input - 1]
        votes[selected_name] += 1
    else:
        print("잘못된 번호입니다. 이 투표는 무효 처리됩니다.")

print("\n---- 투표 결과 ----\n")
for name in candidates:
    print(f"{name}: {votes[name]}표")
