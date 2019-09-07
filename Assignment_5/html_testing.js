function myUnits1() {
  var x = document.getElementById("r1").value;
  document.getElementById("line_1").innerHTML = "You have selected to use " + x + " units";
  document.getElementById("unit1").innerHTML ="(ft)";
  document.getElementById("unit2").innerHTML ="(ft)";
  document.getElementById("unit3").innerHTML ="(ft^3)";
  }
  
function myUnits2() {
  var x = document.getElementById("r2").value;
  document.getElementById("line_1").innerHTML = "You have selected to use " + x + " units";
   document.getElementById("unit1").innerHTML ="(m)";
  document.getElementById("unit2").innerHTML ="(m)";
  document.getElementById("unit3").innerHTML ="(m^3)";
  }  

function myShape() {
  document.getElementById("v").innerHTML = 0;
  var x = document.getElementById("mySelect").value;
  document.getElementById("line_2").innerHTML = "You have selected to find the values for a " + x + " shape";
  document.getElementById("s").innerHTML =x;
}
function myRadius() {
  document.getElementById("v").innerHTML = 0;
  var x = document.getElementById("radius").value;
  document.getElementById("r").innerHTML = x;
}
function myHeight() {
  document.getElementById("v").innerHTML = 0;
  var x = document.getElementById("height").value;
  document.getElementById("h").innerHTML = x;
}
function myVolume() {
  var ch = document.getElementById("mySelect").value;
  var r = document.getElementById("radius").value;
  var h = document.getElementById("height").value;
if(ch=="Sphere")
{var v=4/3*3.1416*r*r*r;
document.getElementById("h").innerHTML = 0;
document.getElementById("v").innerHTML = v;}
else if(ch=="Cylinder")
{var v=3.1416*r*r*h;
document.getElementById("v").innerHTML = v;}
else
{var v=1/3*3.1416*r*r*h;
document.getElementById("v").innerHTML = v;}
}
function myReset() {
document.getElementById("line_1").innerHTML = "You have selected to use English units";
document.getElementById("line_2").innerHTML = "You have selected to find the values for a Cone shape";
document.getElementById("s").innerHTML ="Cone";
document.getElementById("unit1").innerHTML ="(ft)";
document.getElementById("unit2").innerHTML ="(ft)";
document.getElementById("unit3").innerHTML ="(ft^3)";
document.getElementById("r").innerHTML = 0;
document.getElementById("h").innerHTML = 0;
document.getElementById("v").innerHTML = 0;
}