#A função eval() recebe uma string, mas trata como um valor numérico

s = "1 + 2"
x=type(s)
y=eval(s)
print("x = ", x)
print("y = ", y)

####exemplo ao executar
#x =  <class 'str'>
#y =  3
