---
title: Java基础_解析与生成XML
date: 2022/9/10 20:46:25
categories: 
- java
---

![img](res/other/异世界蕾姆_0.jpg)

[TOC]

***

# 解析与生成XML

> [Java生成xml文件的四种方式](https://blog.csdn.net/qq_39237801/article/details/78378486)
>
> [四种生成和解析XML文档的方法详解（介绍+优缺点比较+示例）](https://www.cnblogs.com/lanxuezaipiao/archive/2013/05/17/3082949.html)
>
> [Java 自定义生成与解析（Dom4J）XML 文件](https://juejin.im/entry/58cb48f2a22b9d00641fb558)
>
> ```json
> 四种方式总结:
>     1.dom基于tree，sax基于事件，JDOM和DOM4J基于底层API
>     2.dom生成的内容会保存到内存中，方便删除和修改
>     3.sax不能修改已经生成的标签 
>     4.添加JUnit在Libraries选择Add Library中的JUnit即可
> ```
>
> 【DOM】
>
> DOM方式生成xml是基于DOM树的结构，整个DOM树会存在内存中，所以使用DOM方式可以频繁的修改xml的内容，但是因为DOM树是存在内存中的，所以对内存消耗较大。DOM方式比较适用于需要频繁删改的情况。
>
> 【SAX】
>
> SAX方式生成xml是逐步写入的，也就是说，在SAX写入时，已经写入的部分是无法再回头修改的，因为SAX是基于事件驱动的，在写完一个标签之后是不能回头的，也因此，SAX的效率比较快，但是不能进行删改。
>
> 【JDOM】
>
> JDOM方式不是Java提供的基本的生成xml方式，使用时需要导入额外的jar包，但是它是基于基础的API实现的。
>
> 【DOM4J】
>
> DOM4J方式也不是Java提供的基本生成xml的方式，使用时也需要导入额外的jar包，它也是基于基础的API实现的，它功能强大，性能优异，在实际开发中经常使用。
>
> DOM方式是最慢的，SAX方式反而是最快的，DOM4J方式仅次于SAX方式。
>
> 

# Dom方式

>
>
>```java
>import org.junit.Test;
>import org.w3c.dom.DOMConfiguration;
>import org.w3c.dom.Document;
>import org.w3c.dom.Node;
>import org.w3c.dom.bootstrap.DOMImplementationRegistry;
>import org.w3c.dom.ls.DOMImplementationLS;
>import org.w3c.dom.ls.LSOutput;
>import org.w3c.dom.ls.LSSerializer;
>import org.xml.sax.InputSource;
>
>import javax.xml.parsers.DocumentBuilder;
>import javax.xml.parsers.DocumentBuilderFactory;
>import javax.xml.transform.Transformer;
>import javax.xml.transform.TransformerFactory;
>import javax.xml.transform.dom.DOMSource;
>import javax.xml.transform.stream.StreamResult;
>import java.io.ByteArrayOutputStream;
>import java.io.IOException;
>import java.io.StringReader;
>import java.util.ArrayList;
>import java.util.List;
>import java.io.File;
>import javax.xml.parsers.DocumentBuilder;
>import javax.xml.parsers.DocumentBuilderFactory;
>import javax.xml.transform.OutputKeys;
>import javax.xml.transform.Transformer;
>import javax.xml.transform.TransformerFactory;
>import javax.xml.transform.dom.DOMSource;
>import javax.xml.transform.stream.StreamResult;
>import org.junit.Test;
>import org.w3c.dom.Document;
>import org.w3c.dom.Element;
>
>public class DomXml {
>	@Test
>	public void test(){
>		Long start = System.currentTimeMillis();
>		createXml();
>		System.out.println("运行时间："+ (System.currentTimeMillis() - start));
>	}
>
>	/**
>     * 生成xml方法
>    */
>    public static void createXml() {
>        try {
>            // 创建解析器工厂
>            DocumentBuilderFactory factory = DocumentBuilderFactory.newInstance();
>            DocumentBuilder db = factory.newDocumentBuilder();
>            Document document = db.newDocument();
>            // 不显示standalone="no"
>            document.setXmlStandalone(true);
>            Element bookstore = document.createElement("bookstore");
>            // 向bookstore根节点中添加子节点book
>            Element book = document.createElement("book");
>
>            Element name = document.createElement("name");
>            // 不显示内容 name.setNodeValue("不好使");
>            name.setTextContent("雷神");
>            book.appendChild(name);
>            // 为book节点添加属性
>            book.setAttribute("id", "1");
>            // 将book节点添加到bookstore根节点中
>            bookstore.appendChild(book);
>            // 将bookstore节点（已包含book）添加到dom树中
>            document.appendChild(bookstore);
>
>            // 方式一: 保存xml文件
>            // 创建TransformerFactory对象
>//            TransformerFactory tff = TransformerFactory.newInstance();
>            // 创建 Transformer对象
>//            Transformer tf = tff.newTransformer();
>            // 输出内容是否使用换行
>//            tf.setOutputProperty(OutputKeys.INDENT, "yes");
>            // 创建xml文件并写入内容
>//            tf.transform(new DOMSource(document), new StreamResult(new File("book1.xml")));
>//            System.out.println("生成book1.xml成功");
>
>            // 方式二: 转字符串
>            // 创建TransformerFactory对象
>            TransformerFactory transformerFactory = TransformerFactory.newInstance();
>            // 创建Transformer对象
>            Transformer transformer = transformerFactory.newTransformer();
>            // 设置输出数据时换行
>            // tf.setOutputProperty(OutputKeys.INDENT, "yes");
>
>            // xml格式化
>            ByteArrayOutputStream bos = new ByteArrayOutputStream();
>            transformer.transform(new DOMSource(document), new StreamResult(bos));
>            String xmlString = bos.toString();
>            System.out.println(new String(prettyXml(xmlString)));
>        } catch (Exception e) {
>            e.printStackTrace();
>            System.out.println("生成book1.xml失败");
>        }
>    }
>}
>
>```
>
>```java
>	/**
>     * 格式化输出
>     *
>     * @param xmlStr: xml文档字符串
>     * @return 格式化xml
>     */
>    private static byte[] prettyXml(String xmlStr) {
>        byte[] data = null;
>        StringReader stringReader = null;
>        try {
>            DocumentBuilderFactory dbf = DocumentBuilderFactory.newInstance();
>            DocumentBuilder db = dbf.newDocumentBuilder();
>            stringReader = new StringReader(xmlStr);
>            InputSource is = new InputSource(stringReader);
>            Document doc = db.parse(is);
>            data = prettyXml(doc);
>        } catch (Exception e) {
>            throw new RuntimeException(e);
>        } finally {
>            if (stringReader != null) {
>                stringReader.close();
>            }
>        }
>        return data;
>    }
>
>    /**
>     * 格式化输出
>     *
>     * @param node: 文档树节点
>     * @return 格式化完的节点
>     */
>    private static byte[] prettyXml(Node node) {
>        ByteArrayOutputStream byteArrayOutputStream = null;
>        byte[] data = null;
>        try {
>            DOMImplementationRegistry registry = DOMImplementationRegistry.newInstance();
>            DOMImplementationLS impl = (DOMImplementationLS) registry.getDOMImplementation("XML 3.0");
>            LSSerializer serializer = impl.createLSSerializer();
>            DOMConfiguration domConfiguration = serializer.getDomConfig();
>            boolean isSupport = domConfiguration.canSetParameter("format-pretty-print", true);
>            if (isSupport) {
>                domConfiguration.setParameter("format-pretty-print", true);
>            }
>            LSOutput output = impl.createLSOutput();
>            output.setEncoding("UTF-8");
>            byteArrayOutputStream = new ByteArrayOutputStream();
>            output.setByteStream(byteArrayOutputStream);
>            serializer.write(node, output);
>            data = byteArrayOutputStream.toByteArray();
>        } catch (Exception e) {
>            throw new RuntimeException(e);
>        } finally {
>            if (byteArrayOutputStream != null) {
>                try {
>                    byteArrayOutputStream.close();
>                } catch (IOException e) {
>                    e.printStackTrace();
>                }
>            }
>        }
>        return data;
>    }
>```
>
>```xml
><?xml version="1.0"encoding="UTF-8"?>
><bookstore>
>    <book id="1">
>        <name>雷神</name>
>    </book>
></bookstore> 
>```
>
>

# Dom4j方式

>
>
>```java
>import java.io.File;
>import java.io.FileOutputStream;
>
>import org.dom4j.Document;
>import org.dom4j.DocumentHelper;
>import org.dom4j.Element;
>import org.dom4j.io.OutputFormat;
>import org.dom4j.io.XMLWriter;
>import org.junit.Test;
>
>public class Dom4jXml {
>
>	@Test
>	public void test(){
>		Long start = System.currentTimeMillis();
>		createXml();
>		System.out.println("运行时间："+ (System.currentTimeMillis() - start));
>	}
>
>	/**
>	 * 生成xml方法
>	 */
>	public static void createXml(){
>		try {
>			// 1、创建document对象
>			Document document = DocumentHelper.createDocument();
>			// 2、创建根节点rss
>			Element rss = document.addElement("rss");
>			// 3、向rss节点添加version属性
>			rss.addAttribute("version", "2.0");
>			// 4、生成子节点及子节点内容
>			Element channel = rss.addElement("channel");
>			Element title = channel.addElement("title");
>			title.setText("国内最新新闻");
>			// 5、设置生成xml的格式
>			OutputFormat format = OutputFormat.createPrettyPrint();
>			// 设置编码格式
>			format.setEncoding("UTF-8");
>			
>			
>			// 6、生成xml文件			
>			File file = new File("rss.xml");
>			XMLWriter writer = new XMLWriter(new FileOutputStream(file), format);
>			// 设置是否转义，默认使用转义字符
>			writer.setEscapeText(false);
>			writer.write(document);
>			writer.close();
>			System.out.println("生成rss.xml成功");
>		} catch (Exception e) {
>			e.printStackTrace();
>			System.out.println("生成rss.xml失败");
>		}
>	}
>}
>```
>
>

# JDom方式

>
>
>```java
>import java.io.File;
>import java.io.FileOutputStream;
>
>import org.jdom.Document;
>import org.jdom.Element;
>import org.jdom.output.Format;
>import org.jdom.output.XMLOutputter;
>import org.junit.Test;
>
>public class JDomXml {
>	
>	@Test
>	public void test(){
>		Long start = System.currentTimeMillis();
>		createXml();
>		System.out.println("运行时间："+ (System.currentTimeMillis() - start));
>	}
>
>	/**
>	 * 生成xml方法
>	 */
>	public static void createXml(){
>		try {
>			// 1、生成一个根节点
>			Element rss = new Element("rss");
>			// 2、为节点添加属性
>			rss.setAttribute("version", "2.0");			
>			// 3、生成一个document对象
>			Document document = new Document(rss);
>			
>			Element channel = new Element("channel");
>			rss.addContent(channel);
>			Element title = new Element("title");
>			title.setText("国内最新新闻");
>			channel.addContent(title);
>						
>			Format format = Format.getCompactFormat();
>			// 设置换行Tab或空格
>			format.setIndent("	");
>			format.setEncoding("UTF-8");
>						
>			// 4、创建XMLOutputter的对象
>			XMLOutputter outputer = new XMLOutputter(format);
>			// 5、利用outputer将document转换成xml文档
>			File file = new File("rssNew.xml");
>			outputer.output(document, new FileOutputStream(file));
>
>			System.out.println("生成rssNew.xml成功");
>		} catch (Exception e) {
>			System.out.println("生成rssNew.xml失败");
>		}
>	}	
>}
>```
>
>

# Sax方式

>
>
>



# xml解析

>
>
>



```java
import org.springframework.util.Assert;
Assert.notNull(featureDataRow, "数据不能为空");
   Assert.noNullElements(featureDataRow.getColumns().values().toArray(), "该样本存在null特征");
```







