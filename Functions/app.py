def firstnlast(first, last):
    return first + ' ' + last


result1 = firstnlast('Ayume', 'Francis')
print(result1)
result2 = firstnlast('Joe', 'Soap')
print(result2)


def print_lyrics():
    print("I'm a lumberjack, and am okey")
    print("I sleep all night and work all day")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()