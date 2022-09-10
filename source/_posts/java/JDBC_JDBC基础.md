---
title: JDBC_JDBC基础
date: 2022/9/10 20:46:25
---

![img](res/other/异世界蕾姆_1.png)

[TOC]

>[【黑马程序员-Java语言高级部分11】JDBC](https://www.bilibili.com/video/av61491585)

---

# 基础概念

>**概念**：Java DataBase Connectivity  Java 数据库连接， Java语言操作数据库
>
>[JDBC笔记](./res/JDBC_JDBC基础/JDBC笔记.pdf)
>
>**JDBC**`本质`：其实是官方（sun公司）定义的一套操作所有关系型数据库的规则，即接口。各个数据库厂商去实现这套接口，提供数据库驱动jar包。我们可以使用这套接口（JDBC）编程，真正执行的代码是驱动jar包中的实现类。
>
>![image-20200322202245440](res/JDBC_JDBC%E5%9F%BA%E7%A1%80/image-20200322202245440.png)

## 快速入门

>**步骤**：
>
>> 1. 导入驱动jar包 mysql-connector-java-5.1.37-bin.jar
>>
>>    复制mysql-connector-java-5.1.37-bin.jar到项目的libs目录下
>>
>>    右键-->Add As Library
>>
>> 2. 注册驱动
>>
>> 3. 获取数据库连接对象 Connection
>>
>> 4. 定义sql
>>
>> 5. 获取执行sql语句的对象 Statement
>>
>> 6. 执行sql，接受返回结果
>>
>> 7. 处理结果
>>
>> 8. 释放资源
>
>**代码实现**
>
>```java
>// 1. 导入驱动jar包
>// 2.注册驱动
>Class.forName("com.mysql.jdbc.Driver");
>// 3.获取数据库连接对象
>Connection conn = DriverManager.getConnection("jdbc:mysql://localhost:3306/db3", "root", "root");
>// 4.定义sql语句
>String sql = "update account set balance = 500 where id = 1";
>// 5.获取执行sql的对象 Statement
>Statement stmt = conn.createStatement();
>// 6.执行sql
>int count = stmt.executeUpdate(sql);
>// 7.处理结果
>System.out.println(count);
>// 8.释放资源
>stmt.close();
>conn.close();
>```
>
>

# 关键对象

## DriverManager(驱动管理对象)

> **功能**：
>
> ```java
> // 1. 注册驱动：告诉程序该使用哪一个数据库驱动jar
> static void registerDriver(Driver driver) :注册与给定的驱动程序 DriverManager 。 
> // 写代码使用：  
> Class.forName("com.mysql.jdbc.Driver");
> // 通过查看源码发现：在com.mysql.jdbc.Driver类中存在静态代码块
> static {
> 	try {
> 		java.sql.DriverManager.registerDriver(new Driver());
> 		} catch (SQLException E) {
> 		throw new RuntimeException("Can't register driver!");
> 		}
> }
> // 注意：mysql5之后的驱动jar包可以省略注册驱动的步骤。
> ```
>
> ```java
> // 2. 获取数据库连接：
> // 方法：static Connection getConnection(String url, String user, String password) 
> // 细节：如果连接的是本机mysql服务器，并且mysql服务默认端口是3306，则url可以简写为：jdbc:mysql:///数据库名称
> ```
>
> 

## Connection(数据库连接对象)

> 1. 获取执行sql 的对象
> 				
> 	Statement createStatement()
> 	
> 	PreparedStatement prepareStatement(String sql)  
> 	
> 2. 管理事务
>
>       开启事务：setAutoCommit(boolean autoCommit) ：调用该方法设置参数为false，即开启事务
>
>       提交事务：commit() 
>
>       回滚事务：rollback() 

## Statement(执行sql的对象)

>1. boolean execute(String sql) ：可以执行任意的sql 了解 
>
>2. int executeUpdate(String sql) ：执行DML（insert、update、delete）语句、DDL(create，alter、drop)语句
>
>   返回值：影响的行数，可以通过这个影响的行数判断DML语句是否执行成功 返回值>0的则执行成功，反之，则失败。
>
>3. ResultSet executeQuery(String sql): 执行DQL(select)语句
>
>示例:
>
>```java
>Statement stmt = null;
>Connection conn = null;
>try {
>	// 1. 注册驱动
>	Class.forName("com.mysql.jdbc.Driver");
>	// 2. 定义sql
>	String sql = "insert into account values(null,'王五',3000)";
>	// 3. 获取Connection对象
>	conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
>	// 4. 获取执行sql的对象 Statement
>	stmt = conn.createStatement();
>	// 5. 执行sql
>	int count = stmt.executeUpdate(sql);//影响的行数
>	// 6. 处理结果
>	System.out.println(count);
>	if(count > 0){
>		System.out.println("添加成功！");
>	}else{
>		System.out.println("添加失败！");
>	}
>} catch (ClassNotFoundException e) {
>	e.printStackTrace();
>} catch (SQLException e) {
>	e.printStackTrace();
>}finally {
>	// 7. 释放资源
>	// 避免空指针异常
>	if(stmt != null){
>        try {
>            stmt.close();
>		} catch (SQLException e) {
>			e.printStackTrace();
>		}
>	}
>	if(conn != null){
>		try {
>			conn.close();
>		} catch (SQLException e) {
>			e.printStackTrace();
>		}
>	}
>}
>```
>
>

## ResultSet(结果集对象)

>boolean next(): 游标向下移动一行，判断当前行是否是最后一行末尾(是否有数据)，如果是，则返回false，如果不是则返回true
>
>getXxx(参数): 获取数据
>
>Xxx：代表数据类型   如： int getInt() ,	String getString()
>
>参数：
>
>1. int：代表列的编号,从1开始   如： getString(1)
>
>	2. String：代表列名称。 如： getDouble("balance")
>
>```java
>// 循环判断游标是否是最后一行末尾。
>while(rs.next()){
>	// 获取数据
>	// 6.2 获取数据
>	int id = rs.getInt(1);
>	String name = rs.getString("name");
>	double balance = rs.getDouble(3);
>	System.out.println(id + "---" + name + "---" + balance);
>}
>```
>
>

## PreparedStatement(执行sql的对象)

>QL注入问题：在拼接sql时，有一些sql的特殊关键字参与字符串的拼接。会造成安全性问题
>
>* 输入用户随便，输入密码：a' or 'a' = 'a
>* sql：select * from user where username = 'fhdsjkf' and password = 'a' or 'a' = 'a' 
>
>解决sql注入问题：使用PreparedStatement对象来解决
>
>预编译的SQL：参数使用?作为占位符
>
>* 驱动jar包 mysql-connector-java-5.1.37-bin.jar
>* 注册驱动
>* 获取数据库连接对象 Connection
>* 定义sql	sql的参数使用?作为占位符。 如：select * from user where username=? and password = ?;
>* 获取执行sql语句的对象 PreparedStatement  Connection.prepareStatement(String sql) 
>* 给？赋值   setXxx(位置编号, 参数值)
>* 执行sql，接受返回结果，不需要传递sql语句
>* 处理结果
>* 释放资源
>
>**优点**
>
>* 可以防止SQL注入
>* 效率更高

# JDBC工具类 

>目的：简化书写
>
>抽取一个方法获取连接对象
>
>需求：不想传递参数（麻烦），还得保证工具类的通用性
>
>解决：配置文件

> jdbc.properties
>
> ```properties
> url=jdbc:mysql:///db3
> user=root
> password=root
> driver=com.mysql.jdbc.Driver
> ```

>```java
>import java.io.FileReader;
>import java.io.IOException;
>import java.net.URL;
>import java.sql.*;
>import java.util.Properties;
>
>/**
> * JDBC工具类
> */
>public class JDBCUtils {
>    private static String url;
>    private static String user;
>    private static String password;
>    private static String driver;
>    /**
>     * 文件的读取，只需要读取一次即可拿到这些值。使用静态代码块
>     */
>    static{
>        //读取资源文件，获取值
>        try {
>            //1. 创建Properties集合类。
>            Properties pro = new Properties();
>
>            //获取src路径下的文件的方式--->ClassLoader 类加载器
>            ClassLoader classLoader = JDBCUtils.class.getClassLoader();
>            URL res  = classLoader.getResource("jdbc.properties");
>            String path = res.getPath();
>           //2. 加载文件
>            pro.load(new FileReader(path));
>
>            //3. 获取数据，赋值
>            url = pro.getProperty("url");
>            user = pro.getProperty("user");
>            password = pro.getProperty("password");
>            driver = pro.getProperty("driver");
>            //4. 注册驱动
>            Class.forName(driver);
>        } catch (IOException e) {
>            e.printStackTrace();
>        } catch (ClassNotFoundException e) {
>            e.printStackTrace();
>        }
>    }
>
>    /**
>     * 获取连接
>     * @return 连接对象
>     */
>    public static Connection getConnection() throws SQLException {
>
>        return DriverManager.getConnection(url, user, password);
>    }
>
>    /**
>     * 释放资源
>     * @param stmt
>     * @param conn
>     */
>    public static void close(Statement stmt,Connection conn){
>        if( stmt != null){
>            try {
>                stmt.close();
>            } catch (SQLException e) {
>                e.printStackTrace();
>            }
>        }
>        if( conn != null){
>            try {
>                conn.close();
>            } catch (SQLException e) {
>                e.printStackTrace();
>            }
>        }
>    }
>
>    /**
>     * 释放资源
>     * @param stmt
>     * @param conn
>     */
>    public static void close(ResultSet rs,Statement stmt, Connection conn){
>        if( rs != null){
>            try {
>                rs.close();
>            } catch (SQLException e) {
>                e.printStackTrace();
>            }
>        }
>
>        if( stmt != null){
>            try {
>                stmt.close();
>            } catch (SQLException e) {
>                e.printStackTrace();
>            }
>        }
>
>        if( conn != null){
>            try {
>                conn.close();
>            } catch (SQLException e) {
>                e.printStackTrace();
>            }
>        }
>    }
>}
>```
>
>

## 修改记录

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 修改记录
 */
public class JDBCDemo3 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql  = "update account set balance = 1500 where id = 3";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("修改成功！");
            }else{
                System.out.println("修改失败");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```

## 添加记录

```java
package cn.itcast.jdbc;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 添加一条记录 insert 语句
 */
public class JDBCDemo2 {
    public static void main(String[] args) {
        Statement stmt = null;
        Connection conn = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2. 定义sql
            String sql = "insert into account values(null,'王五',3000)";
            //3.获取Connection对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //4.获取执行sql的对象 Statement
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);//影响的行数
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("添加成功！");
            }else{
                System.out.println("添加失败！");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            //stmt.close();
            //7. 释放资源
            //避免空指针异常
            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```

## 删除记录

```java
package cn.itcast.jdbc;


import cn.itcast.util.JDBCUtils;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

/**
 * account表 删除一条记录
 */
public class JDBCDemo4 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
           //conn = JDBCUtils.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql  = "delete from account where id = 3";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            int count = stmt.executeUpdate(sql);
            //6.处理结果
            System.out.println(count);
            if(count > 0){
                System.out.println("删除成功！");
            }else{
                System.out.println("删除失败");
            }

        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源

            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }

            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}

