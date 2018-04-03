print "FLAMES GAME by CodeManga\n"
name1 = raw_input('Enter your Name :')
name2 = raw_input('Enter your GirlFriend name : ')
name_1,name_2 = [],[]
for i in name1:
    name_1.append(i)
for j in name2:
    name_2.append(j)
print name_1
print name_2

for i in name_1:
    for j in name_2:
        if i == j:
            name_1.remove(name_1[name_1.index(i)])
            name_2.remove(name_2[name_2.index(j)])

#counting the number of digits from the remains
number = len(name_1)+len(name_2)
print "Number of letters not related : ",number

#counting over flames
flames = ['friend','lover','affection','marriage','enemy','sister']
for i in range(len(flames)):
    index = round(number%len(flames))-1
    index_2 = int(index)
    flames.remove(flames[index_2])
    if len(flames) == 1:
        print "Flames last element",flames