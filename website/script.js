document.querySelector("button").addEventListener("click", function() {
    const link = document.createElement("a")
    link.setAttribute("download", "dl-icon.png")
    link.setAttribute("href", "/dl-icon.png")
    link.click()
})