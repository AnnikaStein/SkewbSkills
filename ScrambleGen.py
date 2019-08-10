# IMPORT NOTE: This generates scrambles of a given length and combines each of them with each
# colour OR combines each scramble with the specific colour white ("w").
# To write the files with the correct data, choose one of the uppermost blocks to generate the
# onemovers and name this field "onemovers". The other block shall be commented out.
# If you want to generate the one with every colour, choose the upper block, if you only need to
# generate the file with the colour white, choose the second one.
# Choose a suiting filename for each scramble-length by typing
# scambles[number of moves][w (for white) or write nothing here (for all colours)]


posschars = ["R", "R\'", "L", "L\'", "U", "U\'", "B", "B\'"]

posscols = ["w", "y", "g", "r", "b", "o"]
'''
# all eight onemovers combined with all colours
onemovers = []
for i in range(len(posschars)):
    for j in range(len(posscols)):
        kombi = [posschars[i], posscols[j]]
        onemovers.append(kombi)
#print(onemovers)

scr1 = open('scrambles1.txt','w')
for i in range(len(onemovers)):
    for j in range(0,2):
        scr1.write(str(onemovers[i][j])+"\n")
scr1.close()
'''
# only with white or any other specific colour someone chose
onemovers = []
for i in range(len(posschars)):
    kombi = [posschars[i], "w"]
    onemovers.append(kombi)
#print(onemovers)
'''
scr1w = open('scrambles1w.txt','w')
for i in range(len(newonemovers)):
    for j in range(0,2):
        scr1w.write(str(newonemovers[i][j])+"\n")
scr1w.close()
'''
twomovers = []
for j in range(len(onemovers)):
    for i in range(len(posschars)):
        if onemovers[j][0] in posschars[i]:
            continue
        elif posschars[i] in onemovers[j][0]:
            continue
        else:
            kombi2 = [onemovers[j][0]+" "+posschars[i], onemovers[j][1]]
            twomovers.append(kombi2)
#print(twomovers)
scr2 = open('scrambles2w.txt','w')
for i in range(len(twomovers)):
    for j in range(0,2):
        scr2.write(str(twomovers[i][j])+"\n")
scr2.close()

threemovers = []
for j in range(len(twomovers)):
    for i in range(len(posschars)):
        if twomovers[j][0][-2] == " ":
            if twomovers[j][0][-1] == posschars[i][0]:
                continue
        else:
            if twomovers[j][0][-2] == posschars[i][0]:
                continue
        kombi3 = [twomovers[j][0]+" "+posschars[i], twomovers[j][1]]
        threemovers.append(kombi3)
# print(threemovers)
scr3 = open('scrambles3w.txt','w')
for i in range(len(threemovers)):
    for j in range(0,2):
        scr3.write(str(threemovers[i][j])+"\n")
scr3.close()

fourmovers = []
for j in range(len(threemovers)):
    for i in range(len(posschars)):
        if threemovers[j][0][-2] == " ":
            if threemovers[j][0][-1] == posschars[i][0]:
                continue
        else:
            if threemovers[j][0][-2] == posschars[i][0]:
                continue
        kombi4 = [threemovers[j][0]+" "+posschars[i], threemovers[j][1]]
        fourmovers.append(kombi4)
#print(fourmovers)
scr4 = open('scrambles4w.txt','w')
for i in range(len(fourmovers)):
    for j in range(0,2):
        scr4.write(str(fourmovers[i][j])+"\n")
scr4.close()
fivemovers = []
for j in range(len(fourmovers)):
    for i in range(len(posschars)):
        if fourmovers[j][0][-2] == " ":
            if fourmovers[j][0][-1] == posschars[i][0]:
                continue
        else:
            if fourmovers[j][0][-2] == posschars[i][0]:
                continue
        kombi5 = [fourmovers[j][0]+" "+posschars[i], fourmovers[j][1]]
        fivemovers.append(kombi5)
#print(fivemovers)
scr5 = open('scrambles5w.txt','w')
for i in range(len(fivemovers)):
    for j in range(0,2):
        scr5.write(str(fivemovers[i][j])+"\n")
scr5.close()

sixmovers = []
for j in range(len(fivemovers)):
    for i in range(len(posschars)):
        if fivemovers[j][0][-2] == " ":
            if fivemovers[j][0][-1] == posschars[i][0]:
                continue
        else:
            if fivemovers[j][0][-2] == posschars[i][0]:
                continue
        kombi6 = [fivemovers[j][0]+" "+posschars[i], fivemovers[j][1]]
        sixmovers.append(kombi6)
#print(sixmovers)
scr6 = open('scrambles6w.txt','w')
for i in range(len(sixmovers)):
    for j in range(0,2):
        scr6.write(str(sixmovers[i][j])+"\n")
scr6.close()

sevenmovers = []
for j in range(len(sixmovers)):
    for i in range(len(posschars)):
        if sixmovers[j][0][-2] == " ":
            if sixmovers[j][0][-1] == posschars[i][0]:
                continue
        else:
            if sixmovers[j][0][-2] == posschars[i][0]:
                continue
        kombi7 = [sixmovers[j][0]+" "+posschars[i], sixmovers[j][1]]
        sevenmovers.append(kombi7)
#print(sevenmovers)
scr7 = open('scrambles7w.txt','w')
for i in range(len(sevenmovers)):
    for j in range(0,2):
        scr7.write(str(sevenmovers[i][j])+"\n")
scr7.close()
