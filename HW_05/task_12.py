import re


def replace_spam_words(text, spam_words):

    new_text = text

    for word in spam_words:

        format = "{:*^" + str(len(word)) + "}"
        stars_count_for_spam = format.format("")
        new_text = re.sub(word, stars_count_for_spam, new_text, flags=re.IGNORECASE)

    return new_text