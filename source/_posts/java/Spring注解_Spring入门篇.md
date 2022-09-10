---
title: Spring注解_Spring入门篇
date: 2022/9/10 20:46:25
---

![img](res/other/异世界蕾姆_1.png)

[TOC]

# [Spring入门篇](https://www.imooc.com/learn/196)

> [那些年，让我们一起着迷的Spring](https://www.imooc.com/learn/196)
>
> http://spring.io
>
> https://spring.io/projects/spring-framework
>

# 概述

> spring是一个开源框架，是一个轻量级的控制反转(IOC)和面向切面（AOP)的容器框架 
>
> * -从大小与开销两方面而言Spring都是轻量的 
>
> * -通过控制反转（IoC）的技术达到松耦合的目的 
>
> * -提供了面向切面编程的丰富支持，允许通过分离应用的业务逻辑与系统级服务进行内聚性的开发 
>
> * -包含并管理应用对象的配置和生命周期，这个意义上是一种容器 
>
> * -将简单的组件配置、组合成为复杂的应用，这个意义上是框架 
>
> ![spring framework runtime结构图](res/Spring注解_Spring入门篇/spring%20framework%20runtime.png)
>
> [Java 程序员必须掌握的 5 个注解！](https://mp.weixin.qq.com/s?__biz=MzI3ODcxMzQzMw==&mid=2247486373&idx=1&sn=601720b8a9dc1af60ffe6b2bd1dfc917&scene=21#wechat_redirect)



> **Spring作用**
>
> * 容器 ·
> * 提供了对多种技术的支持 -JMS -MQ支持 -UnitTest 
> * AOP（事务管理、日志等） ·
> * 提供了众多方便应用的辅助类（JDBC Template等） ·
> * 对主流应用框架（Hibernate等）提供了良好的支持
>
> **适用范围**
>
> * 构建企业应用（SpringMVC+Spring+Hibernate/ibatis) 
> * 单独使用Bean容器（Bean管理） 
> * 单独使用AOP进行切面处理 
> * 其他的Spring功能，如：对消息的支持等 在互联网中的应用
>
> **什么是框架**
>
> * ·框架的特点 
>
>   * -半成品 -封装了特定的处理流程和控制逻辑 
>
>   * -成熟的、不断升级改进的软件 
>
> * ·框架与类库的区别 
>
>   * -框架一般是封装了逻辑、高内聚的，类库则是松散的工具组合 
>
>   * -框架专注于某一领域，类库则是更通用的 
>
> **为什么使用框架**
>
> * ·软件系统日趋复杂 
> * ·重用度高，开发效率和质量提高 
> * ·软件设计人员要专注于对领域的了解，使需求分析更充分 ·易于上手、快速解决问题 



# Spring IOC容器

## 接口及面向接口编程 

> **接口**
>
> * ·用于沟通的中介物的抽象化 
> * ·实体把自己提供给外界的一种抽象化说明，用以由内部操作分 离出外部沟通方法，使其能被修改内部而不影响外界其他实体 与其交互的方式 
> * ·对应Java接口即声明，声明了哪些方法是对外公开提供的 
> * ·在Java8中，接口可以拥有方法体 
>
> **面向接口编程**
>
> * 结构设计中，分清层次及调用关系，每层只向外（上层）提供 一组功能接口，各层间仅依赖接口而非实现类 
> * 接口实现的变动不影响各层间的调用，这一点在公共服务中尤为重要 
> * “面向接口编程”中的“接口”是用于隐藏具体实现和实现多态性的组件
>
> **什么是IOC**
>
> * IOC:控制反转，控制权的转移，应用程序本身不负责依赖对象的创建和维护，而是由外部容器负责创建和维护 
> * DI（依赖注入）是其一种实现方式 
> * 目的：创建对象并且组装对象之间的关系 
>
> ![IoC container结构图](res/Spring注解_Spring入门篇/IoC%20container.png)
>
> **扩展理解**
>
> * 2004年，Martin Fowler探讨了同一个问题，既然IOC是控制 反转，那么到底是“哪些方面的控制被反转了呢？”，经过详 细地分析和论证后，他得出了答案：“获得依赖对象的过程被 反转了”。控制被反转之后，获得依赖对象的过程由自身管理 变为了由IOC容器主动注入。于是，他给“控制反转”取了一 个更合适的名字叫做“依赖注入（Dependency Injection) "。他的这个答案，实际上给出了实现IOC的方法：注入。所 谓依赖注入，就是由IOC容器在运行期间，动态地将某种依赖 关系注入到对象之中。
>
> **单元测试**
>
> * 下载junit-*.jar并引入工程 
> * 创建UnitTestBase类，完成对Spring配置文件的加载、销毁 所有的单元测试类都继承自UnitTestBase，通过它的 getBean方法获取想要得到的对象 
> * 子类（具体执行单元测试的类）加注解： @RunWith(BlockJUnit4ClassRunner.class) 
> * 单元测试方法加注解：@Test 
> * 右键选择要执行的单元测试方法执行或者执行一个类的全部单 元测试方法 

## Bean容器初始化

> **基础：两个包 **
>
> * -org.springframework.beans 
>
> * -org.springframework.context 
>
> * -BeanFactory提供配置结构和基本功能，加载并初始化Bean 
>
> * -ApplicationContext保存了Bean对象并在Spring中被广泛使用 
>
> **方式，ApplicationContext **
>
> * -本地文件 
>
> * -Classpath 
>
> * -Web应用中依赖servlet或Listener 
>
> **Bean容器初始化**
>
> * ·文件 
>
> ```java
> FileSystemXmlApplicationContext context= new FileSystemXmlApplicationContext("F:/workspace/appcontext.xml"); 
> ```
>
> * ·Classpath 
>
> ```java
> caspatxnlApplicstionc ontext context= new ClaspathxmlAplicationcontextrclasspathispring-contextxml);
> ```
>
> * .Web应用 
>
> ```xml
> <listener> 
> 	<listener-class>
>         org.springframework.web.context.ContextLoaderListener
>     </listener-class> 
> </listener> 
> <servlet> 
>     <servlet-name>context</servlet-name> 
>     <servlet-class>
>         org.springframework.web.context.ContextLoaderServlet
>     </servlet-class> 
>     <load-on-startup>1</load-on-startup> 
> </servlet> 
> ```

## Spring的常用注入方式 

