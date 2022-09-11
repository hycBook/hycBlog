---
title: 多线程_JUC锁集合
date: '2022/9/10 20:46:25'
categories:
  - java
abbrlink: 10fd680e
---

![img](res/other/异世界蕾姆_1.png)

[TOC]

# JUC锁集合 

**同步锁**: 即通过synchronized关键字来进行同步，实现对竞争资源的互斥访问的锁。Java 1.0版本中就已经支持同步锁了。对于每一个对象，有且仅有一个同步锁；不同的线程能共同访问该同步锁。但是，在同一个时间点，该同步锁能且只能被一个线程获取到。这样，获取到同步锁的线程就能进行CPU调度，从而在CPU上执行；而没有获取到同步锁的线程，必须进行等待，直到获取到同步锁之后才能继续运行。这就是，多线程通过同步锁进行同步的原理！ 

**JUC包中的锁** : 相比同步锁，JUC包中的锁的功能更加强大，它为锁提供了一个框架，该框架允许更灵活地使用锁，只是它的用法更难罢了。

　　JUC包中的锁，包括：Lock接口，ReadWriteLock接口，LockSupport阻塞原语，Condition条件，AbstractOwnableSynchronizer/AbstractQueuedSynchronizer/AbstractQueuedLongSynchronizer三个抽象类，ReentrantLock独占锁，ReentrantReadWriteLock读写锁。由于CountDownLatch，CyclicBarrier和Semaphore也是通过AQS来实现的；

**Lock接口**: JUC包中的 Lock 接口支持那些语义不同(重入、公平等)的锁规则。所谓语义不同，是指锁可是有"公平机制的锁"、"非公平机制的锁"、"可重入的锁"等等。"公平机制"是指"不同线程获取锁的机制是公平的"，而"非公平机制"则是指"不同线程获取锁的机制是非公平的"，"可重入的锁"是指同一个锁能够被一个线程多次获取。

 **ReadWriteLock**: ReadWriteLock 接口以和Lock类似的方式定义了一些读取者可以共享而写入者独占的锁。JUC包只有一个类实现了该接口，即 ReentrantReadWriteLock，因为它适用于大部分的标准用法上下文。但程序员可以创建自己的、适用于非标准要求的实现。

 **AQS**: AbstractOwnableSynchronizer/AbstractQueuedSynchronizer/AbstractQueuedLongSynchronizer 　　AbstractQueuedSynchronizer就是被称之为AQS的类，它是一个非常有用的超类，可用来定义锁以及依赖于排队阻塞线程的其他同步器；ReentrantLock，ReentrantReadWriteLock，CountDownLatch，CyclicBarrier和Semaphore等这些类都是基于AQS类实现的。AbstractQueuedLongSynchronizer 类提供相同的功能但扩展了对同步状态的 64 位的支持。两者都扩展了类 AbstractOwnableSynchronizer（一个帮助记录当前保持独占同步的线程的简单类）。

**LockSupport**: LockSupport提供“创建锁”和“其他同步类的基本线程阻塞原语”。 
　　LockSupport的功能和"Thread中的Thread.suspend()和Thread.resume()有点类似"，LockSupport中的park() 和 unpark() 的作用分别是阻塞线程和解除阻塞线程。但是park()和unpark()不会遇到“Thread.suspend 和 Thread.resume所可能引发的死锁”问题。

 **Condition**: Condition需要和Lock联合使用，它的作用是代替Object监视器方法，可以通过await(),signal()来休眠/唤醒线程。
		Condition 接口描述了可能会与锁有关联的条件变量。这些变量在用法上与使用 Object.wait 访问的隐式监视器类似，但提供了更强大的功能。需要特别指出的是，单个 Lock 可能与多个 Condition 对象关联。为了避免兼容性问题，Condition 方法的名称与对应的 Object 版本中的不同。

 **ReentrantLock**: ReentrantLock是独占锁。所谓独占锁，是指只能被独自占领，即同一个时间点只能被一个线程锁获取到的锁。ReentrantLock锁包括"公平的ReentrantLock"和"非公平的ReentrantLock"。"公平的ReentrantLock"是指"不同线程获取锁的机制是公平的"，而"非公平的　　ReentrantLock"则是指"不同线程获取锁的机制是非公平的"，ReentrantLock是"可重入的锁"。

**ReentrantReadWriteLock**: ReentrantReadWriteLock是读写锁接口ReadWriteLock的实现类，它包括子类ReadLock和WriteLock。ReentrantLock是共享锁，而WriteLock是独占锁。

**CountDownLatch**: CountDownLatch是一个同步辅助类，在完成一组正在其他线程中执行的操作之前，它允许一个或多个线程一直等待。CountDownLatch包含了sync对象，sync是Sync类型。CountDownLatch的Sync是实例类，它继承于AQS。

**CyclicBarrier**: CyclicBarrier是一个同步辅助类，允许一组线程互相等待，直到到达某个公共屏障点 (common barrier point)。因为该 barrier 在释放等待线程后可以重用，所以称它为循环 的 barrier。

```java
CyclicBarrier是包含了"ReentrantLock对象lock"和"Condition对象trip"，它是通过独占锁实现的。
CyclicBarrier和CountDownLatch的区别**是：
(01) CountDownLatch的作用是允许1或N个线程等待其他线程完成执行；而CyclicBarrier则是允许N个线程相互等待。
(02) CountDownLatch的计数器无法被重置；CyclicBarrier的计数器可以被重置后使用，因此它被称为是循环的barrier。
```
**Semaphore**: Semaphore是一个计数信号量，它的本质是一个"共享锁"。
	　信号量维护了一个信号量许可集。线程可以通过调用acquire()来获取信号量的许可；当信号量中有可用的许可时，线程能获取该许可；否则线程必须等待，直到有可用的许可为止。 线程可以通过release()来释放它所持有的信号量许可。和"ReentrantLock"一样，Semaphore包含了sync对象，sync是Sync类型；而且，Sync也是一个继承于AQS的抽象类。Sync也包括"公平信号量"FairSync和"非公平信号量"NonfairSync。

# 互斥锁ReentrantLock 

ReentrantLock是一个可重入的互斥锁，又被称为“独占锁”。

```java
顾名思义，ReentrantLock锁在同一个时间点只能被一个线程锁持有；而可重入的意思是，ReentrantLock锁，可以被单个线程多次获取。
ReentrantLock分为“公平锁”和“非公平锁”。它们的区别体现在获取锁的机制上是否公平。“锁”是为了保护竞争资源，防止多个线程同时操作线程而出错，ReentrantLock在同一个时间点只能被一个线程获取(当某线程获取到“锁”时，其它线程就必须等待)；ReentraantLock是通过一个FIFO的等待队列来管理获取该锁所有线程的。在“公平锁”的机制下，线程依次排队获取锁；而“非公平锁”在锁是可获取状态时，不管自己是不是在队列的开头都会获取锁。
```

```java
// ReentrantLock函数列表
// 创建一个 ReentrantLock ，默认是“非公平锁”。
ReentrantLock()
// 创建策略是fair的 ReentrantLock。fair为true表示是公平锁，fair为false表示是非公平锁。
ReentrantLock(boolean fair)
// 查询当前线程保持此锁的次数。
int getHoldCount()
// 返回目前拥有此锁的线程，如果此锁不被任何线程拥有，则返回 null。
protected Thread getOwner()
// 返回一个 collection，它包含可能正等待获取此锁的线程。
protected Collection<Thread> getQueuedThreads()
// 返回正等待获取此锁的线程估计数。
int getQueueLength()
// 返回一个 collection，它包含可能正在等待与此锁相关给定条件的那些线程。
protected Collection<Thread> getWaitingThreads(Condition condition)
// 返回等待与此锁相关的给定条件的线程估计数。
int getWaitQueueLength(Condition condition)
// 查询给定线程是否正在等待获取此锁。
boolean hasQueuedThread(Thread thread)
// 查询是否有些线程正在等待获取此锁。
boolean hasQueuedThreads()
// 查询是否有些线程正在等待与此锁有关的给定条件。
boolean hasWaiters(Condition condition)
// 如果是“公平锁”返回true，否则返回false。
boolean isFair()
// 查询当前线程是否保持此锁。
boolean isHeldByCurrentThread()
// 查询此锁是否由任意线程保持。
boolean isLocked()
// 获取锁。
void lock()
// 如果当前线程未被中断，则获取锁。
void lockInterruptibly()
// 返回用来与此 Lock 实例一起使用的 Condition 实例。
Condition newCondition()
// 仅在调用时锁未被另一个线程保持的情况下，才获取该锁。
boolean tryLock()
// 如果锁在给定等待时间内没有被另一个线程保持，且当前线程未被中断，则获取该锁。
boolean tryLock(long timeout, TimeUnit unit)
// 试图释放此锁。
void unlock()
```



