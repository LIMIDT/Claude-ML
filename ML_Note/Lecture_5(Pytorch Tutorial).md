https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.videopod.episodes&vd_source=af4cf07579045595f3fad858b9bfb593&p=11

What is Pytorch
	在GPU里面快速进行微分运算，
Training&Testing Neural Network![[Pasted image 20261018174125.png]]

Dataset&Dataloader
	batch：一组set![[Pasted image 20261018174323.png]] Init函数，选定把哪些函数放进来，怎么把data都进来，做哪些preprogress
	Getitem函数，把读进来的data回传回去
	Len函数，回传大小![[Pasted image 20261018174627.png]]shuffle：控制的是 **DataLoader 每一轮（epoch）取数据时，是否把样本的顺序随机打乱**。注意它改变的是“取数据的顺序”，而不是数据本身的内容。
Tensor（资料储存形式，一个高维的矩阵）
	![[Pasted image 20261018175143.png]]
	Create Tensor
	![[Pasted image 20261018175250.png]]
	Tensor Operations
	![[Pasted image 20261018175319.png]]
	![[Pasted image 20261018175340.png]]
	Squeeze（拿掉某一个dimension）
	![[Pasted image 20261018175434.png]]
	Unsqueeze
		插入一个dimension
		![[Pasted image 20261018175524.png]]
	Cat
		把很多Tensors接在一起变成一个大的
		![[Pasted image 20261018175634.png]]
		dim=1表示沿着1号轴进行拼接，其他轴必须一样！
	Gradient Calculation
	![[Pasted image 20261018192956.png]]

torch.nn_Network Layers
	Linear Layer![[Pasted image 20261018193512.png]]


torch.nn_Build your own neural netwoork
	![[Pasted image 20261018193729.png]]![[Pasted image 20261018193756.png]]
torch.nn_Loss function
	![[Pasted image 20261018194912.png]]
Training & Testing NeuraI Networks 一 in Pytorch
	![[Pasted image 20261018195136.png]]
torch.optim
	走到最低点
	![[Pasted image 20261018200035.png]]![[Pasted image 20261018200459.png]]
Neural Network Training Setup
	![[Pasted image 20261018200548.png]]![[Pasted image 20261018200736.png]]
Neural Network Training Loop
	![[Pasted image 20261018200905.png]]
	![[Pasted image 20261018201558.png]]
Neural Network validation Loop
	![[Pasted image 20261018201909.png]] validation 只做评估，不更新参数
	![[Pasted image 20261018202752.png]]
	![[Pasted image 20261018202807.png]]
	![[Pasted image 20261018202820.png]]
	**不用算梯度**！！
Neural Network Testing Loop
	![[Pasted image 20261018203119.png]]
	![[Pasted image 20261018203204.png]]
Save/Load Trained Models
	![[Pasted image 20261018203421.png]]
PyTorch Documentation 
	https://pytorch.org/docs/stable/
