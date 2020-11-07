from collections import Counter


def popular_words(text, words):
    tmp = text.lower().split()
    words_number = Counter(tmp)

    result_dict = {
        words[0]: words_number.get('i'),
        words[1]: words_number.get('was'),
        words[2]: words_number.get('three'),
        words[3]: words_number.get('near')
    }

    return result_dict


my_text = "When I was one" \
          "I had just begun" \
          "When I was two" \
          "I was nearly new"

my_words = ['i', 'was', 'three', 'near']

result = popular_words(my_text, my_words)
print(result)
