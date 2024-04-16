import re
import yake


def get_keywords(df, debug):
    all_comments = ' '.join(df['comments'])

    # Remove punctuation, alphanumeric, and numeric characters
    all_comments = re.sub(r'[^a-zA-Z\s]', '', all_comments)

    language = "en"
    max_ngram_size = 3
    deduplication_thresold = 0.9
    deduplication_algo = 'seqm'
    windowSize = 3
    numOfKeywords = 30

    kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size, dedupLim=deduplication_thresold,
                                         dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)

    keywords = kw_extractor.extract_keywords(all_comments)

    # Extract only the first element of each tuple (the keyword)
    keyword_list = [kw[0] for kw in keywords]

    if debug:
        print("Keywords: \n")
        for kw in keyword_list:
            print(kw)

    return keyword_list
