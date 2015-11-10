a = '%6.2f'%1.235
print(a)

a = '%06.2f'%1.235
print(a)#用0补

a='%(name)s:%(score)06.1f'%{'score':9.5,'name':'john'}
print(a)#输出john:0009.5
