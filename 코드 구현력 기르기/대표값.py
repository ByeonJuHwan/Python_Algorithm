# 대표값

#N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고, N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.

#평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 높 은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.

#▣ 입력설명

#첫줄에 자연수 N(5<=N<=100)이 주어지고, 두 번째 줄에는 각 학생의 수학점수인 N개의 자연 수가 주어집니다. 

#학생의 번호는 앞에서부터 1로 시작해서 N까지이다.

#▣ 출력설명

#첫줄에 평균과 평균에 가장 가까운 학생의 번호를 출력한다.

#평균은 소수 첫째 자리에서 반올림합니다.

#▣ 입력예제 1

#10

#45 73 66 87 92 67 75 79 75 80

#▣ 출력예제 1

#74 7

#`round()함수는 값을 반올림해준다(소수점 첫째자리에서)`

#`sum() 함수는 파리미터로 들어온 값의 합을 구해준다.`

#`abs() 함수는 절대값 으로 표현해주는 함수이다`



# 내 풀이

# N명의 학생수 받기
N = int(input())
# N개의 점수 list에 저장
arr = list(map(int,input().split()))
# 점수 평균 계산
avg = 0
sum = 0
for i in range(len(arr)):
    sum+=arr[i]
avg = round(sum/len(arr))
# 평균와의 오차를 새로운 list에 저장(음수일 경우 양수로 바꿔서 저장)
result = list()
for i in range(len(arr)):
    a = avg-arr[i]
    if(a<0):
        a = -a
    result.append(a)
# 가장 오차가 작은 점수와 학생 번호를 출력
arrMin = result[0]
for i in range(1,len(result)):
    if result[i]<arrMin:
        arrMin = result[i]
index = 0
answer = 0
# 같은 값이 나와도 부등호가 < 이므로 좀더 작은 인덱스의 값이 저장됨.
for i in range(len(result)):
    if arrMin == result[i]:
        if answer<arr[i]:
            answer = arr[i]
            index = i
        
print(avg, index+1)


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
