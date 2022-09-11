---
title: MySQL_约束
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: fcd59143
---

![img](res/other/异世界蕾姆_1.png)

[TOC]

> [MySQL约束与设计](./res/MySQL_数据库设计/MySQL约束与设计.pdf)

## 

# 约束

> 概念： 对表中的数据进行限定，保证数据的正确性、有效性和完整性。	
>
> 分类：
> * 主键约束：primary key
> * 非空约束：not null
> * 唯一约束：unique
> * 外键约束：foreign key
>
> * 非空约束：not null，值不能为null
>
> ```mysql
> -- 创建表时添加约束
> CREATE TABLE stu(
>    	id INT,
>    	NAME VARCHAR(20) NOT NULL -- name为非空
> );
> -- 创建表完后，添加非空约束
> ALTER TABLE stu MODIFY NAME VARCHAR(20) NOT NULL;
> 
> -- 删除name的非空约束
> ALTER TABLE stu MODIFY NAME VARCHAR(20);
> ```
>
> 

# 唯一约束：unique

>值不能重复
>
>```mysql
>-- 创建表时，添加唯一约束
>CREATE TABLE stu(
>	id INT,
>	phone_number VARCHAR(20) UNIQUE -- 添加了唯一约束
>);
>-- 注意mysql中，唯一约束限定的列的值可以有多个null
>
>-- 删除唯一约束
>ALTER TABLE stu DROP INDEX phone_number;
>
>-- 在创建表后，添加唯一约束
>ALTER TABLE stu MODIFY phone_number VARCHAR(20) UNIQUE;
>```
>
>

# 主键约束：primary key

> 注意：
> * 含义：非空且唯一
> * 一张表只能有一个字段为主键
> * 主键就是表中记录的唯一标识
>
> ```mysql
> -- 在创建表时，添加主键约束
> create table stu(
> 	id int primary key,-- 给id添加主键约束
> 	name varchar(20)
> );
> 
> -- 删除主键
> -- 错误 alter table stu modify id int ;
> ALTER TABLE stu DROP PRIMARY KEY;
> 
> -- 创建完表后，添加主键
> ALTER TABLE stu MODIFY id INT PRIMARY KEY;
> 
> -- 自动增长：
> -- 概念：如果某一列是数值类型的，使用 auto_increment 可以来完成值得自动增长
> -- 在创建表时，添加主键约束，并且完成主键自增长
> create table stu(
> 	id int primary key auto_increment,-- 给id添加主键约束
> 	name varchar(20)
> );
> 
> -- 删除自动增长
> ALTER TABLE stu MODIFY id INT;
> 
> -- 添加自动增长
> ALTER TABLE stu MODIFY id INT AUTO_INCREMENT;
> ```

# 外键约束：foreign key

> 让表于表产生关系，从而保证数据的正确性。
> ```mysql
> -- 在创建表时，可以添加外键
> create table 表名(
> 	....
> 	外键列
> 	constraint 外键名称 foreign key (外键列名称) references 主表名称(主表列名称)
> );
> 
> -- 删除外键
> ALTER TABLE 表名 DROP FOREIGN KEY 外键名称;
> 
> -- 创建表之后，添加外键
> ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY (外键字段名称) REFERENCES 主表名称(主表列名称);
> ```

# 级联操作

> ```mysql
> -- 添加级联操作
> ALTER TABLE 表名 ADD CONSTRAINT 外键名称 FOREIGN KEY (外键字段名称) REFERENCES 主表名称(主表列名称) ON UPDATE CASCADE ON DELETE CASCADE;
> 
> -- 分类：
> 1. 级联更新：ON UPDATE CASCADE 
> 2. 级联删除：ON DELETE CASCADE 
> ```
>
> 



