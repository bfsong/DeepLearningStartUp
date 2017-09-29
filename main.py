class Keyword:
    word = ''
    count = 0

    def __init__(self, word, count):
        self.word = word
        self.count = count

    def value(self):
        return self.count

    def tostring(self):
        return '{}:{}'.format(self.word, self.count)

def getMinIndex(list):
    minCount = 999999
    minIndex = 0
    for i in range(0, len(list)):
        if list[i].value() <= minCount :
            minIndex = i
            minCount = list[i].value()
    return minIndex

def writeFile(list, filename):
    with open(filename, 'w') as file:
        for item in list:
            file.write(item.tostring())
            print(item.tostring())

map = {}
ignors = ['', '，', '。', '？', '!', '“', '”', '、', '（', '）', '；', '：', '　', '．', '…', '的', '是', '―']
list = []

#统计
with open('happiness_seg.txt') as file:
    for line in file:
        words = line[:len(line) -1].split(' ')
        count = len(words)

        for i in range(0, count - 1):
            if words[i] not in ignors and words[i+1] not in ignors:
                key = words[i] + ' ' + words[i+1]
                if key in map:
                    map[key] += 1
                else:
                    map[key] = 1

#获取出现频率最高的前 10 个
for key, count in map.items():
    if (len(list) < 10):
        list.append(Keyword(key, count))
    else:
        minIndex = getMinIndex(list)
        if count > list[minIndex].value() :
            del list[minIndex]
            list.append(Keyword(key, count))

#排序 & 输出
list.sort(key=Keyword.value, reverse=True)
writeFile(list, 'result.txt')
print('结果已经保存到result.txt中')
