ReadAllScrambles()
ReadAllScramblesAlg()

function toggleFLT() {
  var x = document.getElementById("FLT");
  var y = document.getElementById("AlgT");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
  }
}
function toggleAlgT() {
  var x = document.getElementById("AlgT");
  var y = document.getElementById("FLT");
  if (x.style.display === "none") {
    x.style.display = "block";
    y.style.display = "none";
  } else {
    x.style.display = "none";
  }
}
function toggleSelectAlgs() {
  var x = document.getElementById("selectAlgs");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

function whattodowitht() {
     if (document.getElementById("l4c").checked == false
     || document.getElementById("l5c").checked == false
     || document.getElementById("pi3s").checked == false
     || document.getElementById("pihu").checked == false
     || document.getElementById("pihz").checked == false
     || document.getElementById("pio").checked == false
     || document.getElementById("piswirl").checked == false
     || document.getElementById("pivu").checked == false
     || document.getElementById("piwat").checked == false
     || document.getElementById("pix").checked == false
     || document.getElementById("pizconj").checked == false
     || document.getElementById("p3s").checked == false
     || document.getElementById("phu").checked == false
     || document.getElementById("phzpure").checked == false
     || document.getElementById("po").checked == false
     || document.getElementById("pswirl").checked == false
     || document.getElementById("pvu").checked == false
     || document.getElementById("pwat").checked == false
     || document.getElementById("px").checked == false
     || document.getElementById("pzconj").checked == false) {
        document.getElementById("l4c").checked = true;
        document.getElementById("l5c").checked = true;
        document.getElementById("pi3s").checked = true;
        document.getElementById("pihu").checked = true;
        document.getElementById("pihz").checked = true;
        document.getElementById("pio").checked = true;
        document.getElementById("piswirl").checked = true;
        document.getElementById("pivu").checked = true;
        document.getElementById("piwat").checked = true;
        document.getElementById("pix").checked = true;
        document.getElementById("pizconj").checked = true;
        document.getElementById("p3s").checked = true;
        document.getElementById("phu").checked = true;
        document.getElementById("phzpure").checked = true;
        document.getElementById("po").checked = true;
        document.getElementById("pswirl").checked = true;
        document.getElementById("pvu").checked = true;
        document.getElementById("pwat").checked = true;
        document.getElementById("px").checked = true;
        document.getElementById("pzconj").checked = true;
     } else {
        document.getElementById("l4c").checked = false;
        document.getElementById("l5c").checked = false;
        document.getElementById("pi3s").checked = false;
        document.getElementById("pihu").checked = false;
        document.getElementById("pihz").checked = false;
        document.getElementById("pio").checked = false;
        document.getElementById("piswirl").checked = false;
        document.getElementById("pivu").checked = false;
        document.getElementById("piwat").checked = false;
        document.getElementById("pix").checked = false;
        document.getElementById("pizconj").checked = false;
        document.getElementById("p3s").checked = false;
        document.getElementById("phu").checked = false;
        document.getElementById("phzpure").checked = false;
        document.getElementById("po").checked = false;
        document.getElementById("pswirl").checked = false;
        document.getElementById("pvu").checked = false;
        document.getElementById("pwat").checked = false;
        document.getElementById("px").checked = false;
        document.getElementById("pzconj").checked = false;
     }

}

function ReadAllScrambles() {
    var posschars = ["R", "R\'", "L", "L\'", "U", "U\'", "B", "B\'"];
    // onemovers
    var newscramble1list = [];
    for (var i = 0; i < posschars.length; i++) {
        newscramble1list.push(posschars[i]);
    }
    var scramblelist = newscramble1list;

    //twomovers
    var newscramble2list = [];
    for (j = 0; j < newscramble1list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (posschars[i].indexOf(newscramble1list[j]) != -1) {
                continue;
            } else if (newscramble1list[j].indexOf(posschars[i]) != -1) {
                continue;
            } else {
                newscramble2list.push(newscramble1list[j]+" "+posschars[i]);
            }
        }
    }
    //threemovers
    var newscramble3list = [];
    for (j = 0; j < newscramble2list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (newscramble2list[j][-2] == " ") {
                if (newscramble2list[j][-1] == posschars[i][0]) {
                    continue;
                }
            } else {
                if (newscramble2list[j][-2] == posschars[i][0]) {
                    continue;
                }
            }
            newscramble3list.push(newscramble2list[j]+" "+posschars[i]);
        }
    }
    //fourmovers
    var newscramble4list = [];
    for (j = 0; j < newscramble3list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (newscramble3list[j][-2] == " ") {
                if (newscramble3list[j][-1] == posschars[i][0]) {
                    continue;
                }
            } else {
                if (newscramble3list[j][-2] == posschars[i][0]) {
                    continue;
                }
            }
            newscramble4list.push(newscramble3list[j]+" "+posschars[i]);
        }
    }
    //fivemovers
    var newscramble5list = [];
    for (j = 0; j < newscramble4list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (newscramble4list[j][-2] == " ") {
                if (newscramble4list[j][-1] == posschars[i][0]) {
                    continue;
                }
            } else {
                if (newscramble4list[j][-2] == posschars[i][0]) {
                    continue;
                }
            }
            newscramble5list.push(newscramble4list[j]+" "+posschars[i]);
        }
    }
    //sixmovers
    var newscramble6list = [];
    for (j = 0; j < newscramble5list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (newscramble5list[j][-2] == " ") {
                if (newscramble5list[j][-1] == posschars[i][0]) {
                    continue;
                }
            } else {
                if (newscramble5list[j][-2] == posschars[i][0]) {
                    continue;
                }
            }
            newscramble6list.push(newscramble5list[j]+" "+posschars[i]);
        }
    }
    //sevenmovers
    var newscramble7list = [];
    for (j = 0; j < newscramble6list.length; j++) {
        for (i = 0; i < posschars.length; i++) {
            if (newscramble6list[j][-2] == " ") {
                if (newscramble6list[j][-1] == posschars[i][0]) {
                    continue;
                }
            } else {
                if (newscramble6list[j][-2] == posschars[i][0]) {
                    continue;
                }
            }
            newscramble7list.push(newscramble6list[j]+" "+posschars[i]);
        }
    }
}
function ReadAllScramblesAlg() {
    var scrpiswirl = ["r' R' r R' r z' r z r R'",
            "r R r R' z R r' R' r z2 R' r' R' r",
            "R r' b' r' R r' R r",
            "r' B R r R' z R b' R'",
            "R' B R' B' r' R r z R r R'",
            "R r' R r z R r' R' z' r' R' r",
            "r' R r R b' r R' b'",
            "R r R' z R B r' R' r'"];
    var scrpiwat = ["B' R' r R' B' r' R' r'",
            "R' r' R r R B R' B' R' B R B'",
            "r R' r B r' z r R' r' R' r",
            "R r' R' r' R B' r z R r' R",
            "R' r B' r' R r' z R r' R r",
            "r' R' r B' R' z R r' R' r R r'",
            "R' r R' r' B R B' r R r'",
            "r' R r R r' R' r B R B' R"];
    var scrpix = ["R' r R' r' z' r' R' r z R' r",
            "R r' R r z2 R r' R' r b",
            "R r R' r z2 r' R r z r R r",
            "B R r' R' r z2 R r R' r",
            "b R r' R' r z y l r' R r",
            "B' r' R r z r' R' z R r' R'",
            "R r R' r z2 R r' R' r B",
            "r' R' r z r' R' B R B' r'"];
    var scrpihu = ["r B' r' R r R' r f'",
            "R' b R r' R' r R' b",
            "B r' R r' R' r B r'",
            "l' B b' r B r' R' r",
            "r R' r b' B' R r' R",
            "r' R r' B R B' r' R",
            "R' r R' B b r' R r'",
            "r' B R B' z' r' R r B'"];
    var scrpivu = ["R r' R r B' R' B r' R' r",
            "B' r' R r z B R B' r'",
            "R B R r' R' B'",
            "b' r' R' r y r B"];
    var scrpio = ["r' R' r z R r' R' r R r R'",
            "R r R' z' r' R r R' r' R' r",
            "R r' R' r' R r R' z' r' R r",
            "r' R r R r' R' r B R' B'",
            "B' R' r B' r' R r'",
            "r R B' r z R r' R",
            "r R' r B r' R B",
            "R' r R' z' r' B R' r'"];
    var scrpizconj = ["B' r' R' r B r' R r",
            "r B R B' r' B R' B'",
            "B R B' r B R' B' r'",
            "r' R' r B' r' R r B",
            "r' R r R' z R r' R' r z' R r' R' r",
            "r' R r R' z r' R r R' z' R r' R' r",
            "R r' R' r z' r' R r R' z r' R r R'",
            "R r' R' r z' R r' R' r z r' R r R'"];
    var scrpi3s = ["r R' r' z' r' R' r z r R' r' R' r",
            "r' R r R r' z' r' R r z r R r'"];
    var scrpihz = ["R' r' R' r' B R' B' r'",
            "r' R' r z r R r' R' z' r' R r",
            "R r R' z' r' R' r R z R r' R'"];
    var scrpswirl = ["r R r R' z R r' R' r b",
            "b' r' R r R' z' R r' R' r'",
            "R r' R r B' r' R r B",
            "R' r' R' r z R r R' r",
            "r' R' r R' z' R r' R' r B'",
            "R r' R r R' z' R r' R' r B'",
            "r' R r' R' z' r' R r R",
            "R r' R r z R r' R' r'"];
    var scrpwat = ["r R r R' z R r' R' r' z' r R'",
            "r' R r' z' r' R' r z r' R r R",
            "R r B R B' r' R",
            "B R B' r' R r R",
            "r R' B' l r' y r R r'",
            "R' r R z B' b r' R' r",
            "r' R r' R' r' z' r' R' r R",
            "R r' R r R z R r R' r'"];
    var scrpx = ["R r' R' r z' R r' R' r",
            "r' B r' R r R' r' B",
            "r' R r R' z r' R r R'",
            "B' r R r' R' r B' r",
            "r' R' r z' r' R r R' B",
            "B' R r' R' r z r' R r",
            "B' r' R r R' z R r' R' r R",
            "b r' R r R' z' R r' R'"];
    var scrphu = ["r' l r R r' l' r R'",
            "r R' B R r' y' r' R' r",
            "r R' r' B' r R r' B",
            "B' r R' r' B r R r'",
            "R r' z' r' R r z r R r' R",
            "R r R' r' R' z' r' R' r z R r",
            "R r' R' z R r y r R' B R",
            "r R' r z r R r R' r' z' r"];
    var scrpvu = ["r' R r R' z' R r R' r'",
            "R r' R' r z r' R' r R",
            "r R' r' z' r' R' r z r R",
            "R' r R z R r R' z' R' r'"];
    var scrpo = ["r' R' r R z R r R' r'",
            "R r R' r' z' r' R' r R",
            "r R r' R' z' R' r' R r",
            "R' r' R r z r R r' R'",
            "r R B R B' R' r' R'",
            "R r R B R' B' R' r'",
            "R' r' R' r l r' R r",
            "r' R' r z r' R' r R r"];
    var scrpzconj = ["r' R' r z r' R r' R' r R r' R'",
            "R r R' z' R r' R r R' r' R r",
            "R r R' r' R r R' z' R r' R r",
            "r' R' r R r' R' r z r' R r' R'",
            "R r' R' r z R r' R' r z' R r' R' r",
            "R r' R' r z' R r' R' r z R r' R' r",
            "r' R r R' z' r' R r R' z r' R r R'",
            "r' R r R' z r' R r R' z' r' R r R'"];
    var scrp3s = ["r' R r R' r' R r R' z R r' R' r",
            "R r' R' r z' R r' R' r R r' R' r",
            "r' R r R' r' R r R' z r' R r R'",
            "r' R r R' z r' R r R' r' R r R'"];
    var scrphzpure = ["r' R r R' z B R r' R' r B'",
            "R r' R' r z r' R' r x R r R'",
            "r R r' R' z' r' R' r z r' R r' R'",
            "B L' r B' l' r' y r' R' r"];
    var scrl4c = ["r' l r' l' B' l' B l r'",
            "B' r R' B x R r' R r'",
            "R' r' R' r z2 R r' R' r b'",
            "r' R r' R' r z2 R r' R' r B"];
    var scrl5c = ["R' b R r' R' r R' b R r' R' r",
            "r' R B R' r B R' z b' r R'",
            "R' r B' r' R r R' r B' r' R r",
            "r B' r' R r R' r z2 r' R r' R' r",
            "R' r R B' r B R' B r' R r",
            "r' B R r R' B r' z r' R' r"];

    var scramblelistAlg = ["R R'"];
}
// bis hier hin alles ok


