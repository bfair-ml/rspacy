import base64
import requests
from spacy.tokens import Doc
from spacy.vocab import Vocab
from rspacy.models import AnalyzeResponse

class RemoteSpacy:
    def __init__(self, api_url: str, legacy=True):
        self.api_url = api_url
        self.legacy = legacy
        self.vocab = Vocab()  # Use a default vocab to build spaCy docs

    def __call__(self, text: str) -> Doc:
        response = requests.post(self.api_url, json={"text": text})
        response.raise_for_status()
        parser = AnalyzeResponse.parse_obj if self.legacy else AnalyzeResponse.model_validate
        data = parser(response.json())

        vocab_bytes = base64.b64decode(data.vocab)
        doc_bytes = base64.b64decode(data.doc)

        vocab = Vocab().from_bytes(vocab_bytes)
        doc = Doc(vocab).from_bytes(doc_bytes)
        lexeme_details_per_token = data.lexeme_details_per_token

        # Set attributes (use Token.set_extension if needed for custom ones)
        for token, lex_details in zip(doc, lexeme_details_per_token):
            token.lex.rank = lex_details.rank
            token.lex.flags = lex_details.flags
            token.lex.norm = lex_details.norm
            token.lex.norm_ = lex_details.norm_
            token.lex.lower = lex_details.lower
            token.lex.lower_ = lex_details.lower_
            token.lex.shape = lex_details.shape
            token.lex.shape_ = lex_details.shape_
            token.lex.prefix = lex_details.prefix
            token.lex.prefix_ = lex_details.prefix_
            token.lex.suffix = lex_details.suffix
            token.lex.suffix_ = lex_details.suffix_
            token.lex.is_alpha = lex_details.is_alpha
            token.lex.is_ascii = lex_details.is_ascii
            token.lex.is_digit = lex_details.is_digit
            token.lex.is_lower = lex_details.is_lower
            token.lex.is_upper = lex_details.is_upper
            token.lex.is_title = lex_details.is_title
            token.lex.is_punct = lex_details.is_punct
            token.lex.is_left_punct = lex_details.is_left_punct
            token.lex.is_right_punct = lex_details.is_right_punct
            token.lex.is_space = lex_details.is_space
            token.lex.is_bracket = lex_details.is_bracket
            token.lex.is_quote = lex_details.is_quote
            token.lex.is_currency = lex_details.is_currency
            token.lex.like_url = lex_details.like_url
            token.lex.like_num = lex_details.like_num
            token.lex.like_email = lex_details.like_email
            # token.lex.is_oov = lex_details.is_oov
            token.lex.is_stop = lex_details.is_stop
            token.lex.lang = lex_details.lang
            token.lex.lang_ = lex_details.lang_
            token.lex.prob = lex_details.prob
            token.lex.cluster = lex_details.cluster
            token.lex.sentiment = lex_details.sentiment

        return doc
