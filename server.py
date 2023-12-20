''' Executing this function initiates the application of emotion
    detector to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emo_detector():
    ''' This code receives the text from the HTML interface and 
        runs an emotion detection over it using emotion_detector()
        function. The output returned shows the emotions, their score 
        and the dominant emotion from the text.
    '''
    scoring_table = """[P+: strong positive, 
    P: positive, 
    NEU: neutral, 
    N: negative, 
    N+: strong negative, 
    NONE: without polarity]"""
    text_to_analyze = request.args.get("textToAnalyze")
    sentiment_info = emotion_detector(text_to_analyze)
    status = sentiment_info['status']['msg']
    if status != 'OK':
        return f"Invalid text! Please try again!. Error {status}"
    sentiment_score = sentiment_info.get('score_tag', '')
    sentimented_entity_list = sentiment_info.get('sentimented_entity_list', [])
    if sentimented_entity_list:
        sentiment_label = sentimented_entity_list[0].get('form', '')
    else:
        sentiment_label = "No sentimented entities found."
    formatted_response = f"For the given statement and knowing the range of responses {scoring_table}, the system response is Score : {sentiment_score} and label : {sentiment_label}"
    print(formatted_response)
    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)
