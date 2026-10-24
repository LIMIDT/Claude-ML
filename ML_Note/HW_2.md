https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.videopod.episodes&vd_source=af4cf07579045595f3fad858b9bfb593&p=22
![[Pasted image 20261023173401.png]]
该模型没有设置早停，所以改变了学习率训练时间不会变，如此改变学习率的同时也要增加epoch，不然可能还没到最低但是次数已经是上限了
总的步数是轮数×batch数

在Medium里面卡住了很久，开始添加batchnorm(BN)
原理
	**把某一层的输出，按这个 batch 统计出来的均值和标准差，重新拉回“均值 0、标准差 1”的尺度。**
为什么？
	![[Pasted image 20261024143628.png]]
好处
	1、允许更大的学习率
		![[Pasted image 20261024144751.png]]
	2、梯度传播的更远
		![[Pasted image 20261024144854.png]]
	3、有正则化效果
		正则化
			防止模型背答案，太弱会过拟合，太强会欠拟合
		![[Pasted image 20261024145236.png]]
	**为什么BN收益不明显？？**
		![[Pasted image 20261024152739.png]]

添加Dropout
	原理: 在训练时候随机关掉一些神经元
		![[Pasted image 20261024153949.png]]
	为什么有效
		1、防止“共适应”
			![[Pasted image 20261024154059.png]]
		2、把子网络意见平均
			![[Pasted image 20261024154145.png]]
		3、参数调整与区别
			![[Pasted image 20261024154220.png]]

开始使用RNN
	原理
		RNN使得模型从只能看8帧变成可以看到整个音频
	改动地方
		1、把数据从拼帧变成保持
			**注意要进行padding，不然无法被堆叠**
			![[Pasted image 20261024173032.png]]
			同时还要进行mask，告诉模型哪些是不需要的
		2、模型换成LSTM（普通RNN记不住长序列）
			关于几个方式之间的区别
				https://www.bilibili.com/video/BV1JBDmB8EdT/?spm_id_from=333.1391.0.0