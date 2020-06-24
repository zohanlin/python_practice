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