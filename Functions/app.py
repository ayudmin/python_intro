def firstnlast(first, last):
    return first + ' ' + last


result1 = firstnlast('Ayume', 'Francis')
print(result1)
result2 = firstnlast('Joe', 'Soap')
print(result2)


def print_lyrics():
    print("I'm a lumberjack, and am okay")
    print("I sleep all night and work all day")


def repeat_lyrics():
    print_lyrics()
    print_lyrics()


repeat_lyrics()


def print_bruce(bruce):
    print(bruce)


print_bruce('spam ' * 4)


def right_justify(s):
    print("                                                              " + s)


right_justify('francis')


def print_spam(t):
    print(t + " spam")


def do_twice(f,v):
    f(v)
    f(v)


do_twice(print_spam, 'hello')