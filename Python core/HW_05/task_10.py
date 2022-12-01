import re

def find_word(text, word):
    
    word_match = re.search(word, text)

    dict = {
                "result": True if word_match else False,
                "first_index": word_match.span()[0] if word_match else None,
                "last_index": word_match.span()[1] if word_match else None,
                "search_string": word,
                "string": text
            }

    return dict
