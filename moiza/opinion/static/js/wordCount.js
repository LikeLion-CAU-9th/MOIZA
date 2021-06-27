function wordCount() {
    let reason_content = document.getElementById('reason-content');
    let length = reason_content.value.length;
    console.log(length)
    if (length >= 15) {
        document.querySelector("#submit-button input").style.pointerEvents = "all"
        document.querySelector("#submit-button input").style.backgroundColor = "#7150e7"
    } else {
        document.querySelector("#submit-button input").style.pointerEvents = "none"
        document.querySelector("#submit-button input").style.backgroundColor = "#dddddd"
    }
}