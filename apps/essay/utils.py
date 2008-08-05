
def split_text_to_words(text):
    words_list = []
    last_aplha_chars = []
    
    for char in text:
        if char.isalpha():
            last_aplha_chars.append(char)
        else:
            if last_aplha_chars:
                words_list.append(''.join(last_aplha_chars))
                last_aplha_chars = []
    if last_aplha_chars:
        words_list.append(''.join(last_aplha_chars))
    return words_list

def count_words_in_list_to_dict(words_list):
    words_cout_dict = {}
    for word in words_list:
        word_lower = word.lower()
        if word_lower in words_cout_dict:
            words_cout_dict[word_lower] += 1
        else:
            words_cout_dict[word_lower] = 1
    return words_cout_dict
            

def split_text_to_words_dict_with_counts(text):
    words_list = split_text_to_words(text)
    return count_words_in_list_to_dict(words_list)
