console.log('js')
function loginTypeForm() {
    let regform = document.getElementById("logintypewindow");
    console.log(regform.style.display);
    if (regform.style.display=="none" || regform.style.display=="flex"){
        regform.style.display="block";
    }
    else {
        regform.style.disply="none";
    }
    console.log("form");
}


var expanded = false;

function showCheckboxes1() {
  var checkboxes = document.getElementById("checkboxes1");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
var expanded = false;

function showCheckboxes2() {
  var checkboxes = document.getElementById("checkboxes2");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}
var expanded = false;

function showCheckboxes3() {
  var checkboxes = document.getElementById("checkboxes3");
  if (!expanded) {
    checkboxes.style.display = "block";
    expanded = true;
  } else {
    checkboxes.style.display = "none";
    expanded = false;
  }
}