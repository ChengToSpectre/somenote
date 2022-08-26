using System;

namespace c2
{

    //静态变量：
    public struct varl1
    {
        const int aa = 1;
        const int bb = 2;
        public int c;
        public int d;

    }

    class Program
    {
        //引用类型有：object、dynamic 和 string。

        //object 万能传递中间量 装箱 拆箱
        static void f()
        {
            int val = 8;
            object obj = val;//先装箱
            int nval = (int)obj;//再拆箱

            //or

            string v = "1234";
            object obj0 = v;
            int a = (int)obj0;
        }


        //dynamic您可以存储任何类型的值在动态数据类型变量中。这些变量的类型检查是在运行时发生的。

        //处理诸如 JSON 文档之类的结构内容，这些结构的组成可能要到运行时才能知道
        static void f0()
        {
            dynamic a = 20;
        }

        //string
        //C# string 字符串的前面可以加 @（称作"逐字字符串"）将转义字符（\）当作普通字符对待，比如

        static void f1()
        {
            string str = @"<script type=""text/javascript"">
            <!--
             -->
            </script>";

            Console.Write(str);
        }

        //5. C# 类型转换

        void change1()
        {
            int inum = 100;
            long lnum = inum; 
            // 进行了隐式转换，将 int 型（数据范围小）数据转换为了 long 型（数据范围大）的数据
            Program nn = new Program(); 
            // 这里也是隐式转换，将一个新建的 Program 实例转换为了其基类 Program 类型的实例 nn
        }

        void change2()
        {
            double d = 5673.74;
            int i;

            // 强制转换 double 为 int 显式转换
            i = (int)d;
            Console.WriteLine(i);
            Console.ReadKey();
        }


        //c#含有转换函数，如：
        //int i = 1;i.tostring; 即转换成string类型的"1"
        //还有ToByte ToBoolean ToChar ToDateTime ToDuoble ToDecimal ToInt16...
        //对于double类型，有Convert.ToInt32()方法 取整

        static void Main(string[] args)
        {
            varl1 r = new varl1();

            int num;
            num = Convert.ToInt16(Console.ReadLine());
            r.c = Convert.ToInt32(Console.ReadLine());
            string a = "Hello World!";
            Console.Write(a);
            Console.WriteLine(num);
            Console.WriteLine(r.c);
        }
    }
}
