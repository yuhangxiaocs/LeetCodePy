filename = 'test.txt'
# with open(filename, 'w') as fileobject:
#     fileobject.write("xiao")
#


with open(filename, 'w') as fileobject:
    fileobject.write('yuhang')

x, y = 5, 0

try:
    res = x / y
except ZeroDivisionError:
    print("zero division error")
else:
    print(res)
