namespace c3
{
    using System;

    public struct define1
    {
        const int var1 = 10;
        const string var2 = "Hello World!\n";

        public int a;
        public string str;
    }

    class change
    {
        int change1(int a,int b)
        {
            return a + b;
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            //if else while do...while

            //c# 会多一个 foreach

            int[] a = new int[] { 1, 2, 4, 3, 5, 1, 2, 3, 4 };
            int[] b = new int[20];//int b[20]
            int[] c = new int[20];
            int id = 0;
            for(int i = 1; i <= 10; i++)
            {
                b[i - 1] = i;
            }

            foreach(int i in a)
            {
                c[id] = a[id] + b[id];
                Console.WriteLine(c[id]);
                id++;
            }
        }
    }
}
