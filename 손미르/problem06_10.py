### 코드작성/실행결과 작성 부분의 주석을 지우고 직접 작성하시오.
### 이름 : OOO
#손미르

### 6. 문자열 '1004'를 정수형으로 변환하는 코드를 작성하시오.
#num='1004'

# 코드 작성
num="1004"
print(type(num))
num=int(num)
print(type(num))
print(num)

### 7. 아래 코드의 실행 결과를 예상하시오(Hint 오류인지 아닌지 부터 따질것)

sss = 'python'
sss[0] = 'P'
print(sss)

#오류!!!!


### 8. '닥터스트레인지', '아이언맨', '캡틴아메리카' 를 리스트에 담는 코드를 작성하시오.

# 코드 작성
movies=['닥터스트레인지', '아이언맨', '캡틴아메리카']
print(list(movies))
print(movies)


### 9. 위 리스트에 '캡틴마블' 을 추가하는 코드를 작성하시오. Hint(list에는 append라는 추가할 수 있는 함수가 있다.)

# 코드 작성
movies.append("캡틴마블")
print(movies)


### 10. 밑의 리스트에서 합, 최댓값, 최솟값을 출력하는 코드를 작성하시오.  hint : sum(), min(), max() 함수를 이용
#nums = [2,3,4,1,100,94,-5,10]

# 코드 작성
nums = [2,3,4,1,100,94,-5,10]
print(sum(nums))
print(min(nums))
print(max(nums))
