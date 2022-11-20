---
title: 条件随机场CRF
date: '2022/11/19 19:42:10'
top_img: 'https://pic.hycbook.com/i//hexo/post_imgs/蕾姆0.webp'
cover: 'https://pic.hycbook.com/i//hexo/post_cover/蕾姆0.webp'
categories:
  - machine_learning
tags:
  - 机器学习
  - 条件随机场CRF
mathjax: true
description: 机器学习之条件随机场CRF
abbrlink: 12117
---

---



# 前置知识

> 笔记整理自：Bilibili站上[shuhuai008](https://space.bilibili.com/97068901)强势手推讲解的[白板推导CRF系列课程](https://www.bilibili.com/video/av34444816/?p=1)，课程质量很高！

> 分类问题根据输出的类型，可以将其划分为`硬模型`和`软模型`

* **硬输出**: 输出为0或1

* **软输出**: 引入概率，不直接计算边界，而是计算取各类别的概率

## 软硬模型

### 硬模型

> svm支持向量机(最大间隔)

几何角度出发，求的是max margin classifier，式子最终的形式为
$$
min (\frac {1}{2} w^Tw) \qquad s.t. \ y_i(w^Tx_i+b) \geq1,i=1,\cdots,N
$$

> PLA感知机，可以看作最基本的神经元

$$
f(w) = sing(w^Tx)
$$

> LDA线性判别分析(误分类驱动)

核心思想: 类间大、类内小



### 软模型

#### 概率判别模型

> 建模核心

是对$P(x,y)$进行建模

> 例子_逻辑回归(Logistics Regression, LR)，或者也可以叫SoftMax Regression

> 例子_最大熵模型(Maximum Entropy Model, MEM)

利用最大熵思想(Maximum Entropy Model)驱动模型，从熵模型来看，LG是熵模型的一个特例

在最大熵原则下，如果给定均值和方差，那么Gaussian Dist熵最大

> 例子_最大熵马尔科夫模型(Maximum Entropy Markov Model, MEMM)

结合了MEM和HMM形成了MEMM，图模型可以表达成黄线部分(全局影响)或绿线部分(局部影响)，表达成绿线是为了和HMM对比

![最大熵马尔科夫图模型](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/最大熵马尔科夫图模型.webp)

**潜在问题**: `标注偏差问题`

标注偏差问题(Label Bias Problem): 原因是因为`局部归一化`，上图中灰色虚线可以表达为$p(y_2|y_1,x_2)$，这部分要求符合概率分布，因此需要归一化，强制变为概率分布

**与其他模型的关系**

* 与HMM的关系

  HMM直接求联合概率分布，对于标注问题而言，显然不需要求联合概率分布，求条件概率就可以了，因此MEMM比HMM更简单

  打破了HMM的观测独立假设，比如$y_2$的标注不仅和$x_1$有关，也和$x_2$有关，甚至可以说和整个$x$都有关系，这个假设更加合理，观测间不应该是相互独立的

> CRF

将MEMM的**有向调整为了无向**，因此此时的归一化变为了全局归一化，解决了`标注偏差问题`



#### 概率生成模型

> 建模核心

是对$P(y|x)$进行建模

> 例子_朴素贝叶斯(Naive Bayes, NB)

`朴素贝叶斯假设`公式如下
$$
p(x|y=v_0) = \prod _{i=1}^{p}{p(x_i|y=1或0)}
$$
朴素贝叶斯模型简化为下图:

![朴素贝叶斯假设](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/朴素贝叶斯假设.webp)

该图可以公式表达为$x_i \bot x_j | y,i \neq j$，意思是在给定$y$的情况下，$x_i$独立于$x_j$

或者可以解释为$x_j$和$x_j$之间受到$y$的阻隔，因此在给定$y$的情况下，$x_i$独立于$x_j$

> 例子_隐马尔科夫(Hidden Markov Model, HMM)

朴素贝叶斯中的$y$是分类问题，如果这里把$y$看作是一个标注问题，此时演化为序列预测

![朴素贝叶斯到隐马尔科夫](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/朴素贝叶斯到隐马尔科夫.webp)

**HMM**有两个重要假设

`齐次Markov假设`：

`观测独立假设`：公式表达为$x_i \bot x_j | y_i,i \neq j$，意思是在给定$y_i$的情况下，$x_i$独立于$x_j$

> 例子_高斯混合模型(Gaussian mixture model, GMM)

![高斯混合模型简图](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/高斯混合模型简图.webp)






NB-(0/1 变 seq)-> HMM

GMM-(+times)-> HMM

## 概率图模型结构

D-Separation是一种用来判断变量是否条件独立的图形化方法。换言之，对于一个DAG(有向无环图)E，D-Separation方法可以快速的判断出两个节点之间是否是条件独立的

> head-to-head(a->c<-b)

```mermaid

graph TB
	A --> C
	B --> C
```

在c未知的条件下，a、b被阻断(blocked)，是独立的。反过来讲，在c已知的条件下，a、b是连通的，不独立。数学表示是
$$
\begin{align}
    P(a,b,c)&= P(a)*P(b)*P(c|a,b) \\
    \sum_c P(a,b,c)&=\sum_c P(a)*P(b)*P(c|a,b) \\
    P(a,b)&=P(a)*P(b)
\end{align}
$$

> tail-to-tail

```mermaid
graph TB
	C --> A
	C --> B
```

在c给定的条件下，a，b被阻断(blocked)，是独立的。数学表示是
$$
\begin{align}
    P(a,b,c) &= P(c)*P(a|c)*P(b|c)  \\
    P(a,b|c) &= \frac{P(a,b,c)}{P(c)}  \\
    将式子1带  & 入到式子2中：\nonumber \\
    P(a,b|c) &=P(a|c)*P(b|c)
\end{align}
$$

> head-to-tail

```mermaid
graph LR
	A --> C --> B
```



在**c给定的条件下，a，b被阻断(blocked)，是独立的**。数学表示是$P(a,b,c)=P(a)P(c|a)P(b|c)$

化简后可得
$$
\begin{align}
P(a,b|c) &= \frac{P(a,b,c)}{P(c)}  \\
         &= \frac{P(a)*P(c|a)*P(b|c)}{P(c)}  \\
         &= \frac{P(a,c)*P(b|c)}{P(c)}  \\
         &= P(a|c)*P(b|c)
\end{align}
$$

# 演化

## HMM

> [马尔科夫随机场(MRF)在图像处理中的应用-图像分割、纹理迁移](https://oldpan.me/archives/markov-random-field-deeplearning)

HMM是一个生成模型，可以看成是NB或GMM的泛化

参数定义为$\lambda = (\pi , A, B)$，其中$\pi$是初始状态分布、$A$是y之间的状态转移矩阵($y_t$到$y_{t+1}$的概率)、$B$是从$y$发射到$x$的发射矩阵

**HMM有两个重要假设**(非必须，折中的方式，减少计算量)

`一阶齐次Markov假设`：

一阶: 含义为$y_i$只和$y_{i-1}$有关系，或者表述为给定$y_{i-1}$的情况下$y_i$和$y_{i-2}$是无关的，二阶的话就是给定$y_{i-1}$和$y_{i-2}$的情况下$y_i$和$y_{i-3}$是无关的

齐次: 含义为$y_1, \cdots , y_i$每个$y$的概率是是一致，也可以表述为$p(y_t|y_{t+1})$和$p(y_{t-1}|y_{t-2})$是相等的，也就是与时间$t$无关

术语化表达: $p(y_t|y_{1:t-1},x_{1:t-1}) = p(y_t|y_{t-1})$

`观测独立假设`：公式表达为$x_i \bot x_j | y_i,i \neq j$，意思是在给定$y_i$的情况下，$x_i$独立于$x_j$

术语化表达: $p(x_t|y_{1:t-1},x_{1:t-1}) = p(x_t|y_{t})$

**建模对象**如下
$$
p(X,Y| \lambda) = \prod _{t-1}^T{p(x_t, y_t| \lambda)} = \prod _{t-1}^T{p(y_t|y_{t-1}, \lambda)} \prod _{t-1}^T{p(x_t|y_{t}, \lambda)}
$$
计算复杂度太高，于是引入了前向后向算法

## MEMM

![最大熵马尔科夫图模型](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/最大熵马尔科夫图模型.webp)

与HMM比较，将$x$变为了$y$的输入，此时给定$y_t$的情况下，$x_t$和$x_{t-1}$不是相互独立的，从而**打破观测独立性假设**

此时的MEMM建模对象变为了条件概率，为判别模型
$$
p(Y|X, \lambda) = \prod _{t=1}^T{p(y_t| y_{t-1}, x_{1:t}, \lambda)}
$$
在这里，判别式的模型比生成式模型要好

因为：任务驱动的，在这样的序列标注任务上，在给定一个待标注序列，我们更关注的是标注的是什么，因此，对于这样的任务我们只需要对条件概率建模就足矣了，而去求联合概率分布就将问题复杂化了(计算也复杂化了)

这里把整个输入$X$分成了2个部分，$X=(x_g,x_{1:T})$，即对$Y$的影响分成两个部分：全局的影响+局部的影响

主要缺点是会造成Label Bias Problem，（在John Lafferty论文中，指出了MEMM会造成Label Bias Problem问题）

看上方灰色框内的局部，可以简单看成是逻辑回归，在这个最小单元我们把它当成一个系统，系统从$y_{t−1}$到$y_t$的这样一个转移用数学可以表示成一个函数，是受$y_{t−1}$、$y_t$与$x_t$共同作用的一个函数，系统对外是有一定能量的，这个函数被称为`Mass Score`，而且是大于0的。但是问题出现在：这个Mass Score被局部归一化了。条件概率熵越小，那么对于观测值的考虑越少

> 为了能够更好地理解它的问题所在，这里举一个比较极端的[例子](https://anxiang1836.github.io/2019/11/05/NLP_From_HMM_to_CRF/)

![LabelBiasProblem](https://pic.hycbook.com/i/hexo/bk_resources/machine_learning/条件随机场CRF/LabelBiasProblem.webp)

比如，我们训练好了这样的一个模型，现有一个观测序列是rib

1. 在状态0时，由于$P(4|0)>P(1|0)$，所以我们选择从$0→4$转移路径；
2. 问题出现在了第二步转移上：由于$P(5|4)=1$，是受到了局部归一化的影响，从4状态转移仅有1条路径选择，其转移的条件概率为1，其所具有的熵值为0

为什么从4状态向5转移的条件概率为1

正是因为MEMM在每一步转移的概率都是要做**局部归一化**的，也就是说，从4状态向外转移的所有的情况加和要为1，在这里，仅有1中转移情况，所以$P(5|4)=1$

在这种情况下，无论观测值为什么，都不会影响$4→5$的转移，但是，这样标注出来的序列$0→4→5→3$，即rob就与客观事实不符了，这也就是问题的所在

## CRF

所以，为了解决局部归一化的问题，CRF取消了Y序列的转移方向，也就是取消了局部归一化，改变为了`全局归一化`  



# CRF

