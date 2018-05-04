sum=0
nature_num=1

while nature_num < 1000:
    if nature_num % 3 == 0 or nature_num % 5 == 0:
        sum+=nature_num
    nature_num+=1
print(sum)
