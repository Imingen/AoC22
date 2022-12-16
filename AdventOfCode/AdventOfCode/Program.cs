using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Which day are you solving? Enter number 1-24: \n");
            var day = Convert.ToInt32(Console.ReadLine());

            Console.WriteLine($"Solving day {day}"); 
            var solver = new Solver();

            switch (day)
            {
                default:
                    Console.WriteLine("No day picked try again");
                    break;
                case 2:
                    solver.SolveDayTwo();
                    break;
                case 3:
                    solver.SolveDayThree();
                    break;

            }
        }
    }
}
