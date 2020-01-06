time = int(input("경과 초를 입력하세요"))

day, r = divmod(time, 86400)
hh, r = divmod(r, 3600)
mm, ss = divmod(r, 60)

print(day, "일", hh, "시", mm, "분", ss, "초")


number = input("3자리 정수를 입력하세요:")

while len(number) != 3:
     number = input("3자리 정수를 입력하세요:")
     if len(number) ==3:
         break


result = number[2]+number[1]+number[0]

print(result)