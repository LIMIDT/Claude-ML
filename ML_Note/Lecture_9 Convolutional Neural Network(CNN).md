https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.player.switch&vd_source=af4cf07579045595f3fad858b9bfb593&p=20
Image Classification
	把图片看成三维的tensor
		宽
		高
		channel（RGB）
		![[Pasted image 20261022192302.png]]
		把数字排成向量
		![[Pasted image 20261022192457.png]]
	图像处理
		一定需要fully connected network？
		![[Pasted image 20261022192711.png]]
		不同的neural负责不同的部分，把一小部分当作输入
Simplification
	![[Pasted image 20261022193301.png]]
	每个neural负责一个 Receptive field	
	可以给不同的field设置不同的neural
	彼此之间也可以重叠，同个field可以有多个neural，一个neural也可以负责多个field
	![[Pasted image 20261022193707.png]]
	Typical setting
		一般都是三个channel一起看，选定一个kernel（核）
		![[Pasted image 20261022194603.png]]
		 一般一个field都有好几个neural去守卫
		![[Pasted image 20261022200940.png]]
		 **设置一定的stride使得不同的field有重叠很重要**
		![[Pasted image 20261022201147.png]]
		超出范围进行padding
		**每一个位置都一定要被扫描到**
Simplification 2
	![[Pasted image 20261022202017.png]]
	让两个neural共享参数（weight一样）比如说两张图的鸟嘴不在一个地方但是都想让机器看见鸟嘴，但是不能每个field都放一个识别鸟嘴的field
	**输出也不一样，只是共享参数**
	![[Pasted image 20261022202709.png]]
	公用一组参数(filter)——Parameter Sharing（共享参数）
	![[Pasted image 20261022203536.png]]
	**看的范围越小弹性变小**
	**receptive field（感受野）加上parameter sharing就是卷积神经网络**
	CNN专门为影像设计的，虽然model bias很大（影像之外不一定）
Convolution Layer(another version)
	![[Pasted image 20261022204138.png]] 每一个filter就是去抓一个pattern
	![[Pasted image 20261022204821.png]]
	卷积去扫图片
	![[Pasted image 20261022204858.png]]
	![[Pasted image 20261022205012.png]]
	**filter的高度必须要和被处理的channel个数相同**
两个版本对比
	![[Pasted image 20261022205327.png]]
	![[Pasted image 20261022205402.png]]
	![[Pasted image 20261022205427.png]] 
Observation(Pooling)池化
	![[Pasted image 20261022205609.png]]
	确保鸟被放大缩小还是一只鸟，被移动了也不会变
	Max Pooling
		![[Pasted image 20261022205729.png]]
		选最大的那个，几个一组都行
		![[Pasted image 20261022205825.png]]
		两个基本上都是一起来
		算力充足都可以不用pooling（可有可无的）
The whole CNN
	![[Pasted image 20261022210033.png]]
	Flatten(把所有的拍扁拍成一个向量)，然后交给Fully Connection
Application
	![[Pasted image 20261022210343.png]]
	![[Pasted image 20261022210635.png]]
	![[Pasted image 20261022211005.png]]
	Pooling的使用可以考虑一下
	![[Pasted image 20261022211052.png]]
	语音文字上也可以用CNN（要根据特性设计）
	![[Pasted image 20261022211241.png]]