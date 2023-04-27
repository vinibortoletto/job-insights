from src.pre_built.counter import count_ocurrences


def test_counter():
    path = "data/jobs.csv"
    word_list_in_lowercase = [("python", 1639), ("javascript", 122)]
    word_list_in_uppercase = [("PYTHON", 1639), ("JAVASCRIPT", 122)]

    """ Test if returns correct counter """

    for word in word_list_in_lowercase:
        result = count_ocurrences(path, word[0])
        assert result == word[1]

    """ Test if returns correct counter if word is in uppercase"""
    for word in word_list_in_uppercase:
        result = count_ocurrences(path, word[0])
        assert result == word[1]

    """ Test if raises error if  """
    word_list_with_wrong_count = [("Python", 0), ("JavaScript", 0)]

    for word in word_list_with_wrong_count:
        result = count_ocurrences(path, word[0])
        assert result != word[1]
