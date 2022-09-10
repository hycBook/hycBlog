---
title: Java基础_打jar包
date: 2022/9/10 20:46:25
---

![img](res/other/异世界蕾姆_0.jpg)

[TOC]

***

# 详细步骤

## assembly.xml

```xml
<?xml version="1.0" encoding="UTF-8"?>
<assembly
        xmlns="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.3"
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        xsi:schemaLocation="http://maven.apache.org/plugins/maven-assembly-plugin/assembly/1.1.3 http://maven.apache.org/xsd/assembly-1.1.3.xsd">
    <id>test</id>
    <formats>
        <format>jar</format>
    </formats>
    <includeBaseDirectory>false</includeBaseDirectory>
    <fileSets>
        <!--将测试类和应用都打包进jar包-->
        <fileSet>
            <directory>${project.build.directory}/test-classes</directory>
            <outputDirectory>/</outputDirectory>
            <includes>
                <include>**/*.class</include>
                <include>**/*.properties</include>
                <include>**/*.xml</include>
            </includes>
            <useDefaultExcludes>false</useDefaultExcludes>
        </fileSet>

    </fileSets>
</assembly>
```

## pom.xml

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
         http://maven.apache.org/xsd/maven-4.0.0.xsd">

    <parent>
        <groupId>com.code.hyc</groupId>
        <artifactId>test</artifactId>
        <version>1.0</version>
    </parent>
    <modelVersion>4.0.0</modelVersion>

    <artifactId>hycCall</artifactId>
    <packaging>jar</packaging>

    <!--构建配置，不要删，需要的话打开-->
    <build>
        <plugins>
            <!--打成可执行jar包-->
            <plugin>
                <artifactId>maven-assembly-plugin</artifactId>
                <version>2.3</version>
                <configuration>
                    <descriptor>src/main/resources/assembly.xml</descriptor>
                </configuration>
                <executions>
                    <execution>
                        <id>make-assembly</id>
                        <phase>package</phase>
                        <goals>
                            <goal>single</goal>
                        </goals>
                        <configuration>
                            <archive>
                                <manifest>
                                    <!--该处设置为要执行的主类-->
                                    <mainClass>
                                        com.code.hyc.HycTest
                                    </mainClass>
                                </manifest>
                            </archive>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
            <!--依赖导出插件-->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-dependency-plugin</artifactId>
                <executions>
                    <execution>
                        <id>copy-dependencies</id>
                        <phase>package</phase>
                        <goals>
                            <goal>copy-dependencies</goal>
                        </goals>
                        <configuration>
                            <outputDirectory>${project.build.directory}/lib</outputDirectory>
                            <excludeTransitive>false</excludeTransitive>
                            <stripVersion>true</stripVersion>
                        </configuration>
                    </execution>
                </executions>
            </plugin>
        </plugins>
    </build>

</project>
```

## HycTest.java

```java
public class HycTest{
    public static void main(String[] args) throws Throwable {
        System.out.println("打包成功！");
    }
}
```

>执行maven->clean->package
>
>在target将hycCall.jar移动到lib文件夹下，此时lib文件夹和hycCal-testl.jar就是可以执行的jar包了



## 命令行

```shell
// 命令行debug模式(-Xms4G -Xmx8G -XX:PermSize=4G -XX:MaxPermSize=8G为指定内存大小)
java -Xdebug -Xrunjdwp:transport=dt_socket,address=5005,server=y,suspend=y -jar -Xms4G -Xmx8G -XX:PermSize=4G -XX:MaxPermSize=8G -Djava.ext.dirs=./lib mist-calculate-1.0-test.jar

// 后台执行模式(nohup xxx &)
nohup java -jar -Xms4G -Xmx8G -XX:PermSize=4G -XX:MaxPermSize=8G -Djava.ext.dirs=./lib mist-calculate-1.0-test.jar &

// 日志查看
tail -10f nohup.out

// 查看java命令的进程
ps -a | grep java

// 杀死指定线程号
kill -9  线程号
```







