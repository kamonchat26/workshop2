# จงเขียนคำสั่งเพื่อแสดงต้น christmas โดยใช้คำสั่ง for โปรแกรมสามารถกำหนดความสูงของต้น christmas ได้

# input: height = 5
# outpu:
#      *
#     ***
#    *****
#   *******
#  *********

# input: height = 3
# outpu:
#    *
#   ***
#  *****

# input: height = 10
# outpu:
#           *
#          ***
#         *****
#        *******
#       *********
#      ***********
#     *************
#    ***************
#   *****************
#  *******************

height = int(input("Height = "))

for i in range(height, 0, -1):
    print((i * " " + (height - i) * "*") + "*" + ((height - i) * "*") + (i * " "))
