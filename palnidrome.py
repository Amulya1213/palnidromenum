import sys

def is_palindrome(text):
    return text == text[::-1]

if __name__ == "__main__":
    word = sys.argv[1]

    if is_palindrome(word):
        print("Palindrome")
    else:
        print("Not Palindrome")