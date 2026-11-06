https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.788.videopod.episodes&vd_source=af4cf07579045595f3fad858b9bfb593&p=28
图像分类
![[Pasted image 20261030153736.png]]
![[Pasted image 20261030154400.png]]
![[Pasted image 20261030154726.png]]

对于过拟合的阐释
1、模型在训练集上面的进步超过了在验证集上面的进步
	类似于进步变慢了，但是多训练还是可以变好
2、验证集达到最高点开始下降
	类似于已经开始退步了，不能再训练了
如何区分？
	看 valid 的趋势  →  还能不能继续训（有没有到拐点）
	看 gap 的趋势    →  泛化能力如何（训练到底有没有用）

![[Pasted image 20261030210352.png]]
**参数并不会决定过拟合**只是会产生一定影响

在图片分类的时候，虽然池化会使得图片是真，但是也使得图片可以去除掉噪音，保留真正想要被留下来的

transforms.RandomCrop (size, padding=16 )
	意图：让食物在画面里面随偏移16个像素
	动作：先在四周补上16像素的边，128×128变成160×160，再从160×160里面随机裁出一块128×128
	**还可以再16后面加上padding_mode='reflect'意思是把图片做自然的延申，不然补上的都会是黑边**

transforms.RandomPerspective（distortion_scale=‘默认0.5’）
	把图形进行随机视角
	![[Pasted image 20261103064706.png]]

CNN到头以后换成ResNet继续实验
	1、在configuration里面换model
		model = torchvision.models.resnet18(weights=None, num_classes=11).to(device)
		整个模型内部的18层神经网络已经搭建好了，weight=none说明不加载别人的模型自己训练参数
	2、更换优化器
		优化器换成AdamW
		对于大模型，强正则化的场景，AdamW使得惩罚单独拿出来进行处理，不受自适应步长的干扰，不会把惩罚塞进去梯度里面一起处理

label smoothing
	原本
	criterion = nn.CrossEntropyLoss()
	改成
	criterion = nn.CrossEntropyLoss(label_smoothing=0.1）
	相当于让模型最后不要训练到把正确类推到百分百，不会部分去讨好目标
