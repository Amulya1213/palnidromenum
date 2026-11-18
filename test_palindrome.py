from palindrome import palindrome

def test_palindrome():
    assert palindrome(121) == True

def test_not_palindrome():
    assert palindrome(123) == False

def test_single_digit():
    assert palindrome(5) == True