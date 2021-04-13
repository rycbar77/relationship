import jieba
import re


def cut_txt():
    jieba.load_userdict('name_dict.txt')
    jieba.load_userdict('userdict.txt')
    stop_words = [line.strip() for line in open('StopwordsCN.txt', encoding='utf-8').readlines()]  # 简体中文停用词

    with open('content.txt', 'r', encoding='utf-8') as f:
        content = f.readlines()

    with open('content_cut.txt', 'w', encoding='utf-8') as f:
        for i in content:
            if len(i) <= 10:
                pass
            else:
                sentences = i.split("。")
                for sentence in sentences:
                    words = list(jieba.cut(re.sub(r'[-，。？：“”！]+|第[0-9]*集', '', sentence.strip())))
                    w = [word for word in words if word not in stop_words]
                    cut = " ".join(w)
                    f.write(cut.strip() + '\n')


if __name__ == "__main__":
    cut_txt()
