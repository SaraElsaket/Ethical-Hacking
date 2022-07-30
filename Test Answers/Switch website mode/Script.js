var btn = document.querySelector("button")
var body =document.querySelector("body")
function switchmode(){
    if (btn.textContent=="Dark Mode"){
        body.style.background="#2f2f2f"
        body.style.color="#fff"
        btn.textContent="Light Mode"
        btn.style.color="#fff"
    }
    else{
        body.style.background="#fff"
        body.style.color="#2f2f2f"
        btn.textContent="Dark Mode"
        btn.style.color="#2f2f2f"
    }
}
btn.addEventListener("click",switchmode)