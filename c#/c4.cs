using System;

namespace RectangleApplication
{
    class Rectangle
    {
        //成员变量
        private double length;
        private double width;

        public void Acceptdetails()
        {
            Console.WriteLine("请输入长度：");
            length = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("请输入宽度：");
            width = Convert.ToDouble(Console.ReadLine());
        }
        public double GetArea()
        {
            return length * width;
        }
        public void Display()
        {
            Console.WriteLine("长度： {0}", length);
            Console.WriteLine("宽度： {0}", width);
            Console.WriteLine("面积： {0}", GetArea());
        }
    }//end class Rectangle    

    class Program
    {
        public void swap(ref int x, ref int y)//ref 声明应用，如 c++ &
        {
            int temp;

            temp = x; /* 保存 x 的值 */
            x = y;    /* 把 y 赋值给 x */
            y = temp; /* 把 temp 赋值给 y */
        }

        public void getValue(out int x)//由于return只能返回一个值，则使用引用后out返回多个
        {
            int temp = 5;
            x = temp;
        }

        //? and ??
        public void Ways()
        {
            int? a = null;//隐式表达
            int? b = 20;
            double? m = null;
            double? n = 3.14;
            bool? judge = null;

            Console.WriteLine("{0},{1},{2},{3},{4}", a, b, m, n, judge);

            int c;
            c = a ?? 3;
            Console.WriteLine(c);
            c = b ?? 20;
            Console.WriteLine(c);
        }

        public void array()
        {
            int[,] a = new int[10,10];
            for(int i = 0; i < 10; i++)
            {
                for(int j = 0; j < 10; j++)
                {
                    a[i, j] = i * j;
                    Console.Write(a[i, j]+" ");
                }
                Console.WriteLine();
            }

            int[,,] muarr = new int[2, 2, 3]
            {
              {{1,2,3},{4,5,6}},
              {{7,8,9},{2,3,4}}
            };
        }
    }

    class ExecuteRectangle
    {
        static void Main(string[] args)
        {
            Rectangle r = new Rectangle();
            r.Acceptdetails();
            r.Display();
            //Console.ReadLine();

            Console.WriteLine("--------------------");

            Program p = new Program();
            p.Ways();

            Console.WriteLine("--------------------");

            p.array();
        }
    }
}

/*
 比如说：一个人A为父类，他的儿子B，妻子C，私生子D（注：D不在他家里）

如果我们给A的事情增加修饰符：

 public事件，地球人都知道，全公开
 protected事件，A，B，D知道（A和他的所有儿子知道，妻子C不知道）
 private事件，只有A知道（隐私？心事？）
 internal事件，A，B，C知道（A家里人都知道，私生子D不知道）
 protected internal事件，A，B，C，D都知道,其它人不知道


 (1) Pubilc ：任何公有成员可以被外部的类访问。
 (2) Private ：只有同一个类中的函数可以访问它的私有成员。
 (3) Protected ：该类内部和继承类中可以访问。
 (4) internal : 同一个程序集的对象可以访问。
 (5) Protected internal ：3 和 4 的并集，符合任意一条都可以访问。
 * 
 */
