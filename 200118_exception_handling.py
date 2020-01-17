# try, except문
try:
    print("Hi")
    print(param)
except:
    pass

try:
    print("Hi")
    print(param)
except:
    print("예외가 발생했습니다.")


# try, except, else문
short_list=['a','b','c']
position=2
try:
    short_list[position]
except:
    print('Need a position between 0 and 2')
else:
    print(short_list[position])


# try, except, else, finally문
short_list=['apple','banana','grape']
position=7
try:
    short_list[position]
except:
    print('Need a position between 0 and 2')
else:
    print(short_list[position])
finally:
    print('과일의 갯수는:', len(short_list),'개')
