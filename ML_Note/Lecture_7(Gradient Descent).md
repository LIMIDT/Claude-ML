https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.player.switch&vd_source=af4cf07579045595f3fad858b9bfb593&p=18
 Introduction
	 ![[Pasted image 20261022155508.png]]
	 图中要找的是Loss **function的最小值**
 梯度下降过程
	 ![[Pasted image 20261022155725.png]]
Turning your learning rate（调整学习率） 
	![[Pasted image 20261022155939.png]]
	学习率调的太高会导致**Loss Function update以后误差越来越大**
	每次参数更新都要注意看一下Loss
	![[Pasted image 20261022160218.png]]
	Adaptive Learning Rates
		最好的情况是**每个参数都有自己的Learning Rate**
		不同的方法
			Adagrad
				![[Pasted image 20261022161004.png]]
				![[Pasted image 20261022161120.png]]
				W是步长，和Learning Rate成反比
			Stochastic Gradient Decent（随机梯度下降）
				![[Pasted image 20261022163406.png]]
				![[Pasted image 20261022163816.png]]
			Feature scaling（特征缩放）
			![[Pasted image 20261022164409.png]]
			可以使得不同数值之间的变化对于输出的影像更均匀
			![[Pasted image 20261022164709.png]]
			**图中W2对Loss的影响更大**
			如果这样的瘪瘪的Learning Rate就不好找，参数要更多
			![[Pasted image 20261022164854.png]]
			**使得参数的Update更有效率**
Tylor Serise处理二维梯度下降
	![[Pasted image 20261022170043.png]]
	![[Pasted image 20261022170433.png]]
	![[Pasted image 20261022170630.png]]
	![[Pasted image 20261022170750.png]]
		这个就是梯度下降
		**红色圈就是Learning Rate**
Limitation of Gradient Decent
	![[Pasted image 20261022171201.png]]
	有可能微分是零但还是“高原”不是最低值

---
## 关联笔记
- [[Lecture_6(Introduction of Deep Learning）]] —— Step 3 提到的梯度下降，这篇是细讲
- [[Lecture 8_Backpropagation（反向传播，BP算法）]] —— 把这里的梯度下降扩展到多层网络（链式法则）
- [[Hw_1]] —— 笔记里对比的 SGD / Adam 等优化器，HW1 的 Practice_1 实际用到