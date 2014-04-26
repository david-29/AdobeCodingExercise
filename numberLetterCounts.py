# Number Letter Counts

DEBUG = False

word_list = [
    'one', 'two', 'three', 'four', 'five', 'six',
    'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen',
    'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen',
    'nineteen', 'twenty', 'thirty', 'forty', 'fifty', 'sixty',
    'seventy', 'eighty', 'ninety', 'hundred', 'and', 'thousand']

# initialize dictionary with word letter counts
letter_counts = {x: len(x) for x in word_list}


units_words = ['', 'one', 'two', 'three', 'four', 'five', 'six',
               'seven', 'eight', 'nine']

tens_words = ['', 'ten', 'twenty', 'thirty', 'forty',
              'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

special_words = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
                 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']


def convert_number_to_words(n):
    """Generate the word representation of a number"""

    if n > 9999:
        raise RuntimeError('Number: {0} is too large.'.format(n))
    words = []
    if n >= 1000:
        q, r = divmod(n, 1000)
        words += [units_words[q], 'thousand']
        if 0 < r < 100:
            words += ['and']
        n = r
    if n >= 100:
        q, r = divmod(n, 100)
        words += [units_words[q], 'hundred']
        if r > 0:
            words += ['and']
        n = r
    done = False
    if n >= 10:
        q, r = divmod(n, 10)
        if q > 1:
            words += [tens_words[q]]
        elif q == 1:
            words += [special_words[r]]
            done = True
        n = r
    if n > 0:
        if not done:
            words += [units_words[n]]
    return words


def get_number_letter_count_for_range(n1, n2):
    """
    Get the count of letters in the word representations of
    numbers in a given range <n1> .. <n2>
    """

    total_letters = 0

    for nn in range(n1, n2+1):
        number_words = convert_number_to_words(nn)
        if DEBUG:
            print(' -- {0} as words: {1}'.format(nn, " ".join(number_words)))

        # loop over words in number and sum their letter counts
        number_letters = 0
        for w in number_words:
            number_letters += letter_counts[w]

        total_letters += number_letters

    return total_letters