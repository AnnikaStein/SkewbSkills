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
function decrMoves() {

}
function incrMoves() {

}
function changescrlen() {

}
function changescrlenAlg() {

}
function ScramblePlusColour() {

}
function ScramblePlusColourAlg() {

}