> **Spring注入**
>
> * Spring注入是指在启动Spring容器加载bean配置的时候，完成对变量的赋值行为 
>
> * 常用的两种注入方式 
>
>      * -设值注入 
>
> ```xml
>  <?xml version="1.0"encoding="UTF-8?> 
>  <beans xmlns="http:/www.springframework.org/schema/beans" 			
>  		xmlns:xsi="htto://www.w3.org/2001/XMLSchema-instance"
>  		xsi:schemaLocation="http:/www.springframework.org/schema/beans 
>  		http:/www.springframeworkorg/schema/beans/spring-beans.xsd"> 
>     <bean id="injectionService"class='com.imooc.ioc.injection.service.InjiectionServicelmp/>
>     	<property name="injection0AO"ref=tipjection0Ag'1p</property> 
>     </bean> 
>     <bean id=ipjection0AO"class="com.imooc.iodinjiection.dao.lpjection0AOlmp/></bean> 
> </beans>
> 
> ```
>
> ```java
> import com.imooc.ioc.injection.dao.InjectionDAO; 
> public class InjectionServicelmpl implements InjectionService{ 
>     private InjectionDAO injectionDAO; 
>     //设值注入 
>     public void setlnjectionDAO(InjectionDAO injectionDAO)
>     { 
>         this.injectionDAO=injectionDAO; 
>     } 
>     public void save(String arg)
>     { 
>         //模拟业务操作 
>         System.outprintin(CService接收参数：+arg); 
>         arg=arg +":"+this.hashCode0; 
>         injectionDAO.save(arg);
>     }
> }
> ```
>
> ​	-构造注入 
>
>
> ```xml
>  <?xml version="1.0"encoding="UTF-8?> 
>  <beans xmlns="http:/www.springframework.org/schema/beans" 			
>  		xmlns:xsi="htto://www.w3.org/2001/XMLSchema-instance"
>  		xsi:schemaLocation="http:/www.springframework.org/schema/beans 
>  		http:/www.springframeworkorg/schema/beans/spring-beans.xsd"> 
>     <bean id="injectionService"class='com.imooc.ioc.injection.service.InjiectionServicelmp/>
>     	<constructor-arg name="injection0AO"ref=iniection0AQ>I</constructor-arg>  
>     </bean> 
>     <bean id=ipjection0AO"class="com.imooc.iodinjiection.dao.lpjection0AOlmp/></bean> 
> </beans>
> 
> ```
>
> ```java
> import com.imooc.ioc.injection.dao.InjectionDAO; 
> public class InjectionServicelmpl implements InjectionService{ 
>     private InjectionDAO injectionDAO; 
>     //构造器注入 
>     public InjectionServicelmpl(InjectionDAO injectionDAO)
>     { 
>         this.injectionDAO=injectionDAO;
>     }
>     public void save(String arg)
>     { 
>         //模拟业务操作 
>         System.outprintin(CService接收参数：+arg); 
>         arg=arg +":"+this.hashCode0; 
>         injectionDAO.save(arg);
>     }
> }
> 
> ```
>
> 



# Spring Bean装配

> [Bean装配，从Spring到Spring Boot]( https://juejin.im/post/5d5a48615188257c7d1648ae )
>
> **Bean配置项**
>
> * Class 
> * Scope 
> * Constructor 
> * arguments 
> * Properties 
> * Autowiring 
> * mode 
> * lazy-initialization mode 
> * Initialization/destruction method 
>
> **Bean的作用域**
>
> * singleton:单例，指一个Bean容器中只存在一份 
> * prototype：每次请求（每次使用）创建新的实例，destroy 方式不生效 
> * request:每次http请求创建一个实例且仅在当前request内 有效 
> * session:同上，每次http请求创建，当前session内有效 
> * global session:基于portlet的web中有效（portlet定义了 global session),如果是在web中，同session 
>
> ```xml
> <bean id="beanScope"class="com.imooc.bean.BeanScope" scope=singletor'"></bean> 
> ```
>
> 

## Bean的生命周期

> **生命周期**
>
> * -定义 
>
> * -初始化
>
>   * -实现org.springframework.beans.factory.InitializingBean接口 ，覆盖afterPropertiesSet方法 
>
>   ```java
>   public class ExamplelnitializingBean implements InitializingBean{ 
>       @Override 
>       public void afterPropertiesSet0 throws Exception{ 
>           //do something
>       }
>   }
>   ```
>
>   * -配置init-method
>
>   ```xml
>   <bean id="exampleInitBean" class="examples.ExampleBean" init-method="init"/〉  
>   ```
>
>   ```java
>   public class ExampleBean { 
>       public void init(){ 
>           //do some initialization work 
>       }
>   }
>   ```
>
> * -使用 
>
> * -销毁 
>
>   * -实现org.springframework.beans.factory.DisposableBean接口 ，覆盖destroy方法 
>
>     ```java
>     public class ExampleDisposableBean implements DisposableBean{ 
>         @Override 
>         public void destroy0 throws Exception{ 
>             //do something
>         }
>     }
>     ```
>
>     
>
>   * 配置destroy-method 
>
>     ```xml
>     <bean id="exampleInitRean" class="examples.ExampleBean"destroy-method="cleanup"/> 
>     ```
>
>     ```java
>     public class ExampleBean { 
>         public void cleanup(){ 
>             //do some destruction work (like releasing pooled connections) 
>         }
>     }
>     ```
>
> * 配置全局默认初始化、销毁方法 
>
>   ```xml
>   <?xml version=1.0"encoding='UTF-8?>
>   <beans xmlns="http:/www.springframework.org/schema/beans" 
>   		xmlns:xsi="http://www.w3.org/2001/XML Schema-instance" 
>   		xsi:schemaLocation="http://www.springframeworkorg/schema/beans 
>   		http:/www.springframework.org/schema/beans/spring-beans.xsd"
>   		default-init-method="init"default-destroy-method="destroys">
>   </beans>
>   ```
>
> * 优先顺序  
>
>   * InitializingBean和DisposableBean(定义完需实现)
>   * 配置init-method和destroy-method(定义完需实现)
>   * 默认(可选)

## Aware接口

