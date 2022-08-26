using System;
using System.Text;

namespace c5
{
    class Program
    {
        static void Main()
        {
            string fname, lname;
            fname = "Rowan";
            lname = "Atkinson";

            string fullname = fname + lname;
            Console.WriteLine("Full Name: {0}", fullname);
            string try0 = String.Concat(fname, lname);
            Console.WriteLine(" ");
            Console.WriteLine("Full Name: {0}", fullname);

            //通过使用 string 构造函数
            char[] letters = { 'H', 'e', 'l', 'l', 'o' };
            string greetings = new string(letters);
            Console.WriteLine("Greetings: {0}", greetings);

            //方法返回字符串
            string[] sarray = { "Hello", "From", "Tutorials", "Point" };
            string message = String.Join(" ", sarray);
            Console.WriteLine("Message: {0}", message);

            //用于转化值的格式化方法
            DateTime waiting = new DateTime(2012, 10, 10, 17, 58, 1);
            string chat = String.Format("Message sent at {0:t} on {0:D}",
            waiting);
            Console.WriteLine("Message: {0}", chat);
            //Console.ReadKey();

            Console.WriteLine("------------------------------");

            Program p = new Program();
            p.str(ref fname,ref lname);
        }

        public void str(ref string s1,ref string s2)
        {
            s1 = "This is a text!";
            s2 = "This is a text!";
            int con = String.Compare(s1, s2);
            Console.WriteLine("The answer is :"+con);

            string ans1 = s1.ToLower();
            Console.WriteLine(ans1);

            bool ans2 = s1.Contains("a");
            Console.WriteLine(ans2);

            int ans3 = s1.IndexOf("is");
            Console.WriteLine(ans3);

            string ans4 = s1;
            string anst = ans4.Replace("is", "IS");
            Console.WriteLine(anst);

            string[] ans5 = ans4.Split();
            ans5[ans3] = "I";
            Console.WriteLine(ans5);
        }

    }
}
