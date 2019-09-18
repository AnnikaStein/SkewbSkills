// show or hide the corresponding div's
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

// show or hide all alg sets available
function toggleSelectAlgs() {
  var x = document.getElementById("selectAlgs");
  if (x.style.display === "none") {
    x.style.display = "block";
  } else {
    x.style.display = "none";
  }
}

// select multiple alg sets at once or unselect them
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
     changescrlenAlg();
}
function whattodowithi() {
     if (document.getElementById("pi3s").checked == false
     || document.getElementById("pihu").checked == false
     || document.getElementById("pihz").checked == false
     || document.getElementById("pio").checked == false
     || document.getElementById("piswirl").checked == false
     || document.getElementById("pivu").checked == false
     || document.getElementById("piwat").checked == false
     || document.getElementById("pix").checked == false
     || document.getElementById("pizconj").checked == false) {
        document.getElementById("pi3s").checked = true;
        document.getElementById("pihu").checked = true;
        document.getElementById("pihz").checked = true;
        document.getElementById("pio").checked = true;
        document.getElementById("piswirl").checked = true;
        document.getElementById("pivu").checked = true;
        document.getElementById("piwat").checked = true;
        document.getElementById("pix").checked = true;
        document.getElementById("pizconj").checked = true;
     } else {
        document.getElementById("pi3s").checked = false;
        document.getElementById("pihu").checked = false;
        document.getElementById("pihz").checked = false;
        document.getElementById("pio").checked = false;
        document.getElementById("piswirl").checked = false;
        document.getElementById("pivu").checked = false;
        document.getElementById("piwat").checked = false;
        document.getElementById("pix").checked = false;
        document.getElementById("pizconj").checked = false;
     }
     changescrlenAlg();
}
function whattodowithu() {
     if (document.getElementById("p3s").checked == false
     || document.getElementById("phu").checked == false
     || document.getElementById("phzpure").checked == false
     || document.getElementById("po").checked == false
     || document.getElementById("pswirl").checked == false
     || document.getElementById("pvu").checked == false
     || document.getElementById("pwat").checked == false
     || document.getElementById("px").checked == false
     || document.getElementById("pzconj").checked == false) {
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
     changescrlenAlg();
}
function whattodowithl() {
     if (document.getElementById("l4c").checked == false
     || document.getElementById("l5c").checked == false) {
        document.getElementById("l4c").checked = true;
        document.getElementById("l5c").checked = true;
     } else {
        document.getElementById("l4c").checked = false;
        document.getElementById("l5c").checked = false;
     }
     changescrlenAlg();
}

// produces all scrambles for the first layer / saves the L2L algs as arrays
var posschars = ["R", "R'", "L", "L'", "U", "U'", "B", "B'"];
// onemovers
var newscramble1list = [];
for (var i = 0; i < posschars.length; i++) {
    newscramble1list.push(posschars[i]);
}
var scramblelist = newscramble1list.slice(0);

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
        if ((newscramble2list[j]).charAt(newscramble2list[j].length - 2) == " ") {
            if ((newscramble2list[j]).charAt(newscramble2list[j].length - 1) == (posschars[i]).charAt(0)) {
                continue;
            }
        } else {
            if ((newscramble2list[j]).charAt(newscramble2list[j].length - 2) == (posschars[i]).charAt(0)) {
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
        if ((newscramble3list[j]).charAt(newscramble3list[j].length - 2) == " ") {
            if ((newscramble3list[j]).charAt(newscramble3list[j].length - 1) == (posschars[i]).charAt(0)) {
                continue;
            }
        } else {
            if ((newscramble3list[j]).charAt(newscramble3list[j].length - 2) == (posschars[i]).charAt(0)) {
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
        if ((newscramble4list[j]).charAt(newscramble4list[j].length - 2) == " ") {
            if ((newscramble4list[j]).charAt(newscramble4list[j].length - 1) == (posschars[i]).charAt(0)) {
                continue;
            }
        } else {
            if ((newscramble4list[j]).charAt(newscramble4list[j].length - 2) == (posschars[i]).charAt(0)) {
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
        if ((newscramble5list[j]).charAt(newscramble5list[j].length - 2) == " ") {
            if ((newscramble5list[j]).charAt(newscramble5list[j].length - 1) == (posschars[i]).charAt(0)) {
                continue;
            }
        } else {
            if ((newscramble5list[j]).charAt(newscramble5list[j].length - 2) == (posschars[i]).charAt(0)) {
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
        if ((newscramble6list[j]).charAt(newscramble6list[j].length - 2) == " ") {
            if ((newscramble6list[j]).charAt(newscramble6list[j].length - 1) == (posschars[i]).charAt(0)) {
                continue;
            }
        } else {
            if ((newscramble6list[j]).charAt(newscramble6list[j].length - 2) == (posschars[i]).charAt(0)) {
                continue;
            }
        }
        newscramble7list.push(newscramble6list[j]+" "+posschars[i]);
    }
}
// read L2L scrambles
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

// (de/in-)crement the number of moves for the first layer trainer scrambles
function decrMoves() {
    var scrlen = parseInt(document.getElementById("scrlenlabel").innerHTML);
    if (scrlen > 1) {
        scrlen -= 1;
        document.getElementById("scrlenlabel").innerHTML = scrlen;
        changescrlen();
    }
}
function incrMoves() {
    var scrlen = parseInt(document.getElementById("scrlenlabel").innerHTML);
    if (scrlen < 7) {
        scrlen += 1;
        document.getElementById("scrlenlabel").innerHTML = scrlen;
        changescrlen();
    }
}

// when a change of the selected algs has been made by (un-)selecting a set or a whole bunch of sets
// change the style of the toggle buttons and save the correct combination of scrambles as auxscrl
// shuffle them and save them as the scramblelist to be used in further functions
function changescrlen() {
    var scrlen = parseInt(document.getElementById("scrlenlabel").innerHTML);

    if (scrlen === 1) {
        var auxscr1 = newscramble1list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr1);
            scramblelist = auxscr1;
        } else {
            scramblelist = auxscr1;
        }
    }
    if (scrlen === 2) {
        var auxscr2 = newscramble2list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr2);
            scramblelist = auxscr2;
        } else {
            scramblelist = auxscr2;
        }
    }
    if (scrlen === 3) {
        var auxscr3 = newscramble3list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr3);
            scramblelist = auxscr3;
        } else {
            scramblelist = auxscr3;
        }
    }
    if (scrlen === 4) {
        var auxscr4 = newscramble4list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr4);
            scramblelist = auxscr4;
        } else {
            scramblelist = auxscr4;
        }
    }
    if (scrlen === 5) {
        var auxscr5 = newscramble5list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr5);
            scramblelist = auxscr5;
        } else {
            scramblelist = auxscr5;
        }
    }
    if (scrlen === 6) {
        var auxscr6 = newscramble6list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr6);
            scramblelist = auxscr6;
        } else {
            scramblelist = auxscr6;
        }
    }
    if (scrlen === 7) {
        var auxscr7 = newscramble7list.slice(0);
        if (document.getElementById("shufflescrchecker").checked === true) {
            shuffle(auxscr7);
            scramblelist = auxscr7;
        } else {
            scramblelist = auxscr7;
        }
    }
}
function changescrlenAlg() {
    // style of the buttons according to the
    // states of the checkboxes
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
        document.getElementById("toggleAll").style.color = 'black';
    } else {
        document.getElementById("toggleAll").style.color = 'green';

     }
    if (document.getElementById("pi3s").checked == false
     || document.getElementById("pihu").checked == false
     || document.getElementById("pihz").checked == false
     || document.getElementById("pio").checked == false
     || document.getElementById("piswirl").checked == false
     || document.getElementById("pivu").checked == false
     || document.getElementById("piwat").checked == false
     || document.getElementById("pix").checked == false
     || document.getElementById("pizconj").checked == false) {
        document.getElementById("togglePi").style.color = 'black';
    } else {
        document.getElementById("togglePi").style.color = 'green';

     }
    if (document.getElementById("p3s").checked == false
     || document.getElementById("phu").checked == false
     || document.getElementById("phzpure").checked == false
     || document.getElementById("po").checked == false
     || document.getElementById("pswirl").checked == false
     || document.getElementById("pvu").checked == false
     || document.getElementById("pwat").checked == false
     || document.getElementById("px").checked == false
     || document.getElementById("pzconj").checked == false) {
        document.getElementById("togglePeanut").style.color = 'black';
    } else {
        document.getElementById("togglePeanut").style.color = 'green';

     }
    if (document.getElementById("l4c").checked == false
     || document.getElementById("l5c").checked == false) {
        document.getElementById("toggleL").style.color = 'black';
    } else {
        document.getElementById("toggleL").style.color = 'green';

     }

    // get the correct scrambles
    var auxscrl = [];
    if (document.getElementById("l4c").checked == false
     && document.getElementById("l5c").checked == false
     && document.getElementById("pi3s").checked == false
     && document.getElementById("pihu").checked == false
     && document.getElementById("pihz").checked == false
     && document.getElementById("pio").checked == false
     && document.getElementById("piswirl").checked == false
     && document.getElementById("pivu").checked == false
     && document.getElementById("piwat").checked == false
     && document.getElementById("pix").checked == false
     && document.getElementById("pizconj").checked == false
     && document.getElementById("p3s").checked == false
     && document.getElementById("phu").checked == false
     && document.getElementById("phzpure").checked == false
     && document.getElementById("po").checked == false
     && document.getElementById("pswirl").checked == false
     && document.getElementById("pvu").checked == false
     && document.getElementById("pwat").checked == false
     && document.getElementById("px").checked == false
     && document.getElementById("pzconj").checked == false) {
        auxscrl.push("R R'");
    }
    if (document.getElementById("l4c").checked === true) {
        for (var i = 0; i < scrl4c.length; i++) {
            auxscrl.push((scrl4c.slice(0))[i]);
        }
    }
    if (document.getElementById("l5c").checked === true) {
        for (var i = 0; i < scrl5c.length; i++) {
            auxscrl.push((scrl5c.slice(0))[i]);
        }
    }
    if (document.getElementById("p3s").checked === true) {
        for (var i = 0; i < scrp3s.length; i++) {
            auxscrl.push((scrp3s.slice(0))[i]);
        }
    }
    if (document.getElementById("phu").checked === true) {
        for (var i = 0; i < scrphu.length; i++) {
            auxscrl.push((scrphu.slice(0))[i]);
        }
    }
    if (document.getElementById("phzpure").checked === true) {
        for (var i = 0; i < scrphzpure.length; i++) {
            auxscrl.push((scrphzpure.slice(0))[i]);
        }
    }
    if (document.getElementById("pi3s").checked === true) {
        for (var i = 0; i < scrpi3s.length; i++) {
            auxscrl.push((scrpi3s.slice(0))[i]);
        }
    }
    if (document.getElementById("pihu").checked === true) {
        for (var i = 0; i < scrpihu.length; i++) {
            auxscrl.push((scrpihu.slice(0))[i]);
        }
    }
    if (document.getElementById("pihz").checked === true) {
        for (var i = 0; i < scrpihz.length; i++) {
            auxscrl.push((scrpihz.slice(0))[i]);
        }
    }
    if (document.getElementById("pio").checked === true) {
        for (var i = 0; i < scrpio.length; i++) {
            auxscrl.push((scrpio.slice(0))[i]);
        }
    }
    if (document.getElementById("piswirl").checked === true) {
        for (var i = 0; i < scrpiswirl.length; i++) {
            auxscrl.push((scrpiswirl.slice(0))[i]);
        }
    }
    if (document.getElementById("pivu").checked === true) {
        for (var i = 0; i < scrpivu.length; i++) {
            auxscrl.push((scrpivu.slice(0))[i]);
        }
    }
    if (document.getElementById("piwat").checked === true) {
        for (var i = 0; i < scrpiwat.length; i++) {
            auxscrl.push((scrpiwat.slice(0))[i]);
        }
    }
    if (document.getElementById("pix").checked === true) {
        for (var i = 0; i < scrpix.length; i++) {
            auxscrl.push((scrpix.slice(0))[i]);
        }
    }
    if (document.getElementById("pizconj").checked === true) {
        for (var i = 0; i < scrpizconj.length; i++) {
            auxscrl.push((scrpizconj.slice(0))[i]);
        }
    }
    if (document.getElementById("po").checked === true) {
        for (var i = 0; i < scrpo.length; i++) {
            auxscrl.push((scrpo.slice(0))[i]);
        }
    }
    if (document.getElementById("pswirl").checked === true) {
        for (var i = 0; i < scrpswirl.length; i++) {
            auxscrl.push((scrpswirl.slice(0))[i]);
        }
    }
    if (document.getElementById("pvu").checked === true) {
        for (var i = 0; i < scrpvu.length; i++) {
            auxscrl.push((scrpvu.slice(0))[i]);
        }
    }
    if (document.getElementById("pwat").checked === true) {
        for (var i = 0; i < scrpwat.length; i++) {
            auxscrl.push((scrpwat.slice(0))[i]);
        }
    }
    if (document.getElementById("px").checked === true) {
        for (var i = 0; i < scrpx.length; i++) {
            auxscrl.push((scrpx.slice(0))[i]);
        }
    }
    if (document.getElementById("pzconj").checked === true) {
        for (var i = 0; i < scrpzconj.length; i++) {
            auxscrl.push((scrpzconj.slice(0))[i]);
        }
    }
    shuffle(auxscrl);
    scramblelistAlg = auxscrl;
}

