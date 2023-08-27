document.querySelector("button").addEventListener("click", function() {
    const link = document.createElement("a")
    link.setAttribute("download", "BabyBotv2.rar")
    link.setAttribute("href", "D:/Projects/B-BabyBot/B-BabyBot v2/BabyBotv2")
    link.click()
})