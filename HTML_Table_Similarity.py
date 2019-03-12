# -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import Levenshtein
import sys
import time
import jieba
from jieba import posseg
import math

class SimilarityWholeHTML(object):
    """
    get HTMlsimilarity whole
    @:param HTMLText string
    """
    def __init__(self):
        pass

    def getLevenshteinSimilarity(self, str1, str2):
        soupfcontent1 = BeautifulSoup(str(str1), "html.parser")
        soupfcontent2 = BeautifulSoup(str(str2), "html.parser")
        similarity = Levenshtein.ratio(soupfcontent1.get_text(), soupfcontent2.get_text())


class SimilarityHTMLTable(object):
    """
    get HTMlsimilarity by <table> or <p> <span> etc
    @:param HTMLText string
    """
    def __init__(self):
        pass

    def getLevenshteinSimilarity(self, str1, str2):
        soupfcontent1 = BeautifulSoup(str(str1), "html.parser")
        content_table1 = soupfcontent1.find_all('table')
        soupfcontent2 = BeautifulSoup(str(str2), "html.parser")
        content_table2 = soupfcontent2.find_all('table')

        for i in range(0, len(content_table1)):
            for j in range(0, len(content_table2)):
                similarity = Levenshtein.ratio(content_table1[i].get_text(), content_table2[j].get_text())
                print similarity

    def getJaccradSimilarity(self,str1, str2):  # terms_reference为源句子，terms_model为候选句子
        temp=int()
        soupfcontent1 = BeautifulSoup(str(str1), "html.parser")
        content_table1 = soupfcontent1.find_all('table')
        soupfcontent2 = BeautifulSoup(str(str2), "html.parser")
        content_table2 = soupfcontent2.find_all('table')

        terms_reference = jieba.cut(str(content_table1))  # 默认精准模式
        terms_model = jieba.cut(str(content_table2))
        grams_reference = set(terms_reference)  # 去重；如果不需要就改为list
        grams_model = set(terms_model)
        for i in grams_reference:
            if i in grams_model:
                temp = temp + 1
        fenmu = len(grams_model) + len(grams_reference) - temp  # 并集
        print temp
        print fenmu
        jaccard_coefficient = float(float(temp) / float(fenmu))  # 交集
        print jaccard_coefficient

    def getCosinSimilarity(self,str1, str2):
        soupfcontent1 = BeautifulSoup(str(str1), "html.parser")
        content_table1 = soupfcontent1.find_all('table')
        soupfcontent2 = BeautifulSoup(str(str2), "html.parser")
        content_table2 = soupfcontent2.find_all('table')

        cut_str1 = [w for w, t in posseg.lcut(str(content_table1)) if 'n' in t or 'v' in t]
        cut_str2 = [w for w, t in posseg.lcut(str(content_table2)) if 'n' in t or 'v' in t]
        # 列出所有词
        all_words = set(cut_str1 + cut_str2)
        # 计算词频
        freq_str1 = [cut_str1.count(x) for x in all_words]
        freq_str2 = [cut_str2.count(x) for x in all_words]
        # 计算相似度
        sum_all = sum(map(lambda z, y: z * y, freq_str1, freq_str2))
        sqrt_str1 = math.sqrt(sum(x ** 2 for x in freq_str1))
        sqrt_str2 = math.sqrt(sum(x ** 2 for x in freq_str2))
        cosin_similarity = sum_all / (sqrt_str1 * sqrt_str2)
        print cosin_similarity

if __name__ == '__main__':
    reload(sys)
    sys.setdefaultencoding("utf-8")
    getSimilarity = SimilarityHTMLTable()
    str1=""
    str2=""
    for i in range(0,1000):
        getSimilarity.getJaccradSimilarity(str1,str2)
    t2 = time.time()
    print t2 - t1