// grab new scrambles when button is clicked, if array is empty, get new ones; write scramble and
// colour into corresponding labels
function ScramblePlusColour() {
    if (scramblelist.length == 0) {
        changescrlen();
    }

    var scramblezumanzeigen = scramblelist[scramblelist.length - 1];
    scramblelist.pop();
    document.getElementById("scramblelabel").innerHTML = scramblezumanzeigen;

    ShowScramble(scramblezumanzeigen);

    if (document.getElementById("anycolourchecker").checked === true) {
        var cl = ["w", "y", "g", "r", "b", "o"][Math.floor(Math.random() * 6)];
        if (cl === "w") {
            document.getElementById("colourlabel").style.background = 'white';
        } else if (cl === "y") {
            document.getElementById("colourlabel").style.background = 'yellow';
        } else if(cl === "g") {
            document.getElementById("colourlabel").style.background = 'green';
        } else if(cl === "r") {
            document.getElementById("colourlabel").style.background = 'red';
        } else if(cl === "b") {
            document.getElementById("colourlabel").style.background = 'blue';
        } else {
            document.getElementById("colourlabel").style.background = 'orange';
        }
    } else {
        document.getElementById("colourlabel").style.background = 'white';
    }
}
function ScramblePlusColourAlg() {
    if (scramblelistAlg.length == 0) {
        changescrlenAlg();
    }

    var scramblezumanzeigenAlg = scramblelistAlg[scramblelistAlg.length - 1];
    scramblelistAlg.pop();
    document.getElementById("scramblelabelAlg").innerHTML = scramblezumanzeigenAlg;

    ShowScramble(scramblezumanzeigenAlg);
}

