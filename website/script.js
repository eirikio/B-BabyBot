document.querySelector("button").addEventListener("click", function() {
    const link = document.createElement("a")
    link.setAttribute("download", "BabyBotv2.rar")
    link.setAttribute("href", "/website/BabyBotV2.rar")
    link.click()
})