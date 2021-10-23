import numpy as np

'''สร้าง array'''

arr = np.array([[[1, 2, 3], [7, 8, 9]], [[4, 5, 6], [10, 11, 12]]])
print(arr)
print(arr[0][0][2])  # ระบุตำแหน่งสมาชิกที่ต้องการนำมาใช้งาน (index)
print(arr.ndim)

# ใส่ dtype="int" ระบุชนิดข้อมูลใน array ได้
# np.zeros(ขนาด) สร้าง matrix 0
# np.ones(ขนาด) สร้าง matrix 1
# np.full(ขนาด, ค่าคงที่) สร้าง matrix ค่าคงที่
# np.empty(ขนาด) สร้าง matrix แบบสุ่มค่า ปกติใช้แบบสนใจเฉพาะขนาด
# np.identity(ขนาด) สร้าง matrix เอกลักษณ์ แบบจัตุรัส
# np.eye(ขนาด, k) สร้าง matrix เอกลักษณ์ กำหนดขนาด กำหนดค่า k
# np.linspace(start, stop, number) สร้างตั้งแต่เลข start ถึง stop number คือกำหนกจำนวน สามารถตั้ง endpoint=False ถ้าไม่ต้องการตัวสุดท้าย
# สมาชิกทุกตัว จะมีระยะห่างเท่าๆกัน

print(np.linspace(1, 5, dtype="int"))

# np.arange(start, stop, step) ทำงานเหมือน range ใน for loop

print(np.arange(2, 8))

# np.random.random(ขนาด) สุ่มค่าใส array ในช่วง 0-1

print(np.random.random((2, 2)))

'''numpy attribute'''

# array.ndim บอกมิติของ array
# array.dtype บอก datataype ของ array
# array.shape รูปร่างของ array (ขนาด หรือโคงสร้าง) ex. (4, 3) คือ 4 แถว 3 คอลัม
# array.size บอกว่า array มีกี่ตัว
# array.itemsize ดูว่ามีขนาดกี่ไบต์

'''array slice'''

# array[start:stop:step]
# กรณีของ 2 มิติ array[start:stop:step, start:stop:step] row & col

arr2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2)
print(arr2[1:, 1:])

'''index operater'''

x = np.arange(1, 10)
index = np.array([1, 5, 7])
print(x)
print(x[index])  # เข้าถึงสมาชิกหลายตัว แบบไม่ต้อง index ทีละตัว

x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(x2)
print(x2[[0, 2], [2, 0]])  # ไม้ต้องสร้างตัวแปรเก็บ index ที่เราต้องการ

# สามารถ filter สมาชิกใน array ได้

print(x[x % 2 == 0])

# array สามารถ + - * / ** % // ได้

print(x**2)  # นำสมาชิกใน array x ทุกตัวมายกกำลัง 2

x_a = np.array([1, 2, 6, 8])
x_b = np.array([2, 5, 6, 9])
# นำ 2 array มา + - * / ** % // กันได้ เมื่อ array 2 ตัว มีขนาดเท่ากัน(x_a.shape == x_b.shape)
# array ต่างมิติกัน แต่มีจำนวนสมาชิกเท่ากัน สามารถ operation กันได้ (ไม่ Boardcast Error)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.array(
    [2, 4, 6])  # มันจะเพิ่มแถวตัวเอง เพื่อไปบวกกับ array x ที่มี 3 แถว '''Boardcasting'''
print(x + y)

# ขนาด และมิติของ Array 2 ตัวสอดคล้องกัน
# Array ที่เล็กกว่าจะทำซ้ำเพื่อเพิ่มขนาด หรือมิติ เพื่อให้สอดคล้างกับ array อีกตัวนึง

'''จัดเรียง Array'''

a = np.arange(10)
print(a)
print(a.reshape((2, 5)))
print(a)
# ต้องมีตัวแปรมารองกับในการเปลี่ยนแปลงโครงสร้าง ไม่กระทบกับ a
b = a.reshape((2, 5))
print(b)

a.resize((2, 5))
print(a)  # ไมต้องมีตัวแปรมารองรับ เปลี่ยนแปลงข้อมูลในตัวมันเอง

'''เปลี่ยนแปลง array 2 มิติ 3 มิติ จัดรูปร่างใหม่เป็น 1 มิติ'''