```java
// ReentrantLock示例

import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;

// LockTest1.java
// 仓库
class Depot { 
    private int size;        // 仓库的实际数量
    private Lock lock;        // 独占锁

    public Depot() {
        this.size = 0;
        this.lock = new ReentrantLock();
    }

    public void produce(int val) {
        lock.lock();
        try {
            size += val;
            System.out.printf("%s produce(%d) --> size=%d\n", 
                    Thread.currentThread().getName(), val, size);
        } finally {
            lock.unlock();
        }
    }

    public void consume(int val) {
        lock.lock();
        try {
            size -= val;
            System.out.printf("%s consume(%d) <-- size=%d\n", 
                    Thread.currentThread().getName(), val, size);
        } finally {
            lock.unlock();
        }
    }
}; 

// 生产者
class Producer {
    private Depot depot;
    
    public Producer(Depot depot) {
        this.depot = depot;
    }

    // 消费产品：新建一个线程向仓库中生产产品。
    public void produce(final int val) {
        new Thread() {
            public void run() {
                depot.produce(val);
            }
        }.start();
    }
}

// 消费者
class Customer {
    private Depot depot;
    
    public Customer(Depot depot) {
        this.depot = depot;
    }

    // 消费产品：新建一个线程从仓库中消费产品。
    public void consume(final int val) {
        new Thread() {
            public void run() {
                depot.consume(val);
            }
        }.start();
    }
}

public class LockTest1 {  
    public static void main(String[] args) {  
        Depot mDepot = new Depot();
        Producer mPro = new Producer(mDepot);
        Customer mCus = new Customer(mDepot);

        mPro.produce(60);
        mPro.produce(120);
        mCus.consume(90);
        mCus.consume(150);
        mPro.produce(110);
    }
}


Thread-0 produce(60) --> size=60
Thread-1 produce(120) --> size=180
Thread-3 consume(150) <-- size=30
Thread-2 consume(90) <-- size=-60
Thread-4 produce(110) --> size=50

结果分析：
(01) Depot 是个仓库。通过produce()能往仓库中生产货物，通过consume()能消费仓库中的货物。通过独占锁lock实现对仓库的互斥访问：在操作(生产/消费)仓库中货品前，会先通过lock()锁住仓库，操作完之后再通过unlock()解锁。
(02) Producer是生产者类。调用Producer中的produce()函数可以新建一个线程往仓库中生产产品。
(03) Customer是消费者类。调用Customer中的consume()函数可以新建一个线程消费仓库中的产品。
(04) 在主线程main中，我们会新建1个生产者mPro，同时新建1个消费者mCus。它们分别向仓库中生产/消费产品。
根据main中的生产/消费数量，仓库最终剩余的产品应该是50。运行结果是符合我们预期的！

这个模型存在两个问题：
(01) 现实中，仓库的容量不可能为负数。但是，此模型中的仓库容量可以为负数，这与现实相矛盾！
(02) 现实中，仓库的容量是有限制的。但是，此模型中的容量确实没有限制的！
这两个问题，我们稍微会讲到如何解决。现在，先看个简单的示例2；通过对比“示例1”和“示例2”,我们能更清晰的认识lock(),unlock()的用途。

```

```java
// 在“示例2”中，我们通过Condition去解决“示例1”中的两个问题：
// “仓库的容量不可能为负数”
// “仓库的容量是有限制的”。
// 解决该问题是通过Condition。Condition是需要和Lock联合使用的：通过Condition中的await()方法，能让线程阻塞[类似于wait()]；通过Condition的signal()方法，能让唤醒线程[类似于notify()]。
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.ReentrantLock;
import java.util.concurrent.locks.Condition;

// LockTest3.java
// 仓库
class Depot {
    private int capacity;    // 仓库的容量
    private int size;        // 仓库的实际数量
    private Lock lock;        // 独占锁
    private Condition fullCondtion;            // 生产条件
    private Condition emptyCondtion;        // 消费条件

    public Depot(int capacity) {
        this.capacity = capacity;
        this.size = 0;
        this.lock = new ReentrantLock();
        this.fullCondtion = lock.newCondition();
        this.emptyCondtion = lock.newCondition();
    }

    public void produce(int val) {
        lock.lock();
        try {
             // left 表示“想要生产的数量”(有可能生产量太多，需多此生产)
            int left = val;
            while (left > 0) {
                // 库存已满时，等待“消费者”消费产品。
                while (size >= capacity)
                    fullCondtion.await();
                // 获取“实际生产的数量”(即库存中新增的数量)
                // 如果“库存”+“想要生产的数量”>“总的容量”，则“实际增量”=“总的容量”-“当前容量”。(此时填满仓库)
                // 否则“实际增量”=“想要生产的数量”
                int inc = (size+left)>capacity ? (capacity-size) : left;
                size += inc;
                left -= inc;
                System.out.printf("%s produce(%3d) --> left=%3d, inc=%3d, size=%3d\n", 
                        Thread.currentThread().getName(), val, left, inc, size);
                // 通知“消费者”可以消费了。
                emptyCondtion.signal();
            }
        } catch (InterruptedException e) {
        } finally {
            lock.unlock();
        }
    }

    public void consume(int val) {
        lock.lock();
        try {
            // left 表示“客户要消费数量”(有可能消费量太大，库存不够，需多此消费)
            int left = val;
            while (left > 0) {
                // 库存为0时，等待“生产者”生产产品。
                while (size <= 0)
                    emptyCondtion.await();
                // 获取“实际消费的数量”(即库存中实际减少的数量)
                // 如果“库存”<“客户要消费的数量”，则“实际消费量”=“库存”；
                // 否则，“实际消费量”=“客户要消费的数量”。
                int dec = (size<left) ? size : left;
                size -= dec;
                left -= dec;
                System.out.printf("%s consume(%3d) <-- left=%3d, dec=%3d, size=%3d\n", 
                        Thread.currentThread().getName(), val, left, dec, size);
                fullCondtion.signal();
            }
        } catch (InterruptedException e) {
        } finally {
            lock.unlock();
        }
    }

    public String toString() {
        return "capacity:"+capacity+", actual size:"+size;
    }
}; 

// 生产者
class Producer {
    private Depot depot;
    
    public Producer(Depot depot) {
        this.depot = depot;
    }

    // 消费产品：新建一个线程向仓库中生产产品。
    public void produce(final int val) {
        new Thread() {
            public void run() {
                depot.produce(val);
            }
        }.start();
    }
}

// 消费者
class Customer {
    private Depot depot;
    
    public Customer(Depot depot) {
        this.depot = depot;
    }

    // 消费产品：新建一个线程从仓库中消费产品。
    public void consume(final int val) {
        new Thread() {
            public void run() {
                depot.consume(val);
            }
        }.start();
    }
}

public class LockTest3 {  
    public static void main(String[] args) {  
        Depot mDepot = new Depot(100);
        Producer mPro = new Producer(mDepot);
        Customer mCus = new Customer(mDepot);

        mPro.produce(60);
        mPro.produce(120);
        mCus.consume(90);
        mCus.consume(150);
        mPro.produce(110);
    }
}

Thread-0 produce( 60) --> left=  0, inc= 60, size= 60
Thread-1 produce(120) --> left= 80, inc= 40, size=100
Thread-2 consume( 90) <-- left=  0, dec= 90, size= 10
Thread-3 consume(150) <-- left=140, dec= 10, size=  0
Thread-4 produce(110) --> left= 10, inc=100, size=100
Thread-3 consume(150) <-- left= 40, dec=100, size=  0
Thread-4 produce(110) --> left=  0, inc= 10, size= 10
Thread-3 consume(150) <-- left= 30, dec= 10, size=  0
Thread-1 produce(120) --> left=  0, inc= 80, size= 80
Thread-3 consume(150) <-- left=  0, dec= 30, size= 50
```

# 公平锁

**基本概念**:

* **AQS**  -- 指AbstractQueuedSynchronizer类。
  AQS是java中管理“锁”的抽象类，锁的许多公共方法都是在这个类中实现。AQS是独占锁(例如，ReentrantLock)和共享锁(例如，Semaphore)的公共父类。

* AQS**锁的类别** -- 分为“独占锁”和“共享锁”两种。
  (01) 独占锁 -- 锁在一个时间点只能被一个线程锁占有。根据锁的获取机制，它又划分为“公平锁”和“非公平锁”。公平锁，是按照通过CLH等待线程按照先来先得的规则，公平的获取锁；而非公平锁，则当线程要获取锁时，它会无视CLH等待队列而直接获取锁。独占锁的典型实例子是ReentrantLock，此外，ReentrantReadWriteLock.WriteLock也是独占锁。
  (02) 共享锁 -- 能被多个线程同时拥有，能被共享的锁。JUC包中的ReentrantReadWriteLock.ReadLock，CyclicBarrier， CountDownLatch和Semaphore都是共享锁。这些锁的用途和原理，在以后的章节再详细介绍。

* **CLH队列** -- Craig, Landin, and Hagersten lock queue
  CLH队列是AQS中“等待锁”的线程队列。在多线程中，为了保护竞争资源不被多个线程同时操作而起来错误，我们常常需要通过锁来保护这些资源。在独占锁中，竞争资源在一个时间点只能被一个线程锁访问；而其它线程则需要等待。CLH就是管理这些“等待锁”的线程的队列。
  CLH是一个非阻塞的 FIFO 队列。也就是说往里面插入或移除一个节点的时候，在并发条件下不会阻塞，而是通过自旋锁和 CAS 保证节点插入和移除的原子性。

* **CAS函数** -- Compare And Swap 
  CAS函数，是比较并交换函数，它是原子操作函数；即，通过CAS操作的数据都是以原子方式进行的。例如，compareAndSetHead(), compareAndSetTail(), compareAndSetNext()等函数。它们共同的特点是，这些函数所执行的动作是以原子的方式进行的。

## 获取公平锁

```java
1. lock()
lock()在ReentrantLock.java的FairSync类中实现
说明：“当前线程”实际上是通过acquire(1)获取锁的。
	这里说明一下“1”的含义，它是设置“锁的状态”的参数。对于“独占锁”而言，锁处于可获取状态时，它的状态值是0；锁被线程初次获取到了，它的状态值就变成了1。
	由于ReentrantLock(公平锁/非公平锁)是可重入锁，所以“独占锁”可以被单个线程多此获取，每获取1次就将锁的状态+1。也就是说，初次获取锁时，通过acquire(1)将锁的状态值设为1；再次获取锁时，将锁的状态值设为2；依次类推...这就是为什么获取锁时，传入的参数是1的原因了。
	可重入就是指锁可以被单个线程多次获取。
        
2. acquire()
acquire()在AQS中实现的
(01) “当前线程”首先通过tryAcquire()尝试获取锁。获取成功的话，直接返回；尝试失败的话，进入到等待队列排序等待(前面还有可能有需要线程在等待该锁)。
(02) “当前线程”尝试失败的情况下，先通过addWaiter(Node.EXCLUSIVE)来将“当前线程”加入到"CLH队列(非阻塞的FIFO队列)"末尾。CLH队列就是线程等待队列。
(03) 再执行完addWaiter(Node.EXCLUSIVE)之后，会调用acquireQueued()来获取锁。由于此时ReentrantLock是公平锁，它会根据公平性原则来获取锁。
(04) “当前线程”在执行acquireQueued()时，会进入到CLH队列中休眠等待，直到获取锁了才返回！如果“当前线程”在休眠等待过程中被中断过，acquireQueued会返回true，此时"当前线程"会调用selfInterrupt()来自己给自己产生一个中断。
```

