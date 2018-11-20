# 什么是数据分析与挖掘技术
    # 所谓数据分析，即对已知的数据进行分析，然后提取出一些有价值的信息，比如统计平均数，标准差等信息。
    # 数据分析的数据量有时可能不会太大。
    # 数据挖掘，是指对大量的数据进行分析与挖掘，得到一些未知的，有价值的潜在信息。
    # 比如从网站的用户或用户行为数据中挖掘出用户的潜在需求信息，从而对网站进行改善等。
    # 数据分析与数据挖掘密不可分，数据挖掘是数据分析的提升。

# 数据分析与挖掘技术能做什么事情
    # 数据挖掘技术可以帮助我们更好的发现事物之间的联系与规律。
    # 我们可以利用数据挖掘技术实现数据规律的探索
    # 比如啤酒和尿不湿的潜在联系指导超市货架的物品摆放
    # 比如发现窃电用户，发掘用户潜在需求，实现信息的个性化推送，发现疾病与症状深知疾病与药物之间的规律

# 数据挖掘的过程
    # 定义目标明确需求--->获取数据(爬虫采集；自有数据)--->数据探索
    # --->数据预处理(数据清洗去除脏数据，数据集成将不同来源的数据放置在一起，数据变换规范化我们的数据，数据规约合并精简我们的数据)
    # --->挖掘建模(分类，聚类，关联，预测)(这一步算法是关键！)
    # --->模型评价与发布

# 数据分析与挖掘的python相关模块(cmd->pip list命令查看本机安装好的模块)
    # numpy 数组支持，其他模块的基础
    # pandas 数据探索和分析
    # matplotlib 作图与可视化
    # scipy 矩阵运算，积分，傅里叶变换，微分方程...
    # statsmodels 统计分析
    # Gensim 文本挖掘
    # sklearn 机器学习
    # keras 深度学习


# python导入数据
    # 导入csv数据
        # i1 = pandas.read_csv("文件地址")
        # i1.describe()
        # i1.sort_values(by="列名")
        # print(i1)
        
    # 导入excel数据
        # i2 = pandas.read_excel("文件地址")
        # print(i2)
        
    # 导入MySQL数据
        # conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='Devilhunter9527', db='dangdang', charset='utf8', use_unicode=True)
        # sql = "select * from ..."
        # i3 = pandas.read_sql(sql, conn)
        # i3.describe()
        # print(i3)
        
    # 导入html的<table>数据
        # i4 = pandas.read_html("文件地址或url")
        # print(i4)
        
    # 导入文本数据
        # i5 = pandas.read_html("文件地址")
        # print(i5)




    
