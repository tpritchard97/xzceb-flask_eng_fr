from flask import Flask, render_template, request
from machinetranslation import translator

app = Flask("Web Translator")

@app.route("/")
def renderIndexPage():
    return render_template('index.html')

@app.route('/englishToFrench', methods=['POST'])
def translate_english_to_french():
    english_text = request.form['english_text']
    if not english_text:
        return "Error: No English text provided."
    
    french_text = translator.english_to_french(english_text)
    return french_text

@app.route('/frenchToEnglish', methods=['POST'])
def translate_french_to_english():
    french_text = request.form['french_text']
    if not french_text:
        return "Error: No French text provided."
    
    english_text = translator.french_to_english(french_text)
    return english_text

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
