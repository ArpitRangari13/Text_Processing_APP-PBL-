📝 Interactive Text Processing Playground
A lightweight, Flask-based web application for exploring fundamental Natural Language Processing (NLP) tasks. This tool provides a real-time interface to visualize how text is broken down and analyzed using SpaCy and NLTK.

🚀 Features
The application supports five core NLP operations based on the provided backend logic:

Tokenization: Splits text into individual words and punctuation marks.

Stopword Removal: Identifies and highlights common "stopwords" (e.g., "the", "is", "at") using NLTK's English corpus.

Lemmatization: Returns the base or dictionary form of words (lemmas).

Part-of-Speech (POS) Tagging: Assigns grammatical categories (Noun, Verb, Adjective, etc.) to each token.

Named Entity Recognition (NER): Detects and classifies real-world objects like persons, organizations, and locations.

🛠️ Tech Stack

Backend: Flask 

NLP Engines:

SpaCy: Used for tokenization, lemmatization, POS tagging, and NER.

NLTK: Used specifically for managing the English stopwords list.

Frontend: HTML5 with custom CSS for the playground interface.

Dependencies: Includes scikit-learn, textblob, and transformers for future scalability.
