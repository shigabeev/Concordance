import json
import sys
import os

if __name__ == "__main__":
    # Settings
    left = 2
    right = 2
    start_line = 30
    end_line = 200       # None for unlimited
    export = "DB.json"
    folder = "Data"
    # defaults override
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    if len(sys.argv) > 2:
        left = sys.argv[2]
    if len(sys.argv) > 3:
        right = sys.argv[3]
    # /settings
    dic = {}
    files = os.listdir(folder)
    for filename in files:
        if filename[0] == '.':
            continue
        with open("%(folder)s/%(file)s" % {'folder': folder, 'file': filename}, 'r', encoding="utf-8") as f:
            for line in f.readlines()[start_line:end_line]:
                words = line.lower()                         # Tokenizing
                for stop in [',', '-', '.', '?', '–']:      # symbols to avoid
                    words = words.replace(stop, '')
                words = words.split()
                for i, word in enumerate(words):
                    if word not in dic:
                        dic[word] = []
                    for l in range(1, left+1):
                        if i > l:
                            dic[word].append(words[i - l])
                    for r in range(1, right+1):
                        if i < len(words) - r:
                            dic[word].append(words[i + r])
    with open(export, 'w') as f:
        json.dump(dic, f, ensure_ascii=False)

# TODO
# Сделать так чтобы принимал параметры. Больше контекста жрать и учитывать положение в предложении. - Done
# Принимает 4 параметра: папка с вводными файлами (может быть несколько) - Done
# Левый и правый контекст — сколько слов влево, сколько слов вправо - Done
# Учитывать ли границу предложения
# Принудительное ограничение количества слов.
# Улучшить работу с памятю. Использовать кольцевой буфер
#
