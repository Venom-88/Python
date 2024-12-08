def single_root_words(root_word, *other_words):
    same_words = []
    root_lower = root_word.lower()
    for word in other_words:
        w_lower = word.lower()
        if (root_lower in w_lower) or (w_lower in root_lower):
            same_words.append(word)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)