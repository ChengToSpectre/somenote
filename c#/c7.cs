using System;

namespace OperatorOvlApplication
{
    class Box
    {
        private double length;      // 长度
        private double breadth;     // 宽度
        private double height;      // 高度

        public double getVolume()
        {
            return length * breadth * height;
        }
        public void setLength(double len)
        {
            length = len;
        }

        public void setBreadth(double bre)
        {
            breadth = bre;
        }

        public void setHeight(double hei)
        {
            height = hei;
        }



        // 重载 + 运算符来把两个 Box 对象相加
        public static Box operator +(Box b, Box c)
        {
            Box box = new Box();
            box.length = b.length + c.length;
            box.breadth = b.breadth + c.breadth;
            box.height = b.height + c.height;
            return box;
        }
        public static bool operator ==(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length == rhs.length && lhs.height == rhs.height
               && lhs.breadth == rhs.breadth)
            {
                status = true;
            }
            return status;
        }
        public static bool operator !=(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length != rhs.length || lhs.height != rhs.height
                || lhs.breadth != rhs.breadth)
            {
                status = true;
            }
            return status;
        }
        public static bool operator <(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length < rhs.length && lhs.height
                < rhs.height && lhs.breadth < rhs.breadth)
            {
                status = true;
            }
            return status;
        }

        public static bool operator >(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length > rhs.length && lhs.height
                > rhs.height && lhs.breadth > rhs.breadth)
            {
                status = true;
            }
            return status;
        }

        public static bool operator <=(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length <= rhs.length && lhs.height
                <= rhs.height && lhs.breadth <= rhs.breadth)
            {
                status = true;
            }
            return status;
        }

        public static bool operator >=(Box lhs, Box rhs)
        {
            bool status = false;
            if (lhs.length >= rhs.length && lhs.height
               >= rhs.height && lhs.breadth >= rhs.breadth)
            {
                status = true;
            }
            return status;
        }
        public override string ToString()
        {
            return String.Format("({0}, {1}, {2})", length, breadth, height);
        }

    }

    class Tester
    {
        static void Main(string[] args)
        {
            Box Box1 = new Box();          // 声明 Box1，类型为 Box
            Box Box2 = new Box();          // 声明 Box2，类型为 Box
            Box Box3 = new Box();          // 声明 Box3，类型为 Box
            Box Box4 = new Box();
            double volume = 0.0;   // 体积

            // Box1 详述
            Box1.setLength(6.0);
            Box1.setBreadth(7.0);
            Box1.setHeight(5.0);

            // Box2 详述
            Box2.setLength(12.0);
            Box2.setBreadth(13.0);
            Box2.setHeight(10.0);

            // 使用重载的 ToString() 显示两个盒子
            Console.WriteLine("Box1： {0}", Box1.ToString());
            Console.WriteLine("Box2： {0}", Box2.ToString());

            // Box1 的体积
            volume = Box1.getVolume();
            Console.WriteLine("Box1 的体积： {0}", volume);

            // Box2 的体积
            volume = Box2.getVolume();
            Console.WriteLine("Box2 的体积： {0}", volume);

            // 把两个对象相加
            Box3 = Box1 + Box2;
            Console.WriteLine("Box3： {0}", Box3.ToString());
            // Box3 的体积
            volume = Box3.getVolume();
            Console.WriteLine("Box3 的体积： {0}", volume);

            //comparing the boxes
            if (Box1 > Box2)
                Console.WriteLine("Box1 大于 Box2");
            else
                Console.WriteLine("Box1 不大于 Box2");
            if (Box1 < Box2)
                Console.WriteLine("Box1 小于 Box2");
            else
                Console.WriteLine("Box1 不小于 Box2");
            if (Box1 >= Box2)
                Console.WriteLine("Box1 大于等于 Box2");
            else
                Console.WriteLine("Box1 不大于等于 Box2");
            if (Box1 <= Box2)
                Console.WriteLine("Box1 小于等于 Box2");
            else
                Console.WriteLine("Box1 不小于等于 Box2");
            if (Box1 != Box2)
                Console.WriteLine("Box1 不等于 Box2");
            else
                Console.WriteLine("Box1 等于 Box2");
            Box4 = Box3;
            if (Box3 == Box4)
                Console.WriteLine("Box3 等于 Box4");
            else
                Console.WriteLine("Box3 不等于 Box4");

            Console.ReadKey();
        }
    }
}

/*
 * operator 关键字用于在类或结构声明中声明运算符。运算符声明可以采用下列四种形式之一：
 * 
 public static result-type operator unary-operator ( op-type operand )
 public static result-type operator binary-operator ( op-type operand, op-type2 operand2 )
 public static implicit operator conv-type-out ( conv-type-in operand )
 public static explicit operator conv-type-out ( conv-type-in operand )
 * 
 * 
 result-type 运算符的结果类型。
 unary-operator 下列运算符之一：+ - ! ~ ++ — true false
 op-type 第一个（或唯一一个）参数的类型。
 operand 第一个（或唯一一个）参数的名称。
 binary-operator 其中一个：+ - * / % & | ^ << >> == != > < >= <=
 op-type2 第二个参数的类型。
 operand2 第二个参数的名称。
 conv-type-out 类型转换运算符的目标类型。
 conv-type-in 类型转换运算符的输入类型。
 */
