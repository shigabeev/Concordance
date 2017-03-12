import json
import sys
import os

if __name__ == "__main__":
    if len(sys.argv) == 2:      # takes only one input file for now
        folder = sys.argv[1]
    else:
        folder = "Data"
    # Settings
    left = 2
    right = 2
    start_line = 30
    end_line = 100
    export = "DB.json"
    # /settings
    dic = {}
    files = os.listdir(folder)
    for filename in files:
        lines = []
        with open("%(folder)s/%(file)s" % {'folder': folder, 'file': filename}, 'r') as f:
            for line in f:
                temp = line.lower()                         # Tokenizing
                for stop in [',', '-', '.', '?', '–']:      # symbols to avoid
                    temp = temp.replace(stop, '')
                lines.append(temp.split())
        for line in lines[start_line:end_line]:
            for i, word in enumerate(line):
                if word not in dic:
                    dic[word] = []
                for l in range(1, left+1):
                    if i > l:
                        dic[word].append(line[i - l])
                for r in range(1, right+1):
                    if i < len(line) - r:
                        dic[word].append(line[i + r])
    with open(export, 'w') as f:
        json.dump(dic, f, ensure_ascii=False)

# TODO
# Сделать так чтобы принимал параметры. Больше контекста жрать и учитывать положение в предложении. - Done
# Принимает 4 параметра: папка с вводными файлами (может быть несколько) - Done
# Левый и правый контекст — сколько слов влево, сколько слов вправо - Done
# Учитывать ли границу предложения
# Принудительное ограничение количества слов.
#
#
