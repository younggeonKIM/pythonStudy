a="I eat %d apples." %3
print(a)

a="I eat %s apples." %"five"
print(a)


number=10
b="I want %d axes." %number
print(b)


money=10000
feeling='happy'
c="I have %d wons, I was %s in all that day." %(money, feeling)
print(c)

"""
rate=10
d='This products have %d% of defect rate.' %rate    ---> 문자열 포맷 코드 %d를 사용할 때는 %를 
                                                        그냥 사용할 수 없고 %% 라는 문자열 포맷
                                                        코드를 또 사용해야 %를 그대로 사용할 수
                                                        있음
print(d)
"""

rate=10
d='This products have %d%% of defect rates.' %rate
print(d)


#문자열 포맷 코드에 숫자를 같이 지정해주면 지정 문자열을 오른쪽에 정렬시키고 나머지는 공백으로 채우게 됨.
e="%10s" %"hello"
print(e)

#문자열 포맷 코드에 음수인 숫자를 같이 지정해주면 지정 문자열을 왼쪽에 정렬시키고 나머지는 공백으로 채우게 됨.
e="%-10sI'm %s" %("hi", "younggeon")
print(e)

#문자열 포맷 코드에 "0.*"을 같이 지정해줄 경우 *에 지정한 숫자만큼 소수점 자리수를 표현하게 됨.
f="%0.4f" %3.1415926535
print(f)

#문자열 포맷 코드에 소수점 자리수 표현할 때 "%0.*f" 에서 "0"을 생략해도 결과는 같음.
f="%.4f" %3.1415926535
print(f)