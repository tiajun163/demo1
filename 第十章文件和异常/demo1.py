''''练习'''
name='s.txt'
with open(name) as fiel_object:
    fiel_name=fiel_object.read()
print(fiel_name)
# pi_name=[]
# for lin in fiel_name:
#     pi_name+=lin
#     print(pi_name)
with open(name)as f:
    f_n=f.readline()
    for n in f_n:
        print(n.rstrip())
print('CS额人：',f_n)
for cs in f_n:
    # print(cs.rstrip())
    print(cs.replace('d','ooo'))
