def convert(number):
    #define variable raindrops as a string
    raindrops = ''

    if number % 3 == 0:
        raindrops += 'Pling'

    if number % 5 == 0:
        raindrops += 'Plang'

    if number % 7 == 0:
        raindrops += 'Plong'

    return str(raindrops or number)