// testen ab hier

function decrMoves() {
    var scrlen = parseInt(document.getElementById("scrlenlabel").innerHTML);
    if (scrlen > 1) {
        scrlen -= 1;
        document.getElementById("scrlenlabel").innerHTML = scrlen;
    }
}
function incrMoves() {
    var scrlen = parseInt(document.getElementById("scrlenlabel").innerHTML);
    if (scrlen < 7) {
        scrlen += 1;
        document.getElementById("scrlenlabel").innerHTML = scrlen;
    }
}
/*
function changescrlen() {

}
function changescrlenAlg() {

}
function ScramblePlusColour() {

}
function ScramblePlusColourAlg() {

}
*/
function threeswap(listname,i,j,k) {
    [listname[j], listname[k]] = [listname[k], listname[j]];
    [listname[i], listname[j]] = [listname[j], listname[i]];
}
function fourswap(listname,i,j,k,l) {
    [listname[k], listname[l]] = [listname[l], listname[k]];
    [listname[j], listname[k]] = [listname[k], listname[j]];
    [listname[i], listname[j]] = [listname[j], listname[i]];
}
/* this function uses Qt and should be replaced
function corrcol(list,i) {
    if (list[i] == "o") {
        return //QtGui.QColor( 0xFF, 0x68, 0x00 )
    } else if (list[i] == "g") {
        return //Qt.green
    } else if (list[i] == "r") {
        return //Qt.red
    } else if (list[i] == "b") {
        return //Qt.blue
    } else if (list[i] == "w") {
        return //Qt.white
    } else {
        return //Qt.yellow
    }
}*/