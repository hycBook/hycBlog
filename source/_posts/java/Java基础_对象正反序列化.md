---
title: Java基础_对象正反序列化
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: 336a2a82
---

---

[TOC]


# 对象正反序列化

```java
import java.io.*;
import java.util.Base64;

/**
 * 对象编码工具类
 */
public class ObjEncodeUtil {
    public static String encodeBase64(Object object) {
        if (object == null) {
            return null;
        }
        ObjectOutputStream oos = null;
        String result;
        try {
            ByteArrayOutputStream bos = new ByteArrayOutputStream();
            oos = new ObjectOutputStream(bos);
            oos.writeObject(object);
            result = Base64.getEncoder().encodeToString(bos.toByteArray());
        } catch (IOException e) {
            throw new RuntimeException(e);
        } finally {
            try {
                if (oos != null) {
                    oos.close();
                }
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
        return result;
    }

    public static <T> T decodeBase64(String str) {
        ObjectInputStream ois = null;
        T result;
        try {
            ByteArrayInputStream bis = new ByteArrayInputStream(Base64.getDecoder().decode(str));
            ois = new ObjectInputStream(bis);
            result = (T) ois.readObject();
        } catch (IOException | ClassNotFoundException e) {
            throw new RuntimeException(e);
        } finally {
            if (ois != null) {
                try {
                    ois.close();
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
        }
        return result;
    }
}

class Bean{
        int length;
        double width;

        public Bean() {
        }

        public Bean(int length, double width) {
            this.length = length;
            this.width = width;
        }

        public int getLength() {
            return length;
        }

        public void setLength(int length) {
            this.length = length;
        }

        public double getWidth() {
            return width;
        }

        public void setWidth(double width) {
            this.width = width;
        }
    }

Bean bean = new Bean(5,3.2);
String modelStr = ObjEncodeUtil.encodeBase64(bean);
Bean bean2 = ObjEncodeUtil.decodeBase64(modelStr);

```

```java
import com.alibaba.fastjson.JSON;
ModelBean bean = new ModelBean();

String jsonResult = JSON.toJSONString(bean);
ModelBean bean2 = JSON.parseObject(jsonResult, ModelBean.class);

```
