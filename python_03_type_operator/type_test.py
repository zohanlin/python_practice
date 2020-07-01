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

print("\ntuple test")
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
#
# https://python-forum.io/Thread-Why-the-result-of-extended-iterable-unpacking-with-set-is-unpredictable
# because set is unordered collection by definition :-) by buran
d1, *d2, d3 = {1, 2, 3, "a", "acc"}
print("d1 =", d1, ", d2 =", d2, ", d3 =", d3)
print("type(d1) =", type(d1), ", type(d2) =", type(d2), ", type(d3) =", type(d3))

print("\nVariable test")
e1 = [1, 2, 3]
e2 = e1
print("sys.getrefcount(e1) =", sys.getrefcount(e1))
print("sys.getrefcount(e2) =", sys.getrefcount(e2))
print("id(e1) =", id(e1))
print("id(e2) =", id(e2))
e1 = [1, 2, 3]
e2 = e1
e3 = e2
print("sys.getrefcount(e1) =", sys.getrefcount(e1))
print("sys.getrefcount(e2) =", sys.getrefcount(e2))
print("sys.getrefcount(e3) =", sys.getrefcount(e3))
print("id(e1) =", id(e1))
print("id(e2) =", id(e2))
print("id(e3) =", id(e3))
print("e3 =", e3)
e1[0] = 99
print("e2 =", e2)
e3[2] = 101
print("e1 =", e1)
print("sys.getrefcount(e1) =", sys.getrefcount(e1))
print("sys.getrefcount(e2) =", sys.getrefcount(e2))
print("sys.getrefcount(e3) =", sys.getrefcount(e3))
print("id(e1) =", id(e1))
print("id(e2) =", id(e2))
print("id(e3) =", id(e3))
e2 = 20
print("e1 =", e1)
print("e2 =", e2)
print("e3 =", e3)
print("sys.getrefcount(e1) =", sys.getrefcount(e1))
print("sys.getrefcount(e2) =", sys.getrefcount(e2))
print("sys.getrefcount(e3) =", sys.getrefcount(e3))
print("id(e1) =", id(e1))
print("id(e2) =", id(e2))
print("id(e3) =", id(e3))
del e3
print("e1 =", e1)
print("e2 =", e2)
print("sys.getrefcount(e1) =", sys.getrefcount(e1))
print("sys.getrefcount(e2) =", sys.getrefcount(e2))
print("id(e1) =", id(e1))
print("id(e2) =", id(e2))

import decimal
arg1 = 0.8
arg2 = 0.8
f1 = float(arg1)
f2 = float(arg2)
g1 = decimal.Decimal(arg1)
g2 = decimal.Decimal(arg2)
print("\n#### float ####")
print("{0} + {1} = {2}".format(f1, f2, f1 + f2))
print("{0} - {1} = {2}".format(f1, f2, f1 - f2))
print("{0} * {1} = {2}".format(f1, f2, f1 * f2))
print("{0} / {1} = {2}".format(f1, f2, f1 / f2))
print("\n#### decimal ####")
print("{0} + {1} = {2}".format(g1, g2, g1 + g2))
print("{0} - {1} = {2}".format(g1, g2, g1 - g2))
print("{0} * {1} = {2}".format(g1, g2, g1 * g2))
print("{0} / {1} = {2}".format(g1, g2, g1 / g2))

print("\n")
print("{0} ** {1} = {2}".format(2, 3, 2 ** 3))
print("{0} ** {1} = {2}".format(16, 0.5, 16 ** 0.5))

