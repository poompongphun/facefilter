# import numpy as np
# arr = np.array(10)
# print(arr.ndim)
# li1 = [1, 2, 3]
# arr1 = np.array(li1)
# print(arr1.ndim)
# li2 = [[1, 2, 3], [2, 3, 4]]
# arr2 = np.array(li2)
# print(arr2.ndim)
# li3 = [[[1, 2], [3, 4]], [[4, 5], [6, 7]]]
# arr3 = np.array(li3)
# print(arr3)
# print("*" * 4)
def fx(x):
    return (x**2 + 1)
block = 4
end, start = 2, 0
isRight = True
deltax = (end - start) / block
x = start + (deltax * isRight)
result = 0
for i in range(block):
    result += deltax * fx(x)
    x += deltax
print("%.3f" % result)
print("%.2f" % result)
print("%.1f" % result)
print("%-.1f" % result)
#fix
