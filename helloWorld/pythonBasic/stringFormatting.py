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