>* Spring中提供了一些以Aware结尾的接口，实现了Aware接 口的bean在被初始化之后，可以获取相应资源 
>* 通过Aware接口，可以对Spring相应资源进行操作（一定要慎 重） 
>* 为对Spring进行简单的扩展提供了方便的入口 
>
>[Spring中的aware接口](https://www.jianshu.com/p/c5c61c31080b)
>
>```java
>import org.springframework.beans.BeansException;
>import org.springframework.beans.factory.BeanNameAware;
>import org.springframework.context.ApplicationContext;
>import org.springframework.context.ApplicationContextAware;
>
>public class MoocBeanName implements BeanNameAware, ApplicationContextAware {
>	private String beanName;
>	
>	@Override
>	public void setBeanName(String name) {
>		this.beanName = name;
>		System.out.println("MoocBeanName : " + name);
>	}
>
>	@Override
>	public void setApplicationContext(ApplicationContext applicationContext)
>			throws BeansException {
>		System.out.println("setApplicationContext : " + applicationContext.getBean(this.beanName).hashCode());
>	}
>}
>```
>
>



## Bean的自动装配

> **Bean的自动装配（Autowiring)** 
>
> * No:不做任何操作 
>
> * byName:根据属性名自动装配。此选项将检查容器并根据名字 查找与属性完全一致的bean，并将其与属性自动装配 
>
>   ```xml
>   <?xml version="1.0" encoding="UTF-8"?>
>   <beans xmlns="http://www.springframework.org/schema/beans"
>       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>       xsi:schemaLocation="http://www.springframework.org/schema/beans
>       http://www.springframework.org/schema/beans/spring-beans.xsd" 
>       default-autowire="byName">
>       <bean id="autoWiringService" class="com.imooc.autowiring.AutoWiringService" ></bean>
>       <bean id="autoWiringDAO" class="com.imooc.autowiring.AutoWiringDAO" ></bean>
>   </beans>
>   ```
>
>   ```java
>   public class AutoWiringDAO {
>   	public void say(String word) {
>   		System.out.println("AutoWiringDAO : " + word);
>   	}
>   }
>   ```
>
>   ```java
>   public class AutoWiringService {
>       private AutoWiringDAO autoWiringDAO;
>       public void setAutoWiringDAO(AutoWiringDAO autoWiringDAO) {
>           System.out.println("setAutoWiringDAO");
>           this.autoWiringDAO = autoWiringDAO;
>       }
>       public void say(String word) {
>           this.autoWiringDAO.say(word);
>       }
>   }
>   ```
>
> * byType:如果容器中存在一个与指定属性类型相同的bean，那 么将与该属性自动装配；如果存在多个该类型bean，那么抛出 异常，并指出不能使用byType方式进行自动装配；如果没有找 到相匹配的bean，则什么事都不发生 
>
>   ```xml
>   <?xml version="1.0" encoding="UTF-8"?>
>   <beans xmlns="http://www.springframework.org/schema/beans"
>       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>       xsi:schemaLocation="http://www.springframework.org/schema/beans
>       http://www.springframework.org/schema/beans/spring-beans.xsd" 
>       default-autowire="byType">
>       <bean id="autoWiringService" class="com.imooc.autowiring.AutoWiringService" ></bean>
>       <bean id="autoWiringDAO" class="com.imooc.autowiring.AutoWiringDAO" ></bean>
>   </beans>
>   <!--autoWiringDAO  也可以是其它名字不影响， 甚至删除也可以-->
>   ```
>
> * Constructor:与byType方式类似，不同之处在于它应用于构造器参数。如果容器中没有找到与构造器参数类型一致的bean，那么抛出异常 
>
>   ```xml
>   <?xml version="1.0" encoding="UTF-8"?>
>   <beans xmlns="http://www.springframework.org/schema/beans"
>       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>       xsi:schemaLocation="http://www.springframework.org/schema/beans
>       http://www.springframework.org/schema/beans/spring-beans.xsd" 
>       default-autowire="constructor">
>       <bean id="autoWiringService" class="com.imooc.autowiring.AutoWiringService" ></bean>
>       <bean class="com.imooc.autowiring.AutoWiringDAO" ></bean>
>   </beans>
>   ```
>
>   ```java
>   public class AutoWiringService {
>       private AutoWiringDAO autoWiringDAO;
>       public AutoWiringService(AutoWiringDAO autoWiringDAO) {
>           System.out.println("AutoWiringService");
>           this.autoWiringDAO = autoWiringDAO;
>       }
>       public void say(String word) {
>           this.autoWiringDAO.say(word);
>       }
>   }
>   ```

## Bean的Resources

>**针对于资源文件的统一接口Resources**
>
>* -UrlResource：URL对应的资源，根据一个URL地址即可构建 
>* -ClassPathResource：获取类路径下的资源文件 
>* -FileSystemResource:获取文件系统里面的资源 
>* -ServletContextResource:ServletContext封装的资源，用于访问ServletContext环境下的资源 
>* -InputStreamResource:针对于输入流封装的资源 
>* -ByteArrayResource:针对于字节数组封装的资源 
>
>**ResourceLoader** 
>
>* 所有的application contexts都实现了ResourceLoader接口，因此在Resource实例中都可以使用application contexts。
>
>  ```java
>  public interface ResourceLoader{
>      Resource getResource(String location);
>  }
>  Resource template=ctx.getResource("some/resource/path/myTemplate.txt");
>  Resource template=ctx.getResource("classpath:some/resource/path/myTemplate.txt");
>  Resource template=ctx.getResource("file:/some/resource/path/myTemplate.txt");
>  ```
>
>  ```java
>  import java.io.IOException;
>  import org.springframework.beans.BeansException;
>  import org.springframework.context.ApplicationContext;
>  import org.springframework.context.ApplicationContextAware;
>  import org.springframework.core.io.Resource;
>  
>  public class MoocResource implements ApplicationContextAware  {
>  	private ApplicationContext applicationContext;
>  	@Override
>  	public void setApplicationContext(ApplicationContext applicationContext)
>  			throws BeansException {
>  		this.applicationContext = applicationContext;
>  	}
>  	public void resource() throws IOException {
>  		Resource resource = applicationContext.getResource("config.txt");
>  		System.out.println(resource.getFilename());
>  		System.out.println(resource.contentLength());
>  	}
>  }
>  ```
>
>  

## Bean的定义及作用域

