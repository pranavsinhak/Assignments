char = input("Enter a character: ")

if len(char) != 1:
    print("Please enter exactly one character.")
else:
    ascii_val = ord(char)

    if 65 <= ascii_val <= 90:
        print("It is an uppercase letter.")
    elif 97 <= ascii_val <= 122:
        print("It is a lowercase letter.")
    elif 48 <= ascii_val <= 57:
        print("It is a digit.")
    else:
        print("It is a special symbol.")
