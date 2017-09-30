#基础任务
from collections import Counter
from zhon.hanzi import punctuation

#读取文件内容
with open('happiness_seg.txt') as file:
    content = file.read()

#拆分
words = content.split()

#去除标点
words = list(word for word in words if word not in punctuation)

#生成二元词组
words = list(zip(words[:-1], words[1:]))

#获取出现频率最高的前 10 个
print(Counter(words).most_common(10))
