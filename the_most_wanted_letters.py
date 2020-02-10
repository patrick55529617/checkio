import string

def checkio(text: str) -> str:
    text = text.lower()
    return max(string.ascii_lowercase, key = text.count)

    #total = 0
    #lower = text.lower()
    #most = lower[0]
    #for i in lower:
    #    if i.isalpha():
    #        if lower.count(i) > total:
     #           most = i
    #            total = lower.count(i)
      #      elif lower.count(i) == total:
       #         if i < most:
        #            most = i
         #           total = lower.count(i)
    #return most
if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
