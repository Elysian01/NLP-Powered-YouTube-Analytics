import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.parsing.preprocessing import preprocess_string, strip_punctuation, strip_numeric

from .preprocess_comments import TextPreprocessor


def sent_to_words(sentences):
    for sentence in sentences:
        # deacc=True removes punctuations
        yield (gensim.utils.simple_preprocess(str(sentence), deacc=True))


def get_topics(df, debug=False):
    preprocessor = TextPreprocessor(df, debug=False)
    df = preprocessor.preprocess_text()
    data_words = list(sent_to_words(df['comments'].values.tolist()))

    # Create Dictionary
    id2word = corpora.Dictionary(data_words)
    # Create Corpus
    texts = data_words
    # Term Document Frequency
    corpus = [id2word.doc2bow(text) for text in texts]

    num_topics = 10

    # Build LDA model
    lda_model = gensim.models.LdaMulticore(corpus=corpus,
                                           id2word=id2word,
                                           num_topics=num_topics)
    # Print the Keyword in the 1 topics
    doc_lda = lda_model[corpus]

    lda_topics = lda_model.show_topics(num_words=10)

    topics = []
    filters = [lambda x: x.upper(), strip_punctuation, strip_numeric]

    for topic in lda_topics:
        processed = preprocess_string(topic[1], filters)
        topics.append(processed)

    unique_topics_set = set()

    # Iterate over each sublist and add unique topic names to the set
    for sublist in topics:
        unique_topics_set.update(sublist)
    unique_topics_list = list(unique_topics_set)

    if debug:
        print("Total Unique Topics: ", len(unique_topics_list))
        print(unique_topics_list)


if __name__ == "__main__":
    pass
