from matplotlib import pyplot as plt
import matplotlib.font_manager as fm

font = fm.FontProperties(fname='SimSun.ttf')
with open('name_dict.txt', encoding='utf-8') as f1:
    names = f1.readlines()
with open('content_cut.txt', encoding='utf-8') as f2:
    content = f2.read()

# from collections import defaultdict
count = {}
for name in names:
    count[name.strip()] = content.count(name.strip())
print(count)

count = sorted(count.items(), key=lambda x: x[1])
ay, ax = plt.subplots()
numbers = [x[1] for x in count[-10:]]
names = [x[0] for x in count[-10:]]
ax.barh(range(10), numbers, align='center')
ax.set_title('出场次数', fontsize=14, fontproperties=font)
ax.set_yticks(range(10))
ax.set_yticklabels(names, fontsize=14, fontproperties=font)
plt.show()
episodes = []
episode = ""
for i in content.split('\n'):
    if i == '':
        episodes.append(episode)
        episode = ""
    else:
        episode += i + ' '

# print(episodes)
