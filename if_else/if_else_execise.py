# จงเขียนโปรแกรมเพื่อทำการคำนวณเกรดโดยมีเงื่อนไขดังนี้

# คะแนน 75 - 79 ได้ B+
# คะแนน 70 - 74 ได้ B
# คะแนน 65 - 69 ได้ C+
# คะแนน 60 - 64 ได้ C
# คะแนน 55 - 59 ได้ D+
# คะแนน 50 - 54 ได้ D
# คะแนน 0 - 49 ได้ F

# และให้แสดงผลตามตัวอย่างด้านล่าง

# Enter your score: 49
# grade:  F

score = int(input("Enter your score: "))

if score >= 80:
    print("grade: A")
elif 75 <= score <= 79:
    print("grade: B+")
elif 70 <= score <= 74:
    print("grade: B")
elif 65 <= score <= 69:
    print("grade: C+")
elif 60 <= score <= 64:
    print("grade: C")
elif 55 <= score <= 59:
    print("grade: D+")
elif 50 <= score <= 54:
    print("grade: D")
else:
    print("grade: F")