---
title: Java进阶_注解
date: 2022/9/10 20:46:25
categories: 
- java
---

![img](res/other/异世界蕾姆_1.png)

[TOC]

> [【黑马程序员-Java语言高级部分9.3】Java 注解](https://www.bilibili.com/video/av62102209)



# 注解基础概念

> **注释**：用文字描述程序的，给程序员看的
>
> 百度上的解释：
>
> > Java 注解（Annotation）又称 Java 标注，是 JDK5.0 引入的一种注释机制，是一种代码级别的说明。Java 语言中的类、方法、变量、参数和包等都可以被标注。
> >
> > 和 Javadoc 不同，Java 标注可以通过反射获取标注内容。在编译器生成类文件时，标注可以被嵌入到字节码中。Java 虚拟机可以保留标注内容，在运行时可以获取到标注内容 。 
> >
> > 当然它也支持自定义 Java 标注。
>
> **概念描述：**
>
> - JDK1.5 之后的新特性
> - 用来说明程序的
> - 使用注解：@注解名称
>
> **作用分类**
>
> 1. **编译检查**：通过代码里标识的注解让编译器能够实现基本的编译检查【Override】
> 2. **编写文档**：通过代码里标识的注解生成文档，API文档是通过抽取代码中的文档注释生成的。
> 3. **代码分析**：通过代码里标识的注解对代码进行分析【使用反射】
>
> >大多数时候，我们会使用注解而不是自定义注解
> >
> >注解给编译器和解析程序用
> >
> >注解不是程序的一部分，可以理解为标签

## 预定义注解

>> `@Override`：检测被该注解标注的方法是否搜集继承自父类(接口)的，定义在java.lang.Override中，此注释只适用于修辞方法，表示一个方法声明打算重写超类中的另一个方法声明
>
>> `@Deprecated`：将该注解标注的内容，表示已过时，定义在java.lang.Deprecated中，此注释可以用于修辞方法，属性，类，表示不鼓励程序员使用这样的元素，通常是因为它很危险或者存在更好的选择
>
>> `@SuppressWarnings`：压制警告，一般传递参数all，定义在java.lang.SuppressWarnings中，用来抑制编译时的警告信息。与前两个注释有所不同，你需要添加一个参数才能正确使用，这些参数都是已经定义好了的，我们选择性的使用就好了
>>
>    > 如@SuppressWarnings("all")、@SuppressWarnings("all")、@SuppressWarnings("unchecked")、@SuppressWarnings(value={"unchecked","deprecation"})
> 
>    
> 

# 自定义注解

>**基本格式**
>
>```java
>@元注解
>public @interface 注解名称{}
>```
>
>**注解的本质**: 注解本质上就是一个接口，该接口默认继承java.lang.annotation.Annotation接口
>
>```java
>// 将以下注解编译过后进行反编译，得到结果：
>// 1. 编译前
>public @interface MyAnno{
>	String name default "hyc"; 
>    // 每一个方法实际上是声明了一个配置参数，本质上是抽象方法
>    // 方法的名称就是参数的名称
>    // 返回值类型就是参数的类型（返回值只能是基本类型，注解，String，Enum，以上类型的数组)
>    // 可以通过default来声明参数的默认值
>    // 如果只有一个参数成员，一般参数名为value，那么value可以省略，直接赋值即可
>    // 注解元素必须要有值，我们定义注解元素时，经常使用空字符串，0作为默认值
>    // 数组赋值时，值使用大括号包裹，如果数组中只有一个值，那么{}可以省略
>}
>
>// 2. 反编译后
>public interface MyAnno extends java.lang.annotation.Annotation{}
>```
>
>

## 元注解

>**概念**：用于描述注解的注解。
>
>元注解的作用就是负责注解其他注解，Java定义了4个标准的meta-annotation类型，他们被用来提供对其他annotation类型作说明。这些类型和它们所支持的类在java.lang.annotation包中可以找到。
>
>> `@Target`：描述能够作用的位置（即：被描述的注解可以用在什么地方）
>>
>> ```java
>> @Target(value = {ElementType.TYPE,ElementType.METHOD,ElementType.FIELD}) 
>> //表示该MyAnno注解可以同时作用于类上，方法上和成员变量上
>> public @interface MyAnno {}
>> ```
>>
>> 其中value中ElementType取值可以有以下几种情况：
>>
>> - TYPE:可以作用在类上
>> - METHOD:可以作用在方法上
>> - FIELD：可以作用于成员变量上
>
>> `@Retention`：描述注解被保留的阶段，用于描述注解的生命周期
>>
>> @Retention(RetentionPolicy.RUNTIME)：当前被描述的注解，会保留到字节码文件中，并被JVM读取到，一般自己定义的注解都加RUNTIME
>
>> `@Documented`：描述该注解是否会被抽取到api文档中
>
>> `@Inherited`：描述注解是否被子类继承




# 使用注解

>注解在程序中经常和`反射`一起使用，注解大多数来说都是用来`替换配置文件`的
>
>```java
>import java.lang.annotation.ElementType;
>import java.lang.annotation.Retention;
>import java.lang.annotation.RetentionPolicy;
>import java.lang.annotation.Target;
>
>@Target(ElementType.TYPE) //可以被作用在类上
>@Retention(RetentionPolicy.RUNTIME)
>public @interface AnnoReflect {
>   String className();
>   String methodName();
>}
>```
>
>```java
>// 使用注解的方式来淘汰配置文件(注释很重要)：
>import java.io.InputStream;
>import java.lang.reflect.Method;
>import java.util.Properties;
>
>@AnnoReflect(className = "cn.other.annotation.AnnoTest",methodName = "play")
>public class ReflectAnnotationTest {
>   public static void main(String[] args) throws Exception {
>       /**
>        * 前提：不能改变该类的任何代码。可以创建任意类的对象，可以执行任意方法
>        * 即：拒绝硬编码
>        */
>
>       //1. 解析注解
>       //1.1 获取该类的字节码文件对象
>       Class<ReflectAnnotationTest> rac = ReflectAnnotationTest.class;
>       //1.2 获取上面的注解对象,其实就是在内存中生成了一个该注解接口的子类实现对象
>       AnnoReflect an = rac.getAnnotation(AnnoReflect.class);
>       /* 相当于
>           public class AnnotationReflect implements AnnoReflect{
>               public String className(){
>                   return "cn.other.annotation.AnnoTest1";
>               }
>               public String methodName(){
>                   return "play";
>               }
>           } */
>       //2. 调用注解对象中定义的抽象方法，获取返回值
>       String className = an.className();
>       String methodName = an.methodName();
>
>       //3.加载该类进内存
>       Class cls = Class.forName(className);
>       //4.创建对象
>       Object obj = cls.newInstance();
>       //5.获取方法对象
>       Method method = cls.getMethod(methodName);
>       //6.执行方法
>       method.invoke(obj);
>   }
>}
>```
>
>![img](res/Java%E8%BF%9B%E9%98%B6_%E6%B3%A8%E8%A7%A3/20200306202943796.png)
>
>在程序中使用注解：获取注解中定义的属性值
>
>> 1. 获取注解定义的位置的对象 (Class, Method, Field)
>> 2. 获取指定的注解：getAnnotation(Class)
>> 3. 调用注解中的抽象方法获取配置的属性值



# 案例分析

## 测试框架

>`需求`：设计一个框架，检测一个类中的方法使用有异常，并进行统计。
>
>```java
>public class calculator {
>    @Check
>    public void add(){
>        System.out.println("1+0="+(1+0));
>   }
>    @Check
>    public void sub(){
>        System.out.println("1-0="+(1-0));
>    }
>    @Check
>    public void mul(){
>        System.out.println("1*0="+(1*0));
>    }
>    @Check
>    public void div(){
>        System.out.println("1/0="+(1/0));
>    }
>    public void show(){
>        System.out.println("今天天气真不错！");
>    }
> }
> ```

> ```java
> // 自定义一个注解
> @Retention(RetentionPolicy.RUNTIME) //运行时
> @Target(ElementType.METHOD) //加在方法前面
> public @interface Check {}
> ```
>
> 

>编写一个类专门用于检查(注意注释)：
>
>````java
>import java.io.BufferedWriter;
>import java.io.FileWriter;
>import java.io.IOException;
>import java.lang.reflect.InvocationTargetException;
>import java.lang.reflect.Method;
>
>// 简单的测试框架
>// 当主方法执行后，会自动自行检测所有方法(加了check注解的方法)，判断方法是否有异常并记录
>public class TestCheck {
>   public static void main(String[] args) throws IOException {
>       //1. 创建计算机对象
>       calculator c = new calculator();
>       //2. 获取字节码文件对象
>        Class cls = c.getClass();
>       //3. 获取所有方法
>        Method[] methods = cls.getMethods();
> 
>        int num = 0; //记录出现异常的次数
>        BufferedWriter bw = new BufferedWriter(new FileWriter("bug.txt"));
>
>        for(Method method:methods){
>            //4. 判断方法上是否有Check注解
>            if(method.isAnnotationPresent(Check.class)){
>                //5. 有注解就执行,捕获异常
>                try {
>                    method.invoke(c);
>                } catch (Exception e) {
>                    e.printStackTrace();
>                    //6.将异常记录在文件中
>                    num++;
>                    bw.write(method.getName()+"方法出异常了");
>                    bw.newLine();
>                    bw.write("异常的名称是："+e.getCause().getClass().getSimpleName());
>                    bw.newLine();
>                    bw.write("异常原因："+e.getCause().getMessage());
>                    bw.newLine();
>                    bw.write("=====================");
>                    bw.newLine();
>                }
>            }
>        }
>        bw.write("本次测试一共出现"+num+"次异常");
>        bw.flush();
>        bw.close();
>    }
> }
> ````
> 
> 运行TestCheck类中的主方法，就会自动检查所有注解@Check的方法是否异常：
> 
> ![img](res/Java%E8%BF%9B%E9%98%B6_%E6%B3%A8%E8%A7%A3/20200306214605527.png)
> 
> ![img](res/Java%E8%BF%9B%E9%98%B6_%E6%B3%A8%E8%A7%A3/20200306214630500.png)

## ORM实例

>![image-20200309223608769](res/Java%E8%BF%9B%E9%98%B6_%E6%B3%A8%E8%A7%A3/image-20200309223608769.png)
>
>```java
>// 类名的注解 
>@Target(ElementType.TYPE) 
>@Retention(RetentionPolicy.RUNTIME) 
>@interface Tablekuang{ string value(); }
>
>// 属性的注解 
>@Target(ElementType.FIELD) 
>@Retention(RetentionPolicy.RUNTIME) 
>@interface Fieldkuang{ 
>	String columnName(); 
>	string type(); 
>	int length();
>}
>```
>
>```java
>@Tablekuang("db_student") 
>class student{ 
>	@Fieldkuang(columnName="db_id",type="int",length =10) 
>	private int id;
>	@Fieldkuang(columnName="db_age",type="int",length=10) 
>	private int age; 
>	@Fieldkuang(columnName ="db_name",type =""varchar",length=3) 
>	private String name; 
>	public student(){}
>	public student(int id,int age,String name){ 
>		this.id=id;
>		this.age=age;
>		this.name=name;
>	}
>}
>```
>
>```java
>public static void main(string[] args) throws ClassNotFoundException { 
>	Class c1=Class.forName("com.huangy.reflection.Student"); 
>	//通过反射获得注解 		
>	Annotation[] annotations=c1.getAnnotations();
>    annotations.foreach(System.out::println);
>    
>    //获得注解的alue的值。
>    Tablekuang tablekuang =(Tablekuang)c1.getAnnotation(Tablekuang.class); 
>    System.out.printn(ablekuang.value()); 
>
>    //获得类指定的注解 
>    Field f=c1.getDeclaredField("name"); 
>    Fieldkuang annotation=f.getAnnotation(Fieldkuang.class); 
>    System.out.println(annotation.columnName());
>    System.out.println(annotation.type());
>    System.out.println(annotation.length());
>}
>```
>
>![image-20200309224336761](res/Java%E8%BF%9B%E9%98%B6_%E6%B3%A8%E8%A7%A3/image-20200309224336761.png)

