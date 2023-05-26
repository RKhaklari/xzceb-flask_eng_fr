from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    english_to_french(english_text)
    return "Translated text to French"

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    french_to_english(french_text)
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
    return index.html
 
