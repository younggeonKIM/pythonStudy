course = 'Python for Beginners'
print(course.upper())
print(course.find('y'))
print(course.find('for'))
print(course.find('Y'))
print(course.replace('for', '4'))
print(course.replace('x', '4'))
print('Python' in course)
print(course)

name = """Kim Younggeon"""
print(name)
print(name.upper())

#작은 따옴표 안에 있는 큰 따옴표는 문자열로 인식되지 않음
dialogue = '"Whatever my lot, it is well with my soul" said Oh'
print(dialogue)


#이스케이프 문자인 역슬래시(\) 를 이용해 문자열 내에 작은따옴표나 큰따옴표를 포함시킬 수 있음
anniversary = 'NY\'s birthday'
print(anniversary + ' is Feb 4th')

#큰 따옴표 3번 입력하면 개행을 한 장문의 문자열을 변수에 대입할 수 있음.
QTTime = """
I AM THE GATE; whoever enters through Me will be saved.
I am not a locked barrier but an open door for you-for all My chosen followers.
I came into the world so that you might have Life and have it to the full.
"""
print(QTTime)


#큰 따옴표 한 쌍으로는 개행된 문자열을 나타낼 수 없고 괄호로 묶어서 개행한 뒤에 큰따옴표를 이어서 입력할
# 수밖에 없다.
"""
QTTime2 = "A full life means different things for different people.
So in your quest to live abundantly, dont's compare your circumstances with those of others.
"
print(QTTime2)    <--- 에러발생
"""


#파이썬에는 다른 프로그래밍 언어에는 없는 다른 재미있는 기능이 있음.
b = 'Sato'
print(b * 2)


#문자열 곱셈 응용
print('=' * 50)
print("NYLove")
print('=' * 50)