// manipulates the initial order of coloured stickers, assigns swaps to moves, displays polygons
// filled with the correct colours
function ShowScramble(scramble) {
    const stickercol = ["o", "o", "o", "o", "o", "g", "g", "g", "g", "g", "y", "y", "y", "y", "y",
                      "w", "w", "w", "w", "w", "r", "r", "r", "r", "r", "b", "b", "b", "b", "b"];
    var scrsplit = scramble.split(" ");
    if (document.getElementById("AlgT").style.display == "block") {
        for (var i = 0; i < scrsplit.length; i++) {
            if (scrsplit[i] == "x") {
                fourswap(stickercol, 15, 25, 10, 5);
                fourswap(stickercol, 24, 21, 22, 23);
                fourswap(stickercol, 2, 1, 4, 3);
                fourswap(stickercol, 17, 29, 12, 7);
                fourswap(stickercol, 6, 16, 28, 11);
                fourswap(stickercol, 9, 19, 27, 14);
                fourswap(stickercol, 18, 26, 13, 8);
            } else if (scrsplit[i] == "x'") {
                fourswap(stickercol, 5, 10, 25, 15);
                fourswap(stickercol, 23, 22, 21, 24);
                fourswap(stickercol, 3, 4, 1, 2);
                fourswap(stickercol, 7, 12, 29, 17);
                fourswap(stickercol, 11, 28, 16, 6);
                fourswap(stickercol, 14, 27, 19, 9);
                fourswap(stickercol, 8, 13, 26, 18);
            } else if (scrsplit[i] == "x2") {
                fourswap(stickercol, 5, 10, 25, 15);
                fourswap(stickercol, 23, 22, 21, 24);
                fourswap(stickercol, 3, 4, 1, 2);
                fourswap(stickercol, 7, 12, 29, 17);
                fourswap(stickercol, 11, 28, 16, 6);
                fourswap(stickercol, 14, 27, 19, 9);
                fourswap(stickercol, 8, 13, 26, 18);
                fourswap(stickercol, 5, 10, 25, 15);
                fourswap(stickercol, 23, 22, 21, 24);
                fourswap(stickercol, 3, 4, 1, 2);
                fourswap(stickercol, 7, 12, 29, 17);
                fourswap(stickercol, 11, 28, 16, 6);
                fourswap(stickercol, 14, 27, 19, 9);
                fourswap(stickercol, 8, 13, 26, 18);
            } else if (scrsplit[i] == "y") {
                fourswap(stickercol, 19, 16, 17, 18);
                fourswap(stickercol, 14, 13, 12, 11);
                fourswap(stickercol, 25, 20, 5, 0);
                fourswap(stickercol, 21, 6, 1, 26);
                fourswap(stickercol, 29, 24, 9, 4);
                fourswap(stickercol, 23, 8, 3, 28);
                fourswap(stickercol, 27, 22, 7, 2);
            } else if (scrsplit[i] == "y'") {
                fourswap(stickercol, 18, 17, 16, 19);
                fourswap(stickercol, 11, 12, 13, 14);
                fourswap(stickercol, 0, 5, 20, 25);
                fourswap(stickercol, 26, 1, 6, 21);
                fourswap(stickercol, 4, 9, 24, 29);
                fourswap(stickercol, 28, 3, 8, 23);
                fourswap(stickercol, 2, 7, 22, 27);
            } else if (scrsplit[i] == "y'") {
                fourswap(stickercol, 18, 17, 16, 19);
                fourswap(stickercol, 11, 12, 13, 14);
                fourswap(stickercol, 0, 5, 20, 25);
                fourswap(stickercol, 26, 1, 6, 21);
                fourswap(stickercol, 4, 9, 24, 29);
                fourswap(stickercol, 28, 3, 8, 23);
                fourswap(stickercol, 2, 7, 22, 27);
                fourswap(stickercol, 18, 17, 16, 19);
                fourswap(stickercol, 11, 12, 13, 14);
                fourswap(stickercol, 0, 5, 20, 25);
                fourswap(stickercol, 26, 1, 6, 21);
                fourswap(stickercol, 4, 9, 24, 29);
                fourswap(stickercol, 28, 3, 8, 23);
                fourswap(stickercol, 2, 7, 22, 27);
            } else if (scrsplit[i] == "z") {
                fourswap(stickercol, 15, 20, 10, 0);
                fourswap(stickercol, 9, 6, 7, 8);
                fourswap(stickercol, 29, 28, 27, 26);
                fourswap(stickercol, 18, 24, 11, 2);
                fourswap(stickercol, 17, 23, 14, 1);
                fourswap(stickercol, 19, 21, 12, 3);
                fourswap(stickercol, 16, 22, 13, 4);
            } else if (scrsplit[i] == "z'") {
                fourswap(stickercol, 0, 10, 20, 15);
                fourswap(stickercol, 8, 7, 6, 9);
                fourswap(stickercol, 26, 27, 28, 29);
                fourswap(stickercol, 2, 11, 24, 18);
                fourswap(stickercol, 1, 14, 23, 17);
                fourswap(stickercol, 3, 12, 21, 19);
                fourswap(stickercol, 4, 13, 22, 16);
            } else if (scrsplit[i] == "z2") {
                fourswap(stickercol, 0, 10, 20, 15);
                fourswap(stickercol, 8, 7, 6, 9);
                fourswap(stickercol, 26, 27, 28, 29);
                fourswap(stickercol, 2, 11, 24, 18);
                fourswap(stickercol, 1, 14, 23, 17);
                fourswap(stickercol, 3, 12, 21, 19);
                fourswap(stickercol, 4, 13, 22, 16);
                fourswap(stickercol, 0, 10, 20, 15);
                fourswap(stickercol, 8, 7, 6, 9);
                fourswap(stickercol, 26, 27, 28, 29);
                fourswap(stickercol, 2, 11, 24, 18);
                fourswap(stickercol, 1, 14, 23, 17);
                fourswap(stickercol, 3, 12, 21, 19);
                fourswap(stickercol, 4, 13, 22, 16);
            } else if (scrsplit[i] == "r" || scrsplit[i] == "r'2") {
                threeswap(stickercol, 3, 7, 16);
                threeswap(stickercol, 10, 20, 25);
                threeswap(stickercol, 11, 21, 27);
                threeswap(stickercol, 12, 22, 28);
                threeswap(stickercol, 13, 23, 29);
             } else if (scrsplit[i] == "r'" || scrsplit[i] == "r2") {
                threeswap(stickercol, 16, 7, 3);
                threeswap(stickercol, 25, 20, 10);
                threeswap(stickercol, 27, 21, 11);
                threeswap(stickercol, 28, 22, 12);
                threeswap(stickercol, 29, 23, 13);
            } else if (scrsplit[i] == "R" || scrsplit[i] == "R'2") {
                threeswap(stickercol, 15, 25, 20);
                threeswap(stickercol, 16, 29, 21);
                threeswap(stickercol, 17, 26, 22);
                threeswap(stickercol, 24, 19, 28);
                threeswap(stickercol, 6, 4, 12);
            } else if (scrsplit[i] == "R'" || scrsplit[i] == "R2") {
                threeswap(stickercol, 20, 25, 15);
                threeswap(stickercol, 21, 29, 16);
                threeswap(stickercol, 22, 26, 17);
                threeswap(stickercol, 28, 19, 24);
                threeswap(stickercol, 12, 4, 6);
            } else if (scrsplit[i] == "l" || scrsplit[i] == "L" || scrsplit[i] == "l'2" || scrsplit[i] == "L'2") {
                threeswap(stickercol, 0, 5, 10);
                threeswap(stickercol, 1, 7, 13);
                threeswap(stickercol, 2, 8, 14);
                threeswap(stickercol, 3, 9, 11);
                threeswap(stickercol, 18, 23, 27);
            } else if (scrsplit[i] == "l'" || scrsplit[i] == "L'" || scrsplit[i] == "l2" || scrsplit[i] == "L2") {
                threeswap(stickercol, 10, 5, 0);
                threeswap(stickercol, 13, 7, 1);
                threeswap(stickercol, 14, 8, 2);
                threeswap(stickercol, 11, 9, 3);
                threeswap(stickercol, 27, 23, 18);
            } else if (scrsplit[i] == "f" || scrsplit[i] == "f'2") {
                threeswap(stickercol, 5, 20, 10);
                threeswap(stickercol, 7, 23, 11);
                threeswap(stickercol, 17, 28, 2);
                threeswap(stickercol, 24, 12, 8);
                threeswap(stickercol, 6, 22, 14);
            } else if (scrsplit[i] == "f'" || scrsplit[i] == "f2") {
                threeswap(stickercol, 10, 20, 5);
                threeswap(stickercol, 11, 23, 7);
                threeswap(stickercol, 2, 28, 17);
                threeswap(stickercol, 8, 12, 24);
                threeswap(stickercol, 14, 22, 6);
            } else if (scrsplit[i] == "B" || scrsplit[i] == "U" || scrsplit[i] == "B'2" || scrsplit[i] == "U'2") {
                threeswap(stickercol, 0, 25, 15);
                threeswap(stickercol, 1, 27, 16);
                threeswap(stickercol, 3, 29, 18);
                threeswap(stickercol, 4, 26, 19);
                threeswap(stickercol, 9, 13, 21);
            } else if (scrsplit[i] == "B'" || scrsplit[i] == "U'" || scrsplit[i] == "B2" || scrsplit[i] == "U2") {
                threeswap(stickercol, 15, 25, 0);
                threeswap(stickercol, 16, 27, 1);
                threeswap(stickercol, 18, 29, 3);
                threeswap(stickercol, 19, 26, 4);
                threeswap(stickercol, 21, 13, 9);
            } else if (scrsplit[i] == "b" || scrsplit[i] == "b'2") {
                threeswap(stickercol, 0, 10, 25);
                threeswap(stickercol, 2, 12, 26);
                threeswap(stickercol, 3, 13, 27);
                threeswap(stickercol, 4, 14, 28);
                threeswap(stickercol, 8, 22, 19);
            } else {
                threeswap(stickercol, 25, 10, 0);
                threeswap(stickercol, 26, 12, 2);
                threeswap(stickercol, 27, 13, 3);
                threeswap(stickercol, 28, 14, 4);
                threeswap(stickercol, 19, 22, 8);
            }
        }
    } else {
        for (var i = 0; i < scrsplit.length; i++) {
            if (scrsplit[i] == "R") {
                threeswap(stickercol, 3, 7, 16);
                threeswap(stickercol, 10, 20, 25);
                threeswap(stickercol, 11, 21, 27);
                threeswap(stickercol, 12, 22, 28);
                threeswap(stickercol, 13, 23, 29);
             } else if (scrsplit[i] == "R'") {
                threeswap(stickercol, 16, 7, 3);
                threeswap(stickercol, 25, 20, 10);
                threeswap(stickercol, 27, 21, 11);
                threeswap(stickercol, 28, 22, 12);
                threeswap(stickercol, 29, 23, 13);
            } else if (scrsplit[i] == "L") {
                threeswap(stickercol, 0, 5, 10);
                threeswap(stickercol, 1, 7, 13);
                threeswap(stickercol, 2, 8, 14);
                threeswap(stickercol, 3, 9, 11);
                threeswap(stickercol, 18, 23, 27);
            } else if (scrsplit[i] == "L'") {
                threeswap(stickercol, 10, 5, 0);
                threeswap(stickercol, 13, 7, 1);
                threeswap(stickercol, 14, 8, 2);
                threeswap(stickercol, 11, 9, 3);
                threeswap(stickercol, 27, 23, 18);
            } else if (scrsplit[i] == "U") {
                threeswap(stickercol, 0, 25, 15);
                threeswap(stickercol, 1, 27, 16);
                threeswap(stickercol, 3, 29, 18);
                threeswap(stickercol, 4, 26, 19);
                threeswap(stickercol, 9, 13, 21);
            } else if (scrsplit[i] == "U'") {
                threeswap(stickercol, 15, 25, 0);
                threeswap(stickercol, 16, 27, 1);
                threeswap(stickercol, 18, 29, 3);
                threeswap(stickercol, 19, 26, 4);
                threeswap(stickercol, 21, 13, 9);
            } else if (scrsplit[i] == "B") {
                threeswap(stickercol, 0, 10, 25);
                threeswap(stickercol, 2, 12, 26);
                threeswap(stickercol, 3, 13, 27);
                threeswap(stickercol, 4, 14, 28);
                threeswap(stickercol, 8, 22, 19);
            } else {
                threeswap(stickercol, 25, 10, 0);
                threeswap(stickercol, 26, 12, 2);
                threeswap(stickercol, 27, 13, 3);
                threeswap(stickercol, 28, 14, 4);
                threeswap(stickercol, 19, 22, 8);
            }
        }
    }

    if (document.getElementById("AlgT").style.display == "block") {
        var canvas = document.getElementById("scrDrawingAlg");
    } else {
        var canvas = document.getElementById("scrDrawing");
    }
    var ctx = canvas.getContext('2d');
    ctx.translate(10, 10);
    ctx.strokeStyle = "black";
    ctx.lineWidth = 3;
    ctx.lineJoin = "round";
    ctx.lineCap = "round";
    ctx.fillStyle = corrcol(stickercol, 0);
    ctx.beginPath();
    ctx.moveTo(0.0, 75.0);
    ctx.lineTo(60, 30);
    ctx.lineTo(120, 135);
    ctx.lineTo(60, 180);
    ctx.lineTo(0, 75);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 1);
    ctx.beginPath();
    ctx.moveTo(60, 30);
    ctx.lineTo(120, 135);
    ctx.lineTo(120, 60);
    ctx.lineTo(60, 30);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 2);
    ctx.beginPath();
    ctx.moveTo(120, 135);
    ctx.lineTo(120, 210);
    ctx.lineTo(60, 180);
    ctx.lineTo(120, 135);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 3);
    ctx.beginPath();
    ctx.moveTo(0, 75);
    ctx.lineTo(60, 180);
    ctx.lineTo(0, 150);
    ctx.lineTo(0, 75);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 4);
    ctx.beginPath();
    ctx.moveTo(0, 0);
    ctx.lineTo(60, 30);
    ctx.lineTo(0, 75);
    ctx.lineTo(0, 0);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 5);
    ctx.beginPath();
    ctx.moveTo(120, 135);
    ctx.lineTo(180, 90);
    ctx.lineTo(240, 195);
    ctx.lineTo(180, 240);
    ctx.lineTo(120, 135);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 6);
    ctx.beginPath();
    ctx.moveTo(180, 90);
    ctx.lineTo(240, 120);
    ctx.lineTo(240, 195);
    ctx.lineTo(180, 90);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 7);
    ctx.beginPath();
    ctx.moveTo(240, 195);
    ctx.lineTo(240, 270);
    ctx.lineTo(180, 240);
    ctx.lineTo(240, 195);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 8);
    ctx.beginPath();
    ctx.moveTo(120, 135);
    ctx.lineTo(180, 240);
    ctx.lineTo(120, 210);
    ctx.lineTo(120, 135);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 9);
    ctx.beginPath();
    ctx.moveTo(120, 60);
    ctx.lineTo(180, 90);
    ctx.lineTo(120, 135);
    ctx.lineTo(120, 60);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 10);
    ctx.beginPath();
    ctx.moveTo(180, 240);
    ctx.lineTo(240, 345);
    ctx.lineTo(180, 390);
    ctx.lineTo(120, 285);
    ctx.lineTo(180, 240);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 11);
    ctx.beginPath();
    ctx.moveTo(180, 240);
    ctx.lineTo(240, 270);
    ctx.lineTo(240, 345);
    ctx.lineTo(180, 240);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 12);
    ctx.beginPath();
    ctx.moveTo(240, 345);
    ctx.lineTo(240, 420);
    ctx.lineTo(180, 390);
    ctx.lineTo(240, 345);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 13);
    ctx.beginPath();
    ctx.moveTo(120, 285);
    ctx.lineTo(180, 390);
    ctx.lineTo(120, 360);
    ctx.lineTo(120, 285);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 14);
    ctx.beginPath();
    ctx.moveTo(120, 210);
    ctx.lineTo(180, 240);
    ctx.lineTo(120, 285);
    ctx.lineTo(120, 210);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 15);
    ctx.beginPath();
    ctx.moveTo(180, 90);
    ctx.lineTo(180, 30);
    ctx.lineTo(300, 30);
    ctx.lineTo(300, 90);
    ctx.lineTo(180, 90);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 16);
    ctx.beginPath();
    ctx.moveTo(300, 30);
    ctx.lineTo(360, 60);
    ctx.lineTo(300, 90);
    ctx.lineTo(300, 30);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 17);
    ctx.beginPath();
    ctx.moveTo(180, 90);
    ctx.lineTo(300, 90);
    ctx.lineTo(240, 120);
    ctx.lineTo(180, 90);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 18);
    ctx.beginPath();
    ctx.moveTo(120, 60);
    ctx.lineTo(180, 30);
    ctx.lineTo(180, 90);
    ctx.lineTo(120, 60);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 19);
    ctx.beginPath();
    ctx.moveTo(180, 30);
    ctx.lineTo(240, 0);
    ctx.lineTo(300, 30);
    ctx.lineTo(180, 30);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 20);
    ctx.beginPath();
    ctx.moveTo(240, 195);
    ctx.lineTo(300, 90);
    ctx.lineTo(360, 135);
    ctx.lineTo(300, 240);
    ctx.lineTo(240, 195);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 21);
    ctx.beginPath();
    ctx.moveTo(300, 90);
    ctx.lineTo(360, 60);
    ctx.lineTo(360, 135);
    ctx.lineTo(300, 90);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 22);
    ctx.beginPath();
    ctx.moveTo(300, 240);
    ctx.lineTo(360, 135);
    ctx.lineTo(360, 210);
    ctx.lineTo(300, 240);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 23);
    ctx.beginPath();
    ctx.moveTo(240, 195);
    ctx.lineTo(300, 240);
    ctx.lineTo(240, 270);
    ctx.lineTo(240, 195);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 24);
    ctx.beginPath();
    ctx.moveTo(240, 120);
    ctx.lineTo(300, 90);
    ctx.lineTo(240, 195);
    ctx.lineTo(240, 120);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 25);
    ctx.beginPath();
    ctx.moveTo(360, 135);
    ctx.lineTo(420, 30);
    ctx.lineTo(480, 75);
    ctx.lineTo(420, 180);
    ctx.lineTo(360, 135);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 26);
    ctx.beginPath();
    ctx.moveTo(420, 30);
    ctx.lineTo(480, 0);
    ctx.lineTo(480, 75);
    ctx.lineTo(420, 30);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 27);
    ctx.beginPath();
    ctx.moveTo(420, 180);
    ctx.lineTo(480, 75);
    ctx.lineTo(480, 150);
    ctx.lineTo(420, 180);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 28);
    ctx.beginPath();
    ctx.moveTo(360, 135);
    ctx.lineTo(420, 180);
    ctx.lineTo(360, 210);
    ctx.lineTo(360, 135);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.fillStyle = corrcol(stickercol, 29);
    ctx.beginPath();
    ctx.moveTo(360, 60);
    ctx.lineTo(420, 30);
    ctx.lineTo(360, 135);
    ctx.lineTo(360, 60);
    ctx.closePath();
    ctx.fill();
    ctx.stroke();
    ctx.translate(-10, -10);
}

