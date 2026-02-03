from flask import Flask, render_template, request, jsonify
import spacy
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))
nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process_text():
    text = request.form['text']
    action = request.form['action']
    doc = nlp(text)

    if action == 'tokenize':
        tokens = [token.text for token in doc]
        return jsonify(tokens=tokens)

    elif action == 'stopwords':
        highlighted = []
        cleaned = []
        for token in doc:
            if token.text.lower() in stop_words:
                highlighted.append(f"<span class='stopword'>{token.text}</span>")
            else:
                highlighted.append(token.text)
                cleaned.append(token.text)
        return jsonify(highlighted=" ".join(highlighted), cleaned=" ".join(cleaned))

    elif action == 'lemmatize':
        lemmas = [token.lemma_ for token in doc]
        return jsonify(lemmas=lemmas)

    elif action == 'pos':
        pos_tags = [(token.text, token.pos_) for token in doc]
        return jsonify(pos_tags=pos_tags)

    elif action == 'ner':
        entities = [(ent.text, ent.label_) for ent in doc.ents]
        return jsonify(entities=entities)

    return jsonify(error="Invalid action")

if __name__ == '__main__':
    app.run(debug=True)