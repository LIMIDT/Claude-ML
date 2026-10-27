https://www.bilibili.com/video/BV1TD4y137mP/?spm_id_from=333.1391.0.0&p=15&vd_source=af4cf07579045595f3fad858b9bfb593
文字拆解为token，图像是pixel像素，语音是分辨率
生成影片，生成语言

生成策略：
	1、各个击破
	2、一次到位
	
两者对比：
	1、各个击破比一次到位慢（影像一般用一次到位——比较长，像素多）
	2、各个击破的生成品质更好![[Pasted image 20261018172206.png]]

两个配合用：
	语音合成：先用各个击破9（产生每秒大概100个向量）再用一步到位（取采样点）
	把一次到位改成n次到位：图片生成，模糊图片越来越清楚——==Diffusion Model==

---
## 关联笔记
- [[Lecture_11 Transfomer]] —— 这里的"各个击破/一次到位"对应 Transformer 笔记里的 Autoregressive/Non-autoregressive(NAT)