print(a.flatten())
b = a.flatten()  # แปลงชั่วคราว หรือต้องมีตัวแปรมารองรับ ไม่กระทบกับ a
print(a)
print(b)

c = a.ravel()
print(c)
c[0] = 10  # เมื่อมีการเปลี่ยนแปลงข้อมูล จะทำการเปลี่ยนแปลงทั้ง array ใหม่ และ array เก่า
print(c)
print(a)

'''Transpose Array'''
# เปลี่ยนแนวนอนเป็นแนวตั้ง แนวตั้งเป็นแนวนอน

print(a)
print(a.transpose())
b = a.transpose()  # แปลงชั่วคราว หรือต้องมีตัวแปรมารองรับ ไม่กระทบกับ a

'''Array w/ statistic'''

# Array 1 มิติ
a = np.array([10, 5, 4, 6, 99, 100, 50, 30])
print(a.sum())  # ผลรวมของสมาชิกทุกตัวใน Array
print(a.prod())  # ผลคุณของสมาชิกทุกตัวใน Array
print(a.mean())  # ค่าเฉลี่ย
print(a.max(), a.min())  # ค่าสูงสุด-ต่ำสุดใน array
print(a.argmax(), a.argmin())  # ตำแหน่งของค่าสูงสุด-ต่ำสุดใน array

# Array 2 มิติ ต้องระบุแกนด้วย ว่าจะดูแนวตั้งหรือแนวนอน (axis 0 = แนวตั้ง, axis 1 = แนวนอน)
b = np.array([[1, 5, 60], [100, 2, 90], [54, 9, 200]])
print(np.min(b, axis=1))  # ค่าต่ำสุดของ array b ในแนวนอน
print(np.max(b, axis=0))  # ค่าสูงสุดของ array b ในแนวตั้ง

'''matrix dot product'''
# matrix จัตุรัส 2 ตัวมาคูณกัน เป็นผลคูณสเกลาร์

a = np.array([[1, 2], [3, 4]])
b = np.array([[11, 12], [13, 14]])
c = a.dot(b)  # ขนาดของ matrix ทั้ง 2 ตัวต้องมีขนาด row and col เท่ากัน
print(c)
# [[37 40]  [[1*11 + 2*13, 1*12 + 2*14]
#  [85 92]]  [3*11 + 4*13, 3*12 + 4*14]]

'''concatenate และการเพิ่ม-ลดสมาชิกใน Array'''
# สมาชิก 2 กลุ่ม รวมกันเป็นก้อนเดียว
print(np.concatenate((a, b)))  # ชั่วคราว

# เพิ่มสมาชิกใน array
d = np.arange(10)
print(d)
print(np.append(d, 100))  # ชั่วคราว
print(d)
d = np.append(d, 100)
print(d)

# Array 2 มิติ ต้องระบุแกนด้วย ว่าจะดูแนวตั้งหรือแนวนอน (axis 0 = แนวตั้ง, axis 1 = แนวนอน)
print(np.append(a, [[10], [20]], axis=1))
print(np.append(a, [[10, 20]], axis=0))

# Insert การเพิ่มข้อมูลในตำแหน่งที่เรากำหนด
# np.insert(array, ตำแหน่ง, สมาชิกที่ต้องการเพิ่ม, แกน(ถ้าเป็น 2 มิติ))
print(np.insert(a, 1, [[10, 20]], axis=0))

# delete ลบข้อมูลสมาชิก
# np.delete(array, ตำแหน่งที่ต้องการลบ, แกน(ถ้าเป็น 2 มิติ))
print(np.delete(d, 1))
# axis 1 = แนวตั้ง, axis 0 = แนวนอน !!! มีการสลับขั้วกัน
print(np.delete(a, 1, axis=1))

'''split'''
# แยกข้อมูลใน Array แบ่งจำนวนที่เท่าๆกัน
a = np.arange(1, 21)
print(a)
print(np.split(a, 4))  # ต้องเป็นเลขที่หารลงตัว

# Array 2 มิติต้องมีการระบุแกน
a = a.reshape(5, 4)
print(a)
print(np.hsplit(a, 4))  # แบ่งในแนวตั้ง
print(np.vsplit(a, 5))  # แบ่งในแนวนอน
