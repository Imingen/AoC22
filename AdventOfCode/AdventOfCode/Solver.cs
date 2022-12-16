using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AdventOfCode
{
    public class Solver
    {

        public void SolveDayTwo()
        {

            // A - Rock
            // B - Paper
            // C - Scissor

            // X - Rock
            // Y - Paper
            // Z - Scissor

            var realValues = new Dictionary<string, string>()
            {
                {"A", "Rock" },
                {"B", "Paper" },
                {"C", "Scissor" },
                {"X", "Rock" },
                {"Y", "Paper" },
                {"Z", "Scissor"}
            };


            var pointSettings = new Dictionary<string, int>()
            {
                {"X", 1 },
                {"Y", 2 }, 
                {"Z", 3 },
            };

            var points = 0;
            var points2 = 0;


            string[] lines = System.IO.File.ReadAllLines(@"C:\Users\marisi\source\repos\AdventOfCode2022\AdventOfCode\AdventOfCode\datasets\2.txt");

            foreach (var line in lines)
            {
                var x = line.Split();
                var enemy = x[0];
                var me = x[1];

                if (enemy == "A" && me == "X")
                {
                    points += 3;
                    points += pointSettings[me];

                    points2 += pointSettings["Z"];
                }
                else if(enemy == "A" && me == "Y")
                {
                    Console.WriteLine($"I won with {realValues[me]} over enemy {realValues[enemy]}");
                    points += 6;
                    points += pointSettings[me];

                    points2 += 3;
                    points2 += pointSettings["X"];
                }
                else if(enemy == "A" && me == "Z")
                {
                    Console.WriteLine($"Enemy won with {realValues[enemy]} over my {realValues[me]}");
                    points += pointSettings[me];

                    points2 += 6;
                    points2 += pointSettings["Y"];
                }
                else if(enemy == "B" && me == "Y")
                {
                    points += 3;
                    points += pointSettings[me];

                    points2 += 3;
                    points2 += pointSettings["Y"];
                }
                else if(enemy == "B" && me == "X")
                {
                    Console.WriteLine($"Enemy won with {realValues[enemy]} over my {realValues[me]}");
                    points += pointSettings[me];

                    points2 += pointSettings["X"];
                }
                else if(enemy == "B" && me == "Z")
                {
                    Console.WriteLine($"I won with {realValues[me]} over enemy {realValues[enemy]}");
                    points += 6;
                    points += pointSettings[me];

                    points2 += 6;
                    points2 += pointSettings["Z"];
                }    
                else if(enemy == "C" && me == "X")
                {
                    Console.WriteLine($"I won with {realValues[me]} over enemy {realValues[enemy]}");
                    points += 6;
                    points += pointSettings[me];

                    points2 += pointSettings["Y"];
                }
                else if(enemy == "C" && me == "Y")
                {
                    Console.WriteLine($"Enemy won with {realValues[enemy]} over my {realValues[me]}");
                    points += pointSettings[me];

                    points2 += 3;
                    points2 += pointSettings["Z"];
                }
                else if(enemy == "C" && me == "Z")
                {
                    points += 3;
                    points += pointSettings[me];

                    points2 += 6;
                    points2 += pointSettings["X"];
                }
            }


            Console.WriteLine($"Total points at the end:{points}");
            Console.WriteLine($"Total points at the end for part 2: {points2}");


        }


    }
}