// permute the selected entries of the list cyclically
function threeswap(listname,i,j,k) {
    [listname[j], listname[k]] = [listname[k], listname[j]];
    [listname[i], listname[j]] = [listname[j], listname[i]];
}
function fourswap(listname,i,j,k,l) {
    [listname[k], listname[l]] = [listname[l], listname[k]];
    [listname[j], listname[k]] = [listname[k], listname[j]];
    [listname[i], listname[j]] = [listname[j], listname[i]];
}

function corrcol(list,i) {
    if (list[i] == "o") {
        return 'orange';
    } else if (list[i] == "g") {
        return 'green';
    } else if (list[i] == "r") {
        return 'red';
    } else if (list[i] == "b") {
        return 'blue';
    } else if (list[i] == "w") {
        return 'white';
    } else {
        return 'yellow';
    }
}

function shuffle(array) {
   for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
  }

// timer
var x;
var startstop = 0;

function startStop() { /* Toggle StartStop */

  startstop = startstop + 1;

  if (startstop === 1) {
    start();
    document.getElementById("start").innerHTML = "Stop";
  } else if (startstop === 2) {
    document.getElementById("start").innerHTML = "Start";
    startstop = 0;
    stop();
  }

}


function start() {
  x = setInterval(timer, 10);
  document.getElementById("reset").style.display = "none";
} /* Start */

