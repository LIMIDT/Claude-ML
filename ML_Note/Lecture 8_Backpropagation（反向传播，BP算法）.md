https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.player.switch&vd_source=af4cf07579045595f3fad858b9bfb593&p=19
引入
	面对上百维的向量，如何算梯度（本质还是如何进行梯度下降）
Chain Rule（链式传播）
	![[Pasted image 20261022172718.png]]
Backpropagation
	![[Pasted image 20261022173046.png]]
	只要计算所有的偏微分然后相加
	![[Pasted image 20261022173308.png]]
		Forward Pass
			![[Pasted image 20261022173712.png]]
		Backward Pass
			![[Pasted image 20261022174019.png]]
			a对z的偏导就是激活函数的导数
			![[Pasted image 20261022174155.png]]
			![[Pasted image 20261022174254.png]]
			只要解决问好的式子就方便了
			如何解决问号内容？
				![[Pasted image 20261022174539.png]]
				σ的导已经知道了是个常数
				Case 1：如果下一层是Output会很容易
					![[Pasted image 20261022174808.png]]
				Case 2：下一层不是Output
					类似于递归，一直走下去，直到触及Output层
					**为了减少运算就从后向前运算**
					![[Pasted image 20261022175502.png]]
			**相当于反向再做一个network进行运算**

---
## 关联笔记
- [[Lecture_7(Gradient Descent)]] —— 这篇讲的链式法则是对梯度下降扩展到多层网络的补充