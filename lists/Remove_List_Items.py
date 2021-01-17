# Ex1
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")  # banana โดนลบ
print(thislist)

# Ex2
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)  # banana โดนลบ
print(thislist)

# Ex3
thislist = ["apple", "banana", "cherry"]
thislist.pop()  # เอาตัวที่อยู่ตำแหน่งสุดท้ายออกไป
print(thislist)

# Ex4
thislist = ["apple", "banana", "cherry"]
del thislist[0]  # apple โดนลบ
print(thislist)

# Ex5
thislist = ["apple", "banana", "cherry"]
thislist.clear()  # output: []
print(thislist)