> **Classpath扫描与组件管理**
>
> * 从Spring3.0开始，Spring JavaConfig项目提供了很多特性 ，包括使用java而不是XML定义bean，比如@Configuration,@Bean,@Import,@DependsOn 
> * @Component是一个通用注解，可用于任何bean 
> * @Repository,@Service,@Controller是更有针对性的注解 
>   * -@Repository通常用于注解DAO类，即持久层 
>   * -@Service通常用于注解Service类，即服务层 
>   * -@Controller通常用于Controller类，即控制层（MVC）
>
> **类的自动检测及Bean的注册**
>
> * ·Spring可以自动检测类并注册Bean到ApplicationContext中
>
> ```java
> @Service 
> bublic class SimpleMovielister{ 
> private MovieFinder movieFinder; 
> @Autovired 
> public SimpleMovieLister(MovieFinder movieFinder){ 
>     this.movieFinder=movieFinder;
> }
> }
> 
> @Repository public class JpaMovieFinder implements MovieFinder{ 
> 	//implementation elided for clarity
> }
> ```
>
> **context:annotation-config** 
>
>   * 通过在基于XML的Spring配置如下标签（请注意包含上下文 命名空间） 
>
>   * \<context:annotation-config/>仅会查找在同一个applicatcontext中的Bean注解
>
>  ```xml
>  <?xml version="1.0" encoding="UTF-8"?>
>  <beans xmlns="http://www.springframework.org/schema/beans"
>      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>      xmlns:context="http://www.springframework.org/schema/context"
>      xsi:schemaLocation="http://www.springframework.org/schema/beans
>          http://www.springframework.org/schema/beans/spring-beans.xsd
>          http://www.springframework.org/schema/context
>          http://www.springframework.org/schema/context/spring-context.xsd" >
>      <context:annotation-config/>
>  </beans>
>  ```
>
> **类的自动检测及Bean的注册**
>
> * 为了能够检测这些类并注册相应的Bean，需要下面内容
>
> ```xml
> <beans>
>    <context:component-scan base-package="org.example"/>
> </beans>
> ```
>
> * \<context:component-scan>包含<context:annotation- config>，通常在使用前者后，不用再使用后者，前者包含后者全部功能
>
> * AutowiredAnnotationBeanPostProcessor和 CommonAnnotationBeanPostProcessor也会被包含进来
>
> **使用过滤器进行自定义扫描**
>
> * 默认情况下，类被自动发现并注册bean的条件是：使用 @Component,@Repository,@Service,@Controller注解或者使用@Component的自定义注解 
>
> * 可以通过过滤器修改上面的行为，如:下面例子的XML配置忽略所有的@Repository注解并用“Stub”代替
>
> ```xml
> <beans> 
>    <context:component-scan base-package="org.example"> 
>    <context:include-filter type="regex" expression=".*Stub.*Repository"/> 
>    <context:exclude-filter type="annotation" expression="org.springframework.stereotype.Repository"/> </context:component-scan> 
> </beans>
> ```
>
> *  还可使用use-default-filters="false"禁用自动发现与注册
>
> **定义Bean**
>
> * 扫描过程中组件被自动检测，那么Bean名称是由 BeanNameGenerator生成的（@Component, @Repository,@Service,@Controller都会有个name属性用 于显式设置Bean Name) 
>
> ```java
> @Service("myMovieLister")
> Repository public class SimpleMovieLister {}
> @Repository
> public class MovieFinderImpl implements MovieFinder{}
> ```
>
> * 可自定义bean命名策略，实现BeanNameGenerator接口， 并一定要包含一个无参数构造函器
>
> ```xml
> <beans> 
>    <context:component-scan base-package="org.example" name-generator="org.example.MyNameGenerator"/>
> </beans>
> ```
>
> **作用域（Scope)**
>
> * 通常情况下自动查找的Spring组件，其scope是singleton，Spring2.5提供了一个标识scope的注解@Scope
>
> ```java
> @Scope("prototype") 
> @Repository 
> public class MovieFinderImpl implements MovieFinder{}
> ```
>
> * 也可以自定义scope策略，实现ScopeMetadataResolver接 口并提供一个无参构造器，比如在多线程中
>
> ```xml
> <beans> 
> 	<context:component-scan base-package="org.example” scope-resolver="org.example.MyScopeResolver"/> 
> </beans> 
> ```
> * proxyMode属性
>
>   ```java
>   @Scope("prototype" proxyMode=ScopedProxyMode.TARGET_CLASS )
>   public class MovieFinderImpl implements MovieFinder{}
>   ```
>
>   



## Autowired注解说明

> **@Required**
>
> * @Required注解适用于bean属性的setter方法 
>
> * 这个注解仅仅表示，受影响的bean属性必须在配置时被填充， 通过在bean定义或通过自动装配一个明确的属性值 
>
>   ```java
>   public class SimpleMovieLister {
>   private MovieFinder movieFinder; 
>       @Required 
>       public void setMovieFinder(MovieFinder movieFinder){ 
>           this.movieFinder=movieFinder; 
>       }
>   }
>   ```
>
> **@Autowired**
>
> * 可以将@Autowired注解为“传统"的setter方法 
>
>   ```java
>   private MovieFinder movieFinder; 
>       @Autovired 
>       public void setMovieFinder(MovieFinder movieFinder)
>       { 
>       	this.moviesinder=movieFinder; 
>       }
>   }
>   ```
>
> * 可用于构造器或成员变量 
>
>   ```java
>   @Autovired 
>   private MovieCatalog movieCatalog; 
>   private CustomerPreferenceDao customerPreferenceDao; 
>   @Autovired 
>   public MovieRecommender(CustomerPreferenceDao customerPreferenceDao){ 
>       this.customerPreferenceDao=customerPreferenceDao;
>   }
>   ```
>
> * 默认情况下，如果因找不到合适的bean将会导致autowiring 失败抛出异常，可以通过下面的方式避免
>
>   ```java
>   public class simpleMovieLister{ 
>       private MovieFinder movieFinder; 
>       @Autovired(required=false) 
>       public void setMovieFinder(MovieFinder movieFinder){ 
>           this.movieFinder=movieFinder;
>       }
>   }
>   ```
>
> * 每个类只能有一个构造器被标记为required=true 
>
> * @Autowired的必要属性，建议使用@Required注解 
>
>   ```xml
>   <?xml version="1.0" encoding="UTF-8"?>
>   <beans xmlns="http://www.springframework.org/schema/beans"
>       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>       xmlns:context="http://www.springframework.org/schema/context"
>       xsi:schemaLocation="http://www.springframework.org/schema/beans
>           http://www.springframework.org/schema/beans/spring-beans.xsd
>           http://www.springframework.org/schema/context
>           http://www.springframework.org/schema/context/spring-context.xsd" >
>   	<context:component-scan base-package="com.imooc.beanannotation">
>       </context:component-scan>
>    </beans>
>   ```
>
>   ```java
>   import org.springframework.beans.factory.annotation.Autowired;
>   import org.springframework.stereotype.Service;
>   import com.imooc.beanannotation.injection.dao.InjectionDAO;
>       
>   @Service
>   public class InjectionServiceImpl implements InjectionService {
>       // 方式一
>   	// @Autowired
>   	private InjectionDAO injectionDAO;
>   	    
>       // 方式二
>   	@Autowired
>   	public InjectionServiceImpl(InjectionDAO injectionDAO) {
>   		this.injectionDAO = injectionDAO;
>   	}
>   	    
>       // 方式三
>   	// @Autowired
>   	public void setInjectionDAO(InjectionDAO injectionDAO) {
>   		this.injectionDAO = injectionDAO;
>   	}
>           
>   	@Override
>   	public void save(String arg) {
>   		System.out.println("Service接收参数：" + arg);
>   		injectionDAO.save(arg + ":" + this.hashCode());
>   	}
>   }
>   ```