## tryAcquire()

```java
1. tryAcquire()
说明：根据代码，我们可以分析出，tryAcquire()的作用就是尝试去获取锁。注意，这里只是尝试！
	尝试成功的话，返回true；尝试失败的话，返回false，后续再通过其它办法来获取该锁。后面我们会说明，在尝试失败的情况下，是如何一步步获取锁的。
	
2. hasQueuedPredecessors()
说明：通过代码，能分析出，hasQueuedPredecessors() 是通过判断"当前线程"是不是在CLH队列的队首，来返回AQS中是不是有比“当前线程”等待更久的线程。下面对head、tail和Node进行说明。

3. Node的源码
说明：Node是CLH队列的节点，代表“等待锁的线程队列”。
(01) 每个Node都会一个线程对应。
(02) 每个Node会通过prev和next分别指向上一个节点和下一个节点，这分别代表上一个等待线程和下一个等待线程。
(03) Node通过waitStatus保存线程的等待状态。
(04) Node通过nextWaiter来区分线程是“独占锁”线程还是“共享锁”线程。如果是“独占锁”线程，则nextWaiter的值为EXCLUSIVE；如果是“共享锁”线程，则nextWaiter的值是SHARED。

4. compareAndSetState()
说明： compareAndSwapInt() 是sun.misc.Unsafe类中的一个本地方法。对此，我们需要了解的是 compareAndSetState(expect, update) 是以原子的方式操作当前线程；若当前线程的状态为expect，则设置它的状态为update。

5. setExclusiveOwnerThread()
说明：setExclusiveOwnerThread()的作用就是，设置线程t为当前拥有“独占锁”的线程

6. getState(), setState()
说明：state表示锁的状态，对于“独占锁”而已，state=0表示锁是可获取状态(即，锁没有被任何线程锁持有)。由于java中的独占锁是可重入的，state的值可以>1。
```

## addWaiter(Node.EXCLUSIVE)

```java
addWaiter(Node.EXCLUSIVE)的作用是，创建“当前线程”的Node节点，且Node中记录“当前线程”对应的锁是“独占锁”类型，并且将该节点添加到CLH队列的末尾。

1.addWaiter()
说明：对于“公平锁”而言，addWaiter(Node.EXCLUSIVE)会首先创建一个Node节点，节点的类型是“独占锁”(Node.EXCLUSIVE)类型。然后，再将该节点添加到CLH队列的末尾。

2. compareAndSetTail()
说明：compareAndSetTail也属于CAS函数，也是通过“本地方法”实现的。compareAndSetTail(expect, update)会以原子的方式进行操作，它的作用是判断CLH队列的队尾是不是为expect，是的话，就将队尾设为update。

3. enq()
说明： enq()的作用很简单。如果CLH队列为空，则新建一个CLH表头；然后将node添加到CLH末尾。否则，直接将node添加到CLH末尾。

小结：addWaiter()的作用，就是将当前线程添加到CLH队列中。这就意味着将当前线程添加到等待获取“锁”的等待线程队列中了。
```

## acquireQueued()

```java
acquireQueued()的作用就是逐步的去执行CLH队列的线程，如果当前线程获取到了锁，则返回；否则，当前线程进行休眠，直到唤醒并重新获取锁了才返回。

1. acquireQueued()
说明：acquireQueued()的目的是从队列中获取锁。

2. shouldParkAfterFailedAcquire()
说明：
(01) 关于waitStatus请参考下表(中扩号内为waitStatus的值)，更多关于waitStatus的内容，可以参考前面的Node类的介绍。
    CANCELLED[1]  -- 当前线程已被取消
    SIGNAL[-1]    -- “当前线程的后继线程需要被unpark(唤醒)”。一般发生情况是：当前线程的后继线程处于阻塞状态，而当前线程被release或cancel掉，因此需要唤醒当前线程的后继线程。
    CONDITION[-2] -- 当前线程(处在Condition休眠状态)在等待Condition唤醒
    PROPAGATE[-3] -- (共享锁)其它线程获取到“共享锁”
    [0]           -- 当前线程不属于上面的任何一种状态。
(02) shouldParkAfterFailedAcquire()通过以下规则，判断“当前线程”是否需要被阻塞。
    规则1：如果前继节点状态为SIGNAL，表明当前节点需要被unpark(唤醒)，此时则返回true。
    规则2：如果前继节点状态为CANCELLED(ws>0)，说明前继节点已经被取消，则通过先前回溯找到一个有效(非CANCELLED状态)的节点，并返回false。
    规则3：如果前继节点状态为非SIGNAL、非CANCELLED，则设置前继的状态为SIGNAL，并返回false。
如果“规则1”发生，即“前继节点是SIGNAL”状态，则意味着“当前线程”需要被阻塞。接下来会调用parkAndCheckInterrupt()阻塞当前线程，直到当前先被唤醒才从parkAndCheckInterrupt()中返回。

3. parkAndCheckInterrupt())
说明：parkAndCheckInterrupt()的作用是阻塞当前线程，并且返回“线程被唤醒之后”的中断状态。
它会先通过LockSupport.park()阻塞“当前线程”，然后通过Thread.interrupted()返回线程的中断状态。

这里介绍一下线程被阻塞之后如何唤醒。一般有2种情况：
第1种情况：unpark()唤醒。“前继节点对应的线程”使用完锁之后，通过unpark()方式唤醒当前线程。
第2种情况：中断唤醒。其它线程通过interrupt()中断当前线程。

补充：LockSupport()中的park(),unpark()的作用 和 Object中的wait(),notify()作用类似，是阻塞/唤醒。
它们的用法不同，park(),unpark()是轻量级的，而wait(),notify()是必须先通过Synchronized获取同步锁。

4. 再次tryAcquire()
说明：
(01) 通过node.predecessor()获取前继节点。predecessor()就是返回node的前继节点，若对此有疑惑可以查看下面关于Node类的介绍。
(02) p == head && tryAcquire(arg)
首先，判断“前继节点”是不是CHL表头。如果是的话，则通过tryAcquire()尝试获取锁。
其实，这样做的目的是为了“让当前线程获取锁”，但是为什么需要先判断p==head呢？理解这个对理解“公平锁”的机制很重要，因为这么做的原因就是为了保证公平性！
	(a) 前面，我们在shouldParkAfterFailedAcquire()我们判断“当前线程”是否需要阻塞；
	(b) 接着，“当前线程”阻塞的话，会调用parkAndCheckInterrupt()来阻塞线程。当线程被解除阻塞的时候，我们会返回线程的中断状态。而线程被解决阻塞，可能是由于“线程被中断”，也可能是由于“其它线程调用了该线程的unpark()函数”。
	(c) 再回到p==head这里。如果当前线程是因为其它线程调用了unpark()函数而被唤醒，那么唤醒它的线程，应该是它的前继节点所对应的线程(关于这一点，后面在“释放锁”的过程中会看到)。 OK，是前继节点调用unpark()唤醒了当前线程！
此时，再来理解p==head就很简单了：当前继节点是CLH队列的头节点，并且它释放锁之后；就轮到当前节点获取锁了。然后，当前节点通过tryAcquire()获取锁；获取成功的话，通过setHead(node)设置当前节点为头节点，并返回。
	总之，如果“前继节点调用unpark()唤醒了当前线程”并且“前继节点是CLH表头”，此时就是满足p==head，也就是符合公平性原则的。否则，如果当前线程是因为“线程被中断”而唤醒，那么显然就不是公平了。这就是为什么说p==head就是保证公平性！

小结：acquireQueued()的作用就是“当前线程”会根据公平性原则进行阻塞等待，直到获取锁为止；并且返回当前线程在等待过程中有没有并中断过。
```

## selfInterrupt()

```java
private static void selfInterrupt() {
    Thread.currentThread().interrupt();
}

说明：selfInterrupt()的代码很简单，就是“当前线程”自己产生一个中断。但是，为什么需要这么做呢？
这必须结合acquireQueued()进行分析。如果在acquireQueued()中，当前线程被中断过，则执行selfInterrupt()；否则不会执行。

在acquireQueued()中，即使是线程在阻塞状态被中断唤醒而获取到cpu执行权利；但是，如果该线程的前面还有其它等待锁的线程，根据公平性原则，该线程依然无法获取到锁。它会再次阻塞！ 该线程再次阻塞，直到该线程被它的前面等待锁的线程锁唤醒；线程才会获取锁，然后“真正执行起来”！
也就是说，在该线程“成功获取锁并真正执行起来”之前，它的中断会被忽略并且中断标记会被清除！ 因为在parkAndCheckInterrupt()中，我们线程的中断状态时调用了Thread.interrupted()。该函数不同于Thread的isInterrupted()函数，isInterrupted()仅仅返回中断状态，而interrupted()在返回当前中断状态之后，还会清除中断状态。 正因为之前的中断状态被清除了，所以这里需要调用selfInterrupt()重新产生一个中断！
小结：selfInterrupt()的作用就是当前线程自己产生一个中断。

总结:
再回过头看看acquire()函数，它最终的目的是获取锁！
public final void acquire(int arg) {
    if (!tryAcquire(arg) &&
        acquireQueued(addWaiter(Node.EXCLUSIVE), arg))
        selfInterrupt();
}
(01) 先是通过tryAcquire()尝试获取锁。获取成功的话，直接返回；尝试失败的话，再通过acquireQueued()获取锁。
(02) 尝试失败的情况下，会先通过addWaiter()来将“当前线程”加入到"CLH队列"末尾；然后调用acquireQueued()，在CLH队列中排序等待获取锁，在此过程中，线程处于休眠状态。直到获取锁了才返回。 如果在休眠等待过程中被中断过，则调用selfInterrupt()来自己产生一个中断。
```

