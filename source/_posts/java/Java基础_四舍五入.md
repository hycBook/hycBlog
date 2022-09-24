---
title: Java基础_四舍五入
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: 48f373f3
---

---

[TOC]


# 四舍五入

```java
ROUND_UP：远离零方向舍入。向绝对值最大的方向舍入，只要舍弃位非0即进位。
ROUND_DOWN：趋向零方向舍入。向绝对值最小的方向输入，所有的位都要舍弃，不存在进位情况。
ROUND_CEILING：向正无穷方向舍入。向正最大方向靠拢。若是正数，舍入行为类似于ROUND_UP，若为负数，舍入行为类似于ROUND_DOWN。Math.round()方法就是使用的此模式。
ROUND_FLOOR：向负无穷方向舍入。向负无穷方向靠拢。若是正数，舍入行为类似于ROUND_DOWN；若为负数，舍入行为类似于ROUND_UP。
HALF_UP：最近数字舍入(5进)。这是我们最经典的四舍五入。
HALF_DOWN：最近数字舍入(5舍)。在这里5是要舍弃的。
HAIL_EVEN：银行家舍入法。

public class Test {
    public static void main(String[] args) {
        double a = 1.66728D;
        double b = 1.33333D;
        double c = 1.00000D;

        BigDecimal aa = new BigDecimal(a);
        BigDecimal bb = new BigDecimal(b);
        BigDecimal cc = new BigDecimal(c);
        System.out.println(aa.setScale(2, BigDecimal.ROUND_UP));
        System.out.println(aa.setScale(2, BigDecimal.ROUND_DOWN));
        System.out.println(bb.setScale(2, BigDecimal.ROUND_UP));
        System.out.println(bb.setScale(2, BigDecimal.ROUND_DOWN));
        System.out.println(cc.setScale(2, BigDecimal.ROUND_UP));
        System.out.println(cc.setScale(2, BigDecimal.ROUND_DOWN));
        System.out.println("-------------------------------------");
        System.out.println(aa.setScale(2, RoundingMode.UP));
        System.out.println(aa.setScale(2, RoundingMode.DOWN));
        System.out.println(bb.setScale(2, RoundingMode.UP));
        System.out.println(bb.setScale(2, RoundingMode.DOWN));
        System.out.println(cc.setScale(2, RoundingMode.UP));
        System.out.println(cc.setScale(2, RoundingMode.DOWN));

    }
}

1.67
1.66
1.34
1.33
1.00
1.00
-------------------------------------
1.67
1.66
1.34
1.33
1.00
1.00
```













