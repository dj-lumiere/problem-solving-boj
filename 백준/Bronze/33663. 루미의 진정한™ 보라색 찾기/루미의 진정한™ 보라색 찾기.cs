using System;
using System.Linq;

namespace ProblemSolving
{
    public class BOJ33663
    {
        public static (Double, Double, Double) RGBToHSV(Int32 r, Int32 g, Int32 b)
        {
            Double h, s, v, m;
            v = Math.Max(r, Math.Max(g, b));
            m = Math.Min(r, Math.Min(g, b));
            s = 255.0 * (v - m) / v;
            if (r == v)
            {
                h = 60.0 * (g - b) / (v - m);
            }
            else if (g == v)
            {
                h = 120.0 + 60.0 * (b - r) / (v - m);
            }
            else
            {
                h = 240.0 + 60.0 * (r - g) / (v - m);
            }
            if (h < 0)
            {
                h += 360.0;    
            }
            return (h, s, v);
        }

        public static void Main(string[] args)
        {
            Int32 hLow, hHigh, sLow, sHigh, vLow, vHigh, r, g, b;
            var hLine = Console.ReadLine().Split(' ').Select(Int32.Parse).ToArray();
            hLow = hLine[0];
            hHigh = hLine[1];
            var sLine = Console.ReadLine().Split(' ').Select(Int32.Parse).ToArray();
            sLow = sLine[0];
            sHigh = sLine[1];
            var vLine = Console.ReadLine().Split(' ').Select(Int32.Parse).ToArray();
            vLow = vLine[0];
            vHigh = vLine[1];
            var rgbLine = Console.ReadLine().Split(' ').Select(Int32.Parse).ToArray();
            r = rgbLine[0];
            g = rgbLine[1];
            b = rgbLine[2];
            var (h, s, v) = RGBToHSV(r, g, b);
            if (hLow <= h && h <= hHigh && sLow <= s && s <= sHigh && vLow <= v && v <= vHigh)
            {
                Console.WriteLine("Lumi will like it.");
            }
            else
            {
                Console.WriteLine("Lumi will not like it.");
            }
        }
    }
}