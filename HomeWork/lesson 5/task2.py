word = input("Введите слово из маленьких латинских букв: ")

vowels = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
consonants = 0

for letter in word:
    if letter in vowels:
        vowels[letter] += 1
    elif letter.isalpha() and letter not in vowels:
        consonants += 1
    else:
        print(False)
        break
else:
    print(f"Количество гласных: {sum(vowels.values())}")
    print(f"Количество согласных: {consonants}")
    for vowel, count in vowels.items():
        print(f"Количество буквы {vowel}: {count}")