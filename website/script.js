let dlBtn = document.getElementById("download-btn").addEventListener("click", () => {
    const link = document.createElement("a")
    link.setAttribute("download", "BabyBotV2.rar")
    link.setAttribute("href", "static/BabyBotV2.rar")
    link.click()
})

//let donateBtn = document.getElementById("donate-button").addEventListener("click", () => {
//    let params = `scrollbars=no,resizable=no,status=no,location=no,toolbar=no,menubar=no,
//    width=800,height=700,left=-1300,top=0`;
//
//    window.open("donate.html", 
//                "targetWindow", 
//                params);
//})

let donateBtn = document.getElementById("donate-button")
let donateWindow = document.getElementById("frame-donate")

let infoBtn = document.getElementById("button-info")
let infoWindow = document.getElementById("frame-info")

let closeBtn = document.getElementsByClassName("close-icon")

donateBtn.addEventListener("click", () => {
    console.log("click")
    donateWindow.style.display = "flex";
})

infoBtn.addEventListener("click", () => {
    infoWindow.style.display = "block";
})

closeBtn[0].addEventListener("click", () => {
        donateWindow.style.display = "none"
})
closeBtn[1].addEventListener("click", () => {
    infoWindow.style.display = "none"
})

let imgA = document.getElementById("item-a")

imgA.addEventListener("mousedown", () => {
    imgA.style.zIndex = "100"
    imgA.style.transform = "scale(3)"
})

imgA.addEventListener("mouseleave", () => {
    console.log("click")
    imgA.style.zIndex = "0"
    imgA.style.transform = "scale(1)"
})

imgA.addEventListener("mouseup", () => {
    imgA.style.zIndex = "0"
    imgA.style.transform = "scale(1)"
})

let imgB = document.getElementById("item-b")

imgB.addEventListener("mousedown", () => {
    imgB.style.zIndex = "100"
    imgB.style.transform = "scale(3)"
})

imgB.addEventListener("mouseleave", () => {
    imgB.style.zIndex = "0"
    imgB.style.transform = "scale(1)"
})

imgB.addEventListener("mouseup", () => {
    imgB.style.zIndex = "0"
    imgB.style.transform = "scale(1)"
})

let imgC = document.getElementById("item-c")

imgC.addEventListener("mousedown", () => {
    imgC.style.zIndex = "100"
    imgC.style.transform = "scale(3)"
})

imgC.addEventListener("mouseleave", () => {
    imgC.style.zIndex = "0"
    imgC.style.transform = "scale(1)"
})

imgC.addEventListener("mouseup", () => {
    imgC.style.zIndex = "0"
    imgC.style.transform = "scale(1)"
})