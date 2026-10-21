https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.player.switch&vd_source=af4cf07579045595f3fad858b9bfb593&p=17
1、Deep Learning's ups and downs
	1958：Perceptron
	1969：Perceptron has limitation
	1980s：Muti-layer perceptron
		Do not have significant difference from DNN
	1986：backpropagation
	1989： 1 hidden layer is "good enough?"
	2006：RBM initialization**受限玻尔兹曼机**（Restricted Boltzmann Machine）(breakthrough)
	 2009：GPU
	 2011：Strat to be popular
	 2012：win ILSVRC image competition
2、Three Step for Deep Learning
	Step 1 ：Neural Network
		不同连接方式
			Fully Connect Feedforward Network![[Pasted image 20261021164638.png]]![[Pasted image 20261021164714.png]]
			可以将整个过程看作是define一个set function
			开始考虑多个的情况
			![[Pasted image 20261021165132.png]]
			**Fully**
			Deep就是有很多hidden layers
			**其中进行的是矩阵运算**![[Pasted image 20261021165651.png]]
			上图中的黄色是weight，蓝色是bias，中间是激活function
			![[Pasted image 20261021165919.png]]
			这一过程可以用GPU加速
			![[Pasted image 20261021170320.png]]
			output是对应到每一个数字的概率
			![[Pasted image 20261021170531.png]]
			对于影像识别和语音识别来说其实找到更好的**neural network比找到feature更重要**
	Step 2：定义模型好坏
		![[Pasted image 20261021171350.png]]
		Cross Entropy（交叉熵）
			![[Pasted image 20261021172003.png]]
			用来衡量留给正确答案不同概率的损失
			![[Pasted image 20261021172207.png]]
			softmax function
				把一堆任意分数，变成一堆概率加起来等于 1
	Step 3：找到最小的Loss
		![[Pasted image 20261021172355.png]]
		用梯度下降解决上面的问题，找到最小的Total Loss
		![[Pasted image 20261021172512.png]]
		