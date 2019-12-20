# this module can convert Rubiksskewb algs to WCA notation, given that the algs use the moves
# specified down below

# the two algs as in SkewbSkills itself to swap three or four stickers cyclically
# each permutation is split up into transpositions of pairs


def threeswap(listname, i, j, k):

    # cycles three elements i,j,k of a given list by performing two transpositions
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]


def fourswap(listname, i, j, k, l):

    # same as threeswap, but cycles four elements i,j,k,l, which needs three transpositions
    listname[k], listname[l] = listname[l], listname[k]
    listname[j], listname[k] = listname[k], listname[j]
    listname[i], listname[j] = listname[j], listname[i]

# the main function to perform the transposition to WCA scrambles which needs the previous ones
# so it must follow them


def transftoWCA(scr):
    # define list carrying all stickers of the skewb and the color that is placed there initially

    # note that for this subprogram of SkewbSkills, we only need the centers and can therefore
    # use arbitrary letters for all other facelets

    # might be improved in the future so that there are only 6 elements in the list
    # but right know it does not matter (we only have to do it once and never again, in principle)
    stickercol = ["o", "a", "a", "a", "a", "g", "a", "a", "a", "a", "y", "a", "a", "a", "a",
                  "w", "a", "a", "a", "a", "r", "a", "a", "a", "a", "b", "a", "a", "a", "a"]

    # define a string carrying the WCA notation scramble
    finalscr = ""

    # split the scramble sequence into distinct moves (default split character space)
    scrsplit = scr.split()

    # store all the cycled centers (as in: all permutations of three centers) in one list
    allcycles = []

    # go through all elements (moves) and find out what centers they permute
    for i in scrsplit:
        # ensure we can compare the current with previous list
        previous = stickercol.copy()

        # for each move, store the permuted centers
        thecycledcolors = []

        # use a lighter version of the code in MainWindow.py, so just permute centers as they are
        # sufficient to describe the notation (abbreviations for moves) or in other words the
        # centers implicate unambiguous move sequence
        if i == "x":
            fourswap(stickercol, 15, 25, 10, 5)

        elif i == "x'":
            fourswap(stickercol, 5, 10, 25, 15)

        elif i == "x2":
            fourswap(stickercol, 5, 10, 25, 15)
            fourswap(stickercol, 5, 10, 25, 15)

        elif i == "y":
            fourswap(stickercol, 25, 20, 5, 0)

        elif i == "y'":
            fourswap(stickercol, 0, 5, 20, 25)

        elif i == "y2":
            fourswap(stickercol, 0, 5, 20, 25)
            fourswap(stickercol, 0, 5, 20, 25)

        elif i == "z":
            fourswap(stickercol, 15, 20, 10, 0)

        elif i == "z'":
            fourswap(stickercol, 0, 10, 20, 15)

        elif i == "z2":
            fourswap(stickercol, 0, 10, 20, 15)
            fourswap(stickercol, 0, 10, 20, 15)

        elif i == "r" or i == "r'2":
            threeswap(stickercol, 10, 20, 25)

        elif i == "r'" or i == "r2":
            threeswap(stickercol, 25, 20, 10)

        elif i == "R" or i == "R'2":
            threeswap(stickercol, 15, 25, 20)

        elif i == "R'" or i == "R2":
            threeswap(stickercol, 20, 25, 15)

        elif i == "l" or i == "L" or i == "l'2" or i == "L'2":
            threeswap(stickercol, 0, 5, 10)

        elif i == "l'" or i == "L'" or i == "l2" or i == "L2":
            threeswap(stickercol, 10, 5, 0)

        elif i == "f" or i == "f'2":
            threeswap(stickercol, 5, 20, 10)

        elif i == "f'" or i == "f2":
            threeswap(stickercol, 10, 20, 5)

        elif i == "B" or i == "U" or i == "B'2" or i == "U'2":
            threeswap(stickercol, 0, 25, 15)

        elif i == "B'" or i == "U'" or i == "B2" or i == "U2":
            threeswap(stickercol, 15, 25, 0)

        elif i == "b" or i == "b'2":
            threeswap(stickercol, 0, 10, 25)

        else:
            threeswap(stickercol, 25, 10, 0)

        # "read the previous" "compare with current" only if i = real move (no rotations)

        if i not in ("x", "x'", "x2", "y", "y'", "y2", "z", "z'", "z2"):
            # check all centers (if they changed or not)
            for j in (0, 5, 10, 15, 20, 25):
                if previous[j] == stickercol[j]:
                    continue
                else:
                    # store the previous and the current color
                    thecycledcolors.append([previous[j], stickercol[j]])
            # after all centers have been checked, store the list of the three varied centers
            # in one bigger list
            allcycles.append(thecycledcolors)

            # whole process is repeated for all moves in the Rubiksskewb notation scramble sequence

    # print("The cycles made by the non-WCA scramble, containing previous and current color: ", allcycles)

    # find out the WCA moves that permute the exact same 3-tuples of centers

    # store the corresponding permuted INDICES for each move; find out, beginning
    # with the initial state, which INDICES need to be permuted with each move
    # for that: transform the cycle of colors to a cycle of indices (knowing where the three cycled
    # colors were in the previous and the current stickercol list is necessary, and then you go
    # back to their indices)

    # go through all the cycled centers
    # move them either directly (rather: their indices) with WCA moves
    # or move the opposite indices with WCA moves

    # find the indices on the WCA skewb, starting with the initial = solved state

    stickercolWCA = ["o", "a", "a", "a", "a", "g", "a", "a", "a", "a", "y", "a", "a", "a", "a",
                     "w", "a", "a", "a", "a", "r", "a", "a", "a", "a", "b", "a", "a", "a", "a"]

    # go through all real moves changing three centers
    for o in range(len(allcycles)):
        # find out the indices of the three premuted colors on the WCA-scrambled cube
        # for this I take the two colors of the first entry (one transposition) and find the
        # third one by checking if the remaining entrys are already covered by the variables
        # "first" and "second" or not -> then I use the third and last color that is affected
        # by the move
        first = stickercolWCA.index(allcycles[o][0][1])
        second = stickercolWCA.index(allcycles[o][0][0])
        if (stickercolWCA.index(allcycles[o][1][0]) == first) \
            or (stickercolWCA.index(allcycles[o][1][0]) == second):
            third = stickercolWCA.index(allcycles[o][2][0])
        else:
            third = stickercolWCA.index(allcycles[o][1][0])

        # just for convenience and to check what's going on, I print the three indices as a tuple
        #print(first, second, third)

        # find out which WCA move corresponds to the permuted centers (or if this is not possible,
        # I check if the permuted centers are opposite to the normally affected centers by
        # standard WCA moves)

        # in either case, print the corresponding WCA move and swap the corresponding centers
        # to proceed with the next real move
        if ((first, second, third) in ((20,25,10),(25,10,20),(10,20,25),
                                      (0,15,5),(15,5,0),(5,0,15))):
            finalscr += "R "
            threeswap(stickercolWCA, 10, 20, 25)
        elif ((first, second, third) in ((10,25,20),(20,10,25),(25,20,10),
                                      (5,15,0),(0,5,15),(15,0,5))):
            finalscr += "R' "
            threeswap(stickercolWCA, 25, 20, 10)
        elif ((first, second, third) in ((0,5,10),(5,10,0),(10,0,5),
                                      (15,25,20),(25,20,15),(20,15,25))):
            finalscr += "L "
            threeswap(stickercolWCA, 0, 5, 10)
        elif (first, second, third) in ((10,5,0),(0,10,5),(5,0,10),
                                      (20,25,15),(15,20,25),(25,15,20)):
            finalscr += "L' "
            threeswap(stickercolWCA, 10, 5, 0)
        elif (first, second, third) in ((15,0,25),(0,25,15),(25,15,0),
                                      (5,20,10),(20,10,5),(10,5,20)):
            finalscr += "U "
            threeswap(stickercolWCA, 0, 25, 15)
        elif (first, second, third) in ((25,0,15),(15,25,0),(0,15,25),
                                      (10,20,5),(5,10,20),(20,5,10)):
            finalscr += "U' "
            threeswap(stickercolWCA, 15, 25, 0)
        elif (first, second, third) in ((25,0,10),(0,10,25),(10,25,0),
                                      (15,20,5),(20,5,15),(5,15,20)):
            finalscr += "B "
            threeswap(stickercolWCA, 0, 10, 25)
        elif (first, second, third) in ((10,0,25),(25,10,0),(0,25,10),
                                      (5,20,15),(15,5,20),(20,15,5)):
            finalscr += "B' "
            threeswap(stickercolWCA, 25, 10, 0)

    return(finalscr)


# call the function by putting in a Rubiksskewb scramble sequence as a string


#print(transftoWCA("r R' r' B' r R r' B"))


