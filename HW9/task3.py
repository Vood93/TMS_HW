import os


def find_most_frequent_word(text):
    """Находит самое частое слово в строке.
    Args:
      text: Строка для анализа.
    Returns:
      Кортеж (слово, количество повторений).
    """

    word_count = {}
    words = text.split()
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Находим слово с максимальным количеством повторений
    most_common_word = max(word_count, key=word_count.get)
    return most_common_word, word_count[most_common_word]


def process_file(input_file, output_file):
    """Обрабатывает файл, записывая результаты в новый файл.
    Args:
      input_file: Путь к входному файлу.
      output_file: Путь к выходному файлу.
    """

    with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
        for line in f_in:
            word, count = find_most_frequent_word(line.strip())
            f_out.write(f"{word} {count}\n")


# Задаем пути к файлам
input_path = os.path.join("txt_files/text.txt")
output_path = os.path.join("txt_files/result.txt")

# Обрабатываем файл
process_file(input_path, output_path)
print("Выполнено.")
