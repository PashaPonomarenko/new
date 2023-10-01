import random

a = input("Введіть рядок слів, розділених пробілами: ")

#Розділяємо рядок на слова
words = a.split()

# Виводимо слова, що починаються з великої літери
capitalized_words = [word for word in words if word[0].isupper()]

for word in capitalized_words:
    print(word)


# Перемішуємо слова у випадковому порядку
random.shuffle(words)

# Об'єднуємо перемішані слова в рядок і виводимо
b = ' '.join(words)
print(b)
