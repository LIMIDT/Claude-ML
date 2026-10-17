随机的几率分布取样（输出文字）
	过去的互动也会产生影响

LLM（语言模型）：语言接龙的模型

training的时候要上网搜寻找到function，testing的时候不用


function的找到：人类进行督导式学习，大量的正确输入和输出，对不同的字样判断几率
![[Pasted image 20261017150626.png]]机器从网上的资料进行反向学习，自己找到function


机器学习：目的让机器自己找到function
根据function输出来分类：
	回归（Regression）
		函数输出的是一个数值
	分类（classification) 
		函数输出的是一个类别（做选择题）e.g.垃圾邮件过滤

生成式学习（Structured Learning）


找出function的步骤：
	1、设定范围（确定候选函数的集合（Model））
		深度学习中的神经网络的结构（CNN，RNN，Transfomer）都是不同候选函数的集合
	2、确定标准 
	（Loss function）
		越小函数越好
		要确定标准答案（属于是Supervised Learning)
		Loss function取决于训练资料
	（Semi-Supervised Learning）
		L（f_1）=输出距离正确答案+与真实的差距
	3、达成目标（找到最好的函数——最佳化（Optimization)
		找到一个function是的他的Loss最小
		How to find：
			https://youtu.be/yKKNr-QKz2Q
			https://youtu.be/ibJpTrp5mcE
	![[Pasted image 20261017161235.png|654]]


==**通过三个步骤确定论文里面的方法是哪个层面**==
