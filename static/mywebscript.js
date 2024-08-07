let RunSentimentAnalysis = () => {
    let textToAnalyze = document.getElementById("textToAnalyze").value;

    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4) {
            if (this.status == 200) {
                let response = JSON.parse(this.responseText);
                let formattedResponse = `For the given statement, the system response is 'anger': ${response.anger}, 'disgust': ${response.disgust}, 'fear': ${response.fear}, 'joy': ${response.joy} and 'sadness': ${response.sadness}. The dominant emotion is ${response.dominant_emotion}.`;
                document.getElementById("system_response").innerHTML = formattedResponse;
            } else if (this.status == 400) {
                let errorResponse = JSON.parse(this.responseText);
                document.getElementById("system_response").innerHTML = errorResponse.error;
            }
        }
    };
    xhttp.open("POST", "/emotionDetector", true);
    xhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xhttp.send(JSON.stringify({ statement: textToAnalyze }));
}