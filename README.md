### 本工具没有使用机器学习与自然语言处理库，适用于简单判断两个HTML表格的相似度,移植可用

| 一个普通标题 | 一个普通标题 | 一个普通标题 |
| ------ | ------ | ------ |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

| 一个普通标题 | 一个普通标题 | 一个普通标题 |
| ------ | ------ | ------ |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 与上面表格不同 |


本工具代码中采用了三种对比方式，来计算两张表格的相似度

### 1.Levenshtein 距离
具体解释 参考：https://en.wikipedia.org/wiki/Levenshtein_distance

### 2.Jaccard系数计算+jieba分词方法
Jaccard系数计算：https://en.wikipedia.org/wiki/Jaccard

### 3.Cosin相似度+jieba分词方法
Cosin相似度：https://baike.baidu.com/item/%E4%BD%99%E5%BC%A6%E7%9B%B8%E4%BC%BC%E5%BA%A6/17509249?fr=aladdin

