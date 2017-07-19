from lexos.processors.prepare.cutter import split_keep_whitespace, \
    count_words, cut_by_number


class TestCutByNumbers:
    def test_split_keep_whitespace(self):
        assert split_keep_whitespace("Test string") == ["Test", " ", "string"]
        assert split_keep_whitespace("Test") == ["Test"]
        assert split_keep_whitespace(" ") == ["", " ", ""]  # intended?
        assert split_keep_whitespace("") == [""]

    def test_count_words(self):
        assert count_words(["word", "word", " ", "not", "word"]) == 4
        assert count_words(['\n', '\t', ' ', '', '\u3000', "word"]) == 1
        assert count_words([""]) == 0
