//
//#define	它用于定义一系列成为符号的字符。
//#undef	它用于取消定义符号。
//#if	它用于测试符号是否为真。
//#else	它用于创建复合条件指令，与 #if 一起使用。
//#elif	它用于创建复合条件指令。
//#endif	指定一个条件指令的结束。
//#line	它可以让您修改编译器的行数以及（可选地）输出错误和警告的文件名。
//#error	它允许从代码的指定位置生成一个错误。
//#warning	它允许从代码的指定位置生成一级警告。
//#region	它可以让您在使用 Visual Studio Code Editor 的大纲特性时，指定一个可展开或折叠的代码块。
//#endregion	它标识着 #region 块的结束。


using System;
using first_space;
using second_space;
using SomeNameSpace;
using SomeNameSpace.Nested;


interface IMyInterface
{
    // 接口成员
    void MethodToImplement();
}

class InterfaceImplementer : IMyInterface
{
    static void Main()
    {
        InterfaceImplementer iImp = new InterfaceImplementer();
        iImp.MethodToImplement();
    }

    public void MethodToImplement()
    {
        Console.WriteLine("MethodToImplement() called.");
    }
}

namespace first_space
{
    class abc
    {
        public void func()
        {
            Console.WriteLine("Inside first_space");
        }
    }
}
namespace second_space
{
    class efg
    {
        public void func()
        {
            Console.WriteLine("Inside second_space");
        }
    }
}
class TestClass
{
    static void Main(string[] args)
    {
        abc fc = new abc();
        efg sc = new efg();
        fc.func();
        sc.func();
        Console.ReadKey();
    }
}

namespace SomeNameSpace
{
    public class MyClass
    {
        static void Main()
        {
            Console.WriteLine("In SomeNameSpace");
            Nested.NestedNameSpaceClass.SayHello();
        }
    }

    // 内嵌命名空间
    namespace Nested
    {
        public class NestedNameSpaceClass
        {
            public static void SayHello()
            {
                Console.WriteLine("In Nested");
            }
        }
    }
}
