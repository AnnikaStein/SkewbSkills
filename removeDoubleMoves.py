def doubleMoveRemover(scramble):
    newScr = []
    newScrString = ""
    scrSplit = scramble.split()
    # go through all moves
    for i in range(len(scrSplit)):
        # if newScr contains already one element, check the properties of consecutive moves
        if len(newScr) >= 1:
            # newScr contains at least one element.
            # check if the previous and current move are equal
            if newScr[-1] == scrSplit[i]:
                # e.g. R R or R' R'
                # now find out whether they've got the ' or not by checking the length
                if len(scrSplit[i]) == 1:
                    # just one character --> case (e.g.) R R
                    newScr.pop()
                    newScr.append(scrSplit[i]+"'")
                else:
                    # it's the case when there's more than one char, so e.g. R' R'
                    newScr.pop()
                    newScr.append(scrSplit[i][0])
            else:
                # previous and current move are not equal
                # check whether they are just a prime away from each other or completely
                # different moves
                if newScr[-1][0] == scrSplit[i][0]:
                    # first char is equal --> e.g. R' R --> don't add the new one, but
                    # remove the previous one, as they cancel out each other
                    newScr.pop()
                else:
                    # completely different moves --> we can safely add the current move
                    newScr.append(scrSplit[i])
        # there is no entry in newScr, so we can safely add the move as is
        else:
            newScr.append(scrSplit[i])
    for move in newScr:
        newScrString += move + " "
    return newScrString
#print(doubleMoveRemover("R' R L L'"))