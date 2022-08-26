//using System;
//namespace InheritanceApplication
//{
//    class Shape
//    {
//        public void setWidth(int w)
//        {
//            width = w;
//        }
//        public void setHeight(int h)
//        {
//            height = h;
//        }
//        protected int width;
//        protected int height;
//    }

//    //多肽
//    public class TestData
//    {
//        public int Add(int a, int b, int c)
//        {
//            return a + b + c;
//        }
//        public int Add(int a, int b)
//        {
//            return a + b;
//        }
//    }

//    // 基类 PaintCost
//    public interface PaintCost
//    {
//        int getCost(int area);

//    }
//    // 派生类
//    class Rectangle : Shape, PaintCost
//    {
//        public int getArea()
//        {
//            return (width * height);
//        }
//        public int getCost(int area)
//        {
//            return area * 70;
//        }
//    }
//    class Program
//    {
//        static void Main(string[] args)
//        {
//            Rectangle Rect = new Rectangle();
//            int area;
//            Rect.setWidth(5);
//            Rect.setHeight(7);
//            area = Rect.getArea();
//            // 打印对象的面积
//            Console.WriteLine("总面积： {0}", Rect.getArea());
//            Console.WriteLine("油漆总成本： ${0}", Rect.getCost(area));
//            Console.WriteLine("");

//            Console.WriteLine("------------------------------------");

//            TestData dataClass = new TestData();
//            int add1 = dataClass.Add(1, 2);
//            int add2 = dataClass.Add(1, 2, 3);

//            Console.WriteLine("add1 :" + add1);
//            Console.WriteLine("add2 :" + add2);
//        }
//    }
//}



using System;
using System.Collections.Generic;

public class Shape
{
    public int X { get; private set; }
    public int Y { get; private set; }
    public int Height { get; set; }
    public int Width { get; set; }

    // 虚方法
    public virtual void Draw()
    {
        Console.WriteLine("执行基类的画图任务");
    }
}

class Circle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("画一个圆形");
        base.Draw();
    }
}
class Rectangle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("画一个长方形");
        base.Draw();
    }
}
class Triangle : Shape
{
    public override void Draw()
    {
        Console.WriteLine("画一个三角形");
        base.Draw();
    }
}

class Program
{
    static void Main(string[] args)
    {
        // 创建一个 List<Shape> 对象，并向该对象添加 Circle、Triangle 和 Rectangle
        var shapes = new List<Shape>
        {
            new Rectangle(),
            new Triangle(),
            new Circle()
        };

        // 使用 foreach 循环对该列表的派生类进行循环访问，并对其中的每个 Shape 对象调用 Draw 方法
        foreach (var shape in shapes)
        {
            shape.Draw();
        }

        Console.WriteLine("按下任意键退出。");
        Console.ReadKey();
    }

}
