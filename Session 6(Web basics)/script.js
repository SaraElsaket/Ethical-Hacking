//get needed elements to change background color
var h2 = document.querySelector("h2");
var color1 = document.querySelector(".color1");
var body = document.querySelector("body");

//set color according to chosen color
function setcolor() {
	body.style.background = color1.value;
	h2.textContent = body.style.background + ";"; //apend color value in rgb to the header
}
//Pick and set background color
color1.addEventListener("input", setcolor);