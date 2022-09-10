---
title: MySQL_基础
date: 2022/9/10 20:46:25
---

![img](res/other/异世界蕾姆_1.png)

[TOC]



>[【黑马程序员-Java语言高级部分10】MySQL入门学习](https://www.bilibili.com/video/av56473701)



---

# 基础概念

>`数据库`的英文单词： DataBase(简称DB)
>
>数据库: 用于存储和管理数据的仓库
>
>数据库的**特点**：
>
>* **持久化**存储数据的。其实数据库就是一个文件系统
>* 方便**存储**和**管理**数据
>* 使用了**统一**的方式**操作**数据库 -- SQL
>
>[常见的数据库软件](./res/MySQL_基础/MySQL基础.pdf)



# 数据库软件

> 1. [安装](./res/MySQL_基础/MySQL基础.pdf)
>
> 2. 卸载
>
>    > * 去mysql的安装目录找到my.ini文件
>    >   复制 datadir="C:/ProgramData/MySQL/MySQL Server 5.5/Data/"
>    > * 卸载MySQL
>    > * 删除C:/ProgramData目录下的MySQL文件夹。
>
> 3. 配置
>
>    >* **MySQL服务启动**
>    >
>    >   > * 手动
>    >   >
>    >   > * cmd--> services.msc 打开服务的窗口
>    >   >
>    >   > * 使用管理员打开cmd
>    >   >   * net start mysql : 启动mysql的服务
>    >   >   * net stop mysql:关闭mysql服务
>    >
>    >* **MySQL登录**
>    >
>    >   > * mysql -uroot -p密码
>    >   >
>    >   > * mysql -hip -uroot -p连接目标的密码
>    >   >
>    >   > * mysql --host=ip --user=root --password=连接目标的密码
>    >
>    >* **MySQL退出**(exit or quit)
>    >
>    >* **MySQL目录结构**
>    >
>    >   > 1. MySQL安装目录：basedir="D:/develop/MySQL/"
>    >   >    * 配置文件 my.ini
>    >   > 2. MySQL数据目录：datadir="C:/ProgramData/MySQL/MySQL Server 5.5/Data/"
>    >   >    * 几个概念
>    >   >      * 数据库：文件夹
>    >   >      * 表：文件
>    >   >      * 数据：数据
>    >
>    >
>
>    



# SQL基础

> **什么是SQL**
>
> > Structured Query Language：结构化查询语言
> > 其实就是定义了操作所有关系型数据库的规则。每一种数据库操作的方式存在不一样的地方，称为“方言”。
>
> **SQL通用语法**
>
> > SQL 语句可以单行或多行书写，以分号结尾。
> >
> > 可使用空格和缩进来增强语句的可读性。
> >
> > MySQL 数据库的 SQL 语句不区分大小写，关键字建议使用大写。
> >
> > 3种注释
> >
> > * 单行注释: -- 注释内容 或 # 注释内容(mysql 特有) 
> > * 多行注释: /* 注释 */
>
> **SQL分类**
>
> > `DDL(Data Definition Language)数据定义语言`
> > 	用来定义数据库对象：数据库，表，列等。关键字：create, drop,alter 等
> >
> > `DML(Data Manipulation Language)数据操作语言`
> > 	用来对数据库中表的数据进行增删改。关键字：insert, delete, update 等
> >
> > `DQL(Data Query Language)数据查询语言`
> > 	用来查询数据库中表的记录(数据)。关键字：select, where 等
> > `DCL(Data Control Language)数据控制语言(了解)`
> > 	用来定义数据库的访问权限和安全级别，及创建用户。关键字：GRANT， REVOKE 等
> 
> ![异世界.png](res/MySQL_%E5%9F%BA%E7%A1%80/SQL分类.bmp)

# DDL: 操作数据库、表

## 操作数据库：CRUD

> 1. C(Create): **创建**
>   * 创建数据库：
>
>     ```mysql
>     create database 数据库名称;
>     ```
>
>   * 创建数据库，判断不存在，再创建：
>
>     ```mysql
>     create database if not exists 数据库名称;
>     ```
>
>   * 创建数据库，并指定字符集
>
>     ```mysql
>     create database 数据库名称 character set 字符集名;
>     ```
>
>   * 练习： 创建db4数据库，判断是否存在，并制定字符集为gbk
>
>     ```mysql
>     create database if not exists db4 character set gbk;
>     ```
> 2. R(Retrieve)：**查询**
>   * 查询所有数据库的名称:
>
>     ```mysql
>     show databases;
>     ```
>
>   * 查询某个数据库的字符集:查询某个数据库的创建语句
>
>     ```mysql
>     show create database 数据库名称;
>     ```
> 3. U(Update): **修改**
>   * 修改数据库的字符集
>
>     ```mysql
>     alter database 数据库名称 character set 字符集名称;
>     ```
> 4. D(Delete): **删除**
>   * 删除数据库
>
>     ```mysql
>     drop database 数据库名称;
>     ```
>
>   * 判断数据库存在，存在再删除
>
>     ```mysql
>     drop database if exists 数据库名称;
>     ```
> 5. **使用**数据库
>
>   * 查询当前正在使用的数据库名称
>
>     ```mysql
>     select database();
>     ```
>
>   * 使用数据库
>
>     ```mysql
>     use 数据库名称;
>     ```

## 操作表

> 1. C(Create): **创建**
>     ```mysql
>     create table 表名(
>     		列名1 数据类型1,
>     		列名2 数据类型2,
>     		....
>     		列名n 数据类型n
>     	);
>     ```
>
>      * 注意：最后一列，不需要加逗号（,）
>
>     > 数据库类型：
>     >
>     > 1. int：整数类型
>     >    * age int,
>     > 2. double:小数类型
>     >    * score double(5,2)
>     > 3. date:日期，只包含年月日，yyyy-MM-dd
>     > 4. datetime:日期，包含年月日时分秒	 yyyy-MM-dd HH:mm:ss
>     > 5. timestamp:时间错类型	包含年月日时分秒	 yyyy-MM-dd HH:mm:ss	
>     >    * 如果将来不给这个字段赋值，或赋值为null，则默认使用当前的系统时间，来自动赋值
>     > 6. varchar：字符串
>     >    * name varchar(20): 姓名最大20个字符
>     >    * zhangsan 8个字符  张三 2个字符
>
>     创建表:
>
>     ```mysql
>     create table student(
>     		id int,
>     		name varchar(32),
>     		age int ,
>     		score double(4,1),
>     		birthday date,
>     		insert_time timestamp
>     	);
>     ```
>
>     复制表：
>
>     ```mysql
>     create table 表名 like 被复制的表名;
>     ```
>
> 2. R(Retrieve): **查询**
>   * 查询某个数据库中所有的表名称
>
>     ```mysql
>     show tables;
>     ```
>
>   * 查询表结构
>
>     ```mysql
>     desc 表名;
>     ```
>
> 3. U(Update): **修改**
>   * 修改表名
>
>     ```mysql
>     alter table 表名 rename to 新的表名;
>     ```
>     
>   * 修改表的字符集
>     
> ```mysql
>     alter table 表名 character set 字符集名称;
> ```
>
> * 添加一列
>
>   ```mysql
>   alter table 表名 add 列名 数据类型;
>   ```
>
> * 修改列名称 类型
>
>   ```mysql
>   alter table 表名 change 列名 新列别 新数据类型;
>   alter table 表名 modify 列名 新数据类型;
>   ```
>
> * 删除列
>
>   ```mysql
>   alter table 表名 drop 列名;
>   ```
>
> * D(Delete):删除
>
>   ```mysql
>   drop table 表名;
>   drop table  if exists 表名 ;
>   ```
>
> * 
>   



# DML: 增删改表中数据

> * 添加数据：
>
>   ```mysql
>   insert into 表名(列名1,列名2,...列名n) values(值1,值2,...值n);
>   ```
>
>   注意:
>
>   ```mysql
>   列名和值要一一对应。
>   如果表名后，不定义列名，则默认给所有列添加值
>   	insert into 表名 values(值1,值2,...值n);
>   除了数字类型，其他类型需要使用引号(单双都可以)引起来
>   ```
>
>   
>
> * 删除数据：
>
>   ```mysql
>   delete from 表名 [where 条件]
>   ```
>
>   注意:
>
>   ```mysql
>   如果不加条件，则删除表中所有记录。
>   如果要删除所有记录
>   	delete from 表名; -- 不推荐使用。有多少条记录就会执行多少次删除操作
>   	TRUNCATE TABLE 表名; -- 推荐使用，效率更高 先删除表，然后再创建一张一样的表。
>   ```
>
> * 修改数据：
>
>   ```mysql
>   update 表名 set 列名1 = 值1, 列名2 = 值2,... [where 条件];
>   ```
>
>   注意: 如果不加任何条件，则会将表中所有记录全部修改。
>
> * 备用
>
> 



# DQL: 查询表中的记录

## 语法

```mysql
select
		字段列表
	from
		表名列表
	where
		条件列表
	group by
		分组字段
	having
		分组之后的条件
	order by
		排序
	limit
		分页限定;
```

## 基础查询

> * 多个字段的查询
>
>   ```mysql
>   select 字段名1，字段名2... from 表名；
>   ```
>
>   注意：如果查询所有字段，则可以使用*来替代字段列表。
>
> * 去除重复: distinct
>
> * 计算列
>
>   * 一般可以使用四则运算计算一些列的值。（一般只会进行数值型的计算）
>   * ifnull(表达式1,表达式2)：null参与的运算，计算结果都为null
>      * 表达式1：哪个字段需要判断是否为null
>      * 如果该字段为null后的替换值。
>
> * 起别名  as：as也可以省略
>
> * 备用
>
> 

## 条件查询

> * where子句后跟条件
>
> * 运算符
>
>   ```mysql
>   > 、< 、<= 、>= 、= 、<>
>   BETWEEN...AND  
>   IN( 集合) 
>   LIKE：模糊查询
>   占位符：
>   	_: 单个任意字符
>   	%：多个任意字符
>   IS NULL  
>   and  或 &&
>   or  或 || 
>   not  或 !
>   ```
>
> * 示例
>
>   ```mysql
>   -- 查询年龄大于20岁
>   SELECT * FROM student WHERE age > 20;
>   SELECT * FROM student WHERE age >= 20;
>   			  
>   -- 查询年龄等于20岁
>   SELECT * FROM student WHERE age = 20;
>   			  
>   -- 查询年龄不等于20岁
>   SELECT * FROM student WHERE age != 20;
>   SELECT * FROM student WHERE age <> 20;
>   			  
>   -- 查询年龄大于等于20 小于等于30
>   SELECT * FROM student WHERE age >= 20 &&  age <=30;
>   SELECT * FROM student WHERE age >= 20 AND  age <=30;
>   SELECT * FROM student WHERE age BETWEEN 20 AND 30;
>   			  
>   -- 查询年龄22岁，18岁，25岁的信息
>   SELECT * FROM student WHERE age = 22 OR age = 18 OR age = 25
>   SELECT * FROM student WHERE age IN (22,18,25);
>   			  
>   -- 查询英语成绩为null
>   SELECT * FROM student WHERE english = NULL; -- 不对的。null值不能使用 = （!=） 判断
>   SELECT * FROM student WHERE english IS NULL;
>   			  
>   -- 查询英语成绩不为null
>   SELECT * FROM student WHERE english  IS NOT NULL;
>   			  
>   -- 查询姓马的有哪些？ like
>   SELECT * FROM student WHERE NAME LIKE '马%';
>     
>   -- 查询姓名第二个字是化的人
>   SELECT * FROM student WHERE NAME LIKE "_化%";
>   			  
>   -- 查询姓名是3个字的人
>   SELECT * FROM student WHERE NAME LIKE '___';
>   			  
>   -- 查询姓名中包含德的人
>   SELECT * FROM student WHERE NAME LIKE '%德%';
>   ```
>
>   
>
> * 备用

## 排序查询

> * 语法：order by 子句
>   * order by 排序字段1 排序方式1 ，  排序字段2 排序方式2...
>
> * 排序方式：
>   * ASC：升序，默认的。
>   * DESC：降序。
>
> * 注意：
>   * 如果有多个排序条件，则当前边的条件值一样时，才会判断第二条件。

## 聚合函数

> 将一列数据作为一个整体，进行纵向的计算
>
> * count：计算个数
>
>   一般选择非空的列：主键
>
>   count(*)
>
> * max：计算最大值
>
> * min：计算最小值
>
> * sum：计算和
>
> * avg：计算平均值
>
> 注意：聚合函数的计算，排除null值。
> 解决方案：
>
> * 选择不包含非空的列进行计算
> * IFNULL函数

## 分组查询

> 语法：group by 分组字段；
>
> 注意：
>
> * 分组之后查询的字段：分组字段、聚合函数
>
> * where 和 having 的区别？
>
>   where 在分组之前进行限定，如果不满足条件，则不参与分组。
>
>   having在分组之后进行限定，如果不满足结果，则不会被查询出来
>
>   where 后不可以跟聚合函数，having可以进行聚合函数的判断。
>
> ```mysql
> -- 按照性别分组。分别查询男、女同学的平均分
> SELECT sex , AVG(math) FROM student GROUP BY sex;
> 
> -- 按照性别分组。分别查询男、女同学的平均分,人数
> SELECT sex , AVG(math),COUNT(id) FROM student GROUP BY sex;
> 
> --  按照性别分组。分别查询男、女同学的平均分,人数 要求：分数低于70分的人，不参与分组
> SELECT sex , AVG(math),COUNT(id) FROM student WHERE math > 70 GROUP BY sex;
> 
> --  按照性别分组。分别查询男、女同学的平均分,人数 要求：分数低于70分的人，不参与分组,分组之后。人数要大于2个人
> SELECT sex , AVG(math),COUNT(id) FROM student WHERE math > 70 GROUP BY sex HAVING COUNT(id) > 2;
> SELECT sex , AVG(math),COUNT(id) 人数 FROM student WHERE math > 70 GROUP BY sex HAVING 人数 > 2;
> ```
>
> 

## 分页查询

> 语法：limit 开始的索引,每页查询的条数;
>
> 公式：开始的索引 = （当前的页码 - 1） * 每页显示的条数
> limit 是一个MySQL"方言"
>
> ```mysql
> -- 每页显示3条记录 
> SELECT * FROM student LIMIT 0,3; -- 第1页
> SELECT * FROM student LIMIT 3,3; -- 第2页
> SELECT * FROM student LIMIT 6,3; -- 第3页
> ```
>
> 

# DCL：管理用户和授权

## 用户管理

### 添加用户

```mysql
CREATE USER '用户名'@'主机名' IDENTIFIED BY '密码';
```

### 删除用户

```mysql
DROP USER '用户名'@'主机名';
```

### 修改用户密码

```mysql
UPDATE USER SET PASSWORD = PASSWORD('新密码') WHERE USER = '用户名';
UPDATE USER SET PASSWORD = PASSWORD('abc') WHERE USER = 'lisi';
			
SET PASSWORD FOR '用户名'@'主机名' = PASSWORD('新密码');
SET PASSWORD FOR 'root'@'localhost' = PASSWORD('123');
```

### 忘记密码

>1. 管理员运行cmd
>
>   ```mysql
>   net stop mysql --停止mysql服务
>   ```
>
>2. 使用无验证方式启动mysql服务
>
>   ```mysql
>   mysqld --skip-grant-tables
>   ```
>
>3. 使用无验证方式启动mysql服务
>
>4. 打开新的cmd窗口,直接输入mysql命令，敲回车就可以登录成功
>
>   ```mysql
>   use mysql;
>   update user set password = password('你的新密码') where user = 'root';
>   ```
>
>5. 关闭两个窗口
>
>6. 打开任务管理器，手动结束mysqld.exe 的进程
>
>7. 启动mysql服务，使用新密码登录
>
>

### 查询用户

```mysql
-- 1. 切换到mysql数据库
USE myql;
-- 2. 查询user表
SELECT * FROM USER;		
-- * 通配符： % 表示可以在任意主机使用用户登录数据库
```

## 权限管理

### 查询权限

```mysql
SHOW GRANTS FOR '用户名'@'主机名';
SHOW GRANTS FOR 'lisi'@'%';
```

### 授予权限

```mysql
-- 授予权限
grant 权限列表 on 数据库名.表名 to '用户名'@'主机名';
-- 给张三用户授予所有权限，在任意数据库任意表上
GRANT ALL ON *.* TO 'zhangsan'@'localhost';
```

### 撤销权限

```mysql
-- 撤销权限
revoke 权限列表 on 数据库名.表名 from '用户名'@'主机名';
REVOKE UPDATE ON db3.`account` FROM 'lisi'@'%';
```

