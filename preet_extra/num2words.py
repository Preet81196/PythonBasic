
ones = ('Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine')

twos = ('Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen')

tens = ('Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety', 'Hundred')

suffixes = ('', 'Thousand', 'Million', 'Billion')


def process(amount, index):
    if amount == '0':
        return 'Zero'

    length = len(amount)

    if (length > 3):
        return False

    amount = amount.zfill(3)
    words = ''

    hdigit = int(amount[0])
    tdigit = int(amount[1])
    odigit = int(amount[2])

    words += '' if amount[0] == '0' else ones[hdigit]
    words += ' Hundred ' if not words == '' else ''

    if (tdigit > 1):
        words += tens[tdigit - 2]
        words += ' '
        words += ones[odigit]

    elif (tdigit == 1):
        words += twos[(int(tdigit + odigit) % 10) - 1]

    elif (tdigit == 0):
        words += ones[odigit]

    if (words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    if (not len(words) == 0):
        words += suffixes[index]

    return words;


def getWords(amount):
    length = len(str(amount))

    if length > 12:
        return 'This program supports upto 12 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(process(str(amount)[0 if i - 2 < 0 else i - 2: i + 1], copy - count))
        count -= 1;

    final_words = ''
    for s in reversed(words):
        temp = s + ' '
        final_words += temp

    return final_words

number = int(input('Enter any number: '))
print(  getWords(number))