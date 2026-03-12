#charlie brown

import operator
import spacy

# Load spacy model
try:
    nlp = spacy.load('en_core_web_sm')
except:
    print("Please run: python -m spacy download en_core_web_sm")

def fetch_text(raw_url):
    """
    Downloads text from a URL and saves it to a local cache folder.
    
    Parameters:
        raw_url (str): The web address of the text file.
        
    Returns:
        str: The content of the text file.
    """
    import requests
    from pathlib import Path
    import hashlib
    CACHE_DIR = Path("cs_110_content/text_cache")
    CACHE_DIR.mkdir(parents=True, exist_ok=True)

    def _url_to_filename(url):
        url_hash = hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
        return CACHE_DIR / f"{url_hash}.txt"

    cache_path = _url_to_filename(raw_url)
    try:
        if not cache_path.exists():
            response = requests.get(raw_url, timeout=10)
            response.raise_for_status()
            text_data = response.text
            cache_path.write_text(text_data, encoding="utf-8")
        return cache_path.read_text(encoding="utf-8")
    except Exception as e:
        print(f"Failed to fetch text: {e}")
        return None

def print_text_stats(text):
    """
    Calculates and displays the number of characters, lines, and words in a text.
    
    Parameters:
        text (str): The raw string to be analyzed.
    """
    num_chars = len(text)
    lines = text.splitlines()
    num_lines = len(lines)
    num_words = sum(len(line.split()) for line in lines)
    print(f"Number of characters: {num_chars}")
    print(f"Number of lines: {num_lines}")
    print(f"Number of words: {num_words}")

def get_word_counts(text):
    """
    Counts the frequency of every word in a text by splitting on whitespace.
    
    Parameters:
        text (str): The input text to process.
        
    Returns:
        dict: A dictionary mapping words to their occurrence counts.
    """
    word_counts = {}
    for line in text.splitlines():
        for word in line.split():
            word = word.lower()
            word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts

def print_top_10_frequent_words(text):
    """
    Prints the 10 most frequent words from the uncleaned text.
    
    Parameters:
        text (str): The text to analyze.
    """
    word_counts = get_word_counts(text)
    sorted_words = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    for word, count in sorted_words[:10]:
        print(f"{word}: {count}")

def word_tokenization_normalization(text):
    """
    Uses spaCy to remove stop words, punctuation, and perform lemmatization.
    
    Parameters:
        text (str): The raw text string.
        
    Returns:
        list: A list of cleaned, base-form word tokens.
    """
    doc = nlp(text.lower())
    words_normalized = []
    for word in doc:
        if not word.is_stop and not word.is_punct and not word.like_num and len(word.text.strip()) > 2:
            words_normalized.append(str(word.lemma_))
    return words_normalized

def word_count(word_list):
    """
    Creates a frequency dictionary from a list of words.
    
    Parameters:
        word_list (list): The list of strings to count.
        
    Returns:
        dict: Word counts for the list.
    """
    counts = {}
    for word in word_list:
        word = word.lower()
        counts[word] = counts.get(word, 0) + 1
    return counts

def print_top_15_frequent_words(word_counts):
    """
    Displays the top 15 words from a processed frequency dictionary.
    
    Parameters:
        word_counts (dict): The dictionary of words and counts.
    """
    sorted_counts = sorted(word_counts.items(), key=operator.itemgetter(1), reverse=True)
    for word, count in sorted_counts[:15]:
        print(f"{word}: {count}")

# --- EXECUTION BLOCK ---
# Using the stable Project Gutenberg link for Pride and Prejudice
PRIDE_URL = "https://www.gutenberg.org/cache/epub/1342/pg1342.txt"
pride_prejudice_text = fetch_text(PRIDE_URL)

if pride_prejudice_text:
    print("--- BASIC STATISTICS ---")
    print_text_stats(pride_prejudice_text)
    
    print("\n--- TOP 10 BASIC WORDS ---")
    print_top_10_frequent_words(pride_prejudice_text)
    
    print("\n--- TOP 15 ADVANCED (SPACY) WORDS ---")
    tokens = word_tokenization_normalization(pride_prejudice_text)
    advanced_counts = word_count(tokens)
    print_top_15_frequent_words(advanced_counts)

"""COMPARATIVE ANALYSIS
In this analysis, I observed a significant difference between basic word counting 
and advanced NLP processing. The basic top 10 list was dominated by functional 
"stop words" like 'the' (4800 hits), 'to' (4325 hits), and 'of' (3917 hits). These words 
are necessary for English grammar but provide no actual insight into the specific 
narrative or themes of Jane Austen's writing. If I ran this basic test on a 
completely different book, the results would look almost identical.

However, after using the spaCy library for tokenization and normalization, the 
results became much more descriptive and meaningful. By filtering out stop words, 
punctuation, and short particles, the frequency list finally revealed the actual 
heart of the novel. We see the central characters clearly: Elizabeth leads with 
639 mentions, followed closely by Darcy (428) and the Bennet family (348). 

A key reason for this improvement is the lemmatization. This process allowed the code 
to group different forms of a words like 'said,' 'says,' and 'saying' into the 
single base lemma 'say' (426). This highlights the conversational and social 
nature of the book. The presence of words like 'sister,' 'lady,' and 'miss' in 
the top 15 list further confirms that the text focuses heavily on family 
relationships and social status. Ultimately, advanced text processing 
transforms raw data "noise" into actual literary insight."""