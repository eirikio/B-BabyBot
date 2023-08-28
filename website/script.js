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
    infoWindow.style.display = "flex";
})

closeBtn[0].addEventListener("click", () => {
        donateWindow.style.display = "none"
})
closeBtn[1].addEventListener("click", () => {
    infoWindow.style.display = "none"
})