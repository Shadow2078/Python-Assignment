dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
dic={}
for i in (dic1,dic2,dic3):
    dic.update(i)
print(dic)


#Another Way
d1={1:10,2:20}
d2={3:30,4:40}
d3={5:50,6:60}
d1.update(d2)
d1.update(d3)
print(d1)