## 释放公平锁

```java
1. unlock()
说明：unlock()是解锁函数，它是通过AQS的release()函数来实现的。
在这里，“1”的含义和“获取锁的函数acquire(1)的含义”一样，它是设置“释放锁的状态”的参数。由于“公平锁”是可重入的，所以对于同一个线程，每释放锁一次，锁的状态-1。

2. release()
说明：release()会先调用tryRelease()来尝试释放当前线程锁持有的锁。成功的话，则唤醒后继等待线程，并返回true。否则，直接返回false。

3. tryRelease()
说明：tryRelease()的作用是尝试释放锁。
(01) 如果“当前线程”不是“锁的持有者”，则抛出异常。
(02) 如果“当前线程”在本次释放锁操作之后，对锁的拥有状态是0(即，当前线程彻底释放该“锁”)，则设置“锁”的持有者为null，即锁是可获取状态。同时，更新当前线程的锁的状态为0。

4. unparkSuccessor()
在release()中“当前线程”释放锁成功的话，会唤醒当前线程的后继线程。
根据CLH队列的FIFO规则，“当前线程”(即已经获取锁的线程)肯定是head；如果CLH队列非空的话，则唤醒锁的下一个等待线程。
说明：unparkSuccessor()的作用是“唤醒当前线程的后继线程”。后继线程被唤醒之后，就可以获取该锁并恢复运行了。
关

总结: “释放锁”的过程相对“获取锁”的过程比较简单。释放锁时，主要进行的操作，是更新当前线程对应的锁的状态。如果当前线程对锁已经彻底释放，则设置“锁”的持有线程为null，设置当前线程的状态为空，然后唤醒后继线程。
```

# 非公平锁

## 获取非公平锁

```java
非公平锁和公平锁在获取锁的方法上，流程是一样的；它们的区别主要表现在“尝试获取锁的机制不同”。简单点说，“公平锁”在每次尝试获取锁时，都是采用公平策略(根据等待队列依次排序等待)；而“非公平锁”在每次尝试获取锁时，都是采用的非公平策略(无视等待队列，直接尝试获取锁，如果锁是空闲的，即可获取状态，则获取锁)。
```

```java
1. lock()
说明：lock()会先通过compareAndSet(0, 1)来判断“锁”是不是空闲状态。是的话，“当前线程”直接获取“锁”；否则的话，调用acquire(1)获取锁。
(01) compareAndSetState()是CAS函数，它的作用是比较并设置当前锁的状态。若锁的状态值为0，则设置锁的状态值为1。
(02) setExclusiveOwnerThread(Thread.currentThread())的作用是，设置“当前线程”为“锁”的持有者。

“公平锁”和“非公平锁”关于lock()的对比
公平锁   -- 公平锁的lock()函数，会直接调用acquire(1)。
非公平锁 -- 非公平锁会先判断当前锁的状态是不是空闲，是的话，就不排队，而是直接获取锁。


2. acquire()
(01) “当前线程”首先通过tryAcquire()尝试获取锁。获取成功的话，直接返回；尝试失败的话，进入到等待队列依次排序，然后获取锁。
(02) “当前线程”尝试失败的情况下，会先通过addWaiter(Node.EXCLUSIVE)来将“当前线程”加入到"CLH队列(非阻塞的FIFO队列)"末尾。
(03) 然后，调用acquireQueued()获取锁。在acquireQueued()中，当前线程会等待它在“CLH队列”中前面的所有线程执行并释放锁之后，才能获取锁并返回。如果“当前线程”在休眠等待过程中被中断过，则调用selfInterrupt()来自己产生一个中断。

“公平锁”和“非公平锁”关于acquire()的对比
公平锁和非公平锁，只有tryAcquire()函数的实现不同；即它们尝试获取锁的机制不同。这就是我们所说的“它们获取锁策略的不同所在之处”！
在“Java多线程系列--“JUC锁”03之 公平锁(一)”中，已经详细介绍了acquire()涉及到的各个函数。这里仅对它们有差异的函数tryAcquire()进行说明。
    
说明：
根据代码，我们可以分析出，tryAcquire()的作用就是尝试去获取锁。
(01) 如果“锁”没有被任何线程拥有，则通过CAS函数设置“锁”的状态为acquires，同时，设置“当前线程”为锁的持有者，然后返回true。
(02) 如果“锁”的持有者已经是当前线程，则将更新锁的状态即可。
(03) 如果不术语上面的两种情况，则认为尝试失败。

“公平锁”和“非公平锁”关于tryAcquire()的对比
公平锁和非公平锁，它们尝试获取锁的方式不同。
公平锁在尝试获取锁时，即使“锁”没有被任何线程锁持有，它也会判断自己是不是CLH等待队列的表头；是的话，才获取锁。
而非公平锁在尝试获取锁时，如果“锁”没有被任何线程持有，则不管它在CLH队列的何处，它都直接获取锁。 
```

## 释放非公平锁

```java
非公平锁和公平锁在释放锁的方法和策略上是一样的。
```

# Condition条件

Condition的作用是对锁进行更精确的控制。Condition中的await()方法相当于Object的wait()方法，Condition中的signal()方法相当于Object的notify()方法，Condition中的signalAll()相当于Object的notifyAll()方法。不同的是，Object中的wait(),notify(),notifyAll()方法是和"同步锁"(synchronized关键字)捆绑使用的；而Condition是需要与"互斥锁"/"共享锁"捆绑使用的。

```java
// Condition函数列表
// 造成当前线程在接到信号或被中断之前一直处于等待状态。
void await()
// 造成当前线程在接到信号、被中断或到达指定等待时间之前一直处于等待状态。
boolean await(long time, TimeUnit unit)
// 造成当前线程在接到信号、被中断或到达指定等待时间之前一直处于等待状态。
long awaitNanos(long nanosTimeout)
// 造成当前线程在接到信号之前一直处于等待状态。
void awaitUninterruptibly()
// 造成当前线程在接到信号、被中断或到达指定最后期限之前一直处于等待状态。
boolean awaitUntil(Date deadline)
// 唤醒一个等待线程。
void signal()
// 唤醒所有等待线程。
void signalAll()
```

## Condition示例

```java
// 示例1是通过Object的wait(), notify()来演示线程的休眠/唤醒功能。
public class WaitTest1 {
    public static void main(String[] args) {
        ThreadA ta = new ThreadA("ta");
        synchronized(ta) { // 通过synchronized(ta)获取“对象ta的同步锁”
            try {
       System.out.println(Thread.currentThread().getName()+" start ta");
                ta.start();
                System.out.println(Thread.currentThread().getName()+" block");
                ta.wait();    // 等待
                System.out.println(Thread.currentThread().getName()+" continue");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    static class ThreadA extends Thread{
        public ThreadA(String name) {
            super(name);
        }
        public void run() {
            synchronized (this) { // 通过synchronized(this)获取“当前对象的同步锁”
                System.out.println(Thread.currentThread().getName()+" wakup others");
                notify();    // 唤醒“当前对象上的等待线程”
            }
        }
    }
}
```

```java
// 示例2是通过Condition的await(), signal()来演示线程的休眠/唤醒功能。
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
public class ConditionTest1 {
    private static Lock lock = new ReentrantLock();
    private static Condition condition = lock.newCondition();
    public static void main(String[] args) {
        ThreadA ta = new ThreadA("ta");
        lock.lock(); // 获取锁
        try {
            System.out.println(Thread.currentThread().getName()+" start ta");
            ta.start();
            System.out.println(Thread.currentThread().getName()+" block");
            condition.await();    // 等待
            System.out.println(Thread.currentThread().getName()+" continue");
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            lock.unlock();    // 释放锁
        }
    }

    static class ThreadA extends Thread{
        public ThreadA(String name) {
            super(name);
        }
        public void run() {
            lock.lock();    // 获取锁
            try {
                System.out.println(Thread.currentThread().getName()+" wakup others");
                condition.signal();    // 唤醒“condition所在锁上的其它线程”
            } finally {
                lock.unlock();    // 释放锁
            }
        }
    }
}

运行结果：
main start ta
main block
ta wakup others
main continue
通过“示例1”和“示例2”，我们知道Condition和Object的方法有一下对应关系：
              Object      Condition  
休眠          wait        await
唤醒个线程     notify      signal
唤醒所有线程   notifyAll   signalAll

Condition除了支持上面的功能之外，它更强大的地方在于：能够更加精细的控制多线程的休眠与唤醒。对于同一个锁，我们可以创建多个Condition，在不同的情况下使用不同的Condition。
例如，假如多线程读/写同一个缓冲区：当向缓冲区中写入数据之后，唤醒"读线程"；当从缓冲区读出数据之后，唤醒"写线程"；并且当缓冲区满的时候，"写线程"需要等待；当缓冲区为空时，"读线程"需要等待。
如果采用Object类中的wait(), notify(), notifyAll()实现该缓冲区，当向缓冲区写入数据之后需要唤醒"读线程"时，不可能通过notify()或notifyAll()明确的指定唤醒"读线程"，而只能通过notifyAll唤醒所有线程(但是notifyAll无法区分唤醒的线程是读线程，还是写线程)。  但是，通过Condition，就能明确的指定唤醒读线程。
看看下面的示例3，可能对这个概念有更深刻的理解。
```

