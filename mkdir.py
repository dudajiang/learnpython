# -*- coding: utf-8 -*-
def mkdir(path):
    # 引入模块
    import os
 
    # 去除首位空格
    path=path.strip()
    # 去除尾部 \ 符号
    path=path.rstrip("//")
 
    # 判断路径是否存在
    # 存在     True
    # 不存在   False
    isExists=os.path.exists(path)
 
    # 判断结果
    if not isExists:
        # 如果不存在则创建目录
        # 创建目录操作函数
        os.makedirs(path) 
 
        print path+' 创建成功'
        return True
    else:
        # 如果目录存在则不创建，并提示目录已存在
        print path+' 目录已存在'
        return False
 
# 定义要创建的目录
# mkpath="000-inbox-我的inbox体系//001-page-网页暂存"
# 调用函数
# mkdir(mkpath)

mkpaths = [''000-inbox-我的inbox体系',
'000-inbox-我的inbox体系//001-page-网页暂存',
'000-inbox-我的inbox体系//002-得到',
'000-inbox-我的inbox体系//003-读书心得',
'000-inbox-我的inbox体系//004-来自手机',
'000-inbox-我的inbox体系//005-灵感',
'010-Working Space-工作台',
'010-Working Space-工作台//011-worklog-今年的工作日记',
'100-Work-工作',
'100-Work-工作//101-Archive-往年的工作日记',
'100-Work-工作//102-Communications technology-通信行业',
'100-Work-工作//103-Devops-开发管理',
'200-Learning-学习',
'200-Learning-学习//201-Method-学习方法',
'200-Learning-学习//202-Future-未来会怎样',
'200-Learning-学习//203-Reading-读书听书',
'200-Learning-学习//203.001-dongwu-冬吴相对论',
'200-Learning-学习//203.002-product-产品之道',
'200-Learning-学习//203.003-google-吴军的谷歌方法论',
'210-Codeing-开发',
'210-Codeing-开发//211-js-前后端可用',
'210-Codeing-开发//212-python-运维利器',
'210-Codeing-开发//213-DB-数据库',
'210-Codeing-开发//219-Tools-工具使用',
'220-Mgm-管理学',
'220-Mgm-管理学//221-Qinghua-宁向东的清华管理科',
'230-Econ-经济学',
'230-Econ-经济学//231-Peking-薛兆丰北大经济学',
'240-Promote-心理学脑神经基因',
'240-Promote-心理学脑神经基因//241-Psy-心理学',
'240-Promote-心理学脑神经基因//242-Gene-基因发展',
'240-Promote-心理学脑神经基因//243-Flow-心流',
'250-AI-人工智能大数据',
'250-AI-人工智能大数据//251-Basic-人工智能基础',
'260-Comm-沟通交流及幽默',
'260-Comm-沟通交流及幽默//261-Humor-幽默',
'260-Comm-沟通交流及幽默//262-Expression-表情',
'270-Tools-工具',
'270-Tools-工具//271-template-参考模板',
'300-Life-生活',
'300-Life-生活//301-Baby Moonshine-成长点滴',
'300-Life-生活//302-Life Bank-生活资料库',
'300-Life-生活//303-Life Exp-生活经验',
'300-Life-生活//304-Tour-旅游',
'300-Life-生活//305-Class-老同学',
'300-Life-生活//306-Dearwife-老婆的存档库',
'400-Meaning-兴趣',
'400-Meaning-兴趣//401-Fit-游泳跑步健身',
'400-Meaning-兴趣//402-Lego-乐高',
'400-Meaning-兴趣//403-History-思考历史',
'400-Meaning-兴趣//404-Ancient Chinese-易经中医',
'400-Meaning-兴趣//405-Poem-诗意的表达',
'410-Stock-股票',
'410-Stock-股票//411-Financial-财务基础',
'410-Stock-股票//412-AI-用AI探索股票之道']

newflag = 0
exitflag = 0
for name in mkpaths:
    aa = mkdir(name)
    if aa:
        newflag += 1
    else:
        exitflag += 1

print '新建目录数量：'+newflag
print '原有目录数量：'+exitflag

        