# 조건문 : if ~ elif ~ else문
# if 조건식1:
#    조건식1이 참인 경우에 실행될 문장
# elif 조건식2:
#    조건식2가 참인 경우에 실행될 문장
# else:
#    위의 조건식을 만족하지 않을 경우에 실행될 문장

# 키보드로 점수(0~100점)를 입력 했을때, 입력한 점수가 어느 학점에 해당되는지 판별하는 프로그램
# 90점 이상 A학점
# 80~89점  B학점
# 70~79점  C학점
# 60~69점  D학점
# 60점 미만 F학점

s = int(input('점수를 입력하세요?'))
if s>= 90:
    print('A학점')
elif s>= 80:
    print('B학점')
elif s>= 70:
    print('C학점')
elif s>= 60:
    print('D학점')
else:
    print('F학점')
