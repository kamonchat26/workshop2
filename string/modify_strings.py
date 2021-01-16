string = "Hello, World! "

print(string.upper())  # output: "HELLO, WORLD"
print(string.lower())  # output: "hello, world"
print(string.strip())  # output: "Hello, World"
print(string.replace("H", "J"))  # output: Jello,World! แทนที่Hด้วยJ
print(
    string.split(",")
)  # output: [' Hello', 'World!'] ตัดข้อความด้วย , ตัวที่ตัดจะหายไป
print(len(string))  # 15