```

## 执行DDL语句

```java
package cn.itcast.jdbc;

import java.sql.*;

/**
 * 执行DDL语句
 */
public class JDBCDemo7 {
    public static void main(String[] args) {
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        try {
            //1. 注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接对象
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql  = "select * from account";
            //4.获取执行sql对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.处理结果
            //循环判断游标是否是最后一行末尾。
            while(rs.next()){

                //获取数据
                //6.2 获取数据
                int id = rs.getInt(1);
                String name = rs.getString("name");
                double balance = rs.getDouble(3);

                System.out.println(id + "---" + name + "---" + balance);
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        } finally {
            //7.释放资源
            if(rs != null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```



## 查询并封装

```java
import cn.itcast.domain.Emp;
import cn.itcast.util.JDBCUtils;
import java.sql.*;
import java.util.ArrayList;
import java.util.List;

/**
 * * 定义一个方法，查询emp表的数据将其封装为对象，然后装载集合，返回。
 */
public class JDBCDemo8 {
    public static void main(String[] args) {
        List<Emp> list = new JDBCDemo8().findAll2();
        System.out.println(list);
        System.out.println(list.size());
    }
    /**
     * 查询所有emp对象
     * @return
     */
    public List<Emp> findAll(){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;
        try {
            //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");
            //3.定义sql
            String sql = "select * from emp";
            //4.获取执行sql的对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.遍历结果集，封装对象，装载集合
            Emp emp = null;
            list = new ArrayList<Emp>();
            while(rs.next()){
                //获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象,并赋值
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);
                //装载集合
                list.add(emp);
            }
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            if(rs != null){
                try {
                    rs.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(stmt != null){
                try {
                    stmt.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
            if(conn != null){
                try {
                    conn.close();
                } catch (SQLException e) {
                    e.printStackTrace();
                }
            }
        }
        return list;
    }

    /**
     * 演示JDBC工具类
     * @return
     */
    public List<Emp> findAll2(){
        Connection conn = null;
        Statement stmt = null;
        ResultSet rs = null;
        List<Emp> list = null;
        try {
           /* //1.注册驱动
            Class.forName("com.mysql.jdbc.Driver");
            //2.获取连接
            conn = DriverManager.getConnection("jdbc:mysql:///db3", "root", "root");*/
            conn = JDBCUtils.getConnection();
            //3.定义sql
            String sql = "select * from emp";
            //4.获取执行sql的对象
            stmt = conn.createStatement();
            //5.执行sql
            rs = stmt.executeQuery(sql);
            //6.遍历结果集，封装对象，装载集合
            Emp emp = null;
            list = new ArrayList<Emp>();
            while(rs.next()){
                //获取数据
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");
                // 创建emp对象,并赋值
                emp = new Emp();
                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);
                //装载集合
                list.add(emp);
            }

        } catch (SQLException e) {
            e.printStackTrace();
        }finally {
            JDBCUtils.close(rs,stmt,conn);
        }
        return list;
    }
}
```

# JDBC控制事务

>`事务`：一个包含多个步骤的业务操作。如果这个业务操作被事务管理，则这多个步骤同时成功或同时失败。
>
>操作：
>* 开启事务
>* 提交事务
>* 回滚事务
>
>使用Connection对象来管理事务
>* 开启事务：setAutoCommit(boolean autoCommit) ：调用该方法设置参数为false，即开启事务
>	* 在执行sql之前开启事务
>* 提交事务：commit() ，当所有sql都执行完提交事务
>* 回滚事务：rollback() ，在catch中回滚事务
>
>```java
>import cn.itcast.util.JDBCUtils;
>import java.sql.Connection;
>import java.sql.PreparedStatement;
>import java.sql.SQLException;
>
>/**
> * 事务操作
> */
>public class JDBCDemo10 {
>    public static void main(String[] args) {
>        Connection conn = null;
>        PreparedStatement pstmt1 = null;
>        PreparedStatement pstmt2 = null;
>        try {
>            //1.获取连接
>            conn = JDBCUtils.getConnection();
>            //开启事务
>            conn.setAutoCommit(false);
>
>            //2.定义sql
>            //2.1 张三 - 500
>            String sql1 = "update account set balance = balance - ? where id = ?";
>            //2.2 李四 + 500
>            String sql2 = "update account set balance = balance + ? where id = ?";
>            //3.获取执行sql对象
>            pstmt1 = conn.prepareStatement(sql1);
>            pstmt2 = conn.prepareStatement(sql2);
>            //4. 设置参数
>            pstmt1.setDouble(1,500);
>            pstmt1.setInt(2,1);
>
>            pstmt2.setDouble(1,500);
>            pstmt2.setInt(2,2);
>            //5.执行sql
>            pstmt1.executeUpdate();
>            // 手动制造异常
>            int i = 3/0;
>
>            pstmt2.executeUpdate();
>            //提交事务
>            conn.commit();
>        } catch (Exception e) {
>            //事务回滚
>            try {
>                if(conn != null) {
>                    conn.rollback();
>                }
>            } catch (SQLException e1) {
>                e1.printStackTrace();
>            }
>            e.printStackTrace();
>        }finally {
>            JDBCUtils.close(pstmt1,conn);
>            JDBCUtils.close(pstmt2,null);
>        }
>    }
>}
>```
>
>

