def reverse(text):
    if text == "":
        return ""
    return reverse(text[1:]) + text[0]

text = input("Enter a string: ")
print("Reversed String =", reverse(text))
