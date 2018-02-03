# Medical-data-analysis
对儿童医疗数据进行分析，辅助医生诊断。

代码运行：
--------------
	1、运行medical_predict.py进行预测。
	2、输入相应的age、cure_before（治疗前的疗效，分为5个等级），输入当前诊断。
	
输出结果：
--------------
	1、给出以往最近的5个相似病人用药情况及疗效供医生参考。
	2、模型推荐的药品（共分为西药、中成药、中草药、检查及检验）
	3、输出可能伴随的疾病，起到预防作用（主要利用关联分析找到疾病之间的关系）

部分结果展示：
输入：
--------------
	age:1
	cure_before:1
	diag:P05.102,P70.400,P83.100
		
输出最近几个相似病人：
---------------
		feature: age.0_1 cure_before.1 新生儿低血糖症 新生儿中毒性红斑 足月小样低体重儿
		result_1: cure_after.1 尿常规定量(干化学+尿沉渣) 急诊血培养(需氧+真菌)(住院) 急诊白蛋白(快测ALB) 碳酸氢钠注射液(塑料瓶) 急诊血常规+网织红细胞计数 粪常规+OB 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒) 维生素K1注射液 急诊肾功(干化学法) 急诊C反应蛋白(快测CRP)快测C反应蛋白 急诊肝功(干化学法) 地锌油
		result_2: cure_after.2 中段尿培养及鉴定+菌落计数(住院) 注射用头孢呋辛钠 维生素K1注射液 碳酸氢钠注射液(直立式聚丙烯输液袋) 碳酸氢钠注射液 红霉素眼膏 急诊肝功(干化学法) 粪常规+OB 急诊C反应蛋白(快测CRP)快测C反应蛋白 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒) 尿常规定量(干化学+尿沉渣) 双歧杆菌乳杆菌三联活菌片(金双歧) 急诊肌酸激酶同工酶质量测定(CKMB) 肝素钠注射液 注射用头孢唑林钠 地锌油 急诊血常规+网织红细胞计数 急诊血培养(需氧)(住院) 双肾、输尿管、膀胱彩超
		result_3: cure_after.9 注射用头孢呋辛钠 心脏彩超+左心功能测定(舒张功能) 注射用哌拉西林钠他唑巴坦钠 维生素K1注射液 开塞露 肝素钠注射液 急诊尿常规定量(干化学+尿沉渣) 急诊肝功(干化学法) 粪常规+OB 肝胆胰脾双肾彩超 急诊C反应蛋白(快测CRP)快测C反应蛋白 腹部立位(DR) 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒) 青霉素皮试剂 尿常规定量(干化学+尿沉渣) 急诊粪常规+OB 双歧杆菌乳杆菌三联活菌片(金双歧) 急诊血培养(需氧+真菌)(住院) 急诊肌酸激酶同工酶质量测定(CKMB) 床边拍片 注射用头孢唑林钠 地锌油 甲状腺三项(同位素) 急诊肌酐(快测CRE) 急诊血常规+网织红细胞计数 急诊尿素(快测UREA) 急诊血培养(需氧)(住院)
		result_4: cure_after.3 血培养+药敏(需氧)（住院） 碳酸氢钠注射液 急诊粪常规+OB 急诊尿常规定量(干化学+尿沉渣) 碳酸氢钠注射液(塑料瓶) 急诊血常规+网织红细胞计数 急诊肝功(干化学法) 维生素K1注射液 注射用头孢唑林钠 注射用头孢美唑 血常规(6岁以下，儿童专用) 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒) 地锌油 急诊C反应蛋白(快测CRP)快测C反应蛋白
		result_5: cure_after.1 注射用头孢呋辛钠 维生素K1注射液 开塞露 碳酸氢钠注射液 肝素钠注射液 急诊尿常规定量(干化学+尿沉渣) 急诊肝功(干化学法) 急诊C反应蛋白(快测CRP)快测C反应蛋白 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒) 急诊粪常规+OB 注射用头孢唑林钠 地锌油 急诊肌酐(快测CRE) 急诊血常规+网织红细胞计数 急诊尿素(快测UREA) 急诊血培养(需氧)(住院)

			
模型推荐：
-------------
		西药（A）: 碳酸氢钠注射液 注射用头孢呋辛钠 维生素K1注射液 注射用头孢唑林钠 地锌油
		中成药（B）:
		中草药（C）:
		检验（D）: 尿常规定量(干化学+尿沉渣) 急诊肝功(干化学法) 急诊血常规+网织红细胞计数 粪常规+OB 急诊血培养(需氧)(住院) 急诊C反应蛋白(快测CRP)快测C反应蛋白 优生全套IgM(弓形体、风疹病毒、巨细胞病毒、单纯疱疹病毒)
		检查（E）:
		疗效： 1
		与之相关的疾病有: [(['P59.901'], '0.480769230769'), (['P07.300'], '0.451505016722'), (['P23.900'], '0.391304347826')]
		新生儿高胆红素血症 0.480769230769
		孕29+3周早产儿(适于胎龄儿) 0.451505016722
		新生儿肺炎 0.391304347826
		
