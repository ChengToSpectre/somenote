//c#为一门面向对象的编程语言    c#<=c=>c++
//大部分语法与c++相似，如int,duoble,longlong,sizeof()
//标识符相对于c++多了一个@
//标识符不能是 C# 关键字。除非它们有一个 @ 前缀。 例如，@if 是有效的标识符，但 if 不是，因为 if 是关键字。

//WriteLine() 函数有多个参数时，输出第一个参数(双引号内的)中的内容，
//而第二个及后面的参数中的内容替换掉第一个参数中对应位置的占位符一起输出。

//c#有三种数据类型：
//值类型（Value types）
//引用类型（Reference types）
//指针类型（Pointer types）

/*
using System;

namespace c1
{
    public class Rectangle
    {
        public int a, b;//只能在类中进行定义，无全局变量,有public才能进行调用

        public void change()//有public才能进行传递调用
        {
            a = 10;
            b = 20;
        }
        public int add()
        {
            return a + b * 2;
        }
        public void writeout()
        {
            int mytry = add();
            Console.WriteLine("a = {0}", a, b);
            Console.WriteLine("a = {1}", a,b);
            Console.WriteLine("b = {0}", b);
            Console.WriteLine("mytry = {0}", mytry);
            Console.WriteLine("ans = {0}", add());
        }
    }

    public class ExcuteRectangle 
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle();
            int a = r.a;
            r.change();
            r.add();
            r.writeout();
        }
    }
}
*/

/*
bool 布尔值	True 或 False	False
byte	8 位无符号整数	0 到 255	0
char	16 位 Unicode 字符	U +0000 到 U +ffff	'\0'
decimal	128 位精确的十进制值，28-29 有效位数	(-7.9 x 1028 到 7.9 x 1028) / 100 到 28   0.0M
double 64 位双精度浮点型(+/ -)5.0 x 10 - 324 到(+/ -)1.7 x 10308    0.0D
float 32 位单精度浮点型 - 3.4 x 1038 到 + 3.4 x 1038  0.0F
int 32 位有符号整数类型 - 2,147,483,648 到 2,147,483,647  0
long 64 位有符号整数类型 - 9,223,372,036,854,775,808 到 9,223,372,036,854,775,807  0L
sbyte 8 位有符号整数类型 - 128 到 127  0
short 16 位有符号整数类型 - 32,768 到 32,767    0
uint 32 位无符号整数类型 0 到 4,294,967,295   0
ulong 64 位无符号整数类型 0 到 18,446,744,073,709,551,615  0
ushort 16 位无符号整数类型 0 到 65,535  0
*/

using System;

namespace c1
{
    public class myclass
    {
        //引用类型
        //内置的 引用类型有：object、dynamic 和 string。

        //Object 是 System.Object 类的别名。所以对象（Object）类型
        //其可以被分配任何其他类型（值类型、引用类型、预定义类型或用户自定义类型）的值。
        //但是，在分配值之前，需要先进行类型转换。

        static int val = 8;
        object obj = val;//整型数据转换为了对象类型（装箱）
        int nval = （int）obj;//再拆箱
    }

    public class First
    {
        //值类型：
        int n = 0;//所有值类型需要在函数外定义
        static void Main(string[] args)
        {
            First r = new First();//需要先定义新的一个类，再进行引用
            r.n = 1;
            Console.WriteLine("{2},{1},{0}",sizeof(int),sizeof(long),sizeof(ulong));
        }
    }
}