print("{0} / {1} = {2}".format(10, 3, 10 / 3))
print("{0} // {1} = {2}".format(10, 3, 10 // 3))
print("{0} / {1} = {2}".format(10, 3.0, 10 / 3.0))
print("{0} // {1} = {2}".format(10, 3.0, 10 // 3.0))

print("{0} % {1} = {2}".format(10, 3, 10 % 3))
print("{0} % {1} = {2}".format(11, 3, 11 % 3))

print("\n#### string ####")
h1 = "Avril"
h2 = "Lavigne"
print("h1 =", h1)
print("h2 =", h2)
print("h1 + h2 =", h1 + h2)
print("h1 * 7 =", h1 * 7)

i_str = "101"
i_int = 99
print("i_str =", i_str)
print("i_int =", i_int)

print("i_str + str(i_int) =", i_str + str(i_int))
print("int(i_str) + i_int =", int(i_str) + i_int)

print("\n#### list & tuple ####")

j_list = ["one", "two"]
j_list_2 = ["three", "four"]
print("j_list =", j_list)
print("j_list_2 =", j_list_2)
print("j_list + j_list_2 =", j_list + j_list_2)
print("j_list_2 * 3 =", j_list_2 * 3)
j_list_2_2 = j_list_2
j_list_3 = j_list_2 + j_list ## new list, not reference?
j_list_4 = [j_list_2, j_list]
j_list_5 = j_list_2 * 3 ## new list, not reference?
j_tuple = (j_list_2, j_list)
print("j_list_2_2 =", j_list_2_2)
print("j_list_3 = j_list_2 + j_list =", j_list_3)
print("j_list_4 = [j_list_2, j_list] =", j_list_4)
print("j_list_5 = j_list_2 * 3 =", j_list_5)
print("j_tuple =", j_tuple)
j_list_2[0] = "seven"
print("j_list_2 =", j_list_2)
print("j_list_2_2 =", j_list_2_2)
print("j_list_3 =", j_list_3)
print("j_list_4 =", j_list_4)
print("j_list_5 =", j_list_5)
print("j_tuple =", j_tuple)
j_list_4[0] = j_list_5
# j_tuple[0] = j_list_5  ##'tuple' object does not support item assignment
print("j_list_4 =", j_list_4)
# print("j_tuple =", j_tuple)

k_tuple = ("one", "two")
k_tuple_2 = ("three", "four")
print("k_tuple =", k_tuple)
print("k_tuple_2 =", k_tuple_2)
print("k_tuple + k_tuple_2 =", k_tuple + k_tuple_2)
print("k_tuple_2 * 3 =", k_tuple_2 * 3)
k_tuple_3 = k_tuple_2
k_tuple_4 = k_tuple_2 * 3
k_tuple_5 = k_tuple + k_tuple_2
k_tuple_6 = (k_tuple, k_tuple_2)
print("k_tuple_3 =", k_tuple_3)
print("k_tuple_4 =", k_tuple_4)
print("k_tuple_5 =", k_tuple_5)
print("k_tuple_6 =", k_tuple_6)

print("\ncompare test")
l_str1 = "Mai"
l_str2 = "Kuraki"
print("\"{0}\" > \"{1}\" ?  {2}".format(l_str1, l_str2, l_str1 > l_str2))
print("\"{0}\" == \"{1}\" ?  {2}".format(l_str1, l_str2, l_str1 == l_str2))
print("\"{0}\" < \"{1}\" ?  {2}".format(l_str1, l_str2, l_str1 < l_str2))
print("\"{0}\" != \"{1}\" ?  {2}".format(l_str1, l_str2, l_str1 != l_str2))

print("\nlogic test")
m_str1 = "ZOHAN"
m_str2 = "Dominic"
print("m_str1 =", m_str1)
print("m_str2 =", m_str2)
print("兩個都大寫 ? ", m_str1.isupper() and m_str2.isupper())
print("有一個是大寫 ? ", m_str1.isupper() or m_str2.isupper())
print("都不是大寫 ? ", not (m_str1.isupper() or m_str2.isupper()))
print("都不是大寫 ? ", not (m_str1.isupper()) and not (m_str2.isupper()))
print("m_str1.isupper() and m_str2.isupper() =",  m_str1.isupper() and m_str2.isupper())
print("m_str1.isupper() and \"Avril\" = ", m_str1.isupper() and "Avril")
print("m_str2.isupper() and \"Avril\" =", m_str2.isupper() and "Avril")
print("m_str1.isupper() or \"Avril\" =", m_str1.isupper() or "Avril")
print("m_str2.isupper() or \"Avril\" =", m_str2.isupper() or "Avril")
print("[] and \"Avril\" =", [] and "Avril")
print("[1, 2] and \"Avril\" =", [1, 2] and "Avril")
print("[] or \"Avril\" =", [] or "Avril")
print("[1, 2] or \"Avril\" =", [1, 2] or "Avril")

print("\nbitwise test")
print("0 AND 0 = {0}".format(0 & 0))
print("0 AND 1 = {0}".format(0 & 1))
print("1 AND 0 = {0}".format(1 & 0))
print("1 AND 1 = {0}".format(1 & 1))
print("0 or 0 = {0}".format(0 | 0))
print("0 or 1 = {0}".format(0 | 1))
print("1 or 0 = {0}".format(1 | 0))
print("1 or 1 = {0}".format(1 | 1))
print("0 xor 0 = {0}".format(0 ^ 0))
print("0 xor 1 = {0}".format(0 ^ 1))
print("1 xor 0 = {0}".format(1 ^ 0))
print("1 xor 1 = {0}".format(1 ^ 1))
print("not 0 = {0}".format(~0))
print("not (-1) = {0}".format(~(-1)))
print("not 14 = {0}".format(~14))
print("not (-15) = {0}".format(~(-15)))

dec = 17
print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

n1 = 0b1111
print("n1 =", n1)
print("bin(n1) =", bin(n1))
print("oct(n1) =", oct(n1))
print("hex(n1) =", hex(n1))
print("bin(~n1) =", bin(~n1))
print("n1 >> 1 =", bin(n1 >> 1))
print("n1 >> 2 =", bin(n1 >> 2))
print("n1 >> 3 =", bin(n1 >> 3))
print("n1 >> 4 =", bin(n1 >> 4))
print("n1 >> 5 =", bin(n1 >> 5))
print("n1 << 1 =", bin(n1 << 1))
print("n1 << 2 =", bin(n1 << 2))
print("n1 << 3 =", bin(n1 << 3))
print("n1 << 4 =", bin(n1 << 4))
print("n1 << 5 =", bin(n1 << 5))
n2 = n1 << 5
print("bin(n2) =", bin(n2))
print("n2 >> 1 =", bin(n2 >> 1))
print("n2 << 1 =", bin(n2 << 1))
print("n2 << 100 =", bin(n2 << 100))
print("n2 >> 100 =", bin(n2 >> 100))

admins = {"zohan", "Dominic"}
users = set()
users.add("Monica")
users.add("Judy")
users.add("Simon")
users.add("zohan")
users1 = {"Dominic"}
print("存在user中的admin :{0}".format(admins & users) )
print("存在user中，不是admin :{0}".format(users - admins) )
print("全部的人 :{0}".format(users | admins) )
print("身分不重複 :{0}".format(users ^ admins) )
print("admin有包括users ? {}".format(admins > users) )
print("users有包括admin ? {}".format(admins < users) )
print("admin有包括users1 ? {}".format(admins > users1) )
print("users1有包括admin ? {}".format(admins < users1) )

admins_2 = ["zohan", "Dominic"]
print("{0}".format(admins_2) )
admins_3 = ("zohan", "Dominic")
print("{0}".format(admins_3) )

print("\nslicing test")
o_name = "zohan"
print("o_name = ", o_name)
print("o_name[0] =", o_name[0])
print("o_name[1] =", o_name[1])
print("o_name[2] =", o_name[2])
print("o_name[3] =", o_name[3])
print("o_name[4] =", o_name[4])
print("o_name[-1] =", o_name[-1])
print("o_name[-2] =", o_name[-2])
print("o_name[-3] =", o_name[-3])
print("o_name[-4] =", o_name[-4])
print("o_name[-5] =", o_name[-5])
print("o_name[0:] =", o_name[0:])
print("o_name[0:0] =", o_name[0:0])
print("o_name[0:1] =", o_name[0:1])
print("o_name[0:2] =", o_name[0:2])
print("o_name[0:3] =", o_name[0:3])
print("o_name[0:4] =", o_name[0:4])
print("o_name[0:5] =", o_name[0:5])
print("o_name[0:-1] =", o_name[0:-1])
print("o_name[-4:-1] =", o_name[-4:-1])
print("o_name[0::2] =", o_name[0::2])
print("o_name[0::3] =", o_name[0::3])
print("o_name[0::4] =", o_name[0::4])
print("o_name[0::5] =", o_name[0::5])
print("o_name[0::1] =", o_name[0::1])
print("o_name[::1] =", o_name[::1])
print("o_name[0:5:1] =", o_name[0:5:1])
print("o_name[0:-1:1] =", o_name[0:-1:1])
print("o_name[0::-1] =", o_name[0::-1])
print("o_name[0::-2] =", o_name[0::-2])
print("o_name[:0:-1] =", o_name[:0:-1])
print("o_name[:1:-1] =", o_name[:1:-1])
print("o_name[:-2:-1] =", o_name[:-2:-1])
print("o_name[:-3:-1] =", o_name[:-3:-1])
print("o_name[:-4:-1] =", o_name[:-4:-1])
print("o_name[:-5:-1] =", o_name[:-5:-1])
print("o_name[:-6:-1] =", o_name[:-6:-1])
print("o_name[-1:0:-1] =", o_name[-1:0:-1])
print("o_name[-1:-1:-1] =", o_name[-1:-1:-1])
print("o_name[:-1:-1] =", o_name[:-1:-1])
print("o_name[-1::-1] =", o_name[-1::-1])
print("o_name[-1:-2:-1] =", o_name[-1:-2:-1])
print("o_name[-1:-3:-1] =", o_name[-1:-3:-1])
print("o_name[-1:-4:-1] =", o_name[-1:-4:-1])
print("o_name[-1:-5:-1] =", o_name[-1:-5:-1])
print("o_name[-1:-6:-1] =", o_name[-1:-6:-1])
print("o_name[::-1] =", o_name[::-1])
print("o_name[0::-1] =", o_name[0::-1])
print("o_name[0:-1:-1] =", o_name[0:-1:-1])
print("o_name[-5:-1:-1] =", o_name[-5:-1:-1])
print("o_name[-5::-1] =", o_name[-5::-1])
print("o_name[-1:0:1] =", o_name[-1:0:1])
print("o_name[4:0:1] =", o_name[4:0:1])
print("o_name[4::1] =", o_name[4::1])

# string = "zohan"
#
# step = -1
#   end     <--     <--     <--     start
#   [0]     [1]     [2]     [3]     [4]
#   z       o       h       a       n
#
# step = 1
#   start   <--     <--     <--     end
#   [0]     [1]     [2]     [3]     [4]
#   z       o       h       a       n

p1_num = [1, 2, 3, 4]
p2_num = [5, 6, 7, 8]
print("p1_num =", p1_num)
p1_tuple = (p1_num, p2_num)
p2_tuple = p1_tuple[:]
print("p1_tuple =", p1_tuple)
p2_tuple[0][0] = 900
p2_tuple[0][3] = 903
p2_tuple[1][0] = 910
p2_tuple[1][3] = 913
print("p1_num =", p1_num)
print("p1_tuple =", p1_tuple)
p1_num[1:3] = [82, 83]
print("p1_num =", p1_num)
p1_num[1:3] = ["Avril Lavigne"]
print("p1_num =", p1_num)
del p1_num[1:2]
print("p1_num =", p1_num)
del p1_num[1:2]
print("p1_num =", p1_num)
p1_num[:] = []
print("p1_num =", p1_num)


