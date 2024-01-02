# global var
var0 = "global var"


def fun1():
    # local var
    var0 = "local var"
    print(var0)


def fun2():
    global var0
    var0 = "local var"
    print(var0)


fun1()
print(var0)