function stop() {
  clearInterval(x);
  var stil = getComputedStyle(document.getElementById("start"), null).display;
  if (stil === "inline-block") {
    document.getElementById("reset").style.display = "inline-block";
  } else if (stil === "block") {
    document.getElementById("reset").style.display = "block";
  }
} /* Stop */

var milisec = 0;
var sec = 0; /* holds incrementing value */
var min = 0;

/* Contains and outputs returned value of  function checkTime */

var miliSecOut = 0;
var secOut = 0;
var minOut = 0;

/* Output variable End */

function timer() {
  /* Main Timer */

  miliSecOut = checkTime(milisec);
  secOut = checkTime(sec);
  minOut = checkTime(min);

  milisec = ++milisec;

  if (milisec === 100) {
    milisec = 0;
    sec = ++sec;
  }
  if (sec == 60) {
    min = ++min;
    sec = 0;
  }

  document.getElementById("milisec").innerHTML = miliSecOut;
  document.getElementById("sec").innerHTML = secOut;
  document.getElementById("min").innerHTML = minOut;
}

/* Adds 0 when value is <10 */

function checkTime(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

function reset() {
  /*Reset*/
  milisec = 0;
  sec = 0;
  min = 0

  document.getElementById("milisec").innerHTML = "00";
  document.getElementById("sec").innerHTML = "00";
  document.getElementById("min").innerHTML = "00";
}

// timerAlg
var xAlg;
var startstopAlg = 0;

function startStopAlg() { /* Toggle StartStop */

  startstopAlg = startstopAlg + 1;

  if (startstopAlg === 1) {
    startAlg();
    document.getElementById("startAlg").innerHTML = "Stop";
  } else if (startstopAlg === 2) {
    document.getElementById("startAlg").innerHTML = "Start";
    startstopAlg = 0;
    stopAlg();
  }
}


function startAlg() {
  xAlg = setInterval(timerAlg, 10);
  document.getElementById("resetAlg").style.display = "none";
} /* Start */

function stopAlg() {
  clearInterval(xAlg);
  var stilAlg = getComputedStyle(document.getElementById("startAlg"), null).display;
  if (stilAlg === "inline-block") {
    document.getElementById("resetAlg").style.display = "inline-block";
  } else if (stilAlg === "block") {
    document.getElementById("resetAlg").style.display = "block";
  }
} /* Stop */

var milisecAlg = 0;
var secAlg = 0; /* holds incrementing value */
var minAlg = 0;

/* Contains and outputs returned value of  function checkTime */

var miliSecOutAlg = 0;
var secOutAlg = 0;
var minOutAlg = 0;

/* Output variable End */

function timerAlg() {
  /* Main Timer */

  miliSecOutAlg = checkTimeAlg(milisecAlg);
  secOutAlg = checkTimeAlg(secAlg);
  minOutAlg = checkTimeAlg(minAlg);

  milisecAlg = ++milisecAlg;

  if (milisecAlg === 100) {
    milisecAlg = 0;
    secAlg = ++secAlg;
  }
  if (secAlg == 60) {
    minAlg = ++minAlg;
    secAlg = 0;
  }

  document.getElementById("milisecAlg").innerHTML = miliSecOutAlg;
  document.getElementById("secAlg").innerHTML = secOutAlg;
  document.getElementById("minAlg").innerHTML = minOutAlg;
}

/* Adds 0 when value is <10 */

function checkTimeAlg(i) {
  if (i < 10) {
    i = "0" + i;
  }
  return i;
}

function resetAlg() {
  /*Reset*/
  milisecAlg = 0;
  secAlg = 0;
  minAlg = 0

  document.getElementById("milisecAlg").innerHTML = "00";
  document.getElementById("secAlg").innerHTML = "00";
  document.getElementById("minAlg").innerHTML = "00";
}