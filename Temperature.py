flag = False
answer = ""
direction = 0 # 1 = c to f, 2 = f to c

while(not flag):
    answer = input("Convert from Celsius or Fahrenheit? [c|f] \n")
    if(answer.lower() == "c"):
        direction = 1
        flag = True
    elif(answer.lower() == "f"):
        direction = 2
        flag = True

answer = float(input("Enter a temperature: "))
if(direction == 1):
    answer *= 1.8
    answer += 32
else:
    answer -= 32
    answer /= 1.8

print(round(answer, 1))
