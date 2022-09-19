def is_spam_words(text, spam_words, space_around=False):

    for spam_word in spam_words:

        if not space_around:

            if spam_word.lower() in text.lower():
                return True

        else:

            split_text_space = text.split(" ")
            
            for word in split_text_space:

                word_start_spam_len = word.lower().startswith(
                    spam_word.lower()) and len(
                    word) == len(spam_word)

                word_point_start_spam_len = word.lower().startswith(
                    spam_word.lower()) and len(
                    word) == len(spam_word) + 1 and word.endswith(".")

                if word_start_spam_len or word_point_start_spam_len:
                    return True

    return False
