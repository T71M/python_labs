from string_formatter import StringFormatter


str = "fhfh fjdfjfdj djfwkfjsjfdsf iwdfjwif jfjf dskfsdfsfj kfsl"

print(StringFormatter.delete_words(str, 5))

str1 = "password123 djfdifj3dof"

print(StringFormatter.swap_digits(str1))

str2 = "kwefimfwmfwimfiwmfiwmf dkdcmkd"

print(StringFormatter.split_for_every_symbol(str2))

str3 = "fjfldvm vmbngh vnmbf cmvn gbj kl o"

print(StringFormatter.sort_for_word_len(str3))

str4 = "hello this is example how to sort the word in alphabetical manner"

print(StringFormatter.sort_for_lexicographic(str4))
