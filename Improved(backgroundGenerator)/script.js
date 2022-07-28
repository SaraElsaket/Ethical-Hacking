//get needed elements to change background color
var h2 = document.querySelector("h2");
var color1 = document.querySelector(".color1");
var color2 = document.querySelector(".color2");
var body = document.querySelector("body");
var btn =document.getElementById("random")
var randomFirst=document.getElementById("Firstcolor")
var randomsecond=document.getElementById("Secondcolor")
//set color according to chosen color
function setcolor() {
	body.style.background = `linear-gradient(to right , ${color1.value} ,${color2.value})`;
	h2.textContent = body.style.background + ";"; //apend color value in rgb to the header
}
//function to cahnge the background randomly
function random(){
//variables to represent RGB to regenerate a new linear background
	var R1 = Math.floor(Math.random() * 256);
	var G1 = Math.floor(Math.random() * 256);
	var B1 = Math.floor(Math.random() * 256);
  
	var R2 = Math.floor(Math.random() * 256);
	var G2 = Math.floor(Math.random() * 256);
	var B2 = Math.floor(Math.random() * 256);
	var RColor1 = "rgb(" + R1 + "," + G1 + "," + B1 + ")";
	var RColor2 = "rgb(" + R2 + "," + G2 + "," + B2 + ")";
// assingning random colors to the background of the website
	body.style.background = `linear-gradient(to right , ${RColor1} ,${RColor2})`;
	h2.textContent = body.style.background + ";";
  }
//to change first color
function firstrandom(){
	//variables to represent RGB to regenerate a new linear background
		var R1 = Math.floor(Math.random() * 256);
		var G1 = Math.floor(Math.random() * 256);
		var B1 = Math.floor(Math.random() * 256);
		var FColor1 = "rgb(" + R1 + "," + G1 + "," + B1 + ")";
	// assingning random first color to the background of the website
		body.style.background = `linear-gradient(to right , ${FColor1} ,${color2.value})`;
		h2.textContent = body.style.background + ";";
	  }
//to change second color
function secondrandom(){
		//variables to represent RGB to regenerate a new linear background
		var R1 = Math.floor(Math.random() * 256);
		var G1 = Math.floor(Math.random() * 256);
		var B1 = Math.floor(Math.random() * 256);
		var SColor2 = "rgb(" + R1 + "," + G1 + "," + B1 + ")";
	// assingning random second color to the background of the website
		body.style.background = `linear-gradient(to right , ${color1.value} ,${SColor2})`;
		h2.textContent = body.style.background + ";";
		  }
//take , set,randomize background color
color1.addEventListener("input", setcolor);
color2.addEventListener("input", setcolor);
btn.addEventListener("click", random);
randomFirst.addEventListener("click", firstrandom);
randomsecond.addEventListener("click", secondrandom);