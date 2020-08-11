def get_amount_in_words(amount):
    units = ("", "one ", "two ", "three ", "four ","five ", "six ", "seven ","eight ", "nine ", "ten ", "eleven ", "twelve ", "thirteen ", "fourteen ", "fifteen ","sixteen ", "seventeen ", "eighteen ", "nineteen ")
    tens =("", "", "twenty ", "thirty ", "forty ", "fifty ","sixty ","seventy ","eighty ","ninety ")

    if amount < 0:
        return "minus "+get_amount_in_words(-amount)

    if amount<20:
        return  units[amount]

    if amount<100:

        return  tens[amount // 10]  +units[int(amount% 10)]

    if amount<1000:
        return units[amount // 100]  +"hundred " +get_amount_in_words(int(amount % 100))

    if amount<1000000:
        return  get_amount_in_words(amount // 1000) + "thousand " + get_amount_in_words(int(amount % 1000))

    if num < 1000000000:    
        return get_amount_in_words(amount // 1000000) + "million " + get_amount_in_words(int(amount % 1000000))

    return get_amount_in_words(amount // 1000000000)+ "billion "+ get_amount_in_words(int(amount % 1000000000))


    return get_amount_in_words(amount)
