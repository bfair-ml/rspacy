import base64
import requests
from spacy.tokens import Doc
from spacy.vocab import Vocab


class RemoteSpacy:
    def __init__(self, api_url: str):
        self.api_url = api_url
        self.vocab = Vocab()  # Use a default vocab to build spaCy docs

    def __call__(self, text: str) -> Doc:
        response = requests.post(self.api_url, json={"text": text})
        response.raise_for_status()
        data = response.json()

        vocab_bytes = base64.b64decode(data["vocab"])
        doc_bytes = base64.b64decode(data["doc"])
        tokens_data = data["lexeme_details_per_token"]

        vocab = Vocab().from_bytes(vocab_bytes)
        doc = Doc(vocab).from_bytes(doc_bytes)

        # Set attributes (use Token.set_extension if needed for custom ones)
        for token, tok_data in zip(doc, tokens_data):
            token.lex.rank = tok_data["rank"]
            token.lex.flags = tok_data["flags"]
            token.lex.norm = tok_data["norm"]
            token.lex.norm_ = tok_data["norm_"]
            token.lex.lower = tok_data["lower"]
            token.lex.lower_ = tok_data["lower_"]
            token.lex.shape = tok_data["shape"]
            token.lex.shape_ = tok_data["shape_"]
            token.lex.prefix = tok_data["prefix"]
            token.lex.prefix_ = tok_data["prefix_"]
            token.lex.suffix = tok_data["suffix"]
            token.lex.suffix_ = tok_data["suffix_"]
            token.lex.is_alpha = tok_data["is_alpha"]
            token.lex.is_ascii = tok_data["is_ascii"]
            token.lex.is_digit = tok_data["is_digit"]
            token.lex.is_lower = tok_data["is_lower"]
            token.lex.is_upper = tok_data["is_upper"]
            token.lex.is_title = tok_data["is_title"]
            token.lex.is_punct = tok_data["is_punct"]
            token.lex.is_left_punct = tok_data["is_left_punct"]
            token.lex.is_right_punct = tok_data["is_right_punct"]
            token.lex.is_space = tok_data["is_space"]
            token.lex.is_bracket = tok_data["is_bracket"]
            token.lex.is_quote = tok_data["is_quote"]
            token.lex.is_currency = tok_data["is_currency"]
            token.lex.like_url = tok_data["like_url"]
            token.lex.like_num = tok_data["like_num"]
            token.lex.like_email = tok_data["like_email"]
            # token.lex.is_oov = tok_data["is_oov"]
            token.lex.is_stop = tok_data["is_stop"]
            token.lex.lang = tok_data["lang"]
            token.lex.lang_ = tok_data["lang_"]
            token.lex.prob = tok_data["prob"]
            token.lex.cluster = tok_data["cluster"]
            token.lex.sentiment = tok_data["sentiment"]

        return doc
