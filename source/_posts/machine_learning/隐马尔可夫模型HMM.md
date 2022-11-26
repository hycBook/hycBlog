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
abbrlink: 4987
---

---



# 隐马尔可夫HMM

## 定义

> [一站式解决：隐马尔可夫模型（HMM）全过程推导及实现](https://zhuanlan.zhihu.com/p/85454896)
>
> [关于HMM、MEMM、CRF的一些知识整理整理](https://zhuanlan.zhihu.com/p/172317251)
>
> [图解隐马尔可夫模型HMM_通俗易懂](https://www.jianshu.com/p/1a45adecaf8c)

`隐马尔可夫模型`(hidden Markov model, HMM)是可用于`标注问题`的统计学习模型

描述由`隐藏的马尔可夫链`随机`生成观测序列`的过程，属于`生成模型`

隐藏的马尔可夫链随机生成的状态的序列，称为状态序列(state sequence)每个状态生成一个观测

而由此产生的观测的随机序列，称为观测序列(observation sequence)

序列的每一个位置又可以看作是一个`时刻`

![img](https://pic.hycbook.com/i//hexo/bk_resources/machine_learning/隐马尔可夫模型HMM/HMM模型.webp)

这里的$Z$就是状态序列，$x$是观测序列，设Q是所有可能的状态的集合，V是所有可能的观测的集合，$N$是可能的状态数，$M$是可能的观测数
$$
Q = \{q_1,q_2, \cdots ,q_N \} \qquad V = \{v_1,v_2, \cdots ,v_M \}
$$

## 三要素

> 隐马尔可夫三要素

隐马尔可夫模型由`初始状态概率`$\pi$、`状态转移矩阵`$A$、`观测概率矩阵`(或者叫发射矩阵)$B$决定，记作
$$
\lambda = (\pi, A, B)
$$
其中$\pi$的维度为$N$，$A$的维度为$N \times N$，$B$的维度为$N \times M$

> 例子🌰

🌱假设有4个盒子，每个盒子里面有不同数量的红、白两种颜色的球，具体如下表

| 盒子编号 | 1    | 2    | 3    | 4    |
| -------- | ---- | ---- | ---- | ---- |
| 红球数   | 5    | 3    | 6    | 8    |
| 白球数   | 5    | 7    | 4    | 2    |

按照下面的方法抽球，产生一个球的颜色的观测序列：

1. 开始，从4个盒子里以等概率随机选取1个盒子，从这个盒子里随机抽出1个球，记录其颜色后，放回

2. 然后，从当前盒子随机转移到下一个盒子，**规则**如下：

   * 如果当前盒子是盒子1，那么下一盒子一定是盒子2
   * 如果当前是盒子2或3，那么分别以概率0.4和0.6转移到左边或右边的盒子
   * 如果当前是盒子4，那么各以0.5的概率停留在盒子4或转移到盒子3
3. 确定转移的盒子后，再从这个盒子里随机抽出1个球，记录其颜色，放回
4. 如此下去，重复进行5次，得到一个球的颜色的观测序列：$O＝\{红,红,白,白,红\}$

根据所给条件，可以明确状态集合、观测集合、序列长度以及模型的三要素

1. **盒子对应状态**，状态的集合是$Q＝\{盒子1,盒子2,盒子3,盒子4\}$，$N=4$
2. 球的**颜色对应观测**。观测的集合是$V＝\{红,白\}$，$M＝2$
3. 状态序列和观测序列长度$T＝5$

则初始概率分布为
$$
\pi = (0.25,0.25,0.25,0.25)^T
$$
状态转移概率分布为
$$
A=\left[\begin{array}{cccc}
0 & 1 & 0 & 0 \\
0.4 & 0 & 0.6 & 0 \\
0 & 0.4 & 0 & 0.6 \\
0 & 0 & 0.5 & 0.5
\end{array}\right]
$$
观测概率分布为 (最终盒子红白球的概率)
$$
B=\left[\begin{array}{ll}
0.5 & 0.5 \\
0.3 & 0.7 \\
0.6 & 0.4 \\
0.8 & 0.2
\end{array}\right]
$$

## 三个假设

1. `马尔科夫性假设`: $t$时刻的状态出现的概率只和$t-1$时刻的状态有关
   $$
   P(x_t | x_{t-1}, x_{t-1}, \cdots, x_1) = P(x_t | x_{t-1})
   $$

2. `齐次马尔可夫假设`(假设1)
   $$
   \begin{align}
   & P(x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j | \lambda) 
   = P(z_{t+1}=q_j | x_1, \cdots , x_t, z_t=q_i , \lambda) P(x_1, \cdots , x_t, z_t =q_i | \lambda) 
   \\
   &= P(z_{t+1} = q_j | z_t=q_i) P(x_1, \cdots , x_t, z_t=q_i | \lambda) = a_{ij} \alpha _{t}(i)
   \end{align}
   $$
   
3. `观测独立性假设`(假设2)
   $$
   P(x_{t+1} | x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j , \lambda) = P(x_{t+1} | z_{t+1}=q_j ) = b_j(x_{t+1})
   $$

假设1和假设2在前后向算法推导上有用到

## 观测序列生成

输入：隐马尔可夫模型 $\lambda=(A ,B ,\pi )$ ，观测序列长度$T$
输出：观测序列 $O=\left(O_{1}, O_{2}, \cdots, O_{T}\right)$ 

1. 按照初始状态分布 $\pi$ 产生状态$i_1$
2. 令t $=1$
3. 按照状态$\mathrm{t}$的观测概率分布$$b _{i_t} (k)$$ 生成 $$\mathrm{o}_{\mathrm{t}}$$
4. 按照状态 $$i_{t}$$ 的状态转移概率分布 $$\left\{a_{i_{t}i_{t+1}} \right\}$$ 产生状态 $$i_{t+1}$$，$$i_{t+1}=1,2, \cdots, N$$
5. 令 $\mathrm{t}=\mathrm{t}+1$; 如果 $\mathrm{t}<\mathrm{T}$ ，转步 $(3)$ ；否则，终止

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

🌰举个例子，假设有3个盒子，每个盒子中有白色和红色两种颜色的球，那么从第二个盒子中取出白球的概率，等价于抽到第二个盒子的概率$\times$第二个盒子中抽到白色求的概率

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

| 盒子编号 | 1    | 2    | 3    | 4    |
| -------- | ---- | ---- | ---- | ---- |
| 红球数   | 5    | 3    | 6    | 8    |
| 白球数   | 5    | 7    | 4    | 2    |

现在从这些盒子中抽取$T$个球，每次抽取后记录颜色，再放回原盒子

序列如下图所示

![img](https://pic.hycbook.com/i//hexo/bk_resources/machine_learning/隐马尔可夫模型HMM/HMM模型.webp)

其中$z_i$代表第$i$个`隐序列值`，$q_i$代表第$i$个`隐状态`，$x_i$代表第$i$个`观测序列值`，注意

* `隐序列值`指的是第几个位置，比如第几个盒子、或者第几个单词
* `隐状态`指的是第几个状态，比如红球还是白球，或者名词还是动词

此时$z_t = q_i$表达的含义就是$t$时刻，抽取第$q_i$个盒子，因为有$4$个盒子，所以在这里$i={1,2,3,4}$

对应取到的球的颜色可以记为$x_i$，其中$x_i \in {白色, 红色}$

### 直接计算

给定模型 $\lambda=(A, B, \pi)$ 和观测序列 $$O=\left(o_{1}, o_{2}, \cdots, o_{T}\right)$$，算观测序列 $O$ 出现的 概率 $$P(O \mid \lambda)$$ ，最直接的方法是按概率公式直接计算.

通过列举所有可能的长度为$T$的状态序列$$I=\left(i_{1}, i_{2}, \cdots, i_{T}\right)$$，求各个状态序列$I$与观测序列$$O=\left(o_{1}, o_{2}, \cdots, o_{T}\right)$$ 的联合概率 $$P(O, I \mid \lambda)$$，然后对所有可能的状态序列求和，得到 $$P(O \mid \lambda)$$

状态序列 $$I=\left(i_{1}, i_{2}, \cdots, i_{T}\right)$$ 的概率是
$$
P(I \mid \lambda)=\pi_{i_{1}} a_{i_1 i_{2}} a_{i_{2}, i_{3}} \cdots a_{i_{T-1}-i_{T}}
$$
对固定的状态序列 $$I=\left(i_{1}, i_{2}, \cdots, i_{T}\right)$$，观测序列 $$O=\left(o_{1}, o_{2}, \cdots, o_{T}\right)$$ 的概率是 $$P(O \mid I, \lambda)$$
$$
P(O \mid I, \lambda)=b_{i_{1}}\left(o_{1}\right) b_{i_{2}}\left(o_{2}\right) \cdots b_{i_{r}}\left(o_{T}\right)
$$

$O$ 和 $I$ 同时出现的联合概率为
$$
\begin{aligned}
P(O, I \mid \lambda) &=P(O \mid I, \lambda) P(I \mid \lambda) \\
&=\pi_{i_{1}} b_{i_{1}}\left(o_{1}\right) a_{i_{1}i_{2}} b_{i_{2}}\left(o_{2}\right) \cdots a_{i_{T-1}i_{T}} b_{i_{T}}\left(o_{T}\right)
\end{aligned}
$$
然后, 对所有可能的状态序列 $I$ 求和, 得到观测序列 $O$ 的概率 $P(O \mid \lambda)$, 即
$$
\begin{aligned}
P(O \mid \lambda) &=\sum_{I} P(O \mid I, \lambda) P(I \mid \lambda) \\
&=\sum_{i_{1}, \lambda_{2}, \cdots, i_{r}} \pi_{i_{1}} b_{i_{1}}\left(o_{1}\right) a_{i_{2}} b_{i_{2}}\left(o_{2}\right) \cdots a_{i_{r}-\lambda_{T}} b_{i_{T}}\left(o_{T}\right)
\end{aligned}
$$
但是，利用上述公式计算量很大，是 $O\left(T N^{T}\right)$ 阶的，这种算法不可行

### 🐜前向概率

> 定义

前向概率$ \alpha _t (i) $，它是$t$时刻的状态以及$1, 2, \cdots , t$时刻的观测在给定参数下的`联合概率`
$$
\alpha _t(i) = P(x_1, x_2, \cdots , x_t , z_t =q_i | \lambda)
$$
也就是上图中标记的那一部分，$ \alpha _t (i) $表示的是在$t$时刻，隐状态为$q_i$的概率

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
上述用到的公式为为`概率基础`部分的知识

> 推导递推公式

由前向概率$ \alpha _t (i) $继续推导可以得到$ \alpha _T (i) $
$$
\alpha _T(i) = P(x_1, x_2, \cdots , x_T , z_T =q_i | \lambda) = P(X,z_T=q_i | \lambda)
$$
根据这个公式，遍历$ z_T $的取值求和，可以得到$X$的`边际概率`
$$
\sum _{i=1}^{N}{\alpha _T(i)} = \sum _{i=1}^{N}{P(X,z_T=q_i | \lambda)} = P(X|\lambda)
$$
其中$N$表示的是`状态数量`，比如盒子中只有红球和白球，即状态集合为$\{白球, 红球\}$，此时$N=2$

由前向概率$$ \alpha _t (i) $$推导可以得到$$ \alpha _{t+1} (j) $$
$$
\alpha _{t+1}(j) = P(x_1, x_2, \cdots , x_{t+1} , z_{t+1} =q_j | \lambda)
$$
引入变量$z_t=q_i$，注意($t+1$时刻$=$$z_t$所有状态求和)，所以有
$$
\begin{align}
& \alpha _{t+1}(j) = \sum _{i=1}^{N}{P(x_1, \cdots , x_{t+1}, z_t=q_i, z_{t+1}=q_j | \lambda)} \\
&= \sum _{i=1}^{N}{P(x_{t+1} | x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j , \lambda)} P(x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j | \lambda)
\end{align}
$$
找到了$t$到$t+1$时刻的递推公式，分别看下公式的两个部分

1. 前半部分根据`观测独立假设`
   $$
   P(x_{t+1}| x_1, \cdots, x_t, z_t ,z_{t+1} , \lambda) = P(x_{t+1}|z_{t+1}=q_j)=b_j(x_{t+1})
   $$

2. 后半部分根据`齐次马尔可夫假设`
   $$
   \begin{align}
   & P(x_1, \cdots , x_{t}, z_t=q_i, z_{t+1}=q_j | \lambda) \\
   & = P(z_{t+1}=q_j | x_1, \cdots , x_t, z_t=q_i , \lambda) P(x_1, \cdots , x_t, z_t =q_i | \lambda) \\
   & = P(z_{t+1} = q_j | z_t=q_i) P(x_1, \cdots , x_t, z_t=q_i | \lambda) = a_{ij} \alpha _{t}(i)
   \end{align}
   $$

将上述结果代入$\alpha _{t+1}(j)$可以得到
$$
\alpha _{t+1}(j) = \sum _{i=1}^{N}{a_{ij}* b_j(x_{t+1})* \alpha _{t}(i)}
$$

> 条件概率

$$
P(X|\lambda) = \sum _{i=1}^{N}{\alpha _t(i)}
$$

> 例子[HMM前向和后向算法在计算什么？](https://www.cnblogs.com/wry789/p/12939713.html)

考虑盒子和球模型$\lambda (\pi,A,B)$，状态集合$Q＝\{1,2,3\}$，观测集合$V＝\{红,白\}$
$$
\begin{aligned}
\Pi =(0.2,0.4,0.4)^{T}

\qquad

A =\left(\begin{array}{lll}
0.5 & 0.2 & 0.3 \\
0.3 & 0.5 & 0.2 \\
0.2 & 0.3 & 0.5
\end{array}\right)

\qquad

B =\left(\begin{array}{ll}
0.5 & 0.5 \\
0.4 & 0.6 \\
0.7 & 0.3
\end{array}\right)
\end{aligned}
$$
观测序列 $O=\{ 红, 白, 红 \}$

输出: 观测序列 $O=\{ 红, 白, 红 \}$ 的概率

* $t=1$时刻的前向概率

隐藏状态为盒子1且为红色球的概率为: $$\alpha_{1}(1)=\pi_{1} b_{1}\left(o_{1}\right)=0.2 \times 0.5=0.1$$

隐藏状态为盒子 2 且为红色球的概率为: $$\alpha_{1}(2)=\pi_{2} b_{2}\left(o_{1}\right)=0.4 \times 0.4=0.16$$

隐藏状态为盒子3且为红色球的概率为: $$\alpha_{1}(3)=\pi_{3} b_{3}\left(o_{1}\right)=0.4 \times 0.7=0.28$$

* $t=2$时刻的前向概率(在前一个观测状态为红色球的基础下)

隐藏状态是盒子1且为白色球的概率为
$$
\alpha_{2}(1)=\left[\sum_{i=1}^{3} \alpha_{1}(i) a_{i 1}\right] b_{1}\left(o_{2}\right)=[0.1 * 0.5+0.16 * 0.3+0.28 * 0.2] \times 0.5=0.077
$$
 {% label  关键 green %}: 这里可以理解成，在$t=2$的时候，且盒子为1时，它的$t=1$时刻可能是盒子1或盒子2或盒子3

也就是$t=2$的路径有(盒子1->盒子1、盒子2->盒子1、盒子3->盒子1)，由公式表述就是$$\sum_{i=1}^{3} \alpha_{1}(i) a_{i 1}$$

隐藏状态是盒子2且为白色球的概率为:
$$
\alpha_{2}(2)=\left[\sum_{i=1}^{3} \alpha_{1}(i) a_{i 2}\right] b_{2}\left(o_{2}\right)=[0.1 * 0.2+0.16 * 0.5+0.28 * 0.3] \times 0.6=0.1104
$$
隐藏状态是盒子 3 且为白色球的概率为:
$$
\alpha_{2}(3)=\left[\sum_{i=1}^{3} \alpha_{1}(i) a_{i 3}\right] b_{3}\left(o_{2}\right)=[0.1 * 0.3+0.16 * 0.2+0.28 * 0.5] \times 0.3=0.0606
$$

* $t=3$时刻的前向概率(在1时刻为红色球，2时刻为白色球的基础下)

隐藏状态是盒子1且为红色球的概率为:
$$
\begin{array}{l}
\alpha_{3}(1)=\left[\sum_{i=1}^{3} \alpha_{2}(i) a_{i 1}\right] b_{1}\left(o_{3}\right)=[0.077 * 0.5+0.1104 * 0.3+0.0606 * 0.2] \times 0.5 = 0.04187
\end{array}
$$
隐藏状态是盒子2且为红色球的概率为:
$$
\begin{array}{l}
\alpha_{3}(2)=\left[\sum_{i=1}^{3} \alpha_{2}(i) a_{i 2}\right] b_{2}\left(o_{3}\right)=[0.077 * 0.2+0.1104 * 0.5+0.0606 * 0.3] \times 0.4 =0.03551
\end{array}
$$
隐藏状态是盒子3且为红色球的概率为:
$$
\begin{array}{l}
\alpha_{3}(3)=\left[\sum_{i=1}^{3} \alpha_{2}(i) a_{i 3}\right] b_{3}\left(o_{3}\right)=[0.077 * 0.3+0.1104 * 0.2+0.0606 * 0.5] \times 0.7 =0.05284
\end{array}
$$
最终观测序列 $$O=\{ 红, 白, 红 \}$$ 的概率为: $$P(O \mid \lambda)=\sum_{i=1}^{3} \alpha_{3}(i)= 0.04187+0.03551+0.05284 = 0.13022$$

```python
import numpy as np


def cal_step(pa, pb, state, last):
    pa = np.array(pa)
    pb = np.array(pb)
    res = []
    for idx, s in enumerate(np.array(pb)[:, state]):
        tmp = sum([last[i] * a for i, a in enumerate(pa[:, idx])]) * s
        res.append(round(tmp, 4))
    return res


def cal_forward(pa, pb, ppi, po):
    """ 前向算法 """
    # 初始化状态
    init_state = [round(p * pb[idx][0], 4) for idx, p in enumerate(ppi)]
    print(init_state)

    state = init_state
    for step in range(1, len(po)):
        state = cal_step(pa=pa, pb=pb, state=po[step], last=state)
        print(state)

    print(round(sum(state), 4))


if __name__ == '__main__':
    pi = [0.2, 0.4, 0.4]
    B = [[0.5, 0.5], [0.4, 0.6], [0.7, 0.3], ]
    A = [[0.5, 0.2, 0.3], [0.3, 0.5, 0.2], [0.2, 0.3, 0.5], ]
    # 红 白 红
    O = [0, 1, 0]

    cal_forward(pa=A, pb=B, ppi=pi, po=O)
    print("结束")
```



### 🐝后向概率

> 定义

$$
\beta _t(i) = P(x_T, x_{T-1}, \cdots , x_{t+1}  | z_t =q_i, \lambda)
$$

也就是下图中标记的那一部分，$ \beta _t (i) $表示的是在$t$时刻，隐状态为$q_i$的概率

![img](https://pic.hycbook.com/i//hexo/bk_resources/machine_learning/隐马尔可夫模型HMM/HMM后向算法.webp)

> 后向概率初值，定义为1

$$
\beta _T(1) = \beta _T(2) = \cdots = \beta _T(N) =1
$$
根据后向概率定义可以推出
$$
\beta _1(i) = P(x_T, x_{T-1}, \cdots , x_2 | z_1=q_i, \lambda)
$$
然后来看上式和要计算的概率$ P(X| \lambda ) $之间的关系
$$
\begin{align}
& P(X| \lambda ) = P(x_1, x_2, \cdots , x_T | \lambda) = \sum _{i=1}^{N}{P(x_1, x_2, \cdots , x_T, z_1=q_i | \lambda)} \\
& = \sum _{i=1}^{N}{P(x_1 | x_2, \cdots , x_T, z_1=q_i , \lambda)P(x_2, \cdots , x_T, z_1=q_i | \lambda)} \\
& = \sum _{i=1}^{N}{P(x_1 | z_1=q_i) P(z_1=q_i | \lambda) P(x_T, x_{T-1}, \cdots, x_2 | z_1=q_i, \lambda)}  = \sum _{i=1}^{N}{b_i(x_1) \pi _i \beta _1(i)}
\end{align}
$$
上面$b_i(x_1) \pi _i$也就是$ \alpha _1(i) $的定义，实际上，对于任意时刻$ t $，存在以下等式
$$
P(X | \lambda) = \sum _{i=1}^{N}{\alpha _t(i) \beta _t(i)}
$$
接着，假设已知所有的$$\beta _{t+1}$$，来推导$$\beta _{t}$$
$$
\begin{align}
& \beta _{t}(i) = P(X_T, \cdots , x_{t+1} | z_t=q_i , \lambda) = \sum _{j=1}^{N}{P(x_T, \cdots , x_{t+1}, z_{t+1} =q_j | z_t=q_i , \lambda)} \\
& = \sum _{j=1}^{N}{P(x_T, \cdots , x_{t+1} | z_{t+1} =q_j , z_t=q_i , \lambda) P(z_{t+1} = q_j | z_t =q_i , \lambda)}
\end{align}
$$
观察上式，后部分实际上就是$\alpha _{ij}$，而前半部分，根据前向概率中的`观测独立性假设`，$z_t$与$x_1, \cdots ,x_T$都是无关的，即相互独立，可以省去，因此第二部分可以变为
$$
\begin{align}
& P(x_T, \cdots , x_{t+1} | z_{t+1} =q_j , z_t=q_i , \lambda) = P(x_T, \cdots , x_{t+1} | z_{t+1}=q_j , \lambda) \\
& = P(x_{t+1} | x_T, \cdots , x_{t+2}, z_{t+1}=q_j) P(x_T, \cdots , x_{t+2} | z_{t+1}=q_j , \lambda) = b_j(x_{t+1}) \beta _{t+1} (j)
\end{align}
$$
将结论代入$\beta _t{i}$得到
$$
\beta _t{(i)} = \sum _{j=1}^{N}{a_{ij}*b_j(x_{t+1})*\beta _{t+1}(j)}
$$

> 条件概率

$$
P(X|\lambda) = \sum _{i=1}^{N}{\pi _i b_i(o_1) \beta _1(i)}
$$

> 例子

题目仍为`前向概率`小节所描述

*  $t=2$时刻的后向概率

2时刻隐藏状态为盒子1的条件下， 3观测为红的概率为 $\beta_{2}(1)=0.5 \times 0.5+0.2 \times 0.4+0.3 \times 0.7=0.54$

2时刻隐藏状态为盒子2的条件下， 3观测为红的概率为 $\beta_{2}(2)=0.3 \times 0.5+0.5 \times 0.4+0.2 \times 0.7=0.49$

2时刻隐藏状态为䀂子3的条件下， 3观测为红的概率为 $\beta_{2}(3)=0.2 \times 0.5+0.3 \times 0.4+0.5 \times 0.7=0.57$

* $t=1$时刻的后向概率

1时刻隐藏状态为盒子1的条件下，2为白3为红的概率:
$$
\beta_{1}(1)=0.5 \times 0.5 \times 0.54+0.2 \times 0.6 \times 0.49+0.3 \times 0.3 \times 0.57=0.2451
$$
1时刻隐藏状态为盒子2的条件下，2为白3为红的概率:
$$
\beta_{1}(2)=0.3 \times 0.5 \times 0.54+0.5 \times 0.6 \times 0.49+0.2 \times 0.3 \times 0.57=0.2622
$$
1时刻隐藏状态为盒子2的条件下，2为白3为红的概率:
$$
\beta_{1}(3)=0.2 \times 0.5 \times 0.54+0.3 \times 0.6 \times 0.49+0.5 \times 0.3 \times 0.57=0.2277
$$
最终观测序列$O=\{ 红, 白,  红 \}$ 的概率为:
$$
P(O \mid \lambda)=0.2 \times 0.5 \times 0.2451+0.4 \times 0.4 \times 0.2622+0.4 \times 0.7 \times 0.2277=0.13022
$$


## 参数学习



## 解码问题



