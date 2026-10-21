# Practice 1：共享单车租车量预测（回归）

照着李宏毅 HW1 的骨架做的练习作业，用来重复练完整训练流程。

## 文件

| 文件 | 作用 |
|---|---|
| `Practice_1.ipynb` | 作业 notebook，按顺序从上往下跑 |
| `bike_train.csv` | 3200 行，55 个特征 + `target` |
| `bike_test.csv` | 1200 行，只有特征 |
| `test_labels.csv` | 测试集答案，只用于最后评分 |
| `score.py` | 命令行评分：`python score.py pred.csv` |

## 数据里埋了什么

特征列被故意排成三段：

1. 第 0–19 列 `region_xx`：区域 one-hot，**纯噪声**
2. 第 20–29 列 `noise_xx`：**纯噪声**
3. 第 30 列以后：时间、天气等**可能有用的特征**

所以 `select_all=True` 是基线，`select_all=False` 是在练特征选择。

数值特征已经用**训练集**的均值和标准差做过标准化，target 保持原始单位。

## 规则

1. 一次只改一个变量
2. 改模型/特征后，重新运行「创建模型并训练」那一格
3. 每组实验先写下猜测，再看结果
4. 记录最优 Valid loss 和测试 RMSE

## 建议的实验顺序

- E1 基线 `select_all=True`
- E2 `select_all=False`
- E3 模型加宽
- E4 换优化器
- E5（可选）weight decay / Dropout / 学习率

做完可以让 Claude 帮你看结果。

## 改完东西要重跑哪些格

| 你改了什么 | 必须重跑 |
|---|---|
| 模型结构 | 第 9 节（创建模型 + 训练） |
| `trainer` 里的优化器 | 第 6 节 + 第 9 节 |
| `select_all` / `feat_idx` / `valid_ratio` / `seed` | 第 8 节（DataLoader）+ 第 9 节 |
| `learning_rate` / `n_epochs` / `early_stop` | 第 7 节（config）+ 第 9 节 |

只改 `config` 不重跑第 8 节，特征选择不会生效；不重跑第 9 节，就是在旧模型上继续训练。
