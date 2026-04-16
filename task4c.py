def surprising(L:list[str], other:str) -> list[str]:
    L.append(other.upper())
    return L


words = ["this", "is", "confusing", "code."]
first = surprising(words, "Avoid")
second = surprising(words, "such.")
         # What is the value of words at this point? ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What are the values of first and second at this point? first  = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
# second = ["this", "is", "confusing", "code.", "AVOID", "SUCH."]
         # What happened? the function modified the original list using append
print()