
def generate_pattern(correct: str) -> str:
    '''
    It generates an expression that covers misspelled versions of the correct
    word. It has a lot of potential problems and there are already
    some banks of the misspelled version of the words. That might be better
    to use.

    It is rather an idea than a solution.
    Arg:
        correct str: a correct version of the desired word
    Returns:
        pattern str: a rough pattern that might cover the majority misspells
    '''
    optional_space = r'\s?'
    letters_to_pattern = [
            {},
            {
                "v": "[v|f]",
                "w": "[w|u]",
                "s": "[s|z]",
                "y": "[y|i]",
                "x": "[x|ks]"
            },
            {
                "ei": "[ei|ie|e|i]",
                "ie": "[ei|ie|i|e]",
                "ck": "[ck|c|k]",
                "ph": "[ph|f]"
            }
        ]

    pattern = correct.lower()
    for w_size in range(len(letters_to_pattern) - 1, 0, -1):
        j = len(pattern) - w_size
        while j >= 0:
            w_slice = pattern[j:j+w_size]
            pattern = pattern[:j] + \
                letters_to_pattern[w_size].get(w_slice, w_slice) + \
                pattern[j + w_size:]
            j -= 1

    return optional_space + pattern + optional_space