```java
// 示例3是通过Condition的高级功能。
import java.util.concurrent.locks.Lock;
import java.util.concurrent.locks.Condition;
import java.util.concurrent.locks.ReentrantLock;
class BoundedBuffer {
    final Lock lock = new ReentrantLock();
    final Condition notFull  = lock.newCondition(); 
    final Condition notEmpty = lock.newCondition(); 
    final Object[] items = new Object[5];
    int putptr, takeptr, count;
    public void put(Object x) throws InterruptedException {
        lock.lock();    //获取锁
        try {
            // 如果“缓冲已满”，则等待；直到“缓冲”不是满的，才将x添加到缓冲中。
            while (count == items.length)
                notFull.await();
            // 将x添加到缓冲中
            items[putptr] = x; 
            // 将“put统计数putptr+1”；如果“缓冲已满”，则设putptr为0。
            if (++putptr == items.length) putptr = 0;
            // 将“缓冲”数量+1
            ++count;
            // 唤醒take线程，因为take线程通过notEmpty.await()等待
            notEmpty.signal();
            // 打印写入的数据
            System.out.println(Thread.currentThread().getName() + " put  "+ (Integer)x);
        } finally {
            lock.unlock();    // 释放锁
        }
    }
    public Object take() throws InterruptedException {
        lock.lock();    //获取锁
        try {
            // 如果“缓冲为空”，则等待；直到“缓冲”不为空，才将x从缓冲中取出。
            while (count == 0) 
                notEmpty.await();
            // 将x从缓冲中取出
            Object x = items[takeptr]; 
            // 将“take统计数takeptr+1”；如果“缓冲为空”，则设takeptr为0。
            if (++takeptr == items.length) takeptr = 0;
            // 将“缓冲”数量-1
            --count;
            // 唤醒put线程，因为put线程通过notFull.await()等待
            notFull.signal();
            // 打印取出的数据
            System.out.println(Thread.currentThread().getName() + " take "+ (Integer)x);
            return x;
        } finally {
            lock.unlock();    // 释放锁
        }
    } 
}
public class ConditionTest2 {
    private static BoundedBuffer bb = new BoundedBuffer();
    public static void main(String[] args) {
        // 启动10个“写线程”，向BoundedBuffer中不断的写数据(写入0-9)；
        // 启动10个“读线程”，从BoundedBuffer中不断的读数据。
        for (int i=0; i<10; i++) {
            new PutThread("p"+i, i).start();
            new TakeThread("t"+i).start();
        }
    }
    static class PutThread extends Thread {
        private int num;
        public PutThread(String name, int num) {
            super(name);
            this.num = num;
        }
        public void run() {
            try {
                Thread.sleep(1);    // 线程休眠1ms
                bb.put(num);        // 向BoundedBuffer中写入数据
            } catch (InterruptedException e) {
            }
        }
    }
    static class TakeThread extends Thread {
        public TakeThread(String name) {
            super(name);
        }
        public void run() {
            try {
                Thread.sleep(10);                    // 线程休眠1ms
                Integer num = (Integer)bb.take();    // 从BoundedBuffer中取出数据
            } catch (InterruptedException e) {
            }
        }
    }
}

某一次结果:
p1 put  1
p4 put  4
p5 put  5
p0 put  0
p2 put  2
t0 take 1
p3 put  3
t1 take 4
p6 put  6
t2 take 5
p7 put  7
t3 take 0
p8 put  8
t4 take 2
p9 put  9
t5 take 3
t6 take 6
t7 take 7
t8 take 8
t9 take 9
    
结果说明：
(01) BoundedBuffer 是容量为5的缓冲，缓冲中存储的是Object对象，支持多线程的读/写缓冲。多个线程操作“一个BoundedBuffer对象”时，它们通过互斥锁lock对缓冲区items进行互斥访问；而且同一个BoundedBuffer对象下的全部线程共用“notFull”和“notEmpty”这两个Condition。
    notFull用于控制写缓冲，notEmpty用于控制读缓冲。当缓冲已满的时候，调用put的线程会执行notFull.await()进行等待；当缓冲区不是满的状态时，就将对象添加到缓冲区并将缓冲区的容量count+1，最后，调用notEmpty.signal()缓冲notEmpty上的等待线程(调用notEmpty.await的线程)。 简言之，notFull控制“缓冲区的写入”，当往缓冲区写入数据之后会唤醒notEmpty上的等待线程。
	同理，notEmpty控制“缓冲区的读取”，当读取了缓冲区数据之后会唤醒notFull上的等待线程。
(02) 在ConditionTest2的main函数中，启动10个“写线程”，向BoundedBuffer中不断的写数据(写入0-9)；同时，也启动10个“读线程”，从BoundedBuffer中不断的读数据。
(03) 简单分析一下运行结果。

1, p1线程向缓冲中写入1。    此时，缓冲区数据:   | 1 |   |   |   |   |
     2, p4线程向缓冲中写入4。    此时，缓冲区数据:   | 1 | 4 |   |   |   |
     3, p5线程向缓冲中写入5。    此时，缓冲区数据:   | 1 | 4 | 5 |   |   |
     4, p0线程向缓冲中写入0。    此时，缓冲区数据:   | 1 | 4 | 5 | 0 |   |
     5, p2线程向缓冲中写入2。    此时，缓冲区数据:   | 1 | 4 | 5 | 0 | 2 |
     此时，缓冲区容量为5；缓冲区已满！如果此时，还有“写线程”想往缓冲中写入数据，会调用put中的notFull.await()等待，直接缓冲区非满状态，才能继续运行。
     6, t0线程从缓冲中取出数据1。此时，缓冲区数据:   |   | 4 | 5 | 0 | 2 |
     7, p3线程向缓冲中写入3。    此时，缓冲区数据:   | 3 | 4 | 5 | 0 | 2 |
     8, t1线程从缓冲中取出数据4。此时，缓冲区数据:   | 3 |   | 5 | 0 | 2 |
     9, p6线程向缓冲中写入6。    此时，缓冲区数据:   | 3 | 6 | 5 | 0 | 2 |
     ...
```



# LockSupport

```java
LockSupport是用来创建锁和其他同步类的基本线程阻塞原语。 
LockSupport中的park() 和 unpark() 的作用分别是阻塞线程和解除阻塞线程，而且park()和unpark()不会遇到“Thread.suspend 和 Thread.resume所可能引发的死锁”问题。
因为park() 和 unpark()有许可的存在；调用 park() 的线程和另一个试图将其 unpark() 的线程之间的竞争将保持活性。
```

```java
// LockSupport函数列表
// 返回提供给最近一次尚未解除阻塞的 park 方法调用的 blocker 对象，如果该调用不受阻塞，则返回 null。
static Object getBlocker(Thread t)
// 为了线程调度，禁用当前线程，除非许可可用。
static void park()
// 为了线程调度，在许可可用之前禁用当前线程。
static void park(Object blocker)
// 为了线程调度禁用当前线程，最多等待指定的等待时间，除非许可可用。
static void parkNanos(long nanos)
// 为了线程调度，在许可可用前禁用当前线程，并最多等待指定的等待时间。
static void parkNanos(Object blocker, long nanos)
// 为了线程调度，在指定的时限前禁用当前线程，除非许可可用。
static void parkUntil(long deadline)
// 为了线程调度，在指定的时限前禁用当前线程，除非许可可用。
static void parkUntil(Object blocker, long deadline)
// 如果给定线程的许可尚不可用，则使其可用。
static void unpark(Thread thread)
```

## LockSupport示例

```
public class WaitTest1 {
    public static void main(String[] args) {
        ThreadA ta = new ThreadA("ta");
        synchronized(ta) { // 通过synchronized(ta)获取“对象ta的同步锁”
            try {
                System.out.println(Thread.currentThread().getName()+" start ta");
                ta.start();
                System.out.println(Thread.currentThread().getName()+" block");
                // 主线程等待
                ta.wait();
                System.out.println(Thread.currentThread().getName()+" continue");
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
    static class ThreadA extends Thread{
        public ThreadA(String name) {
            super(name);
        }
        public void run() {
            synchronized (this) { // 通过synchronized(this)获取“当前对象的同步锁”
                System.out.println(Thread.currentThread().getName()+" wakup others");
                notify();    // 唤醒“当前对象上的等待线程”
            }
        }
    }
}
```

```java
import java.util.concurrent.locks.LockSupport;
public class LockSupportTest1 {
    private static Thread mainThread;
    public static void main(String[] args) {
        ThreadA ta = new ThreadA("ta");
        // 获取主线程
        mainThread = Thread.currentThread();
        System.out.println(Thread.currentThread().getName()+" start ta");
        ta.start();
        System.out.println(Thread.currentThread().getName()+" block");
        // 主线程阻塞
        LockSupport.park(mainThread);
        System.out.println(Thread.currentThread().getName()+" continue");
    }
    static class ThreadA extends Thread{
        public ThreadA(String name) {
            super(name);
        }
        public void run() {
            System.out.println(Thread.currentThread().getName()+" wakup others");
            // 唤醒“主线程”
            LockSupport.unpark(mainThread);
        }
    }
}

运行结果：
main start ta
main block
ta wakup others
main continue

说明：park和wait的区别。wait让线程阻塞前，必须通过synchronized获取同步锁。
```

# 共享锁和ReentrantReadWriteLock

```java
ReadWriteLock，顾名思义，是读写锁。它维护了一对相关的锁 — — “读取锁”和“写入锁”，一个用于读取操作，另一个用于写入操作。
“读取锁”用于只读操作，它是“共享锁”，能同时被多个线程获取。
“写入锁”用于写入操作，它是“独占锁”，写入锁只能被一个线程锁获取。
注意：不能同时存在读取锁和写入锁！
ReadWriteLock是一个接口。ReentrantReadWriteLock是它的实现类，ReentrantReadWriteLock包括子类ReadLock和WriteLock。
```

