# Ex 1
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set3 = set1.union(set2)
print(set3)

# Ex 2
set1 = {"a", "b", "c"}
set2 = {"d", "e", "f"}
set1.update(set2)
print(set1)

# Ex 3
set1 = {"apple", "banana", "cherry"}
set2 = {"goole", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # เอาตัวเหมือนกัน

# Ex 4
set1 = {"apple", "banana", "cherry"}
set2 = {"goole", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # ไม่เอาตัวซ้ำ
