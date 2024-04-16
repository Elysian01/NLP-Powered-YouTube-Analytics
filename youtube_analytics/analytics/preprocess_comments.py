import pandas as pd
import re
import string
import emoji
import spacy
from tqdm import tqdm
from langdetect import detect
from contractions import fix
from nltk.corpus import stopwords


class TextPreprocessor:
    def __init__(self, df, debug=False):
        self.df = df
        self.debug = debug

    # Add tqdm to show progress
    # def tqdm_apply(self, series, func, func_name):
    #     total = len(series)
    #     with tqdm(total=total, desc=func_name) as pbar:
    #         for item in series:
    #             yield func(item)
    #             pbar.update(1)
    def tqdm_apply(self, series, func, func_name):
        total = len(series)
        if self.debug:
            pbar = tqdm(total=total, desc=func_name)
        else:
            pbar = None
        for item in series:
            yield func(item)
            if pbar:
                pbar.update(1)
        if pbar:
            pbar.close()

    # Function to detect language
    def detect_language(self, text):
        try:
            return detect(text)
        except:
            return 'unknown'

    # Function to remove HTML tags
    def remove_html_tags(self, text):
        pattern = re.compile('<.*?>')
        return pattern.sub(r'', text)

    # Function to remove URLs
    def remove_url(self, text):
        pattern = re.compile(r'https?://\S+|www\.\S+')
        return pattern.sub(r'', text)

    # Function to remove newlines
    def remove_newlines(self, text):
        return text.replace('\n', ' ')

    # Function to remove dates
    def remove_dates(self, text):
        date_pattern = r'\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{2}\b|\b\d{2}/\d{2}/\d{4}\b|\b\d{1,2} (?:january|february|march|april|may|june|july|august|september|october|november|december) \d{4}\b'
        return re.sub(date_pattern, '', text)

    # Function to convert emojis to text
    def convert_emojis_to_text(self, text):
        text = emoji.demojize(text).split(":")
        text = " ".join(text)
        text = re.sub(r'\s+', ' ', text)
        return text

    # Function to convert emoticons to text
    def convert_emoticons_to_text(self, text):
        EMOTICONS = {
            u":‑\)": "Happy face smiley",
            u":\)": "Happy face smiley",
            u":-\]": "Happy face smiley",
            u":\]": "Happy face smiley",
            u":-3": "Happy face smiley",
            u":3": "Happy face smiley",
            u":->": "Happy face smiley",
            u":>": "Happy face smiley",
            u"8-\)": "Happy face smiley",
            u":o\)": "Happy face smiley",
            u":-\}": "Happy face smiley",
            u":\}": "Happy face smiley",
            u":-\)": "Happy face smiley",
            u":c\)": "Happy face smiley",
            u":\^\)": "Happy face smiley",
            u"=\]": "Happy face smiley",
            u"=\)": "Happy face smiley",
            u":‑D": "Laughing, big grin or laugh with glasses",
            u":D": "Laughing, big grin or laugh with glasses",
            u"8‑D": "Laughing, big grin or laugh with glasses",
            u"8D": "Laughing, big grin or laugh with glasses",
            u"X‑D": "Laughing, big grin or laugh with glasses",
            u"XD": "Laughing, big grin or laugh with glasses",
            u"=D": "Laughing, big grin or laugh with glasses",
            u"=3": "Laughing, big grin or laugh with glasses",
            u"B\^D": "Laughing, big grin or laugh with glasses",
            u":-\)\)": "Very happy",
            u":‑\(": "Frown, sad, andry or pouting",
            u":-\(": "Frown, sad, andry or pouting",
            u":\(": "Frown, sad, andry or pouting",
            u":‑c": "Frown, sad, andry or pouting",
            u":c": "Frown, sad, andry or pouting",
            u":‑<": "Frown, sad, andry or pouting",
            u":<": "Frown, sad, andry or pouting",
            u":‑\[": "Frown, sad, andry or pouting",
            u":\[": "Frown, sad, andry or pouting",
            u":-\|\|": "Frown, sad, andry or pouting",
            u">:\[": "Frown, sad, andry or pouting",
            u":\{": "Frown, sad, andry or pouting",
            u":@": "Frown, sad, andry or pouting",
            u">:\(": "Frown, sad, andry or pouting",
            u":'‑\(": "Crying",
            u":'\(": "Crying",
            u":'‑\)": "Tears of happiness",
            u":'\)": "Tears of happiness",
            u"D‑':": "Horror",
            u"D:<": "Disgust",
            u"D:": "Sadness",
            u"D8": "Great dismay",
            u"D;": "Great dismay",
            u"D=": "Great dismay",
            u"DX": "Great dismay",
            u":‑O": "Surprise",
            u":O": "Surprise",
            u":‑o": "Surprise",
            u":o": "Surprise",
            u":-0": "Shock",
            u"8‑0": "Yawn",
            u">:O": "Yawn",
            u":-\*": "Kiss",
            u":\*": "Kiss",
            u":X": "Kiss",
            u";‑\)": "Wink or smirk",
            u";\)": "Wink or smirk",
            u"\*-\)": "Wink or smirk",
            u"\*\)": "Wink or smirk",
            u";‑\]": "Wink or smirk",
            u";\]": "Wink or smirk",
            u";\^\)": "Wink or smirk",
            u":‑,": "Wink or smirk",
            u";D": "Wink or smirk",
            u":‑P": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u":P": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u"X‑P": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u"XP": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u":‑Þ": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u":Þ": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u":b": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u"d:": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u"=p": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u">:P": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u":‑/": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":/": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":-[.]": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u">:[(\\\)]": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u">:/": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":[(\\\)]": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u"=/": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u"=[(\\\)]": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":L": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u"=L": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":S": "Skeptical, annoyed, undecided, uneasy or hesitant",
            u":‑\|": "Straight face",
            u":\|": "Straight face",
            u":$": "Embarrassed or blushing",
            u":‑x": "Sealed lips or wearing braces or tongue-tied",
            u":x": "Sealed lips or wearing braces or tongue-tied",
            u":‑#": "Sealed lips or wearing braces or tongue-tied",
            u":#": "Sealed lips or wearing braces or tongue-tied",
            u":‑&": "Sealed lips or wearing braces or tongue-tied",
            u":&": "Sealed lips or wearing braces or tongue-tied",
            u"O:‑\)": "Angel, saint or innocent",
            u"O:\)": "Angel, saint or innocent",
            u"0:‑3": "Angel, saint or innocent",
            u"0:3": "Angel, saint or innocent",
            u"0:‑\)": "Angel, saint or innocent",
            u"0:\)": "Angel, saint or innocent",
            u":‑b": "Tongue sticking out, cheeky, playful or blowing a raspberry",
            u"0;\^\)": "Angel, saint or innocent",
            u">:‑\)": "Evil or devilish",
            u">:\)": "Evil or devilish",
            u"\}:‑\)": "Evil or devilish",
            u"\}:\)": "Evil or devilish",
            u"3:‑\)": "Evil or devilish",
            u"3:\)": "Evil or devilish",
            u">;\)": "Evil or devilish",
            u"\|;‑\)": "Cool",
            u"\|‑O": "Bored",
            u":‑J": "Tongue-in-cheek",
            u"#‑\)": "Party all night",
            u"%‑\)": "Drunk or confused",
            u"%\)": "Drunk or confused",
            u":-###..": "Being sick",
            u":###..": "Being sick",
            u"<:‑\|": "Dump",
            u"\(>_<\)": "Troubled",
            u"\(>_<\)>": "Troubled",
            u"\(';'\)": "Baby",
            u"\(\^\^>``": "Nervous or Embarrassed or Troubled or Shy or Sweat drop",
            u"\(\^_\^;\)": "Nervous or Embarrassed or Troubled or Shy or Sweat drop",
            u"\(-_-;\)": "Nervous or Embarrassed or Troubled or Shy or Sweat drop",
            u"\(~_~;\) \(・\.・;\)": "Nervous or Embarrassed or Troubled or Shy or Sweat drop",
            u"\(-_-\)zzz": "Sleeping",
            u"\(\^_-\)": "Wink",
            u"\(\(\+_\+\)\)": "Confused",
            u"\(\+o\+\)": "Confused",
            u"\(o\|o\)": "Ultraman",
            u"\^_\^": "Joyful",
            u"\(\^_\^\)/": "Joyful",
            u"\(\^O\^\)／": "Joyful",
            u"\(\^o\^\)／": "Joyful",
            u"\(__\)": "Kowtow as a sign of respect, or dogeza for apology",
            u"_\(\._\.\)_": "Kowtow as a sign of respect, or dogeza for apology",
            u"<\(_ _\)>": "Kowtow as a sign of respect, or dogeza for apology",
            u"<m\(__\)m>": "Kowtow as a sign of respect, or dogeza for apology",
            u"m\(__\)m": "Kowtow as a sign of respect, or dogeza for apology",
            u"m\(_ _\)m": "Kowtow as a sign of respect, or dogeza for apology",
            u"\('_'\)": "Sad or Crying",
            u"\(/_;\)": "Sad or Crying",
            u"\(T_T\) \(;_;\)": "Sad or Crying",
            u"\(;_;": "Sad of Crying",
            u"\(;_:\)": "Sad or Crying",
            u"\(;O;\)": "Sad or Crying",
            u"\(:_;\)": "Sad or Crying",
            u"\(ToT\)": "Sad or Crying",
            u";_;": "Sad or Crying",
            u";-;": "Sad or Crying",
            u";n;": "Sad or Crying",
            u";;": "Sad or Crying",
            u"Q\.Q": "Sad or Crying",
            u"T\.T": "Sad or Crying",
            u"QQ": "Sad or Crying",
            u"Q_Q": "Sad or Crying",
            u"\(-\.-\)": "Shame",
            u"\(-_-\)": "Shame",
            u"\(一一\)": "Shame",
            u"\(；一_一\)": "Shame",
            u"\(=_=\)": "Tired",
            u"\(=\^\·\^=\)": "cat",
            u"\(=\^\·\·\^=\)": "cat",
            u"=_\^=	": "cat",
            u"\(\.\.\)": "Looking down",
            u"\(\._\.\)": "Looking down",
            u"\^m\^": "Giggling with hand covering mouth",
            u"\(\・\・?": "Confusion",
            u"\(?_?\)": "Confusion",
            u">\^_\^<": "Normal Laugh",
            u"<\^!\^>": "Normal Laugh",
            u"\^/\^": "Normal Laugh",
            u"\（\*\^_\^\*）": "Normal Laugh",
            u"\(\^<\^\) \(\^\.\^\)": "Normal Laugh",
            u"\(^\^\)": "Normal Laugh",
            u"\(\^\.\^\)": "Normal Laugh",
            u"\(\^_\^\.\)": "Normal Laugh",
            u"\(\^_\^\)": "Normal Laugh",
            u"\(\^\^\)": "Normal Laugh",
            u"\(\^J\^\)": "Normal Laugh",
            u"\(\*\^\.\^\*\)": "Normal Laugh",
            u"\(\^—\^\）": "Normal Laugh",
            u"\(#\^\.\^#\)": "Normal Laugh",
            u"\（\^—\^\）": "Waving",
            u"\(;_;\)/~~~": "Waving",
            u"\(\^\.\^\)/~~~": "Waving",
            u"\(-_-\)/~~~ \($\·\·\)/~~~": "Waving",
            u"\(T_T\)/~~~": "Waving",
            u"\(ToT\)/~~~": "Waving",
            u"\(\*\^0\^\*\)": "Excited",
            u"\(\*_\*\)": "Amazed",
            u"\(\*_\*;": "Amazed",
            u"\(\+_\+\) \(@_@\)": "Amazed",
            u"\(\*\^\^\)v": "Laughing,Cheerful",
            u"\(\^_\^\)v": "Laughing,Cheerful",
            u"\(\(d[-_-]b\)\)": "Headphones,Listening to music",
            u'\(-"-\)': "Worried",
            u"\(ーー;\)": "Worried",
            u"\(\^0_0\^\)": "Eyeglasses",
            u"\(\＾ｖ\＾\)": "Happy",
            u"\(\＾ｕ\＾\)": "Happy",
            u"\(\^\)o\(\^\)": "Happy",
            u"\(\^O\^\)": "Happy",
            u"\(\^o\^\)": "Happy",
            u"\)\^o\^\(": "Happy",
            u":O o_O": "Surprised",
            u"o_0": "Surprised",
            u"o\.O": "Surpised",
            u"\(o\.o\)": "Surprised",
            u"oO": "Surprised",
            u"\(\*￣m￣\)": "Dissatisfied",
            u"\(‘A`\)": "Snubbed or Deflated"
        }
        for emoticon, text_rep in EMOTICONS.items():
            text = re.sub(emoticon, text_rep, text)
        return text

    # Function to expand contractions
    def expand_contractions(self, text):
        return fix(text)

    # Function to remove punctuations
    def remove_punctuation(self, text):
        return text.translate(str.maketrans('', '', string.punctuation))

    # Function to remove stopwords
    def remove_stopwords(self, text):
        stop_words = set(stopwords.words('english'))
        return ' '.join(word for word in text.split() if word.lower() not in stop_words)

    # Function to perform lemmatization
    def lemmatize_text(self, text):
        nlp = spacy.load("en_core_web_sm")
        doc = nlp(text)
        lemmas = [token.lemma_ for token in doc]
        return ' '.join(lemmas)

    # Function to preprocess the text
    def preprocess_text(self):
        # Detect language
        self.df['detected_language'] = list(self.tqdm_apply(
            self.df['comments'], self.detect_language, 'Language Detection'))

        # Filter rows where language is English
        self.df = self.df.loc[self.df['detected_language'] == 'en'].copy()

        # Perform text preprocessing steps
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_html_tags, 'Removing HTML Tags'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_url, 'Removing URLs'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_newlines, 'Removing Newlines'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_dates, 'Removing Dates'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.convert_emojis_to_text, 'Converting Emojis to Text'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.convert_emoticons_to_text, 'Converting Emoticons to Text'))
        self.df.loc[:, 'comments'] = self.df['comments'].str.lower()
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.expand_contractions, 'Expanding Contractions'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_punctuation, 'Removing Punctuation'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.remove_stopwords, 'Removing Stopwords'))
        self.df.loc[:, 'comments'] = list(self.tqdm_apply(
            self.df['comments'], self.lemmatize_text, 'Lemmatization'))

        return self.df


if __name__ == '__main':
    pass
    # preprocessor = TextPreprocessor(df)
    # preprocessed_df = preprocessor.preprocess_text()
    # print(preprocessed_df.head())