````
// ReadWriteLock函数列表
// 返回用于读取操作的锁。
Lock readLock()
// 返回用于写入操作的锁。
Lock writeLock()
````

```
// ReentrantReadWriteLock函数列表
// 创建一个新的 ReentrantReadWriteLock，默认是采用“非公平策略”。
ReentrantReadWriteLock()
// 创建一个新的 ReentrantReadWriteLock，fair是“公平策略”。fair为true，意味着公平策略；否则，意味着非公平策略。
ReentrantReadWriteLock(boolean fair)
// 返回当前拥有写入锁的线程，如果没有这样的线程，则返回 null。
protected Thread getOwner()
// 返回一个 collection，它包含可能正在等待获取读取锁的线程。
protected Collection<Thread> getQueuedReaderThreads()
// 返回一个 collection，它包含可能正在等待获取读取或写入锁的线程。
protected Collection<Thread> getQueuedThreads()
// 返回一个 collection，它包含可能正在等待获取写入锁的线程。
protected Collection<Thread> getQueuedWriterThreads()
// 返回等待获取读取或写入锁的线程估计数目。
int getQueueLength()
// 查询当前线程在此锁上保持的重入读取锁数量。
int getReadHoldCount()
// 查询为此锁保持的读取锁数量。
int getReadLockCount()
// 返回一个 collection，它包含可能正在等待与写入锁相关的给定条件的那些线程。
protected Collection<Thread> getWaitingThreads(Condition condition)
// 返回正等待与写入锁相关的给定条件的线程估计数目。
int getWaitQueueLength(Condition condition)
// 查询当前线程在此锁上保持的重入写入锁数量。
int getWriteHoldCount()
// 查询是否给定线程正在等待获取读取或写入锁。
boolean hasQueuedThread(Thread thread)
// 查询是否所有的线程正在等待获取读取或写入锁。
boolean hasQueuedThreads()
// 查询是否有些线程正在等待与写入锁有关的给定条件。
boolean hasWaiters(Condition condition)
// 如果此锁将公平性设置为 ture，则返回 true。
boolean isFair()
// 查询是否某个线程保持了写入锁。
boolean isWriteLocked()
// 查询当前线程是否保持了写入锁。
boolean isWriteLockedByCurrentThread()
// 返回用于读取操作的锁。
ReentrantReadWriteLock.ReadLock readLock()
// 返回用于写入操作的锁。
ReentrantReadWriteLock.WriteLock writeLock()
```

## 获取共享锁

```java
获取共享锁的思想(即lock函数的步骤)，是先通过tryAcquireShared()尝试获取共享锁。尝试成功的话，则直接返回；尝试失败的话，则通过doAcquireShared()不断的循环并尝试获取锁，若有需要，则阻塞等待。doAcquireShared()在循环中每次尝试获取锁时，都是通过tryAcquireShared()来进行尝试的。

1. lock()

2. acquireShared()
说明：acquireShared()首先会通过tryAcquireShared()来尝试获取锁。
尝试成功的话，则不再做任何动作(因为已经成功获取到锁了)。
尝试失败的话，则通过doAcquireShared()来获取锁。doAcquireShared()会获取到锁了才返回。

3. tryAcquireShared()
说明：tryAcquireShared()的作用是尝试获取“共享锁”。
如果在尝试获取锁时，“不需要阻塞等待”并且“读取锁的共享计数小于MAX_COUNT”，则直接通过CAS函数更新“读取锁的共享计数”，以及将“当前线程获取读取锁的次数+1”。
否则，通过fullTryAcquireShared()获取读取锁。

4. fullTryAcquireShared()
说明：fullTryAcquireShared()会根据“是否需要阻塞等待”，“读取锁的共享计数是否超过限制”等等进行处理。如果不需要阻塞等待，并且锁的共享计数没有超过限制，则通过CAS尝试获取锁，并返回1。

5. doAcquireShared()
说明：doAcquireShared()的作用是获取共享锁。
它会首先创建线程对应的CLH队列的节点，然后将该节点添加到CLH队列中。CLH队列是管理获取锁的等待线程的队列。
如果“当前线程”是CLH队列的表头，则尝试获取共享锁；否则，则需要通过shouldParkAfterFailedAcquire()判断是否阻塞等待，需要的话，则通过parkAndCheckInterrupt()进行阻塞等待。
doAcquireShared()会通过for循环，不断的进行上面的操作；目的就是获取共享锁。需要注意的是：doAcquireShared()在每一次尝试获取锁时，是通过tryAcquireShared()来执行的！
```



## 释放共享锁

````java
释放共享锁的思想，是先通过tryReleaseShared()尝试释放共享锁。尝试成功的话，则通过doReleaseShared()唤醒“其他等待获取共享锁的线程”，并返回true；否则的话，返回flase。

1. unlock()
说明：该函数实际上调用releaseShared(1)释放共享锁。

2. releaseShared()
说明：releaseShared()的目的是让当前线程释放它所持有的共享锁。
它首先会通过tryReleaseShared()去尝试释放共享锁。尝试成功，则直接返回；尝试失败，则通过doReleaseShared()去释放共享锁。

3. tryReleaseShared()
说明：tryReleaseShared()的作用是尝试释放共享锁。

4. doReleaseShared()
说明：doReleaseShared()会释放“共享锁”。它会从前往后的遍历CLH队列，依次“唤醒”然后“执行”队列中每个节点对应的线程；最终的目的是让这些线程释放它们所持有的锁。
````

## 公平共享锁和非公平共享锁

```java
和互斥锁ReentrantLock一样，ReadLock也分为公平锁和非公平锁。

公平锁和非公平锁的区别，体现在判断是否需要阻塞的函数readerShouldBlock()是不同的。
在公平共享锁中，如果在当前线程的前面有其他线程在等待获取共享锁，则返回true；否则，返回false。
在非公平共享锁中，它会无视当前线程的前面是否有其他线程在等待获取共享锁。只要该非公平共享锁对应的线程不为null，则返回true。
```

## ReentrantReadWriteLock示例

```java
import java.util.concurrent.locks.ReadWriteLock; 
import java.util.concurrent.locks.ReentrantReadWriteLock; 
public class ReadWriteLockTest1 { 
    public static void main(String[] args) { 
        // 创建账户
        MyCount myCount = new MyCount("4238920615242830", 10000); 
        // 创建用户，并指定账户
        User user = new User("Tommy", myCount); 
        // 分别启动3个“读取账户金钱”的线程 和 3个“设置账户金钱”的线程
        for (int i=0; i<3; i++) {
            user.getCash();
            user.setCash((i+1)*1000);
        }
    } 
} 
class User {
    private String name;            //用户名 
    private MyCount myCount;        //所要操作的账户 
    private ReadWriteLock myLock;   //执行操作所需的锁对象 
    User(String name, MyCount myCount) {
        this.name = name; 
        this.myCount = myCount; 
        this.myLock = new ReentrantReadWriteLock();
    }
    public void getCash() {
        new Thread() {
            public void run() {
                myLock.readLock().lock(); 
                try {
                    System.out.println(Thread.currentThread().getName() +" getCash start"); 
                    myCount.getCash();
                    Thread.sleep(1);
                    System.out.println(Thread.currentThread().getName() +" getCash end"); 
                } catch (InterruptedException e) {
                } finally {
                    myLock.readLock().unlock(); 
                }
            }
        }.start();
    }
    public void setCash(final int cash) {
        new Thread() {
            public void run() {
                myLock.writeLock().lock(); 
                try {
                    System.out.println(Thread.currentThread().getName() +" setCash start"); 
                    myCount.setCash(cash);
                    Thread.sleep(1);
                    System.out.println(Thread.currentThread().getName() +" setCash end"); 
                } catch (InterruptedException e) {
                } finally {
                    myLock.writeLock().unlock(); 
                }
            }
        }.start();
    }
}
class MyCount {
    private String id;         //账号 
    private int    cash;       //账户余额 
    MyCount(String id, int cash) { 
        this.id = id; 
        this.cash = cash; 
    } 
    public String getId() { 
        return id; 
    } 
    public void setId(String id) { 
        this.id = id; 
    } 
    public int getCash() { 
        System.out.println(Thread.currentThread().getName() +" getCash cash="+ cash); 
        return cash; 
    } 
    public void setCash(int cash) { 
        System.out.println(Thread.currentThread().getName() +" setCash cash="+ cash); 
        this.cash = cash; 
    } 
}

Thread-0 getCash start
Thread-2 getCash start
Thread-0 getCash cash=10000
Thread-2 getCash cash=10000
Thread-0 getCash end
Thread-2 getCash end
Thread-1 setCash start
Thread-1 setCash cash=1000
Thread-1 setCash end
Thread-3 setCash start
Thread-3 setCash cash=2000
Thread-3 setCash end
Thread-4 getCash start
Thread-4 getCash cash=2000
Thread-4 getCash end
Thread-5 setCash start
Thread-5 setCash cash=3000
Thread-5 setCash end


结果说明：
(01) 观察Thread0和Thread-2的运行结果，我们发现，Thread-0启动并获取到“读取锁”，在它还没运行完毕的时候，Thread-2也启动了并且也成功获取到“读取锁”。
因此，“读取锁”支持被多个线程同时获取。
(02) 观察Thread-1,Thread-3,Thread-5这三个“写入锁”的线程。只要“写入锁”被某线程获取，则该线程运行完毕了，才释放该锁。
因此，“写入锁”不支持被多个线程同时获取。
```



# CountDownLatch原理和示例

