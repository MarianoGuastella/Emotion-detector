function displayResponse(response) {
    response = response.replace(/\n/g, '<br>');
    document.getElementById("system_response").innerHTML = response;
}

let RunSentimentAnalysis = () => {
    showLoading();
    textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            displayResponse(xhttp.responseText);
            hideLoading();
        }
    };
    xhttp.open("GET", "emotionDetector?textToAnalyze=" + encodeURIComponent(textToAnalyze), true);
    xhttp.send();
}