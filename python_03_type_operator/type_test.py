print("Hello")
print("zohan")
print("Hello", end = '')
print("ztest")
print("Hello", "zboy")
print("Hello", "zod_1", sep = '')
print("Hello", "zod", sep = ',')
print("Hello", "Zod", sep = '! ')
print("{} / {} = {}".format(10, 3, 10/3))
print("{2} / {1} = {0}".format(10/3, 3, 10))
print("{y1} / {x1} = {r1}".format(r1 = 10 / 3, x1 = 3, y1 = 10))

print("\nWidth Test:")
print("{2:4d} / {1:8d} = {0:.8f}".format(10/3, 3, 10))
print("{2:4d} / {1:8d} = {0:10.8f}".format(10/3, 3, 10))
print("{2:4d} / {1:8d} = {0:11.8f}".format(10/3, 3, 10))
print("{2:<4d} / {1:<8d} = {0:11.8f}".format(10/3, 3, 10))
print("{2:<4d} / {1:>8d} = {0:<11.8f}".format(10/3, 3, 10))
print("{2:*^4d} / {1:%^8d} = {0:#^11.8f}".format(10/3, 3, 10))
print("{2:*^4d} / {1:%^8d} = {0:#^18.8f}".format(10/3, 3, 10))
print("{2:*^4d} / {1:%^8d} = {0:#^19.8f}".format(10/3, 3, 10))

print("\nKey Test:")
name_test = ["zohan", "Avril Lavigne", "Mai Kuraki"]
print("All name: {n[1]}, {n[0]}, {n[2]}".format(n = name_test))
password_test = {"zohan" : 1234, "Mai Kuraki" : 5678, "Avril Lavigne" : 9009}
print("The Password of Mai Kuraki is {pt[Mai Kuraki]}".format(pt = password_test))

import sys
print("My platform is {pc.platform}".format(pc=sys))
print(format(3.14159, '.2f'))

print("\nbytes Test:")
text = "耶,，是好吃的apple!"
print(len(text))
print(text.encode('utf-8'))
print(text.encode('UtF-8'))
print(text.encode('UTF-8'))
print(text.encode('Big5'))
print(text.encode('big5'))
print(text.encode('biG5'))
utf8_str = b'\xe8\x80\xb6'
print(utf8_str.decode('UtF-8'))
utf8_str = text.encode('UTF-8')
print(utf8_str.decode('UtF-8'))
big5_str = b'\xadC'
print(big5_str.decode("biG5"))
big5_str = b'\xadc'
print(big5_str.decode("biG5"))
big5_str = b'\xa1A'
print(big5_str.decode("biG5"))
big5_str = b'\xa1a'
print(big5_str.decode("biG5"))
utf8_str = text.encode('"biG5')
print(utf8_str.decode('"biG5'))
test_2 = "你,好"
print(test_2)
print(test_2[0])
print("你" in test_2)
print("," in test_2)
print("女" in test_2)

print("\nList test")
numbers = []
print(numbers)
print("len(numbers) = ", len(numbers))
numbers.append(5)
print(numbers)
print("len(numbers) = ", len(numbers))
numbers.append(6)
numbers.append(7)
print(numbers)
print("len(numbers) = ", len(numbers))
numbers.pop()
print(numbers)
print("len(numbers) = ", len(numbers))
numbers.pop(0)
print(numbers)
print("len(numbers) = ", len(numbers))
numbers.append(7)
numbers.append(8)
numbers.append(10)
print(numbers)
print("len(numbers) = ", len(numbers))
del numbers[2]
print(numbers)
print("len(numbers) = ", len(numbers))
print(7 in numbers)

print("\nSet test")
users = set()
users.add("apple")
users.add("Banana")
print(users)
print("len(users) = ", len(users))
users.add("apple")
print(users)
print("len(users) = ", len(users))
users1 = set()
users1.add("bb")
users1.add("aa")
print(users1)
print("len(users1) = ", len(users1))
users1.add("bb")
print(users1)
print("len(users1) = ", len(users1))
print(set("哈哈,天天開心!"))
print(set([1,2,3]))
print(set((2,4,1)))

print("\ndict test")
#password_dict = {"zohan" : 1234, "Avril Lavigne" : 56789, "Mai Kuraki" : 0909}
password_dict = {"zohan" : 1234, "Avril Lavigne" : 56789, "Mai Kuraki" : 10909}
print(password_dict)
print("len(password_dict) = ", len(password_dict))
password_dict["Liger"] = "000zero"
print(password_dict)
print("len(password_dict) = ", len(password_dict))
del password_dict["zohan"]
print(password_dict)
print("len(password_dict) = ", len(password_dict))
print("zohan" in password_dict)
print("Liger" in password_dict)
print("password_dict.get(\"zohan\") is ", password_dict.get("zohan"))
print(password_dict.get("zohan") == None)
print("password_dict.get(\"zohan\", 9999) is ",password_dict.get("zohan", 9999) == None)
print(password_dict.get("zohan", 9999) == 9999)
print("password_dict.get(\"zohan\", \"bye\") is ",password_dict.get("zohan", "bye") == None)
print(password_dict.get("zohan", "bye") == "bye")
print(list(password_dict))
print(list(password_dict.items()))
print(list(password_dict.keys()))
print(list(password_dict.values()))
password_dict_2 = dict(apple = 1, boy = 23, cat = 45)
print(password_dict_2)
password_dict_2 = dict([("app", 7), ("beach", 889), ("comedy", 99)])
print(password_dict_2)
print(dict.fromkeys(["Avril", "zohan"], "None"))

print("\ndict test")
act = 1, "apple", "ax"
print("type(act)", type(act))
print("act =", act)
act2 = (2, False, "vet", "pet")
print("type(act2)", type(act2))
print("act2 =", act2)
a1, a2, a3, a4 = act2
print("a1 = ", a1, ", a2 = ", a2, ",\na3 = ", a3, ", a4 = ", a4)
print("a1 = ", a1, ", a2 = ", a2, ",\na3 = ", a3, ", a4 = ", a4, sep="")
x = 14
y = 99
print("x =", x, ", y =", y)
x, y = y, x
print("x =", x, ", y =", y)
x, y = (y, x)
print("x =", x, ", y =", y)
b1, *b2, b3 = (1, 2, 3, "a", "a", "acc")
print("b1 =", b1, ", b2 =", b2, ", b3 =", b3)
print("type(b1) =", type(b1), ", type(b2) =", type(b2), ", type(b3) =", type(b3))
c1, *c2, c3 = [1, 2, 3, "a", "a", "acc"]
print("c1 =", c1, ", c2 =", c2, ", c3 =", c3)
print("type(c1) =", type(c1), ", type(c2) =", type(c2), ", type(c3) =", type(c3))

# Extended iterable unpacking with set would generate different results.
d1, *d2, d3 = {1, 2, 3, "a", "acc"}
print("d1 =", d1, ", d2 =", d2, ", d3 =", d3)
print("type(d1) =", type(d1), ", type(d2) =", type(d2), ", type(d3) =", type(d3))
