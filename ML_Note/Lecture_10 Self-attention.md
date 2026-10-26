https://www.youtube.com/watch?v=hYdO9CscNes
随机的输入
	![[Pasted image 20261026150932.png]]
	e.g.文字的输入
		Way1、One-hot编码把文字转成向量（但是没有考虑文字之间的关系）
		Way2、Word enbedding
	e.g.声音的输入
		![[Pasted image 20261026151254.png]]
e.g.图（Greph）
	![[Pasted image 20261026151417.png]]
输入
	一堆输出同样数字的一堆（Sequence Labeling）
		![[Pasted image 20261026152642.png]]
	一堆输入一个输出
		e.g.知道网友对你的商品的评价是好的还是坏的，机器听一段声音，确定是谁说的
	一堆输入机器决定有多少一堆的输出（seq2seq）
先只考虑Sequence Labeling
	之前的玩法，直接每个向量扔进Fully-Connected
	![[Pasted image 20261026153221.png]]
	**把几个向量关联起来，互相建立联系**（比如HW2让你考虑整个数据集）
	![[Pasted image 20261026153312.png]]
	**如果不用self-attention开一个很大的window很容易过拟合，而且FCN里面参数不好调整**
	Self-attention
		![[Pasted image 20261026153638.png]]
		每个向量都考虑了这个句子，然后扔进FCN
		**可以用好几个Self-attention，不止一个**
		![[Pasted image 20261026153809.png]]
		![[Pasted image 20261026154132.png]]
		输入的向量之间的关联程度用α
		![[Pasted image 20261026154231.png]]
		与两个矩阵相乘，Query & Key
		![[Pasted image 20261026154446.png]]
		计算出关联性（attention score）
		**一般自己和自己也要做关联性**
		![[Pasted image 20261026154617.png]]
		最后进行soft-max(或者其他activation function)
		![[Pasted image 20261026155517.png]]
		b¹ = Σᵢ α'₁,ᵢ · vⁱ  = α'₁,₁v¹ + α'₁,₂v² + α'₁,₃v³ + α'₁,₄v⁴
		其中的α'已经进行过了归一化normalization
		从矩阵角度理解
			![[Pasted image 20261026160734.png]]
			![[Pasted image 20261026161014.png]]
			![[Pasted image 20261026161204.png]]
			**WQ，WK，WV是训练梯度算出来的**
		添加注意力头
			![[Pasted image 20261026161635.png]]
			![[Pasted image 20261026161644.png]]
		Positional Encoding
			确定这个字在的位置
			![[Pasted image 20261026162009.png]]
	Self-attention处理图片
		![[Pasted image 20261026163047.png]]
		![[Pasted image 20261026163140.png]]
Self-attention VS CNN
	**CNN可以看作是简化版的Self-attention**
	![[Pasted image 20261026163406.png]]
	![[Pasted image 20261026163459.png]]
	![[Pasted image 20261026163725.png]]
	**资料量大的时候Self-attention才会更好**
Self-attention VS RNN
	![[Pasted image 20261026164148.png]]
	FC指fully connected network，RNN也可以是双向的
		缺点：RNN没有办法平行处理，最前面的memory被带到最后很可能会被遗忘
		![[Pasted image 20261026164529.png]]
		![[Pasted image 20261026164619.png]]
		![[Pasted image 20261026164646.png]]
	Self-attention for Graph
		![[Pasted image 20261026164914.png]]
		![[Pasted image 20261026164939.png]]
		![[Pasted image 20261026165009.png]]
		Self-attention的运算量很大
		