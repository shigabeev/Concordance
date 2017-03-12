lines = []
with open('Tolstoy.txt', 'r') as f:
    for line in f:
        temp = line.lower()
        #temp = temp.replace(stop, '') for stop in [',', '-', '.', '?', '–']
        for stop in [',', '-', '.', '?', '–']:
            temp = temp.replace(stop, '')
        lines.append(temp.split())
print(lines[30:100])
dic = {}
for line in lines[30:100]:
    for i, word in enumerate(line):
        if word in dic:
            if i>1:
                dic[word].append(line[i-1])
            if i<len(line)-1:
                dic[word].append(line[i+1])
        else:
            dic[word] = []
            if i>1:
                dic[word].append(line[i-1])
            if i<len(line)-1:
                dic[word].append(line[i+1])
print(dic)

# TODO
# Сделать так чтобы принимал параметры. Больше контекста жрать и учитывать положение в предложении.
# Принимает 4 параметра: папка с вводными файлами (может быть несколько)
# Левый и правый контекст — сколько слов влево, сколько слов вправо
# Учитывать ли границу предложения
# Принудительное ограничение количества слов.
#
#
