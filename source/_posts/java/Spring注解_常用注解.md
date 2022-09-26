---
title: Spring注解_常用注解
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: a0f3b9ff
---

---



# 12种 Spring 常用注解

# 声明bean的注解

> @Component 组件，没有明确的角色
>
> @Service 在业务逻辑层使用（service层）
>
> @Repository 在数据访问层使用（dao层）
>
> @Controller 在展现层使用，控制器的声明（Controller层）
>
> 



# 注入bean的注解

| ANNOTATION | PACKAGE                          | SOURCE       |
| :--------- | :------------------------------- | :----------- |
| @Resource  | javax.annotation                 | Java JSR-250 |
| @Inject    | javax.inject                     | Java JSR-330 |
| @Autowired | org.springframework.bean.factory | Spring 2.5+  |

JSR是Java Specification Requests的缩写，意思是Java 规范提案。是指向JCP(Java Community Process)提出新增一个标准化技术规范的正式请求。任何人都可以提交JSR，以向Java平台增添新的API和服务。JSR已成为Java界的一个重要标准。

> [*@Resource,@Autowired,@Inject3种注入方式详解*](https://mp.weixin.qq.com/s/Dw62V86Y6uouonHz-fkpIw)
>
> @Autowired：由Spring提供
>
> > 默认按类型装配，找不到或者找到多个则报错。
> >
> > 如果要按名称装配，需要结合Spring另外一个注解Qualifier("name")使用。
> >
> > 默认必须装配requred=true，如果可以为空，可以设置为false，在Spring4+结合jdk8+的情况下还可以使用Optional和false同等的效果，如
> >
> > ```java
> > @Autowired
> > private Optional<UserService> userService;
> > ```
> >
> > 
>
> @Inject：由JSR-330提供
>
> > 和@Autowired类似，可以完全代替@Autowired，但这个没有required属性，要求bean必须存在。
> >
> > 如果要按名称装配，需要结合javax另外一个注解N("name")使用。
>
> @Resource：由JSR-250提供
>
> > 它有两个关键的属性：name－名称，type－类型
> >
> > 1、如果指定了name,type，则从Spring容器中找一个名称和类型相当应的一个bean，找不到则报错。
> >
> > 2、如果只指定了name，则从Spring容器中找一个名称和name一样的bean，找不到则报错。
> >
> > 3、如果只指定了type，则从Spring容器中找一个类型和type一样的bean，找不到或者找到多个则报错。
> >
> > 4、如果没有指定参数，则默认找字段名称装配，找不到则按类型装配，找不到则报错。
>
> 都可以注解在set方法和属性上，推荐注解在属性上（一目了然，少写代码）。
>
> 

**[Spring常用的三种注入方式](https://www.cnblogs.com/moxiaotao/p/9304810.html)**

> Spring通过DI（依赖注入）实现IOC（控制反转），常用的注入方式主要有三种：构造方法注入，setter注入，基于注解的注入。
>
> **1. 构造方法注入**
>
> 在spring的配置文件中注册UserService，将UserDaoJdbc通过constructor-arg标签注入到UserService的某个有参数的构造方法
>
> ```xml
> <!-- 注册userService -->
> <bean id="userService" class="com.lyu.spring.service.impl.UserService">
>    	<constructor-arg ref="userDaoJdbc"></constructor-arg>
> </bean>
> <!-- 注册jdbc实现的dao -->
> <bean id="userDaoJdbc" class="com.lyu.spring.dao.impl.UserDaoJdbc"></bean>
> ```
>
> 如果只有一个有参数的构造方法并且参数类型与注入的bean的类型匹配，那就会注入到该构造方法中。
>
> ```java
> public class UserService implements IUserService {
>        private IUserDao userDao;
>        public UserService(IUserDao userDao) {
>            this.userDao = userDao;
>        }
>        public void loginUser() {
>            userDao.loginUser();
>        }
> }
> ```
>
> > 问题一：如果有多个有参数的构造方法并且每个构造方法的参数列表里面都有要注入的属性，那userDaoJdbc会注入到哪里呢？
> >
> > ```java
> > public class UserService implements IUserService {
> >        private IUserDao userDao;
> >        private User user;
> >        public UserService(IUserDao userDao) {
> >            System.out.println("这是有一个参数的构造方法");
> >            this.userDao = userDao;
> >        }
> >        public UserService(IUserDao userDao, User user) {
> >            System.out.println("这是有两个参数的构造方法");
> >            this.userDao = userDao;
> >            this.user = user;
> >        }
> >        public void loginUser() {
> >            userDao.loginUser();
> >        }
> > }
> > ```
> >
> > 结果：会注入到只有一个参数的构造方法中，并且经过测试注入哪一个构造方法与构造方法的顺序无关
> >
> > 
> >
> > 问题二：如果只有一个构造方法，但是有两个参数，一个是待注入的参数，另一个是其他类型的参数，那么这次注入可以成功吗？
> >
> > ```java
> > public class UserService implements IUserService {
> >        private IUserDao userDao;
> >        private User user;
> >        public UserService(IUserDao userDao, User user) {
> >            this.userDao = userDao;
> >            this.user = user;
> >        }
> >        public void loginUser() {
> >            userDao.loginUser();
> >        }
> > }
> > ```
> >
> > 结果：失败了，即使在costract-arg标签里面通过name属性指定要注入的参数名userDao也会失败.
> >
> > 
> >
> > 问题三：如果我们想向有多个参数的构造方法中注入值该在配置文件中怎么写呢？
> >
> > ```java
> > public class UserService implements IUserService {
> >        private IUserDao userDao;
> >        private User user;
> >        public UserService(IUserDao userDao, User user) {
> >            this.userDao = userDao;
> >            this.user = user;
> >        }
> >        public void loginUser() {
> >            userDao.loginUser();
> >        }
> > }
> > ```
> >
> > 参考写法：通过name属性指定要注入的值，与构造方法参数列表参数的顺序无关
> >
> > ```xml
> > <!-- 注册userService -->
> > <bean id="userService" class="com.lyu.spring.service.impl.UserService">
> >        <constructor-arg name="userDao" ref="userDaoJdbc"></constructor-arg>
> >        <constructor-arg name="user" ref="user"></constructor-arg>
> > </bean>
> > 
> > <!-- 注册实体User类，用于测试 -->
> > <bean id="user" class="com.lyu.spring.entity.User"></bean>
> > <!-- 注册jdbc实现的dao -->
> > <bean id="userDaoJdbc" class="com.lyu.spring.dao.impl.UserDaoJdbc"></bean>
> > ```
> >
> > 
> >
> > 问题四：如果有多个构造方法，每个构造方法只有参数的顺序不同，那通过构造方法注入多个参数会注入到哪一个呢？
> >
> > ```java
> > public class UserService implements IUserService {
> >        private IUserDao userDao;
> >        private User user;
> >        public UserService(IUserDao userDao, User user) {
> >            System.out.println("这是第二个构造方法");
> >            this.userDao = userDao;
> >            this.user = user;
> >        }
> >        public UserService(User user, IUserDao userDao) {
> >            System.out.println("这是第一个构造方法");
> >            this.userDao = userDao;
> >            this.user = user;
> >        }
> >        public void loginUser() {
> >            userDao.loginUser();
> >        }
> > }
> > ```
> >
> > 结果：哪个构造方法在前就注入哪一个，这种情况下就与构造方法顺序有关。
>
> **2. setter方法注入**
>
> >配置文件如下：
> >
> >```xml
> ><!-- 注册userService -->
> ><bean id="userService" class="com.lyu.spring.service.impl.UserService">
> >     	<!-- 写法一 -->
> >     	<!-- <property name="UserDao" ref="userDaoMyBatis"></property> -->
> >     	<!-- 写法二 -->
> >     	<property name="userDao" ref="userDaoMyBatis"></property>
> ></bean>
> >
> ><!-- 注册mybatis实现的dao -->
> ><bean id="userDaoMyBatis" class="com.lyu.spring.dao.impl.UserDaoMyBatis"></bean>
> >```
> >
> >注：上面这两种写法都可以,spring会将name值的每个单词首字母转换成大写，然后再在前面拼接上”set”构成一个方法名,然后去对应的类中查找该方法,通过反射调用,实现注入。
> >
> >*切记：name属性值与类中的成员变量名以及set方法的参数名都无关，只与对应的set方法名有关，下面的这种写法是可以运行成功的*
> >
> >```java
> >public class UserService implements IUserService {
> >        private IUserDao userDao1;
> >        public void setUserDao(IUserDao userDao1) {
> >             this.userDao1 = userDao1;
> >        }
> >        public void loginUser() {
> >             userDao1.loginUser();
> >        }
> >}
> >```
> >
> >还有一点需要注意：如果通过set方法注入属性，那么spring会通过默认的空参构造方法来实例化对象，所以如果在类中写了一个带有参数的构造方法，一定要把空参数的构造方法写上，否则spring没有办法实例化对象，导致报错。
>
> **3. 基于注解的注入**
>
> >- @Resource：java的注解，默认以byName的方式去匹配与属性名相同的bean的id，如果没有找到就会以byType的方式查找，如果byType查找到多个的话，使用@Qualifier注解（spring注解）指定某个具体名称的bean。
> >
> >```java
> >@Resource
> >@Qualifier("userDaoMyBatis")
> >private IUserDao userDao;
> >public UserService(){}
> >```
> >
> >@Resource装配顺序
> >>1. 如果同时指定了name和type，则从Spring上下文中找到唯一匹配的bean进行装配，找不到则抛出异常
> >>2. 如果指定了name，则从上下文中查找名称（id）匹配的bean进行装配，找不到则抛出异常
> >>3. 如果指定了type，则从上下文中找到类型匹配的唯一bean进行装配，找不到或者找到多个，都会抛出异常
> >>4. 如果既没有指定name，又没有指定type，则自动按照byName方式进行装配；如果没有匹配，则回退为一个原始类型进行匹配，如果匹配则自动装配
> >
> >* @Autowired：spring注解，默认是以byType的方式去匹配与属性名相同的bean的id，如果没有找到，就通过byName的方式去查找。
> >
> >```java
> >@Autowired
> >@Qualifier("userDaoJdbc")
> >private IUserDao userDao;
> >```
> >
> >



# java配置类相关注解

> @Configuration 声明当前类为配置类，相当于xml形式的Spring配置（类上）
>
> @Bean 注解在方法上，声明当前方法的返回值为一个bean，替代xml中的方式（方法上）
>
> @Configuration 声明当前类为配置类，其中内部组合了@Component注解，表明这个类是一个bean（类上）
>
> @ComponentScan 用于对Component进行扫描，相当于xml中的（类上）
>
> @WishlyConfiguration 为@Configuration与@ComponentScan的组合注解，可以替代这两个注解
>
> 



# 切面(AOP)相关注解

> Spring支持AspectJ的注解式切面编程。
>
> @Aspect 声明一个切面（类上） 
> 使用@After、@Before、@Around定义建言（advice），可直接将拦截规则（切点）作为参数。
>
> @After 在方法执行之后执行（方法上） 
> @Before 在方法执行之前执行（方法上） 
> @Around 在方法执行之前与之后执行（方法上）
>
> @PointCut 声明切点 
> 在java配置类中使用@EnableAspectJAutoProxy注解开启Spring对AspectJ代理的支持（类上）
>
> 



# @Bean的属性支持

> @Scope 设置Spring容器如何新建Bean实例（方法上，得有@Bean） 
> 其设置类型包括：
>
> > Singleton （单例,一个Spring容器中只有一个bean实例，默认模式）, 
> > Protetype （每次调用新建一个bean）, 
> > Request （web项目中，给每个http request新建一个bean）, 
> > Session （web项目中，给每个http session新建一个bean）, 
> > GlobalSession（给每一个 global http session新建一个Bean实例）
>
> @StepScope 在Spring Batch中还有涉及
>
> @PostConstruct 由JSR-250提供，在构造函数执行完之后执行，等价于xml配置文件中bean的initMethod
>
> @PreDestory 由JSR-250提供，在Bean销毁之前执行，等价于xml配置文件中bean的destroyMethod
>
> 



# @Value注解

> @Value 为属性注入值（属性上） 
> 支持如下方式的注入： 
> 》注入普通字符
>
> @Value("Michael Jackson")String name;
>
> 》注入操作系统属性
>
> @Value("#{systemProperties['os.name']}")String osName;
>
> 》注入表达式结果
>
> @Value("#{ T(java.lang.Math).random() * 100 }") String randomNumber;
>
> 》注入其它bean属性
>
> @Value("#{domeClass.name}")String name;
>
> 》注入文件资源
>
> @Value("classpath:com/hgs/hello/test.txt")String Resource file;
>
> 》注入网站资源
>
> @Value("http://www.javastack.cn")Resource url;
>
> 》注入配置文件
>
> Value("${book.name}")String bookName;
>
> 注入配置使用方法： 
>
> > ① 编写配置文件（test.properties）
> >
> > book.name=《三体》
> >
> > ② @PropertySource 加载配置文件(类上)
> >
> > @PropertySource("classpath:com/hgs/hello/test/test.propertie")
> >
> > ③ 还需配置一个PropertySourcesPlaceholderConfigurer的bean。
>
> 



# 环境切换

> @Profile 通过设定Environment的ActiveProfiles来设定当前context需要使用的配置环境。（类或方法上）
>
> @Conditional Spring4中可以使用此注解定义条件话的bean，通过实现Condition接口，并重写matches方法，从而决定该bean是否被实例化。（方法上）
>
> 



# 异步相关

>@EnableAsync 配置类中，通过此注解开启对异步任务的支持，叙事性AsyncConfigurer接口（类上），点击[*这里*](http://mp.weixin.qq.com/s?__biz=MzI3ODcxMzQzMw==&mid=2247484241&idx=1&sn=2d0378b4842db91985f61c5388584b0c&chksm=eb538667dc240f71c1746f6dd74cc9b3d94a58868139c4a102a8bd794f821467dddb06b543b0&scene=21#wechat_redirect)了解使用详情。
>
>@Async 在实际执行的bean方法使用该注解来申明其是一个异步任务（方法上或类上*所有的方法都将异步*，需要@EnableAsync开启异步任务）
>
>



# 定时任务相关

>@EnableScheduling 在配置类上使用，开启计划任务的支持（类上）
>
>@Scheduled 来申明这是一个任务，包括cron,fixDelay,fixRate等类型（方法上，需先开启计划任务的支持）
>
>



# @Enable*注解说明

>这些注解主要用来开启对xxx的支持。 
>@EnableAspectJAutoProxy 开启对AspectJ自动代理的支持
>
>@EnableAsync 开启异步方法的支持
>
>@EnableScheduling 开启计划任务的支持
>
>@EnableWebMvc 开启Web MVC的配置支持
>
>@EnableConfigurationProperties 开启对@ConfigurationProperties注解配置Bean的支持
>
>@EnableJpaRepositories 开启对SpringData JPA Repository的支持
>
>@EnableTransactionManagement 开启注解式事务的支持
>
>@EnableTransactionManagement 开启注解式事务的支持
>
>@EnableCaching 开启注解式的缓存支持
>
>



# 测试相关注解

>@RunWith 运行器，Spring中通常用于对JUnit的支持
>
>@RunWith(SpringJUnit4ClassRunner.class)
>
>@ContextConfiguration 用来加载配置ApplicationContext，其中classes属性用来加载配置类
>
>@ContextConfiguration(classes={TestConfig.class})
>
>



# SpringMVC相关注解

> @EnableWebMvc 在配置类中开启Web MVC的配置支持，如一些ViewResolver或者MessageConverter等，若无此句，重写WebMvcConfigurerAdapter方法（用于对SpringMVC的配置）。
>
> @Controller 声明该类为SpringMVC中的Controller
>
> @RequestMapping 用于映射Web请求，包括访问路径和参数（类或方法上）
>
> @ResponseBody 支持将返回值放在response内，而不是一个页面，通常用户返回json数据（返回值旁或方法上）
>
> @RequestBody 允许request的参数在request体中，而不是在直接连接在地址后面。（放在参数前）
>
> @PathVariable 用于接收路径参数，比如@RequestMapping(“/hello/{name}”)申明的路径，将注解放在参数中前，即可获取该值，通常作为Restful的接口实现方法。
>
> @RestController 该注解为一个组合注解，相当于@Controller和@ResponseBody的组合，注解在类上，意味着，该Controller的所有方法都默认加上了@ResponseBody。
>
> @ControllerAdvice 通过该注解，我们可以将对于控制器的全局配置放置在同一个位置，注解了@Controller的类的方法可使用@ExceptionHandler、@InitBinder、@ModelAttribute注解到方法上， 
> 这对所有注解了 @RequestMapping的控制器内的方法有效。
>
> @ExceptionHandler 用于全局处理控制器里的异常
>
> @InitBinder 用来设置WebDataBinder，WebDataBinder用来自动绑定前台请求参数到Model中。
>
> @ModelAttribute 本来的作用是绑定键值对到Model里，在@ControllerAdvice中是让全局的@RequestMapping都能获得在此处设置的键值对。
>
> 



# spring 三种装配机制

>**隐式的自动装配bean**
>
>在**《Spring实战》**这本书中将自动装配分为了两个部分（组件扫描和自动装配）：
>**组件扫描**：Spring会自动发现应用上下文（Spring容器）中所创建的bean；
>**自动装配**：Spring自动满足bean之间的依赖
>
>**1、创建可被发现的bean**
>
>```java
>package soundsystem;
>public interface CompactDisc{
>    void play();
>}
>```
>
>创建带有@Component注解的CompactDisc接口的一个实现类，这个类会被Spring扫描到并自动创建bean
>
>```java
>package soundsystem;
>import ...
>
>@Component
>public class SgtPeppers implements CompactDisc{
>        private String title = "Sgt, Pepper's Lonely Hearts Club Band";
>        private String artist = "The Beatles";
>        public void play(){
>             System.out.println("Playing " + title + " By " + artist);
>        }
>}
>```
>
>使用@ComponentScan注解启动组件扫描，@ComponentScan 默认会扫描与配置类相同的包以及其下所有的子包，这样，被@Component注解修饰的类就会被发现
>
>```java
>package soundsystem;
>import ...
>
>@Configuration
>@ComponentScan
>public class CDPlayerConfig{}
>```
>
>也可以使用XML配置的方式来启动组件扫描
>
>```java
><?xml version="1.0" encoding="UTF-8"?>
><beans>
>        <context:component-scan base-package="soundsystem"/>
></beans>
>
>```
>
>**2、为组件扫描的 bean 命名**
>
>若直接使用 @Component 注解来声明一个 bean，bean 的名字默认为类名首字母小写。
>
>例如，如下 SgtPeppers 类的默认 bean 名称为 sgtPeppers
>
>```java
>@Component()
>public class SgtPeppers implements CompactDisc{
>    	...
>}
>```
>
>可以在 @Component 注解中说明此 bean 的名称：
>
>```java
>@Component("lonelyHeartClub")
>public class SgtPeppers implements CompactDisc{
>    	...
>}
>```
>
>此外，也可以使用另外一种为 bean 命名的方式：
>
>```java
>package soundsystem;
>import javax.inject.Named;
> 
>@Named("lonelyHeartClub")
>public class SgtPeppers implements CompactDisc{
>    	...
>}
>```
>
>Spring 支持将 @Named 作为 @Component 注解的替代方案，两者之间有一些细微的差异，但在大多数场景下，它们是可以相互替换的。
>
>推荐使用 @Component 注解，因为 @Named 注解并不能清楚的表明它是做什么的
>
>**3、设置组件扫描的基础包**
>
>在之前的案列中，我们没有为 @ComponentScan 注解设置任何属性，这意味着，按照默认规则，它会以配置类所在包作为基础包（ base  package ）来扫描组件.
>
>在之前的案列中，我们没有为 @ComponentScan 注解设置任何属性，这意味着，按照默认规则，它会以配置类所在包作为基础包（ base package ）来扫描组件.
>
>有一个原因会促使我们要明确的设置基础包，那就是我们想要将配置类放在单独的包中，使其与其他的应用代码区分开来。
>
>为了指定不同的包，只需要在 @ComponentScan 的 value 属性中指明包的名称：
>
>```java
>@Configuration
>@ComponentScan("soundsystem")
>public class CDPlayerConfig{}
>```
>
>或者，如果你想更加明确的表名你所设置的是基础包，那么你可以通过 basePackages 属性进行配置：
>
>```java
>@Configuration
>@ComponentScan(basePackages="soundsystem")
>public class CDPlayerConfig{}
>```
>
>如果你想扫描多个包，只需要将 basePackages 属性的值设置为要扫描包的一个数组即可：
>
>```java
>@Configuration
>@ComponentScan(basePackages={"soundsystem","video"})
>public class CDPlayerConfig{}
>```
>
>注意到，basePackages 属性的值是一个 String 类型的数组，这样配置没有问题，但却是不安全的，如果要重构代码的话，这些包的名字可能会被修改，从而导致包扫描出现错误，除了将包设置为简单的 String 类型之外，@ComponentScan 还提供了另一种方法，那就是将其指定为要扫描包中所含的类或接口。
>
>```java
>@Configuration
>@ComponentScan(basePackageClasses={CDPlayer.class, DVDPlayer.class})
>public class CDPlayerConfig{}
>```
>
>你可以在包中设置一个专门用来进行包扫描的空标记接口，这样，可以避免对任何实际应用的代码进行重构后，包扫描出现错误。
>
>**4、通过为 bean 添加注解实现自动装配**
>
>如果我们的应用程序所有对象都是独立的， 彼此之间没有任何依赖，那么仅仅使用Spring的扫描功能就算完事了,它会自动的帮我们把Java对象创建.但是如果对象与对象之间如果存在相互依赖的联系时,我们就需要用的Spring给我们提供的自动装配了.
>
>```java
>@Component
>public class CDPlayer implements MediaPlayer{
>        private CompactDisc cd;
>        @Autowired
>        public CDPlayer(CompacrDisc cd){
>             this.cd = cd;
>        }
>        public void play(){
>             cd.play();
>        }
>}
>```
>
>以上示例的构造器上添加了 @Autowired 注解，这表明当 Spring 创建 CDPlayer bean 的时候，会通过这个构造器进行实例化并传入一个 CompactDisc 类型的 bean。
>
>@Autowired 注解不仅能够用在构造器上，还可以用在属性设置的 Setter 方法上。
>
>实际上，Setter 方法并没有什么特殊之处，@Autowired 注解可以用在类的任何方法上：如下，@Autowired 注解完全能够发挥作用
>
>```java
>@Autowired
>public void insertDisc(CompactDisc cd){
>        this.cd = cd;
>}
>```
>
>不管是构造器、Setter 方法还是其他方法，Spring 都会尝试满足方法参数上所声明的依赖，假如有且仅有一个 bean 依赖需求的话，那么这个 bean 就会被装填进来。
>
>如果没有匹配的 bean，那么在应用上下文创建的时候，Spring 会抛出一个异常。为了避免异常的出现，你可以将 @Autowired 的 required 属性设置为 false：
>
>```java
>@Autowired(required=false)
>public CDPlayer(CompactDisc cd){
>        this.cd = cd;
>}
>```
>
>如果有多个 bean 都能满足依赖关系的话，Spring 也将会抛出一个异常，表明没有明确指定要选择那个 bean 进行装配。
>
>总结一下，自动装配bean的过程：
>
>> 一、把需要被扫描的类，添加 @Component注解，使它能够被Spring自动发现。
>> 二、通过显示的设置Java代码 @ComponentScan注解或XML配置，让Spring开启组件扫描，并将扫描的结果类创建bean。
>> 三、@Autowried注解能偶实现bean的自动装配，实现依赖注入。
>
>处理自动装配的歧义性问题，[Spring. 处理自动装配的歧义性](https://blog.csdn.net/qq_36420790/article/details/82762104)

>**通过java代码装配bean**
>
>

>**通XML中装配bean**
>
>

