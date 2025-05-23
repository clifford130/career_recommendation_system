# import spacy

# # Load spaCy English model (this will load once when the module is imported)
# nlp = spacy.load("en_core_web_sm")

# def extract_keywords(text):
#     """
#     Process the text with spaCy and return a list of important keywords (nouns and proper nouns).
#     """
#     doc = nlp(text)
#     keywords = []
#     for token in doc:
#         # Consider nouns and proper nouns as keywords
#         if token.pos_ in ['NOUN', 'PROPN'] and not token.is_stop:
#             keywords.append(token.lemma_)
#     # Remove duplicates and return
#     return list(set(keywords))
# import nltk
# from nltk.tokenize import word_tokenize
# from nltk.tag import pos_tag
# from nltk.corpus import stopwords

# # Download necessary NLTK data (only run once)
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('stopwords')

# def extract_keywords(text):
#     """
#     Extracts keywords (nouns and proper nouns) using NLTK.
#     """
#     # Tokenize and tag parts of speech
#     tokens = word_tokenize(text)
#     tagged_tokens = pos_tag(tokens)
    
#     # Filter out stop words and only keep nouns/proper nouns
#     stop_words = set(stopwords.words('english'))
#     keywords = [word for word, tag in tagged_tokens 
#                 if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and word.lower() not in stop_words]
    
#     return list(set(keywords))
import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk.corpus import stopwords

def ensure_nltk_resource(resource, download_name):
    try:
        nltk.data.find(resource)
    except LookupError:
        nltk.download(download_name)

# Check and download required NLTK data if not already present.
ensure_nltk_resource('tokenizers/punkt', 'punkt')
ensure_nltk_resource('taggers/averaged_perceptron_tagger_eng', 'averaged_perceptron_tagger_eng')
ensure_nltk_resource('corpora/stopwords', 'stopwords')

def extract_keywords(text):
    """
    Extracts keywords (nouns and proper nouns) using NLTK.
    """
    tokens = word_tokenize(text)
    tagged_tokens = pos_tag(tokens)
    stop_words = set(stopwords.words('english'))
    keywords = [word for word, tag in tagged_tokens 
                if tag in ['NN', 'NNS', 'NNP', 'NNPS'] and word.lower() not in stop_words]
    return list(set(keywords))

