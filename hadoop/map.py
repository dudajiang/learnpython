'''
wordcount单词统计
map阶段
'''

import sys

def map():
    for line in sys.stdin:
        words = line.split("\t")
        for word in words:
            print("\t".join([word.strip(),"1"]))



if __name__ == "__main__":
    map()