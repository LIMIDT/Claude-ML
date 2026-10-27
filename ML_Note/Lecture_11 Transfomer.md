https://www.youtube.com/watch?v=n9TlOhRjYoc
**本质上是Sequence2Sequence的一种架构
	输入sequence，输出sequence
	应用
		语音辨识
			输入声音，输出文字
		机器翻译
		语音翻译
			可以把没有文字的语言翻译成我们看得懂的文字 
			同时也可以做文字转声音生成
		训练聊天机器人
			Natural Language Processing（NLP），判断文章是好还是坏的sentiment analysis本质上也是一个Question and Answer->**sequence to sequence**
		用特质的模型面对特定的问题比用sequence2sequence更好
		文本剖析
			https://arxiv.org/abs/1412.7449
		Multi-label Classification
			![[Pasted image 20261027203232.png]]
			机器可以决定输出多少东西
		图像分割
			![[Pasted image 20261027203345.png]]
			https://arxiv.org/abs/2005.12872
Sequence2Sequence
	架构
		![[Pasted image 20261027203616.png]]
		encoder（被输入一组向量）
			![[Pasted image 20261027203849.png]]
			self-attention、RNN、CNN都是
			![[Pasted image 20261027203947.png]]
			然而在transfomer里面还有变化（residual connection）
			![[Pasted image 20261027204409.png]]
			**一个block里面的过程**，进行了左边的运算以后才去右边进行Fully Connected
			用的是layer normalization，不是batch，不用考虑。要进行两次normalization
			![[Pasted image 20261027205012.png]]
			前向传播就是fully neural network
			![[Pasted image 20261027205113.png]]
			 **在transfomer里为什么做的是layer的normalization不是batch的normalization？**
				 通俗理解：batch是和“其他人”一起进行标准化，layer是和自己对比进行标准化
				![[Pasted image 20261027210615.png]]
				![[Pasted image 20261027210806.png]]
		decoder（输出一组向量）
			Autoregressive的decoder
				![[Pasted image 20261027211505.png]]
				1、用一个特殊的token作为开始，输出一个特殊的很长的向量，长度为你觉得机器可能输出的字符数量产生这个向量之前先进行softmax，分数最高的作为第一个输出
				2、把第一个输出作为输入和begin的token两个进行输入输出第二个
				![[Pasted image 20261027211920.png]]
				但是存在“一步错，步步错”的可能（和residual connection在encoder里面一样）
				![[Pasted image 20261027212718.png]]
				第一个encoder和decoder不一样的地方是多了一个mask
					mask-attention
						![[Pasted image 20261027212328.png]]
						产生b1的时候只考虑a1，不考虑别的
						![[Pasted image 20261027212533.png]]
						这是self-attention👆
						![[Pasted image 20261027212608.png]]
						mask的self-attention就只考虑了第一二个👆
						对decoder，是先有a1然后a2再a3最后a4，**是一个一个产生的，只能考虑左边的**
					decoder还要自己决定输出的长度
						（encoder是输入几个输出几个）所以不仅要begin还要有end，不然不会停下来，但是要让机器知道自己什么时候end
			Non-autoregressive（NAT）
				直接输出一句话，但是怎么知道该放多少个begin？
				![[Pasted image 20261027213904.png]]
					1、另外训练一个classifier，输出长度的字数
					2、直接让他输出一长串的字数，end后面的就不要
				优势
					1、跑得更快
					2、平行化，不会互相影响
					3、比较能控制输出的长度
				NAT
					![[Pasted image 20261027214519.png]]
		encoder&decoder
			![[Pasted image 20261027214626.png]]
			cross attention
				两个的链接部分
				![[Pasted image 20261027214848.png]]
				a1a2a3是经过normalization的
					![[Pasted image 20261027215123.png]]
					sequence2sequence的语音辨识👆
				一般来说每个encoder都要和decoder的每一层都要cross，但是也有不同的玩法
					![[Pasted image 20261027215857.png]]
	Training
		![[Pasted image 20261027220341.png]]
		先对正确答案的“机”进行one-hot编码，然后算正确答案和预测之间的交叉熵👆（和分类很像）
		![[Pasted image 20261027220620.png]]
		**在训练的时候decoder的输入是正确答案**（Teacher Forcing）
		![[Pasted image 20261027220840.png]]
训练的时候tips
	Copy Mechanism
		应用
			Chat-bot
			![[Pasted image 20261027221633.png]]
			不用考虑这个明知是谁名字是谁，看见“我是谁谁谁”的时候就照着回答👆
			![[Pasted image 20261027221713.png]]
			训练一个专门读摘要的model👆 
	Guided Attention（强迫机器学习每一个例子，强迫attention的时候有固定的方式）
		e.g.语音辨识，语音合成，TTS，Monotonic Attention，Location-aware attention
		![[Pasted image 20261027222511.png]]
		强迫机器从左往右👆
	Beam Search
		Greedy Decoding
		![[Pasted image 20261027223210.png]]
		![[Pasted image 20261027223356.png]]
		如何找到绿色的路👆，Beam Search
		**beam search之适合只有一个答案的任务，不是很有创造性**
	Optimizing Evaluation Metrics
		![[Pasted image 20261027224009.png]]
		有时候不一定看的是entropy，而是BLEU score，但是训练的时候先别用BLEU score，不然loss没有办法微分
		训练时候和实际时候的偏差（exposure bias）
		![[Pasted image 20261027224712.png]]
			解决
				1、给decoder训练时候也加入一些错误答案
				2、![[Pasted image 20261027224727.png]]

---
## 关联笔记
- [[Lecture_10 Self-attention]] —— Transformer 的 encoder/decoder 内部构件就是 Self-attention
- [[HW_2]] —— 笔记里的 Layer Normalization 和 HW2 用到的 BatchNorm 是同类技术的不同变体
- [[Lecture_3]] —— 这里的 Autoregressive/Non-autoregressive(NAT) 对应 Lecture_3 的"各个击破/一次到位"
- [[Lecture_1]] —— 笔记里提到 Transformer 是候选函数集合（Model）的一种