using System;
using System.IO;
using System.Linq;

namespace misc
{
    class Program
    {
        static void Main(string[] args)
        {
			int GetFuel(int mass) => mass/3-2;
			int GetRecursiveFuel(int fuel) =>
				fuel <= 0 ? 0 :
					GetFuel(fuel) +
					Math.Max(GetRecursiveFuel(GetFuel(fuel)), 0);

			File.ReadAllLines("../input/1/input.txt")
					.Select(l => int.Parse(l))
					.Select(l => GetRecursiveFuel(l))
					.Sum()
					.Dump(); // run in LINQPad or https://stackoverflow.com/questions/2699466/how-do-i-use-the-linqpad-dump-extension-method-in-visual-studio
        }
    }
}
