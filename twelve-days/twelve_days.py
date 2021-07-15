def recite(start_verse, end_verse):
    days = ["first", "second", "third", "fourth", "fifth", "sixth",
        "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]

    gifts = ["a Partridge in a Pear Tree", "two Turtle Doves", "three French Hens", "four Calling Birds", "five Gold Rings",
        "six Geese-a-Laying", "seven Swans-a-Swimming", "eight Maids-a-Milking", "nine Ladies Dancing", "ten Lords-a-Leaping",
        "eleven Pipers Piping", "twelve Drummers Drumming"]

    final_song = []
    for i in range(start_verse, end_verse + 1, 1):
        verse = "On the " + days[i - 1] + " day of Christmas my true love gave to me: "
        for j in range(i - 1, 0, -1):
            verse = verse + gifts[j] + ", "
        if i > 1:
            verse = verse + "and "
        verse = verse + gifts[0] + "."
        final_song.append(verse)
    return final_song

  
  