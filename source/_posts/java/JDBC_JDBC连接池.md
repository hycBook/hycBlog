---
title: JDBC_JDBC连接池
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: ae528721
---

---

[TOC]

>[【黑马程序员-Java语言高级部分11】JDBC](https://www.bilibili.com/video/av61491585)

---

# 数据库连接池

>**概念**：其实就是一个容器(集合)，存放数据库连接的容器。
>	当系统初始化好后，容器被创建，容器中会申请一些连接对象，当用户来访问数据库时，从容器中获取连接对象，用户访问完之后，会将连接对象归还给容器。
>
>**好处**：节约资源+用户访问高效
>
>**标准接口**：DataSource   javax.sql包下的
>
>方法：
>* 获取连接：getConnection()
>* 归还连接：Connection.close()。
>
>如果连接对象Connection是从连接池中获取的，那么调用Connection.close()方法，则不会再关闭连接了。而是归还连接
>
>一般我们不去实现它，有数据库厂商来实现
>
>* `C3P0`：数据库连接池技术
>* `Druid`：数据库连接池实现技术，由阿里巴巴提供的

# C3P0

>数据库连接池技术
>
>步骤：
>1. 导入jar包 (两个) c3p0-0.9.5.2.jar mchange-commons-java-0.2.12.jar ，
>
>    * 不要忘记导入数据库驱动jar包
>
>2. 定义配置文件：
>
>    * 名称： c3p0.properties 或者 c3p0-config.xml
>
>    * 路径：直接将文件放在src目录下即可。
>
>    * ```xml
>      <c3p0-config>
>        <!-- 使用默认的配置读取连接池对象 -->
>        <default-config>
>        	<!--  连接参数 -->
>          <property name="driverClass">com.mysql.jdbc.Driver</property>
>          <property name="jdbcUrl">jdbc:mysql://localhost:3306/db4</property>
>          <property name="user">root</property>
>          <property name="password">root</property>
>              
>          <!-- 连接池参数 -->
>          <!--初始化申请的连接数量-->
>          <property name="initialPoolSize">5</property>
>          <!--最大的连接数量-->
>          <property name="maxPoolSize">10</property>
>          <!--超时时间-->
>          <property name="checkoutTimeout">3000</property>
>        </default-config>
>          
>        <named-config name="otherc3p0"> 
>          <!--  连接参数 -->
>          <property name="driverClass">com.mysql.jdbc.Driver</property>
>          <property name="jdbcUrl">jdbc:mysql://localhost:3306/db3</property>
>          <property name="user">root</property>
>          <property name="password">root</property>
>              
>          <!-- 连接池参数 -->
>          <property name="initialPoolSize">5</property>
>          <property name="maxPoolSize">8</property>
>          <property name="checkoutTimeout">1000</property>
>        </named-config>
>      </c3p0-config>
>      ```
>
>3. 创建核心对象 数据库连接池对象 ComboPooledDataSource
>4. 获取连接： getConnection
>
>```java
>// 1. 创建数据库连接池对象
> DataSource ds  = new ComboPooledDataSource();
> // 2. 获取连接对象
> Connection conn = ds.getConnection();
>```
>
>

# Druid

> 数据库连接池实现技术，由阿里巴巴提供的
>
> 步骤：
>
> 1. 导入jar包 druid-1.0.9.jar
>
> 2. 定义配置文件：
>
>    * druid.properties形式
>
>    * 可以叫任意名称，可以放在任意目录下
>
>    * ```properties
>      driverClassName=com.mysql.jdbc.Driver
>      url=jdbc:mysql:///db3
>      username=root
>      password=root
>      # 初始化连接数量
>      initialSize=5
>      # 最大连接数
>      maxActive=10
>      # 最大等待时间
>      maxWait=3000
>      ```
>
> 3. 加载properties配置文件
>
> 4. 获取数据库连接池对象：通过工厂来来获取  DruidDataSourceFactory
>
> 5. 获取连接：getConnection
>
> ```java
> // 3. 加载配置文件
> Properties pro = new Properties();
> InputStream is = DruidDemo.class.getClassLoader().getResourceAsStream("druid.properties");
> pro.load(is);
> // 4. 获取连接池对象
> DataSource ds = DruidDataSourceFactory.createDataSource(pro);
> // 5. 获取连接
> Connection conn = ds.getConnection();
> ```
>
> **JDBCUtils.java**
>
> ```java
> import com.alibaba.druid.pool.DruidDataSourceFactory;
> import javax.sql.DataSource;
> import java.io.IOException;
> import java.sql.Connection;
> import java.sql.ResultSet;
> import java.sql.SQLException;
> import java.sql.Statement;
> import java.util.Properties;
> 
> /**
>  * Druid连接池的工具类
>  */
> public class JDBCUtils {
>     //1.定义成员变量 DataSource
>     private static DataSource ds ;
>     static{
>         try {
>             //1.加载配置文件
>             Properties pro = new Properties();
>             pro.load(JDBCUtils.class.getClassLoader().getResourceAsStream("druid.properties"));
>             //2.获取DataSource
>             ds = DruidDataSourceFactory.createDataSource(pro);
>         } catch (IOException e) {
>             e.printStackTrace();
>         } catch (Exception e) {
>             e.printStackTrace();
>         }
>     }
> 
>     /**
>      * 获取连接
>      */
>     public static Connection getConnection() throws SQLException {
>         return ds.getConnection();
>     }
> 
>     /**
>      * 释放资源
>      */
>     public static void close(Statement stmt,Connection conn){
>        close(null,stmt,conn);
>     }
> 
> 
>     public static void close(ResultSet rs , Statement stmt, Connection conn){
>         if(rs != null){
>             try {
>                 rs.close();
>             } catch (SQLException e) {
>                 e.printStackTrace();
>             }
>         }
>         if(stmt != null){
>             try {
>                 stmt.close();
>             } catch (SQLException e) {
>                 e.printStackTrace();
>             }
>         }
>         if(conn != null){
>             try {
>                 conn.close();//归还连接
>             } catch (SQLException e) {
>                 e.printStackTrace();
>             }
>         }
>     }
> 
>     /**
>      * 获取连接池方法
>      */
> 
>     public static DataSource getDataSource(){
>         return  ds;
>     }
> }
> 
> ```
>
> 























