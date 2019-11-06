using System;

namespace TestDll
{
    public class MyTest
    {

        public void Print()
        {

            Console.WriteLine("Hello world!!!");
        }

        public void Print(string msg)
        {

            Console.WriteLine($"Hello {msg}!!!");
        }

        public double Add(double x, double y)
        {
            return x + y;

        }
    }

}
