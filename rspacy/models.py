from pydantic import BaseModel
from typing import List

class TextInput(BaseModel):
    text: str
    disable: List[str]

class LexemeDetails(BaseModel):
    rank: int
    flags: int
    norm: int
    norm_: str
    lower: int
    lower_: str
    shape: int
    shape_: str
    prefix: int
    prefix_: str
    suffix: int
    suffix_: str
    is_alpha: bool
    is_ascii: bool
    is_digit: bool
    is_lower: bool
    is_upper: bool
    is_title: bool
    is_punct: bool
    is_left_punct: bool
    is_right_punct: bool
    is_space: bool
    is_bracket: bool
    is_quote: bool
    is_currency: bool
    like_url: bool
    like_num: bool
    like_email: bool
    is_oov: bool
    is_stop: bool
    lang: int
    lang_: str
    prob: float
    cluster: int
    sentiment: float

class AnalyzeResponse(BaseModel):
    vocab: bytes
    doc: bytes
    lexeme_details_per_token: List[LexemeDetails]