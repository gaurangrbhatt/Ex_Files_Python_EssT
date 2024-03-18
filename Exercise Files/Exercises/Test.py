
def main():
    print("hello world!")
    name = input("What is your name? ")
    print("Nice to meet you,", name)

    # if('1'==1):
    #     print('1'==1)


def greet(*names):
    print("In greet!")
    """This function greets all
    the person in the names tuple."""

    # names is a tuple with arguments
    for name in names:
        print("Hello", name)


def for_test(*names):
    # '''That's  ok'''
    # "3"
    # '"Once upon a time..", she said .'

    # Below String compilation error
    # "He said,"Yes!""
    return None


def remove_special_characters(para, special1):
    # Python code to remove special char
    # using replace()

    # initializing special characters
    # sp_chars = [';', ':', '!', "*"]

    # given string
    # givenStr = "Hel;lo *w:o!r;ld * de*ar !"

    # print given string
    # print ("Original String : " + para)

    # using replace() to
    # remove special chars
    for i in special1:
        para = para.replace(i, '')

    # printing resultant string
    # print ("After Remove special char : " + str(para))
    return para


def stringmethod(para, special1, special2, list1, strfind):

    print("", end="\n")

    # Remove all the special characters from para specified in special1 and save them in the variable word1.
    word1 = remove_special_characters(para, split_string_to_chars(special1))
    print(word1)
    print("", end="\n")

    # Get the first 70 characters from word1, reverse the strings, save it in variable rword2, and print it.
    first70chars = word1[0:70]
    # print(first70chars)
    rword2 = first70chars[::-1]
    print(rword2)

    # Remove all the wide spaces from rword2, join the characters using the special character specified in special2, and print the joint string.

    # para = remove_special_characters(para, special2)
    # print(para)
    return None


def split_string_to_chars(special1):
    return [char for char in special1]


if __name__ == "__main__":
    # main()
    # greet("Monica", "Luke", "Steve", "John")
    # greet()

    para = '''
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam sem odio, varius nec aliquam nec, tempor commodo ante. Pellentesque sit amet augue vel ante dictum placerat ut ut sapien. Proin maximus eu diam in posuere. Suspendisse in lectus in lectus finibus auctor. Nam sed porttitor arcu. Vestibulum augue odio, posuere quis libero sed, pharetra sollicitudin est. Donec sit amet nunc eu nisi malesuada elementum id ut purus.Nunc sit amet % massa rhoncus, venenatis eros sit amet, ornare augue. Nunc a mi sed est tincidunt facilisis at nec diam. Donec nec ex lorem. Morbi vitae diam tincidunt, dignissim arcu ut, facilisis nisi. Maecenas non felis #ullamcorper, viverra augue id, consequat_nunc. Suspendisse potenti. Proin tempor, sapien ut ornare placerat, sapien mauris luctus sapien, eget aliquam turpis urna at quam. Sed a&eros vel@ ante vestibulum vulputate. Suspendisse vitae vulputate velit. Suspendisse! ligula nisl, semper ut sodales et, ultricies porttitor felis. Nunc ac mattis erat, aliquet pretium risus. Nullam quis congue lacus, et mollis nulla. Nunc laoreet in nisi sit amet facili*sis. Cras rutrum justo ut eros mollis volutpat. Sed quis mi nunc. Nunc sed bibendum nibh, quis bibendum tortor.
    '''
    special1 = ",_!@*%#$."
    special2 = ","
    list1 = ["adipiscing", "Aliquam", "Suspendisse"]
    strfind = "vulputate"

    stringmethod(para, special1, special2, list1, strfind)
