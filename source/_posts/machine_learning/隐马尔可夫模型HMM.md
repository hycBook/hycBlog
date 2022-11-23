---
title: 隐马尔可夫模型HMM
date: '2022/11/23 21:12:53'
top_img: 'https://pic.hycbook.com/i//hexo/post_imgs/蕾姆1.webp'
cover: 'https://pic.hycbook.com/i//hexo/post_cover/蕾姆1.webp'
categories:
  - machine_learning
tags:
  - 机器学习
  - 隐马尔可夫模型HMM
mathjax: true
description: 机器学习之隐马尔可夫模型HMM
---

---



# 隐马尔可夫HMM

## 定义

> [一站式解决：隐马尔可夫模型（HMM）全过程推导及实现](https://zhuanlan.zhihu.com/p/85454896)
>
> [关于HMM、MEMM、CRF的一些知识整理整理](https://zhuanlan.zhihu.com/p/172317251)
>
> [图解隐马尔可夫模型HMM_通俗易懂](https://www.jianshu.com/p/1a45adecaf8c)

HMM是生成模型



## 三要素

> 隐马尔可夫三要素

隐马尔可夫模型由`初始状态概率`$\pi$、`状态转移矩阵`$A$、`观测概率矩阵`(或者叫发射矩阵)$B$决定，记作
$$
\lambda = (\pi, A, B)
$$
其中$\pi$的维度为$N$，$A$的维度为$N \times N$，$B$的维度为$N \times M$

## 三个假设

1. `马尔科夫性假设`: $t$时刻的状态出现的概率只和$t-1$时刻的状态有关
   $$
   P(x_t | x_{t-1}, x_{t-1}, \cdots, x_1) = P(x_t | x_{t-1})
   $$

2. `齐次马尔可夫假设`(假设1)
   $$
   P(x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j | \lambda) \\
   
   = P(z_{t+1}=q_j | x_1, \cdots , x_t, z_t=q_i , \lambda) P(x_1, \cdots , x_t, z_t =q_i | \lambda) 
   \\
   = P(z_{t+1} = q_j | z_t=q_i) P(x_1, \cdots , x_t, z_t=q_i | \lambda) = a_{ij} \alpha _{t}(i)
   $$
   

3. `观测独立性假设`(假设2)
   $$
   P(x_{t+1} | x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j , \lambda) = P(x_{t+1} | z_{t+1}=q_j ) = b_j(x_{t+1})
   $$

假设1和假设2在前后向算法推导上有用到

## 概率基础

> 联合概率

联合概率指的是包含多个条件且**所有条件同时成立**的概率，记作
$$
P(X=a,Y=b)=P(a,b)=P(a \cap b)
$$

> 边缘概率

仅与单个随机变量有关的概率，记作
$$
P(X=a)=P(Y=b)
$$

> 条件概率

条件概率表示在条件$Y=b$成立的情况下，$X=a$的概率，记作
$$
P(X=a|Y=b)=P(a|b)
$$
具有性质：在条件$Y=b$下$X$的条件分布，也是一种$X$的概率分布，穷举$X$的可取值之后，所有这些值对应的概率之和为$1$，即:
$$
\sum _{a}{P(X=a|Y=b)} = 1
$$

> 🌿联合概率、边缘概率与条件概率之间的关系: 联=边*条

$$
P(X=a|Y=b) = \frac {P(X=a,Y=b)}{P(Y=b)}
$$

可以理解成在$Y$选中$b$的情况下，同时$X$选中$b$的概率就是联合概率，表示两个条件同时满足

🍄例如选中第二个盒子同时是红色球的概率，等于选中第二个盒子的概率 乘上 第二个盒子中选中红色球的概率

> 贝叶斯公式

* **先验概率**：知道原因推结果的，P(原因)、P(结果|原因)等
* **后验概率**：根据结果推原因的，P(原因|结果)等



# HMM的三个问题

HMM的基本问题一共有三个:

- `概率计算`：给定参数$ \lambda =( \pi , A, B) $和观测序列$ X=(x_1,x_2, \cdots ,x_T) $，计算观测序列$ X $的条件概率$ P(X|\lambda)$
- `参数学习`：给定观测序列$ X $，反推参数$\pi$、$A$、$B$
- `解码问题`：给定参数$\lambda$和观测序列$ X=(x_1,x_2, \cdots ,x_T) $，求可能性最大的$ Z=(z_1, \cdots ,z_T)$

## 概率计算

> HMM模型定义

🌱假设有4个盒子，每个盒子里面有不同数量的红、白两种颜色的球，具体如下表

![img](res/隐马尔可夫模型HMM/v2-fec4d6fc5042da745cb9735fb42af790_b.jpg)

现在从这些盒子中抽取$T$个球，每次抽取后记录颜色，再放回原盒子，

序列如下图所示

![img](res/隐马尔可夫模型HMM/v2-d7a0a527a28521cdd6dc4e539e613517_720w.jpeg)

其中$z_i$代表第$i$个`隐序列值`，$q_i$代表第$i$个`隐状态`，$x_i$代表第$i$个`观测序列值`，注意

* `隐序列值`指的是第几个位置，比如第几个盒子、或者第几个单词
* `隐状态`指的是第几个状态，比如红球还是白球，或者名词还是动词

此时$z_t = q_i$表达的含义就是$t$时刻，抽取第$q_i$个盒子，因为有$4$个盒子，所以在这里$i={1,2,3,4}$

对应取到的球的颜色可以记为$x_i$，其中$x_i \in {白色, 红色}$

> 🐜前向概率

现在定义一个前向概率$ \alpha _t (i) $，它是$t$时刻的状态以及$1, 2, \cdots , t$时刻的观测在给定参数下的`联合概率`
$$
\alpha _t(i) = P(x_1, x_2, \cdots , x_t , z_t =q_i | \lambda)
$$
也就是下图中标记的那一部分，$ \alpha _t (i) $表示的是在$t$时刻，隐状态为$q_i$的概率

![img](res/隐马尔可夫模型HMM/v2-f307367eb57dab7b76f3290782d4f42e_720w.jpeg)

> 前向概率初值

根据定义可以得到初值:
$$
\alpha _1 (i) = P(x_1,z_1 = q_i | \lambda) = P(z_1=q_i | \lambda)P(x_1|z_1=q_i, \lambda) = \pi _i b_i(x_1)
$$
其中$P(x_1|z_1=q_i, \lambda)$表达的是，给定$\lambda$和状态$z_1=q_i$的情况下，观测值是$x_1$的概率

假设此时$x_1=白色$，这里可以通俗理解为$z_1$表示的第$1$个盒子，即从第一个盒子中取出白球的概率

同时$ b_i(x) $表示由状态$ q_i $生成给定观测数据的概率，例如设$ t $时刻观测数据$ x_t=v_j $，有
$$
b_i(x_t) = b_i(x_t=v_j)=P(x_t=v_j|z_t=q_i)=b_{ij}
$$




上述用到的公式为$P(A,B)=P(AB)=P(A)P(B|A)=P(B)P(A|B)$，直观的解释就是
$$
A事件和B事件同时发生的概率 = A事件发生的概率*A事件发生的情况下B事件发生的概率
$$
🌰举个例子，假设有3个盒子，每个盒子中有白色和红色两种颜色的球，那么从第二个盒子中取出白球的概率，等价于抽到第二个盒子的概率$\times$第二个盒子中抽到白色求的概率



由前向概率$ \alpha _t (i) $继续推导可以得到$ \alpha _T (i) $
$$
\alpha _T(i) = P(x_1, x_2, \cdots , x_T , z_T =q_i | \lambda) = P(X,z_T=q_i | \lambda)
$$
根据这个公式，遍历$ z_T $的取值求和，可以得到$X$的`边际概率`
$$
\sum _{i=1}^{N}{\alpha _T(i)} = \sum _{i=1}^{N}{P(X,z_T=q_i | \lambda)} = P(X|\lambda)
$$
其中$N$表示的是`状态数量`，比如盒子中只有红球和白球，即状态集合为$\{白球, 红球\}$，此时$N=2$



> 推导递推公式

由前向概率$ \alpha _t (i) $推导可以得到$ \alpha _{t+1} (j) $
$$
\alpha _{t+1}(j) = P(x_1, x_2, \cdots , x_{t+1} , z_{t+1} =q_j | \lambda)
$$
引入变量$z_t=q_i$，注意($t+1$时刻$=$$z_t$所有状态求和)，所以有
$$
\alpha _{t+1}(j) = \sum _{i=1}^{N}{P(x_1, \cdots , x_{t+1}, z_t=q_i, z_{t+1}=q_j | \lambda)} = \\

\sum _{i=1}^{N}{P(x_{t+1} | x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j , \lambda)} P(x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j | \lambda)
$$
找到了$t$到$t+1$时刻的地推公式，分别看下公式的两个部分

> 两个假设

将两个假设代入$\alpha _{t+1}(j)$可以得到
$$
\alpha _{t+1}(j) = \sum _{i=1}^{N}{a_{ij}* b_j(x_{t+1})* \alpha _{t}(i)}
$$

> 🐝后向概率

后向概率可以定义为
$$
\beta _t(i) = P(x_T, x_{T-1}, \cdots , x_{t+1}  | z_t =q_i, \lambda)
$$
![img](res/隐马尔可夫模型HMM/v2-d39e1c71e535f8e344e9ed659e010e41_b.jpg)

并且规定初始值
$$
\beta _T(1) = \beta _T(2) = \cdots = \beta _T(N) =1
$$
根据后向概率定义可以推出
$$
\beta _1(i) = P(x_T, x_{T-1}, \cdots , x_2 | z_1=q_i, \lambda)
$$
然后来看上式和要计算的概率$ P(X| \lambda ) $之间的关系
$$
P(X| \lambda ) = P(x_1, x_2, \cdots , x_T | \lambda) \\
= \sum _{i=1}^{N}{P(x_1, x_2, \cdots , x_T, z_1=q_i | \lambda)} \\
= \sum _{i=1}^{N}{P(x_1 | x_2, \cdots , x_T, z_1=q_i , \lambda)P(x_2, \cdots , x_T, z_1=q_i | \lambda)} \\
= \sum _{i=1}^{N}{P(x_1 | z_1=q_i) P(z_1=q_i | \lambda) P(x_T, x_{T-1}, \cdots, x_2 | z_1=q_i, \lambda)} \\
= \sum _{i=1}^{N}{b_i(x_1) \pi _i \beta _1(i)}
$$
上面$b_i(x_1) \pi _i$也就是$ \alpha _1(i) $的定义，实际上，对于任意时刻$ t $，存在以下等式
$$
P(X | \lambda) = \sum _{i=1}^{N}{\alpha _t(i) \beta _t(i)}
$$
接着，假设已知所有的$\beta _{t+1}$，来推导$\beta _{t}$
$$
\beta _{t}(i) = P(X_T, \cdots , x_{t+1} | z_t=q_i , \lambda) \\
= \sum _{j=1}^{N}{P(x_T, \cdots , x_{t+1}, z_{t+1} =q_j | z_t=q_i , \lambda)} \\
= \sum _{j=1}^{N}{P(x_T, \cdots , x_{t+1} | z_{t+1} =q_j , z_t=q_i , \lambda) P(z_{t+1} = q_j | z_t =q_i , \lambda)}
$$
观察上式，后部分实际上就是$\alpha _{ij}$，而前半部分，根据前向概率中的`观测独立性假设`，$z_t$与$x_1, \cdots ,x_T$都是无关的，即相互独立，可以省去，因此第二部分可以变为
$$
P(x_T, \cdots , x_{t+1} | z_{t+1} =q_j , z_t=q_i , \lambda)  \\
= P(x_T, \cdots , x_{t+1} | z_{t+1}=q_j , \lambda) \\
= P(x_{t+1} | x_T, \cdots , x_{t+2}, z_{t+1}=q_j) P(x_T, \cdots , x_{t+2} | z_{t+1}=q_j , \lambda) \\
= b_j(x_{t+1}) \beta _{t+1} (j)
$$
将结论代入$\beta _t{i}$得到
$$
\beta _t{i} = \sum _{j=1}^{N}{a_{ij}*b_j(x_{t+1})*\beta _{t+1}(j)}
$$


## 参数学习



## 解码问题



