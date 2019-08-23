
posschars = ["R", "R\'", "L", "L\'", "U", "U\'", "B", "B\'"]

onemovers = []
for i in range(len(posschars)):
    onemovers.append(posschars[i])
#print(onemovers)

scr1 = open('newscrambles1.txt','w')
for i in range(len(onemovers)):
    scr1.write(str(onemovers[i])+"\n")
scr1.close()

twomovers = []
for j in range(len(onemovers)):
    for i in range(len(posschars)):
        if onemovers[j] in posschars[i]:
            continue
        elif posschars[i] in onemovers[j]:
            continue
        else:
            twomovers.append(onemovers[j]+" "+posschars[i])
#print(twomovers)
scr2 = open('newscrambles2.txt','w')
for i in range(len(twomovers)):
    scr2.write(str(twomovers[i])+"\n")
scr2.close()


threemovers = []
for j in range(len(twomovers)):
    for i in range(len(posschars)):
        if twomovers[j][-2] == " ":
            if twomovers[j][-1] == posschars[i][0]:
                continue
        else:
            if twomovers[j][-2] == posschars[i][0]:
                continue
        threemovers.append(twomovers[j]+" "+posschars[i])
#print(threemovers)
scr3 = open('newscrambles3.txt','w')
for i in range(len(threemovers)):
    scr3.write(str(threemovers[i])+"\n")
scr3.close()

fourmovers = []
for j in range(len(threemovers)):
    for i in range(len(posschars)):
        if threemovers[j][-2] == " ":
            if threemovers[j][-1] == posschars[i][0]:
                continue
        else:
            if threemovers[j][-2] == posschars[i][0]:
                continue
        fourmovers.append(threemovers[j]+" "+posschars[i])
#print(fourmovers)
scr4 = open('newscrambles4.txt','w')
for i in range(len(fourmovers)):
    scr4.write(str(fourmovers[i])+"\n")
scr4.close()


fivemovers = []
for j in range(len(fourmovers)):
    for i in range(len(posschars)):
        if fourmovers[j][-2] == " ":
            if fourmovers[j][-1] == posschars[i][0]:
                continue
        else:
            if fourmovers[j][-2] == posschars[i][0]:
                continue
        fivemovers.append(fourmovers[j]+" "+posschars[i])
#print(fivemovers)
scr5 = open('newscrambles5.txt','w')
for i in range(len(fivemovers)):
    scr5.write(str(fivemovers[i])+"\n")
scr5.close()


sixmovers = []
for j in range(len(fivemovers)):
    for i in range(len(posschars)):
        if fivemovers[j][-2] == " ":
            if fivemovers[j][-1] == posschars[i][0]:
                continue
        else:
            if fivemovers[j][-2] == posschars[i][0]:
                continue
        sixmovers.append(fivemovers[j]+" "+posschars[i])
#print(sixmovers)
scr6 = open('newscrambles6.txt','w')
for i in range(len(sixmovers)):
    scr6.write(str(sixmovers[i])+"\n")
scr6.close()

sevenmovers = []
for j in range(len(sixmovers)):
    for i in range(len(posschars)):
        if sixmovers[j][-2] == " ":
            if sixmovers[j][-1] == posschars[i][0]:
                continue
        else:
            if sixmovers[j][-2] == posschars[i][0]:
                continue
        sevenmovers.append(sixmovers[j]+" "+posschars[i])
print(sevenmovers)
scr7 = open('newscrambles7.txt','w')
for i in range(len(sevenmovers)):
    scr7.write(str(sevenmovers[i])+"\n")
scr7.close()