```java
CountDownLatch是一个同步辅助类，在完成一组正在其他线程中执行的操作之前，它允许一个或多个线程一直等待。
CountDownLatch和CyclicBarrier的区别
(01) CountDownLatch的作用是允许1或N个线程等待其他线程完成执行；而CyclicBarrier则是允许N个线程相互等待。
(02) CountDownLatch的计数器无法被重置；CyclicBarrier的计数器可以被重置后使用，因此它被称为是循环的barrier。
关于CyclicBarrier的原理，后面一章再来学习。
```

```java
// CountDownLatch函数列表
CountDownLatch(int count)
// 构造一个用给定计数初始化的 CountDownLatch。
// 使当前线程在锁存器倒计数至零之前一直等待，除非线程被中断。
void await()
// 使当前线程在锁存器倒计数至零之前一直等待，除非线程被中断或超出了指定的等待时间。
boolean await(long timeout, TimeUnit unit)
// 递减锁存器的计数，如果计数到达零，则释放所有等待的线程。
void countDown()
// 返回当前计数。
long getCount()
// 返回标识此锁存器及其状态的字符串。
String toString()
```

```java
1. CountDownLatch(int count)
说明：该函数是创建一个Sync对象，而Sync是继承于AQS类。

2. await()
说明：该函数实际上是调用的AQS的acquireSharedInterruptibly(1);
说明：acquireSharedInterruptibly()的作用是获取共享锁。
如果当前线程是中断状态，则抛出异常InterruptedException。否则，调用tryAcquireShared(arg)尝试获取共享锁；尝试成功则返回，否则就调用doAcquireSharedInterruptibly()。doAcquireSharedInterruptibly()会使当前线程一直等待，直到当前线程获取到共享锁(或被中断)才返回。
说明：tryAcquireShared()的作用是尝试获取共享锁。
如果"锁计数器=0"，即锁是可获取状态，则返回1；否则，锁是不可获取状态，则返回-1。

说明：
(01) addWaiter(Node.SHARED)的作用是，创建”当前线程“的Node节点，且Node中记录的锁的类型是”共享锁“(Node.SHARED)；并将该节点添加到CLH队列末尾。关于Node和CLH在"Java多线程系列--“JUC锁”03之 公平锁(一)"已经详细介绍过，这里就不再重复说明了。
(02) node.predecessor()的作用是，获取上一个节点。如果上一节点是CLH队列的表头，则”尝试获取共享锁“。
(03) shouldParkAfterFailedAcquire()的作用和它的名称一样，如果在尝试获取锁失败之后，线程应该等待，则返回true；否则，返回false。
(04) 当shouldParkAfterFailedAcquire()返回ture时，则调用parkAndCheckInterrupt()，当前线程会进入等待状态，直到获取到共享锁才继续运行。

3. countDown()
说明：该函数实际上调用releaseShared(1)释放共享锁。
说明：releaseShared()的目的是让当前线程释放它所持有的共享锁。
它首先会通过tryReleaseShared()去尝试释放共享锁。尝试成功，则直接返回；尝试失败，则通过doReleaseShared()去释放共享锁。
说明：tryReleaseShared()的作用是释放共享锁，将“锁计数器”的值-1。

总结：CountDownLatch是通过“共享锁”实现的。在创建CountDownLatch中时，会传递一个int类型参数count，该参数是“锁计数器”的初始状态，表示该“共享锁”最多能被count给线程同时获取。当某线程调用该CountDownLatch对象的await()方法时，该线程会等待“共享锁”可用时，才能获取“共享锁”进而继续运行。而“共享锁”可用的条件，就是“锁计数器”的值为0！而“锁计数器”的初始值为count，每当一个线程调用该CountDownLatch对象的countDown()方法时，才将“锁计数器”-1；通过这种方式，必须有count个线程调用countDown()之后，“锁计数器”才为0，而前面提到的等待线程才能继续运行！
```

## CountDownLatch的使用示例

```java
// 通过CountDownLatch实现："主线程"等待"5个子线程"全部都完成"指定的工作(休眠1000ms)"之后，再继续运行。
import java.util.concurrent.CountDownLatch;
import java.util.concurrent.CyclicBarrier;
public class CountDownLatchTest1 {
    private static int LATCH_SIZE = 5;
    private static CountDownLatch doneSignal;
    public static void main(String[] args) {
        try {
            doneSignal = new CountDownLatch(LATCH_SIZE);
            // 新建5个任务
            for(int i=0; i<LATCH_SIZE; i++)
                new InnerThread().start();
            System.out.println("main await begin.");
            // "主线程"等待线程池中5个任务的完成
            doneSignal.await();
            System.out.println("main await finished.");
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }
    static class InnerThread extends Thread{
        public void run() {
            try {
                Thread.sleep(1000);
                System.out.println(Thread.currentThread().getName() + " sleep 1000ms.");
                // 将CountDownLatch的数值减1
                doneSignal.countDown();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

main await begin.
Thread-0 sleep 1000ms.
Thread-2 sleep 1000ms.
Thread-1 sleep 1000ms.
Thread-4 sleep 1000ms.
Thread-3 sleep 1000ms.
main await finished.
    
结果说明：主线程通过doneSignal.await()等待其它线程将doneSignal递减至0。其它的5个InnerThread线程，每一个都通过doneSignal.countDown()将doneSignal的值减1；当doneSignal为0时，main被唤醒后继续执行。
```

# CyclicBarrier原理和示例

```java
CyclicBarrier是一个同步辅助类，允许一组线程互相等待，直到到达某个公共屏障点 (common barrier point)。因为该 barrier 在释放等待线程后可以重用，所以称它为循环 的 barrier。
注意比较CountDownLatch和CyclicBarrier：
(01) CountDownLatch的作用是允许1或N个线程等待其他线程完成执行；而CyclicBarrier则是允许N个线程相互等待。
(02) CountDownLatch的计数器无法被重置；CyclicBarrier的计数器可以被重置后使用，因此它被称为是循环的barrier。
```

```java
// CyclicBarrier函数列表
CyclicBarrier(int parties)
// 创建一个新的 CyclicBarrier，它将在给定数量的参与者（线程）处于等待状态时启动，但它不会在启动 barrier 时执行预定义的操作。
CyclicBarrier(int parties, Runnable barrierAction)
// 创建一个新的 CyclicBarrier，它将在给定数量的参与者（线程）处于等待状态时启动，并在启动 barrier 时执行给定的屏障操作，该操作由最后一个进入 barrier 的线程执行。
int await()
// 在所有参与者都已经在此 barrier 上调用 await 方法之前，将一直等待。
int await(long timeout, TimeUnit unit)
// 在所有参与者都已经在此屏障上调用 await 方法之前将一直等待,或者超出了指定的等待时间。
int getNumberWaiting()
// 返回当前在屏障处等待的参与者数目。
int getParties()
// 返回要求启动此 barrier 的参与者数目。
boolean isBroken()
// 查询此屏障是否处于损坏状态。
void reset()
// 将屏障重置为其初始状态。
```

````java
1. 构造函数
CyclicBarrier的构造函数共2个：CyclicBarrier 和 CyclicBarrier(int parties, Runnable barrierAction)。第1个构造函数是调用第2个构造函数来实现的，

2. 等待函数
说明：await()是通过dowait()实现的。
说明：dowait()的作用就是让当前线程阻塞，直到“有parties个线程到达barrier” 或 “当前线程被中断” 或 “超时”这3者之一发生，当前线程才继续执行。
(01) generation是CyclicBarrier的一个成员遍历，它的定义如下：
private Generation generation = new Generation();
private static class Generation {
    boolean broken = false;
}
在CyclicBarrier中，同一批的线程属于同一代，即同一个Generation；CyclicBarrier中通过generation对象，记录属于哪一代。
当有parties个线程到达barrier，generation就会被更新换代。
(02) 如果当前线程被中断，即Thread.interrupted()为true；则通过breakBarrier()终止CyclicBarrier。breakBarrier()的源码如下：
private void breakBarrier() {
    generation.broken = true;
    count = parties;
    trip.signalAll();
}
breakBarrier()会设置当前中断标记broken为true，意味着“将该Generation中断”；同时，设置count=parties，即重新初始化count；最后，通过signalAll()唤醒CyclicBarrier上所有的等待线程。
(03) 将“count计数器”-1，即--count；然后判断是不是“有parties个线程到达barrier”，即index是不是为0。
当index=0时，如果barrierCommand不为null，则执行该barrierCommand，barrierCommand就是我们创建CyclicBarrier时，传入的Runnable对象。然后，调用nextGeneration()进行换代工作，nextGeneration()的源码如下：
private void nextGeneration() {
    trip.signalAll();
    count = parties;
    generation = new Generation();
}
首先，它会调用signalAll()唤醒CyclicBarrier上所有的等待线程；接着，重新初始化count；最后，更新generation的值。
(04) 在for(;;)循环中。timed是用来表示当前是不是“超时等待”线程。如果不是，则通过trip.await()进行等待；否则，调用awaitNanos()进行超时等待。
````

## CyclicBarrier的使用示例

```java
// 新建5个线程，这5个线程达到一定的条件时，它们才继续往后运行。
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.BrokenBarrierException;
public class CyclicBarrierTest1 {
    private static int SIZE = 5;
    private static CyclicBarrier cb;
    public static void main(String[] args) {
        cb = new CyclicBarrier(SIZE);
        // 新建5个任务
        for(int i=0; i<SIZE; i++)
            new InnerThread().start();
    }
    static class InnerThread extends Thread{
        public void run() {
            try {
                System.out.println(Thread.currentThread().getName() + " wait for CyclicBarrier.");
                // 将cb的参与者数量加1
                cb.await();
                // cb的参与者数量等于5时，才继续往后执行
                System.out.println(Thread.currentThread().getName() + " continued.");
            } catch (BrokenBarrierException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

Thread-1 wait for CyclicBarrier.
Thread-2 wait for CyclicBarrier.
Thread-3 wait for CyclicBarrier.
Thread-4 wait for CyclicBarrier.
Thread-0 wait for CyclicBarrier.
Thread-0 continued.
Thread-4 continued.
Thread-2 continued.
Thread-3 continued.
Thread-1 continued.


结果说明：主线程中新建了5个线程，所有的这些线程都调用cb.await()等待。所有这些线程一直等待，直到cb中所有线程都达到barrier时，这些线程才继续运行！
```