> * 可以使用@Autowired注解那些众所周知的解析依赖性接口， 比如：BeanFactory，ApplicationContext,Environment, ResourceLoader,ApplicationEventPublisher,and MessageSource 
>
> ```java
> public class MovieRecommender { 
> @Autovired private ApplicationContext context; 
>     public MovieRecommender(){}
> } 
> ```
>
> * 可以通过添加注解给需要该类型的数组的字段或方法，以提供ApplicationContext中的所有特定类型的bean
>
> ```java
> private Set<Moviecatalog> movieCatalogs; 
> @Autovired 
> public void seMovieCatalogs(Set<MovieCatalog> movieCatalogs){( 
> this.movieCatalogs=movieCatalogs;
> }
> ```
>
> * 可以用干装配kew为string的Map
>
> ```java
> private Map<String,Movlecatalog> moviecatalogs; 
> @Aucovired 
> pablic void setMovieCatalogs(Map<String,MovieCatalog > movieCatalogs){
> 	this.movieCatalogs=movieCatalogs;
> }
> ```
>
> * 如果希望数组有序，可以让bean实现 org.springframework.core.Ordered接口或使用的@Order注解，并且只针对数组有效
>
> * @Autowired是由Spring BeanPostProcessor处理的，所以不能在自己的BeanPostProcessor或 BeanFactoryPostProcessor类型应用这些注解，这些类型必须通过XML或者Spring的@Bean注解加载
>
> ```java
> public interface BeanInterface {}
> 
> import org.springframework.core.annotation.Order;
> import org.springframework.stereotype.Component;
> @Order(2)
> @Component
> public class BeanImplOne implements BeanInterface {
> }
> @Order(1)
> @Component
> public class BeanImplTwo implements BeanInterface {
> }
> ```
>
> ```java
> import java.util.List;
> import java.util.Map;
> import org.springframework.beans.factory.annotation.Autowired;
> import org.springframework.beans.factory.annotation.Qualifier;
> import org.springframework.stereotype.Component;
> 
> @Component
> public class BeanInvoker {
> 	@Autowired
> 	private List<BeanInterface> list;
> 	
> 	public void say() {
> 		if (null != list && 0 != list.size()) {
> 			System.out.println("list...");
> 			for (BeanInterface bean : list) {
> 				System.out.println(bean.getClass().getName());
> 			}
> 		} else {
> 			System.out.println("List<BeanInterface> list is null");
> 		}
> 	}
> }
> 
> list...
> com.imooc.beanannotation.multibean.BeanImplTwo
> com.imooc.beanannotation.multibean.BeanImplOne
> ```
>
> ```java
> import java.util.List;
> import java.util.Map;
> import org.springframework.beans.factory.annotation.Autowired;
> import org.springframework.beans.factory.annotation.Qualifier;
> import org.springframework.stereotype.Component;
> 
> @Component
> public class BeanInvoker {
> 	@Autowired
> 	private Map<String, BeanInterface> map;
> 	
> 	public void say() {
> 		if (null != map && 0 != map.size()) {
> 			System.out.println("map...");
> 			for (Map.Entry<String, BeanInterface> entry : map.entrySet()) {
> 				System.out.println(entry.getKey() + "      " + entry.getValue().getClass().getName());
> 			}
> 		} else {
> 			System.out.println("Map<String, BeanInterface> map is null");
> 		}
> 	}
> }
> 
> map...
> beanImplTwo  com.imooc.beanannotation.multibean.BeanImplTwo
> beanImplOne  com.imooc.beanannotation.multibean.BeanImplOne
> ```
>

## @Qualifier注解

