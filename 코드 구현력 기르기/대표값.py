# 강의 풀이

n = int(input())
a = list(map(int,input().split()))
# 평균 round 함수는 소수 첫째 자리에서 반올림해준다.
# sum()은 리스트안의 모든 값을 더해준다.
ave = round(sum(a)/n)

# enumerate란 리스트의 인덱스와 그 값을 대응해서 넣어준다. 여기서는 idx에 인덱스 값이 x에 학생의 성적이 들어간다.
# Section0의 리스트와 내장함수 2 참고
min = float('inf')
min = 2147000000  # 정수형에서 가장 큰 값
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp<min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp==min:
        if x>score:
            score = x
            res = idx + 1
print(ave, res)
