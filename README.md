# rspacy: Remote spaCy

`rspacy` is a remote NLP API built using FastAPI and spaCy. It provides an endpoint to analyze Catalan text and return detailed linguistic features for each token in the text.

## Features
- Analyze text remotely using spaCy's NLP capabilities.
- Extract detailed linguistic features for each token, including lexical attributes, morphology, and more.
- Supports Catalan text analysis.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/rspacy.git
   cd rspacy
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the FastAPI server:
   ```bash
   uvicorn rspacy.api:app --reload
   ```

## Usage
### Client-Side
Use the `RemoteSpacy` class to send text to the API and receive a processed `Doc` object:
```python
from rspacy.remote import RemoteSpacy

api_url = "http://localhost:8000/analyze"
nlp = RemoteSpacy(api_url)

text = "Aquest és un exemple de text en català."
doc = nlp(text)

for token in doc:
    print(token.text, token.lemma_, token.pos_, token.dep_)
```

### API Endpoint
- **Endpoint**: `/analyze`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "text": "Aquest és un exemple de text en català."
  }
  ```
- **Response**:
  ```json
  {
    "vocab": "<base64-encoded vocab>",
    "doc": "<base64-encoded doc>",
    "lexeme_details_per_token": [
      {
        "rank": 0,
        "flags": 0,
        "norm": 0,
        "norm_": "",
        "lower": 0,
        "lower_": "",
        "shape": 0,
        "shape_": "",
        "prefix": 0,
        "prefix_": "",
        "suffix": 0,
        "suffix_": "",
        "is_alpha": true,
        "is_ascii": true,
        "is_digit": false,
        "is_lower": false,
        "is_upper": false,
        "is_title": true,
        "is_punct": false,
        "is_left_punct": false,
        "is_right_punct": false,
        "is_space": false,
        "is_bracket": false,
        "is_quote": false,
        "is_currency": false,
        "like_url": false,
        "like_num": false,
        "like_email": false,
        "is_stop": false,
        "lang": 0,
        "lang_": "",
        "prob": 0.0,
        "cluster": 0,
        "sentiment": 0.0
      }
    ]
  }
  ```

## Contributing
Contributions are welcome! Please open an issue or submit a pull request.