> * 按类型自动装配可能多个bean实例的情况，可以使用Spring的@Qualifier注解缩小范围(或指定唯一)，也可以用于指定单独的构造器参数或方法参数 
>
> * 可用于注解集合类型变量
> 
> * 主要由xml定义和java注解实现这两种方式
> 
> ```xml
> <bean class="example.SimpleMovieCatalog"> 
><qualifier value="main"/> 
> </bean> 
><bean class="example.SimpleMovieCatalog"> 
> <qualifier value="action"/>
> </bean> 
> ```
> 
> * 如果通过名字进行注解注入，主要使用的不是@Autowired( 即使在技术上能够通过@Qualifier定bean的名字），替代方式是使用JSR-250@Resource注解，它是通过其独特的名称 来定义来识别特定的目标（这是一个与所声明的类型是无关的 匹配过程）
> * 因语义差异，集合或Map类型的bean无法通过@Autowired 来注入，因为没有类型匹配到这样的bean，为这些bean使用 @Resource注解，通过唯一名称引用集合或Map的bean 
> * @Autowired适用于fields,constructors,multi-argument methods这些允许在参数级别使用@Qualifier注解缩小范围的情况 
>* @Resource适用于成员变量、只有一个参数的setter方法，所以在目标是构造器或一个多参数方法时，最好的方式是使用qualifiers
> * 可以定义自己的Qualifier
>
> ```java
> @Component
> public class BeanImplOne implements BeanInterface {
> }
> @Component
> public class BeanImplTwo implements BeanInterface {
> }
>
> import org.springframework.beans.factory.annotation.Autowired;
>import org.springframework.beans.factory.annotation.Qualifier;
> import org.springframework.stereotype.Component;
>
> @Component
> public class BeanInvoker {
> 	@Autowired
> 	@Qualifier("beanImplTwo")
> 	private BeanInterface beanInterface;
> 	
> 	public void say() {
> 		if (null != beanInterface) {
> 			System.out.println(beanInterface.getClass().getName());
> 		} else {
> 			System.out.println("beanInterface is null...");
> 		}
> 	}
> }
>
> com.imooc.beanannotation.multibean.BeanImplTwo
> ```
> 



## 基于Java的容器注解

> * @Bean标识一个用于配置和初始化一个由SpringloC容器管理的新对象的方法，类似于XML配置文件的<bean/> 
>
> * 可以在Spring的@Component注解的类中使用@Bean注解 任何方法（仅仅是可以）
>
> * 上一点中，通常使用的是@Configuration 
>
>   ```xml
>   <beans> <bean id="myService" class="com.acme.services.MyServiceImp1"/> </beans>
>   ```
>
>   等价于
>
>   ```java
>   import org.springframework.context.annotation.Bean;
>   import org.springframework.context.annotation.Configuration;
>       
>   @Configuration
>   public class StoreConfig {
>       // 若没有指明name，则默认为方法名
>       // @Bean
>   	@Bean(name="stringStore" initMethod="init" destoryMethod="cleanup")
>   	public StringStore stringStore() {
>   		return new StringStore();
>   	}
>   }
>   ```

> **使用@ImportResource和@Value 注解进行资源文件读取**
>
> ```xml
> <beans>
>     <context:annotation-config/> 
>     <context:property-placeholder location="classpath:/com/acme/jdbc.properties"/> 
>     <bean class="com.acme.AppConfig"/> 
>     <bean class=lWorg.springframework.jdbc.datasource.DriverManagerDataSource"> 
>         <property name="url" value="${jdbc.url}"/> 
>         <property name="username" value="${jdbc.username}"/> 
>         <property name="password" value="S{jdbc.password)"/> 
> 	</bean> 
> </beans> 
> ```
>
>等价于
>
> 
> ```java
> @Configuration 
> ImportResource("classpath:/com/acme/properties-config.xm1") 
> public class AppConfig{
>     @Value("$(jdbc.url)") 
>     private String url; 
>     @Value("$(jdbc.username)") 
>     private String username; 
>     @Value("jdbc.password)") 
>     private String password; 
>     
>     @Bean 
>     public DataSource dataSource(){ 
>         return new DriverManagerDataSource(url,username,password); 
>     }
> }
> ```
>
> ```properties
> # properties-config.xm1
> 
> jdbc.username=root
> password=root
> url=127.00.1
> ```
>

## 基于泛型的装配

>
>
>```java
>public interface Store<T> {}
>public class StringStore implements Store<String> {}
>public class IntegerStore implements Store<Integer> {}
>
>
>import org.springframework.beans.factory.annotation.Autowired;
>import org.springframework.context.annotation.Bean;
>import org.springframework.context.annotation.Configuration;
>import org.springframework.context.annotation.ImportResource;
>
>@Configuration
>@ImportResource("classpath:config.xml")
>public class StoreConfig {
>	@Autowired
>	private Store<String> s1;
>	@Autowired
>	private Store<Integer> s2;
>	
>	@Bean
>	public StringStore stringStore() {
>		return new StringStore();
>	}
>	@Bean
>	public IntegerStore integerStore() {
>		return new IntegerStore();
>	}
>    @Bean(name = "stringStoreTest")
>	public Store stringStoreTest() {
>		System.out.println("s1 : " + s1.getClass().getName());
>		System.out.println("s2 : " + s2.getClass().getName());
>		return new StringStore();
>	}
>}
>```
>
>**CustomAutowireConfigurer**
>
>* CustomAutowireConfigurer是 BeanFactoryPostProcessor的子类，通过它可以注册自己的 qualifier注解类型（即使没有使用Spring的@Qualifier 注解）
>
>  ```xml
>  <bean id="customAutowireConfigurer" class="org.springframework.beans.factory.annotation.CustomAutowireConfigurer"> 
>      <property name="customQualifierTypes"> 
>          <set> 
>              <value>example.CustomQualifier</value> 
>          </set> 
>      </property> 
>  </bean>
>  ```
>
>  
>
>* 该AutowireCandidateResolver决定自动装配的候选者
>
>  * -每个bean定义的autowire-candidate值 
>  * -任何<bean/>中的default-autowire-candidates 
>  * -@Qualifier注解及使用CustomAutowireConfigurer的自定义类型



## JSR支持说明



# Spring AOP基本概念

> [Spring AOP是什么?你都拿它做什么?](https://blog.csdn.net/fygu18/article/details/79989862)

## AOP基本概念和特点

>**什么是AOP**
>
>* AOP：Aspect Oriented Programming的缩写，意为：面向切面编程，通过预编译方式和运行期动态代理实现程序功能 的统一维护的一种技术 
>* 主要的功能是：日志记录，性能统计，安全控制，事务处理， 异常处理等等 
>
>![AOP切面示意图](res/Spring注解_Spring入门篇/AOP%E5%88%87%E9%9D%A2%E7%A4%BA%E6%84%8F%E5%9B%BE.png)
>
>**AOP实现方式**
>
>* 预编译 
>  * -AspectJ 
>* 运行期动态代理（JDK动态代理、CGLib动态代理） 
>  * -SpringAOP
>  * JbossAOP 
>
>**AOP几个相关概念** 
>
>| 名称                    | 说明                                                         |
>| ----------------------- | ------------------------------------------------------------ |
>| 切面(Aspect)            | 一个关注点的模块化，这个关注点可能会横切多个对象             |
>| 连接点(Joinpoint)       | 程序执行过程中的某个特定的点                                 |
>| 通知(Advice)            | 在切面的某个特定的连接点上执行的动作                         |
>| 切入点(Pointcut)        | 匹配连接点的断言，在AOP中通知和一个切入点表达式关联          |
>| 引入(Introduction)      | 在不修改类代码的前提下，为类添加新的方法和属性               |
>| 目标对象(Target Object) | 被一个或者多个切面所通知的对象                               |
>| AOP代理(AOP Proxy)      | AOP框架创建的对象，用来实现切面契约(aspect contract)<br />(包括通知方法执行等功能） |
>| 织入(Weaving)           | 把切面连接到其它的应用程序类型或者对象上，并创建一个被通知<br />的对象，分为：编译时织入、类加载时织入、执行时织入 |
>
>**Advice的类型**
>
>| 名称                                  | 说明                                                         |
>| ------------------------------------- | ------------------------------------------------------------ |
>| 前置通知(Before advice)               | 在某连接点(join point)之前执行的通 知，但不能阻止<br />连接点前的执行(除非它抛出一个异常） |
>| 返回后通知(After returning advice)    | (After returning advice)在某连接点(join point)正常完<br />成后执行的通知 |
>| 抛出异常后通知(After throwing advice) | 在方法抛出异常退出时执行的通知                               |
>| 后通知(After((finally) advice)        | 当某连接点退出的时候执行的通知<br />(不论是正常返回还是异常退出） |
>| 环绕通知(Around Advice)               | 包围一个连接点(join point)的通知                             |
>
>**Spring框架中AOP的用途**
>
>* 提供了声明式的企业服务，特别是EJB的替代服务的声明 
>* 允许用户定制自己的方面，以完成OOP与AOP的互补使用 
>
>**Spring的AOP实现**
>
>* 纯java实现，无需特殊的编译过程，不需要控制类加载器层次 
>* 目前只支持方法执行连接点(通知Spring Bean的方法执行) 
>* 不是为了提供最完整的AOP实现(尽管它非常强大)；而是侧重于提供一种AOP实现和Spring IoC容器之间的整合，用于帮助解决企业应用中的常见问题 
>* Spring AOP不会与AspectU竞争，从而提供综合全面的AOP解决方案 
>
>**有接口和无接口的Spring AOP实现区别**
>
>* Spring AOP默认使用标准的JavaSE动态代理作为AOP代理， 这使得任何接口(或者接口集)都可以被代理 
>* Spring AOP中也可以使用CGLIB代理(如果一个业务对象并没有实现一个接口)
>
>



## 配置切面和切入点

> **Schema-based AOP**
>
> * Spring所有的切面和通知器都必须放在一个<aop：config>内 （可以配置包含多个<aop：config>元素），
>
> * 每一个 \<aop:config>可以包含pointcut，advisor和aspect元素 （它们必须按照这个顺序进行声明 )
>
> * \<aop:config>风格的配置大量使用了Spring的自动代理机制
>
>   ```xml
>   <bean id="moocAspect" class="com.imooc.aop.schema.advice.MoocAspect"></bean> 
>   <bean id="aspectBiz" class="com.imooc.aop.schema.advice.biz.AspectBiz"></bean> <aop:config> 
>       <aop:aspect id="moocAspect4op" ref="moocAspect">
>           <aop:pointcut expression="execution(* com.imooc.aop.schema.advice.biz.*Biz(..))" id="moocPiontcut"/>
>       </aop:aspect>
>   </aop:config> 
>   ```
>
>   | 表达式                                                       | 含义                                                         |
>   | ------------------------------------------------------------ | ------------------------------------------------------------ |
>   | execution(public**(..))                                      | 切入点为执行所有public方法时                                 |
>   | execution(* set*(..))                                        | 切入点为执行所有set开始的方法时                              |
>   | execution(* com.service.Service.*(..))                       | 切入点为执行AccountService类中的所有方法时                   |
>   | execution(* com.xyz.service..(.))                            | 切入点为执行com.xyz.service包下的所有方法时                  |
>   | execution(* com.xyz.service...(..))                          | 切入点为执行com.xyz.service包及其子包下的所有方法时          |
>   | within(com.xyz.service.*)                                    | (only in Spring AOP)                                         |
>   | within(com.xyz.service..*)                                   | (only in Spring AOP) <br />within用于匹配指定类型内的方法执行 |
>   | this(com.xyz.service.AccountService)                         | (only in Spring AOP)<br />this用于匹配当前AOP代理对象类型的执行方法 |
>   | target(com.xyz.service.AccountService)                       | (only in Spring AOP)<br />target 用于匹配当前目标对象类型的执行方法 |
>   | @annotation<br />(org.springframework.transaction.annota tion.Transactional) | (only in Spring AOP)<br />args 用于匹配当前执行的方法传入的参数为<br />指定类型的执行方法 |
>
> 



## Advice应用

>```java
>public class AspectBiz {
>	public void biz() {
>		System.out.println("AspectBiz biz.");
>//		throw new RuntimeException();
>	}
>}
>```
>
>```java
>import org.aspectj.lang.ProceedingJoinPoint;
>
>public class MoocAspect {
>	public void before() {
>		System.out.println("MoocAspect before.");
>	}
>	public void afterReturning() {
>		System.out.println("MoocAspect afterReturning.");
>	}
>	public void afterThrowing() {
>		System.out.println("MoocAspect afterThrowing.");
>	}
>	public void after() {
>		System.out.println("MoocAspect after.");
>	}
>}
>
>```
>
>```xml
><bean id="moocAspect" class="com.imooc.aop.schema.advice.MoocAspect"></bean> 
><bean id="aspectBiz" class="com.imooc.aop.schema.advice.biz.AspectBiz"></bean> <aop:config> 
>    <aop:aspect id="moocAspect4op" ref="moocAspect">
>        <aop:pointcut expression="execution(* com.imooc.aop.schema.advice.biz.*Biz(..))" id="moocPiontcut"/>
>        <aop:before method="before" pointcut-ref="moocPiontcut"/> 
> 		<aop:after-returning method="afterReturning" pointcut-ref="moocPiontcut"/> 
> 		<aop:after-throwing method="afterThrowing" pointcut-ref="moocPiontcut"/> 
> 		<aop:after method="after" pointcut-ref="moocPiontcut"/> 
>    </aop:aspect>
></aop:config> 
>```
>
>```java
>// 输出
>MoocAspect before.
>AspectBiz biz.
>MoocAspect afterReturning.
>MoocAspect after
>```
>
>**Around advice**
>
>* 通知方法的第一个参数必须是ProceedingJoinPoint类型 
>
>  ```xml
>  <aop:around method="around" pointcut-ref="moocPiontcut"/>
>  ```
>
>  ```java
>  public Object around(ProceedingJoinPoint pjp) {
>  		Object obj = null;
>  		try {
>  			System.out.println("MoocAspect around 1.");
>  			obj = pjp.proceed();
>  			System.out.println("MoocAspect around 2.");
>  		} catch (Throwable e) {
>  			e.printStackTrace();
>  		}
>  		return obj;
>  	}
>  ```
>
>**Advice parameters**
>
>```xml
><aop:around method="aroundInit" 
>            pointcut="execution(* com.imooc.aop.schema.advice.biz.AspectBiz.init(String, int)) and args(bizName, times)"/> 
>```
>
>```java
>public class AspectBiz {
>	public void biz() {
>		System.out.println("AspectBiz biz.");
>	}
>	public void init(String bizName, int times) {
>		System.out.println("AspectBiz init : " + bizName + "   " + times);
>	}
>}
>```
>
>```java
>import org.aspectj.lang.ProceedingJoinPoint;
>public class MoocAspect {
>	public Object aroundInit(ProceedingJoinPoint pjp, String bizName, int times) {
>		System.out.println(bizName + "   " + times);
>		Object obj = null;
>		try {
>			System.out.println("MoocAspect aroundInit 1.");
>			obj = pjp.proceed();
>			System.out.println("MoocAspect aroundInit 2.");
>		} catch (Throwable e) {
>			e.printStackTrace();
>		}
>		return obj;
>	}
>}
>```
>
>



## Introduction应用

>* 允许一个切面声明一个实现指定接口的通知对象，并且提供了一个接口实现类来代表这些对象 
>
>* 由\<aop:aspect>中的\<aop:declare-parents>元素声明
>
>* 该元素用于声明所匹配的类型拥有一个新的parent（因此得名）
>
>* schema-defined aspects只支持singleton model 
>
>  ```xml
>  <aop:config>
>      <aop:aspect id="moocAspectAOP" ref="moocAspect">
>          <aop:declare-parents 
>          	types-matching="com.imooc.aop.schema.advice.biz.*(+)"
>              implement-interface="com.imooc.aop.schema.advice.Fit"
>              default-impl="com.imooc.aop.schema.advice.FitImpl"/>
>      </aop:aspect>
>  </aop:config>
>  ```
>
>  ```java
>  public interface Fit {
>  	void filter();
>  }
>  
>  public class FitImpl implements Fit {
>  	@Override
>  	public void filter() {
>  		System.out.println("FitImpl filter.");
>  	}
>  }
>  
>  @Test 
>  public void testFit0{ 
>      Fit fit=(Fit)super.getBean("aspectBiz"); 
>      fit.filter0; 
>  }
>  
>  // 输出
>  FitImpl filter.
>  ```
>
>  



## Advisors

>* advisor就像一个小的自包含的方面，只有一个advice 
>
>* 切面自身通过一个bean表示，并且必须实现某个advice 接口，同时，advisor也可以很好的利用AspectJ的切入 点表达式 
>
>* Spring通过配置文件中\<aop:advisor>元素支持advisor 实际使用中，大多数情况下它会和transactional advice 配合使用 
>
>* 为了定义一个advisor的优先级以便让advice可以有序， 可以使用order属性来定义advisor的顺序 
>
>  ```xml
>  <?xml version="1.0" encoding="UTF-8"?>
>  <beans xmlns="http://www.springframework.org/schema/beans"
>      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
>      xmlns:context="http://www.springframework.org/schema/context"
>      xmlns:aop="http://www.springframework.org/schema/aop"
>      xsi:schemaLocation="http://www.springframework.org/schema/beans 
>          http://www.springframework.org/schema/beans/spring-beans.xsd  
>          http://www.springframework.org/schema/context
>          http://www.springframework.org/schema/context/spring-context.xsd
>          http://www.springframework.org/schema/aop 
>          http://www.springframework.org/schema/aop/spring-aop.xsd">
>  	<context:component-scan base-package="com.imooc.aop.schema">
>      </context:component-scan>
>  
>  	<aop:config>
>  		<aop:aspect id="concurrentOperationRetry" 	
>                      ref="concurrentOperationExecutor">
>  			<aop:pointcut id="idempotentOperation"
>              	expression="execution(* com.imooc.aop.schema.advisors.service.*.*(..)) " />
>  			<aop:around pointcut-ref="idempotentOperation" 
>                          method="doConcurrentOperation" />
>  		</aop:aspect>
>  	</aop:config>
>  	
>  	<bean id="concurrentOperationExecutor" 
>            class="com.imooc.aop.schema.advisors.ConcurrentOperationExecutor">
>  		<property name="maxRetries" value="3" />
>  		<property name="order" value="100" />
>  	</bean>
>   </beans>
>  ```
>
>  ```java
>  import org.aspectj.lang.ProceedingJoinPoint;
>  import org.springframework.core.Ordered;
>  import org.springframework.dao.PessimisticLockingFailureException;
>  
>  public class ConcurrentOperationExecutor implements Ordered {
>  	private static final int DEFAULT_MAX_RETRIES = 2;
>  	private int maxRetries = DEFAULT_MAX_RETRIES;
>  	private int order = 1;
>  
>  	public void setMaxRetries(int maxRetries) {
>  		this.maxRetries = maxRetries;
>  	}
>  	public int getOrder() {
>  		return this.order;
>  	}
>  	public void setOrder(int order) {
>  		this.order = order;
>  	}
>  	public Object doConcurrentOperation(ProceedingJoinPoint pjp) throws Throwable {
>  		int numAttempts = 0;
>  		PessimisticLockingFailureException lockFailureException;
>  		do {
>  			numAttempts++;
>  			System.out.println("Try times : " + numAttempts);
>  			try {
>  				return pjp.proceed();
>  			} catch (PessimisticLockingFailureException ex) {
>  				lockFailureException = ex;
>  			}
>  		} while (numAttempts <= this.maxRetries);
>  		System.out.println("Try error : " + numAttempts);
>  		throw lockFailureException;
>  	}
>  }
>  
>  ```
>
>  ```java
>  import org.springframework.dao.PessimisticLockingFailureException;
>  import org.springframework.stereotype.Service;
>  
>  @Service
>  public class InvokeService {
>  	public void invoke() {
>  		System.out.println("InvokeService ......");
>  	}
>  	public void invokeException() {
>  		throw new PessimisticLockingFailureException("");
>  	}
>  }
>  ```
>
>  ```java
>  @Test 
>  public void testSave0{ 
>      InvokeService service=super.getBeaninvokeService"); 
>      service.invoke0; 
>      System.out printin0.
>      service.invokeException0;
>  }
>  ```
>
>  ```java
>  // 输出
>  Try times:1 
>  InvokeService... 
>      
>  Try times:1 
>  Try times:2 
>  Try times:3 
>  Try times:4 
>  Try error:4 
>  ```
>
>

