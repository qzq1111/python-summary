"""
使用须知：
1. 安装包：pip install pythonnet
2. 文档地址：https://pythonnet.github.io/ 或者 https://github.com/pythonnet/pythonnet
"""
# coding:utf-8
import clr
# C#代码
"""
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

"""

# 引用Dll，不需要添加后缀
clr.AddReference("TestDll")

# 引入DLL命名空间，并导入定义的类
from TestDll import MyTest

# 实例化类
instance = MyTest()
# 无输入及无返回
instance.Print()
# 有输入及无返回
instance.Print("qin")
# 有输入及输出
add_data = instance.Add(1, 1)
print(add_data)
