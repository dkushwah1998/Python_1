'''first_name = input("Enetr your first name: ")
last_name = input("Enter your last name: ")
print(last_name + " " + first_name)'''

'''number = input("enter numbers: ")
list = number.split(" ")
tuple = tuple(list)
print("list: ", list)
print("tuple: ", tuple)'''

'''filename = input("Enter file name: ")
list= filename.split(".")
print("list: ", list)
print("extension of filename: "+ list[-1])'''

'''color_list = ["Red","Green","White" ,"Black"]
print(color_list[0], color_list[-1])'''

'''exam_date = (25,6,2022)
print("Exam start from: %i/%i/%i"%exam_date )'''

a = int(input("Eneter a Integer: "))
n1 = int("%s" % a)
n2 = int("%s%s" % (a,a))
n3 = int("%s%s%s" % (a,a,a))
print(n1+n2+n3)
