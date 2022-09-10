![img](res/other/异世界蕾姆_0.jpg)

[TOC]

***

#  读取配置文件

# 读取properties配置文件

> **properties类中的主要方法**
>
> 1）getProperty(String key)
>
> 用指定的键在此属性列表中搜索属性。也就是通过参数key，得到key所对应的value。
>
> 2）load(InputStream inStream)
>
> 从输入流中读取属性列表（键和元素对）。以供getProperty( String key)来搜索。
>
> 3）setProperty(String key, String value)
>
> 调用Hashtable的方法put 。他通过调用基类的put方法来设置键-值对。
>
> 4）store(OutputStream out, String comments)
>
> 以适合使用load方法加载到Properties表中的格式，将此Properties表中的属性列表（键和元素对）写入输出流。与load方法相反，该方法将键-值对写入到指定的文件中去。
>
> 5）clear()
>
> 清除所有装载的键-值对。该方法在基类中提供

```properties
apple=src.main.java.per.hyc.ReflexAndInvokeTest.Apple
orange=src.main.java.per.hyc.ReflexAndInvokeTest.Orange
```

```java
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.util.Properties;

/**
 * 获取properties文件的配置
 */
public class GetProperties {
    public static Properties getPro(String pathname) {
        Properties pro = new Properties();
        File f = new File(pathname);
        try {
            if (f.exists()) {
                pro.load(new FileInputStream(f));
            }
            //建立一个新的属性文件，同时设置好默认内容
            else {
                pro.setProperty("apple", "per.hyc.ReflexAndInvokeTest.Apple");
                pro.setProperty("orange", "per.hyc.ReflexAndInvokeTest.Orange");
                pro.store(new FileOutputStream(f), "FRUIT CLASS");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        return pro;
    }
}
```



# 读取xml配置文件

```xml
<?xml version="1.0"?>
<config>
    <className>per.hyc.designPattern.Bridge.Blue</className>
    <className>per.hyc.designPattern.Bridge.SmallPen</className>
</config>
```

```java
import javax.xml.parsers.*;
import org.w3c.dom.*;
import java.io.*;

/**
 * 使用java反射创建具体的颜色和画笔
 */
public class XMLUtilPen {
    // 该方法用于从XML配置文件中提取具体类类名，并返回一个实例对象
    public static Object getBean(String args) {
        try {
            //创建文档对象
            DocumentBuilderFactory dFactory = DocumentBuilderFactory.newInstance();
            DocumentBuilder builder = dFactory.newDocumentBuilder();
            Document doc;
            doc = builder.parse(new File(".\\src\\main\\resources\\configPen.xml"));
            Node classNode = null;
            NodeList nl = doc.getElementsByTagName("className");

            if (args.equals("color")) {
                //获取包含类名的文本节点
                classNode = nl.item(0).getFirstChild();
            } else if (args.equals("pen")) {
                //获取包含类名的文本节点
                classNode = nl.item(1).getFirstChild();
            }

            String cName = classNode.getNodeValue();
            //通过类名生成实例对象并将其返回
            return Class.forName(cName).newInstance();
        } catch (Exception e) {
            e.printStackTrace();
            return null;
        }
    }
}
```



# Spring 读取properties文件

> [Java中读取Properties配置文件的几种方式](https://www.jianshu.com/p/d4099f7a29b4)
>
> * @ConfigurationProperties(prefix = "student")
> * @Value
> * Environment
> * 详见项目springbootdemo



# 利用第三方配置工具owner读取配置文件



