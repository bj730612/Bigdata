var1=1

def vartest():
    global var1
    var1 = var1+1

def vartest2():
    print(var1)

# def vartest3():
#     var1 = var1+1
#     print(var1)

vartest()

print(var1)

vartest2()