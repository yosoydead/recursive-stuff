using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace numarare
{
    class Program
    {
        static int[] a = { 1, 2, 3, 5, 7, 8, 9, 1, 2, 4, 2, 1, 5, 9, 4, 2, 3, 1, 4, 4, 5, 6, 8 };
        static int n = a.Length;
        static int x;
        
        //starting at index 0
        static int numarare(int i, int x) {
            if (i == n)
                return 0;

            if (x == a[i])
            {
                Console.WriteLine($"index {i} == x {x}");
                return 1 + numarare(i + 1, x);
            }
            else
                return numarare(i + 1, x);
        }

        //starting at the end of the array
        static int numar(int i, int x)
        {
            if (i < 0)
                return 0;

            if (x == a[i])
            {
                Console.WriteLine($"index {i} == x {x}");
                return 1 + numar(i - 1, x);
            }
            else
                return numar(i - 1, x);
        }
        static void Main(string[] args)
        {
            x = 9;
            Console.WriteLine(numarare(0,x));
            Console.WriteLine(numar(n-1, x));
        }
    }
}
