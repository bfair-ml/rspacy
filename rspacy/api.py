import base64
from fastapi import FastAPI
from rspacy.models import AnalyzeResponse, TextInput, LexemeDetails
import spacy

# Load spaCy Catalan model
nlp = spacy.load("ca_core_news_sm")

app = FastAPI(title="Catalan NLP API")


@app.post("/analyze", response_model=AnalyzeResponse)
def analyze_text(input: TextInput):
    doc = nlp(input.text, disable=input.disable)
    return AnalyzeResponse(
        vocab=base64.b64encode(doc.vocab.to_bytes()).decode("utf-8"),
        doc=base64.b64encode(doc.to_bytes()).decode("utf-8"),
        lexeme_details_per_token=[
            LexemeDetails(
                rank=token.lex.rank,
                flags=token.lex.flags,
                norm=token.lex.norm,
                norm_=token.lex.norm_,
                lower=token.lex.lower,
                lower_=token.lex.lower_,
                shape=token.lex.shape,
                shape_=token.lex.shape_,
                prefix=token.lex.prefix,
                prefix_=token.lex.prefix_,
                suffix=token.lex.suffix,
                suffix_=token.lex.suffix_,
                is_alpha=token.lex.is_alpha,
                is_ascii=token.lex.is_ascii,
                is_digit=token.lex.is_digit,
                is_lower=token.lex.is_lower,
                is_upper=token.lex.is_upper,
                is_title=token.lex.is_title,
                is_punct=token.lex.is_punct,
                is_left_punct=token.lex.is_left_punct,
                is_right_punct=token.lex.is_right_punct,
                is_space=token.lex.is_space,
                is_bracket=token.lex.is_bracket,
                is_quote=token.lex.is_quote,
                is_currency=token.lex.is_currency,
                like_url=token.lex.like_url,
                like_num=token.lex.like_num,
                like_email=token.lex.like_email,
                is_oov=token.lex.is_oov,
                is_stop=token.lex.is_stop,
                lang=token.lex.lang,
                lang_=token.lex.lang_,
                prob=token.lex.prob,
                cluster=token.lex.cluster,
                sentiment=token.lex.sentiment,
            )
            for token in doc
        ],
    )
