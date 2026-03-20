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