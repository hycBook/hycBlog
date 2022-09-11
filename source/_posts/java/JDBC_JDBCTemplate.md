---
title: JDBC_JDBCTemplate
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: e73474f0
---


![img](res/other/异世界蕾姆_1.png)

>[【黑马程序员-Java语言高级部分11】JDBC](https://www.bilibili.com/video/av61491585)

---

# Spring JDBC

## 主要功能

>Spring框架对JDBC的简单封装。
>
>提供了一个JDBCTemplate对象简化JDBC的开发
>
>步骤：
>1. 导入jar包
>
>2. 创建JdbcTemplate对象。依赖于数据源DataSource
>	* JdbcTemplate template = new JdbcTemplate(ds);
>
>3. 调用JdbcTemplate的方法来完成CRUD的操作
>	* `update()`: 执行DML语句。增、删、改语句
>	* `queryForMap()`: 查询结果将结果集封装为map集合，将列名作为key，将值作为value 将这条记录封装为一个map集合
>		* 注意：这个方法查询的结果集长度只能是1
>	* `queryForList()`: 查询结果将结果集封装为list集合
>		* 注意：将每一条记录封装为一个Map集合，再将Map集合装载到List集合中
>	* `query()`: 查询结果，将结果封装为JavaBean对象
>		* query的参数：RowMapper
>			* 一般我们使用BeanPropertyRowMapper实现类。可以完成数据到JavaBean的自动封装
>			* new BeanPropertyRowMapper<类型>(类型.class)
>	* `queryForObject()`：查询结果，将结果封装为对象
>		* 一般用于聚合函数的查询
>
>

## 使用示例

```java
import cn.itcast.utils.JDBCUtils;
import org.junit.Test;
import org.springframework.jdbc.core.BeanPropertyRowMapper;
import org.springframework.jdbc.core.JdbcTemplate;
import org.springframework.jdbc.core.RowMapper;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.List;
import java.util.Map;
import java.util.Date;
public class JdbcTemplateDemo {
    //1. 获取JDBCTemplate对象
    private JdbcTemplate template = new JdbcTemplate(JDBCUtils.getDataSource());
    /**
     * 1. 修改1号数据的 salary 为 10000
     */
    @Test
    public void test1(){
        //2. 定义sql
        String sql = "update emp set salary = 10000 where id = 1001";
        //3. 执行sql
        int count = template.update(sql);
        System.out.println(count);
    }

    /**
     * 2. 添加一条记录
     */
    @Test
    public void test2(){
        String sql = "insert into emp(id,ename,dept_id) values(?,?,?)";
        int count = template.update(sql, 1015, "郭靖", 10);
        System.out.println(count);

    }

    /**
     * 3.删除刚才添加的记录
     */
    @Test
    public void test3(){
        String sql = "delete from emp where id = ?";
        int count = template.update(sql, 1015);
        System.out.println(count);
    }

    /**
     * 4.查询id为1001的记录，将其封装为Map集合
     * 注意：这个方法查询的结果集长度只能是1
     */
    @Test
    public void test4(){
        String sql = "select * from emp where id = ? or id = ?";
        Map<String, Object> map = template.queryForMap(sql, 1001,1002);
        System.out.println(map);
        //{id=1001, ename=孙悟空, job_id=4, mgr=1004, joindate=2000-12-17, salary=10000.00, bonus=null, dept_id=20}

    }

    /**
     * 5. 查询所有记录，将其封装为List
     */
    @Test
    public void test5(){
        String sql = "select * from emp";
        List<Map<String, Object>> list = template.queryForList(sql);

        for (Map<String, Object> stringObjectMap : list) {
            System.out.println(stringObjectMap);
        }
    }

    /**
     * 6. 查询所有记录，将其封装为Emp对象的List集合
     */
    @Test
    public void test6(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new RowMapper<Emp>() {
            @Override
            public Emp mapRow(ResultSet rs, int i) throws SQLException {
                Emp emp = new Emp();
                int id = rs.getInt("id");
                String ename = rs.getString("ename");
                int job_id = rs.getInt("job_id");
                int mgr = rs.getInt("mgr");
                Date joindate = rs.getDate("joindate");
                double salary = rs.getDouble("salary");
                double bonus = rs.getDouble("bonus");
                int dept_id = rs.getInt("dept_id");

                emp.setId(id);
                emp.setEname(ename);
                emp.setJob_id(job_id);
                emp.setMgr(mgr);
                emp.setJoindate(joindate);
                emp.setSalary(salary);
                emp.setBonus(bonus);
                emp.setDept_id(dept_id);

                return emp;
            }
        });

        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
     * 6. 查询所有记录，将其封装为Emp对象的List集合
     */
    @Test
    public void test6_2(){
        String sql = "select * from emp";
        List<Emp> list = template.query(sql, new BeanPropertyRowMapper<Emp>(Emp.class));
        for (Emp emp : list) {
            System.out.println(emp);
        }
    }

    /**
     * 7. 查询总记录数
     */
    @Test
    public void test7(){
        String sql = "select count(id) from emp";
        Long total = template.queryForObject(sql, Long.class);
        System.out.println(total);
    }
}
```

```java
import java.sql.Date;
public class Emp {
    private Integer id;
    private String ename;
    private Integer job_id;
    private Integer mgr;
    private Date joindate;
    private Double salary;
    private Double bonus;
    private Integer dept_id;

    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getEname() {
        return ename;
    }

    public void setEname(String ename) {
        this.ename = ename;
    }

    public Integer getJob_id() {
        return job_id;
    }

    public void setJob_id(Integer job_id) {
        this.job_id = job_id;
    }

    public Integer getMgr() {
        return mgr;
    }

    public void setMgr(Integer mgr) {
        this.mgr = mgr;
    }

    public Date getJoindate() {
        return joindate;
    }

    public void setJoindate(Date joindate) {
        this.joindate = joindate;
    }

    public Double getSalary() {
        return salary;
    }

    public void setSalary(Double salary) {
        this.salary = salary;
    }

    public Double getBonus() {
        return bonus;
    }

    public void setBonus(Double bonus) {
        this.bonus = bonus;
    }

    public Integer getDept_id() {
        return dept_id;
    }

    public void setDept_id(Integer dept_id) {
        this.dept_id = dept_id;
    }

    @Override
    public String toString() {
        return "Emp{" +
                "id=" + id +
                ", ename='" + ename + '\'' +
                ", job_id=" + job_id +
                ", mgr=" + mgr +
                ", joindate=" + joindate +
                ", salary=" + salary +
                ", bonus=" + bonus +
                ", dept_id=" + dept_id +
                '}';
    }
}
```

