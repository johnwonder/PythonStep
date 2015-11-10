import unicodedata

title = u"Klüft skräms inför på fédéral électoral große"
B= unicodedata.normalize('NFKD',title).encode('ascii','ignore')

print(B)

#format字符串http://www.cnblogs.com/cposture/p/4722340.html
print('number is %d'%10)


#字符串转数字
print(int("234"))