```java
// 新建5个线程，当这5个线程达到一定的条件时，执行某项任务。
import java.util.concurrent.CyclicBarrier;
import java.util.concurrent.BrokenBarrierException;
public class CyclicBarrierTest2 {
    private static int SIZE = 5;
    private static CyclicBarrier cb;
    public static void main(String[] args) {
        cb = new CyclicBarrier(SIZE, new Runnable () {
            public void run() {
                System.out.println("CyclicBarrier's parties is: "+ cb.getParties());
            }
        });
        // 新建5个任务
        for(int i=0; i<SIZE; i++)
            new InnerThread().start();
    }
    static class InnerThread extends Thread{
        public void run() {
            try {
                System.out.println(Thread.currentThread().getName() + " wait for CyclicBarrier.");
                // 将cb的参与者数量加1
                cb.await();
                // cb的参与者数量等于5时，才继续往后执行
                System.out.println(Thread.currentThread().getName() + " continued.");
            } catch (BrokenBarrierException e) {
                e.printStackTrace();
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}

Thread-1 wait for CyclicBarrier.
Thread-2 wait for CyclicBarrier.
Thread-3 wait for CyclicBarrier.
Thread-4 wait for CyclicBarrier.
Thread-0 wait for CyclicBarrier.
CyclicBarrier's parties is: 5
Thread-0 continued.
Thread-4 continued.
Thread-2 continued.
Thread-3 continued.
Thread-1 continued.
    
结果说明：主线程中新建了5个线程，所有的这些线程都调用cb.await()等待。所有这些线程一直等待，直到cb中所有线程都达到barrier时，执行新建cb时注册的Runnable任务。
```

# Semaphore信号量的原理和示例

```java
Semaphore是一个计数信号量，它的本质是一个"共享锁"。

信号量维护了一个信号量许可集。线程可以通过调用acquire()来获取信号量的许可；当信号量中有可用的许可时，线程能获取该许可；否则线程必须等待，直到有可用的许可为止。 线程可以通过release()来释放它所持有的信号量许可。
```

```java
// Semaphore的函数列表
// 创建具有给定的许可数和非公平的公平设置的 Semaphore。
Semaphore(int permits)
// 创建具有给定的许可数和给定的公平设置的 Semaphore。
Semaphore(int permits, boolean fair)
// 从此信号量获取一个许可，在提供一个许可前一直将线程阻塞，否则线程被中断。
void acquire()
// 从此信号量获取给定数目的许可，在提供这些许可前一直将线程阻塞，或者线程已被中断。
void acquire(int permits)
// 从此信号量中获取许可，在有可用的许可前将其阻塞。
void acquireUninterruptibly()
// 从此信号量获取给定数目的许可，在提供这些许可前一直将线程阻塞。
void acquireUninterruptibly(int permits)
// 返回此信号量中当前可用的许可数。
int availablePermits()
// 获取并返回立即可用的所有许可。
int drainPermits()
// 返回一个 collection，包含可能等待获取的线程。
protected Collection<Thread> getQueuedThreads()
// 返回正在等待获取的线程的估计数目。
int getQueueLength()
// 查询是否有线程正在等待获取。
boolean hasQueuedThreads()
// 如果此信号量的公平设置为 true，则返回 true。
boolean isFair()
// 根据指定的缩减量减小可用许可的数目。
protected void reducePermits(int reduction)
// 释放一个许可，将其返回给信号量。
void release()
// 释放给定数目的许可，将其返回到信号量。
void release(int permits)
// 返回标识此信号量的字符串，以及信号量的状态。
String toString()
// 仅在调用时此信号量存在一个可用许可，才从信号量获取许可。
boolean tryAcquire()
// 仅在调用时此信号量中有给定数目的许可时，才从此信号量中获取这些许可。
boolean tryAcquire(int permits)
// 如果在给定的等待时间内此信号量有可用的所有许可，并且当前线程未被中断，则从此信号量获取给定数目的许可。
boolean tryAcquire(int permits, long timeout, TimeUnit unit)
// 如果在给定的等待时间内，此信号量有可用的许可并且当前线程未被中断，则从此信号量获取一个许可。
boolean tryAcquire(long timeout, TimeUnit unit)
```

```java
Semaphore是通过共享锁实现的。根据共享锁的获取原则，Semaphore分为"公平信号量"和"非公平信号量"。

"公平信号量"和"非公平信号量"的区别
"公平信号量"和"非公平信号量"的释放信号量的机制是一样的！不同的是它们获取信号量的机制：线程在尝试获取信号量许可时，对于公平信号量而言，如果当前线程不在CLH队列的头部，则排队等候；而对于非公平信号量而言，无论当前线程是不是在CLH队列的头部，它都会直接获取信号量。该差异具体的体现在，它们的tryAcquireShared()函数的实现不同。
```

## 公平信号量获取和释放

```java
1. 公平信号量的获取
Semaphore中的公平信号量是FairSync。
信号量中的acquire()获取函数，实际上是调用的AQS中的acquireSharedInterruptibly()。
说明：tryAcquireShared()的作用是尝试获取acquires个信号量许可数。
对于Semaphore而言，state表示的是“当前可获得的信号量许可数”。
说明：doAcquireSharedInterruptibly()会使当前线程一直等待，直到当前线程获取到共享锁(或被中断)才返回。
(01) addWaiter(Node.SHARED)的作用是，创建”当前线程“的Node节点，且Node中记录的锁的类型是”共享锁“(Node.SHARED)；并将该节点添加到CLH队列末尾。关于Node和CLH在"Java多线程系列--“JUC锁”03之 公平锁(一)"已经详细介绍过，这里就不再重复说明了。
(02) node.predecessor()的作用是，获取上一个节点。如果上一节点是CLH队列的表头，则”尝试获取共享锁“。
(03) shouldParkAfterFailedAcquire()的作用和它的名称一样，如果在尝试获取锁失败之后，线程应该等待，则返回true；否则，返回false。
(04) 当shouldParkAfterFailedAcquire()返回ture时，则调用parkAndCheckInterrupt()，当前线程会进入等待状态，直到获取到共享锁才继续运行。

2. 公平信号量的释放
信号量的releases()释放函数，实际上是调用的AQS中的releaseShared()。
说明：releaseShared()的目的是让当前线程释放它所持有的共享锁。
它首先会通过tryReleaseShared()去尝试释放共享锁。尝试成功，则直接返回；尝试失败，则通过doReleaseShared()去释放共享锁。
Semaphore重写了tryReleaseShared()，
如果tryReleaseShared()尝试释放共享锁失败，则会调用doReleaseShared()去释放共享锁。
说明：doReleaseShared()会释放“共享锁”。它会从前往后的遍历CLH队列，依次“唤醒”然后“执行”队列中每个节点对应的线程；最终的目的是让这些线程释放它们所持有的信号量。
```

## 非公平信号量获取和释放

```java
Semaphore中的非公平信号量是NonFairSync。在Semaphore中，“非公平信号量许可的释放(release)”与“公平信号量许可的释放(release)”是一样的。不同的是它们获取“信号量许可”的机制不同，

说明：非公平信号量的tryAcquireShared()调用AQS中的nonfairTryAcquireShared()。而在nonfairTryAcquireShared()的for循环中，它都会直接判断“当前剩余的信号量许可数”是否足够；足够的话，则直接“设置可以获得的信号量许可数”，进而再获取信号量。
而公平信号量的tryAcquireShared()中，在获取信号量之前会通过if (hasQueuedPredecessors())来判断“当前线程是不是在CLH队列的头部”，是的话，则返回-1。 
```

## Semaphore示例

```java
import java.util.concurrent.ExecutorService; 
import java.util.concurrent.Executors; 
import java.util.concurrent.Semaphore; 
public class SemaphoreTest1 { 
    private static final int SEM_MAX = 10;
    public static void main(String[] args) { 
        Semaphore sem = new Semaphore(SEM_MAX);
        //创建线程池
        ExecutorService threadPool = Executors.newFixedThreadPool(3);
        //在线程池中执行任务
        threadPool.execute(new MyThread(sem, 5));
        threadPool.execute(new MyThread(sem, 4));
        threadPool.execute(new MyThread(sem, 7));
        //关闭池
        threadPool.shutdown();
    }
}
class MyThread extends Thread {
    private volatile Semaphore sem;    // 信号量
    private int count;        // 申请信号量的大小 
    MyThread(Semaphore sem, int count) {
        this.sem = sem;
        this.count = count;
    }
    public void run() {
        try {
            // 从信号量中获取count个许可
            sem.acquire(count);
            Thread.sleep(2000);
            System.out.println(Thread.currentThread().getName() + " acquire count="+count);
        } catch (InterruptedException e) {
            e.printStackTrace();
        } finally {
            // 释放给定数目的许可，将其返回到信号量。
            sem.release(count);
            System.out.println(Thread.currentThread().getName() + " release " + count + "");
        }
    }
}

(某一次)运行结果：
pool-1-thread-1 acquire count=5
pool-1-thread-2 acquire count=4
pool-1-thread-1 release 5
pool-1-thread-2 release 4
pool-1-thread-3 acquire count=7
pool-1-thread-3 release 7

结果说明：信号量sem的许可总数是10个；共3个线程，分别需要获取的信号量许可数是5,4,7。前面两个线程获取到信号量的许可后，sem中剩余的可用的许可数是1；因此，最后一个线程必须等前两个线程释放了它们所持有的信号量许可之后，才能获取到7个信号量许可。
```

