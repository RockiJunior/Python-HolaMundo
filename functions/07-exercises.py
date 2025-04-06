# ----------------------------------------------------------- Usando slicing
# def is_palindrome(text):
#     cleaned_text = text.replace(" ", "").lower()
#     return cleaned_text == cleaned_text[::-1]  # Volteamos la cadena usando slicing


# ----------------------------------------------------------- Usando reversed y join
# def is_palindrome(text):
#     cleaned_text = text.replace(" ", "").lower()
#     return cleaned_text == "".join(reversed(cleaned_text))


# ----------------------------------------------------------- Usando while y comparando extremos
# def is_palindrome(text):
#     cleaned_text = text.replace(" ", "").lower()
#     left, right = 0, len(cleaned_text) - 1

#     while left < right:
#         if cleaned_text[left] != cleaned_text[right]:
#             return False
#         left += 1
#         right -= 1

#     return True


# ----------------------------------------------------------- Usando recursión
# def is_palindrome(text):
#     cleaned_text = text.replace(" ", "").lower()

#     if len(cleaned_text) <= 1:
#         return True

#     if cleaned_text[0] != cleaned_text[-1]:
#         return False

#     return is_palindrome(cleaned_text[1:-1])


# ----------------------------------------------------------- Usando bucle for
def is_palindrome(text):
    cleaned_text = text.lower().replace(" ", "")
    reversed_text = ""

    for char in cleaned_text:
        reversed_text = char + reversed_text
    return cleaned_text == reversed_text


print("A man, a plan, a canal: Panama: ",
      is_palindrome("A man, a plan, a canal: Panama"))


print("abba: ", is_palindrome("abba"))
