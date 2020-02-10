def checkio(data: str) -> bool:
    if len(data) < 10 or len(data) > 64:
        return False
    has_upper = False
    has_lower = False
    has_digit = False
    for ch in data:
        if ch.isupper(): has_upper = True
        elif ch.islower(): has_lower = True
        elif ch.isdigit(): has_digit = True
    
    return (has_upper and has_lower and has_digit)

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

