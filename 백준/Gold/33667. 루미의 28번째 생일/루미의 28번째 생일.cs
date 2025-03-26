using System;

namespace Baekjoon
{
    public class CustomDateTime
    {
        public Int32 year { get; set; }
        public Int32 month { get; set; }
        public Int32 day { get; set; }
        public Int32 hour { get; set; }
        public Int32 minute { get; set; }
        public Int32 second { get; set; }


        public CustomDateTime(Int32 year, Int32 month, Int32 day,
            Int32 hour, Int32 minute, Int32 second)
        {
            this.year = year;
            this.month = month;
            this.day = day;
            this.hour = hour;
            this.minute = minute;
            this.second = second;
        }
    }

    public class Fraction
    {
        public Int64 numerator { get; set; }
        public Int64 denominator { get; set; }

        public Fraction(Int64 numerator, Int64 denominator)
        {
            this.numerator = numerator;
            this.denominator = denominator;
        }

        public static Boolean operator >=(Fraction f1, Fraction f2)
        {
            return f1.numerator * f2.denominator >= f2.numerator * f1.denominator;
        }

        public static Boolean operator <=(Fraction f1, Fraction f2)
        {
            return f1.numerator * f2.denominator <= f2.numerator * f1.denominator;
        }
    }

    public class Program
    {
        static Int32[] monthTable = { 0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31 };
        const Int64 MINUTE_SECONDS = 60;
        const Int64 HOUR_SECONDS = 60 * MINUTE_SECONDS;
        const Int64 DAY_SECONDS = 24 * HOUR_SECONDS;

        private static Boolean IsLeapYear(Int32 year)
        {
            return ((year % 4 == 0) && (year % 100 != 0)) || year % 400 == 0;
        }

        private static Int32 DaysInMonth(Int32 year, Int32 month)
        {
            if (IsLeapYear(year) && month == 2)
            {
                return 29;
            }

            return monthTable[month];
        }

        private static Int64 ToSeconds(CustomDateTime dateTime)
        {
            Int64 totalSeconds = 0;
            var leapYearCount = (dateTime.year - 1) / 4 - (dateTime.year - 1) / 100 +
                                (dateTime.year - 1) / 400;
            totalSeconds += ((Int64)365 * (dateTime.year - 1) + leapYearCount) * DAY_SECONDS;
            for (var month = 1; month < dateTime.month; month += 1)
            {
                totalSeconds += DaysInMonth(dateTime.year, month) * DAY_SECONDS;
            }

            totalSeconds += (dateTime.day - 1) * DAY_SECONDS;
            totalSeconds += dateTime.hour * HOUR_SECONDS;
            totalSeconds += dateTime.minute * MINUTE_SECONDS;
            totalSeconds += dateTime.second;
            return totalSeconds;
        }

        private static Fraction FractionInMonth(CustomDateTime dateTime)
        {
            Int64 totalSeconds = 0;
            totalSeconds += (dateTime.day - 1) * DAY_SECONDS;
            totalSeconds += dateTime.hour * HOUR_SECONDS;
            totalSeconds += dateTime.minute * MINUTE_SECONDS;
            totalSeconds += dateTime.second;
            return new Fraction(totalSeconds,
                DaysInMonth(dateTime.year, dateTime.month) * DAY_SECONDS);
        }

        private static Fraction FractionInYear(CustomDateTime dateTime)
        {
            Int64 totalSeconds = 0;
            for (var month = 1; month < dateTime.month; month += 1)
            {
                totalSeconds += DaysInMonth(dateTime.year, month) * DAY_SECONDS;
            }

            totalSeconds += (dateTime.day - 1) * DAY_SECONDS;
            totalSeconds += dateTime.hour * HOUR_SECONDS;
            totalSeconds += dateTime.minute * MINUTE_SECONDS;
            totalSeconds += dateTime.second;
            return new Fraction(totalSeconds, (365 + (IsLeapYear(dateTime.year)
                ? 1
                : 0)) * DAY_SECONDS);
        }

        public static void Main(String[] args)
        {
            var T = Int32.Parse(Console.ReadLine());
            for (var i = 0; i < T; i += 1)
            {
                var input = Console.ReadLine().Split(' ');
                var a1 = Int32.Parse(input[0]);
                var a2 = Int32.Parse(input[1]);
                var a3 = Int32.Parse(input[2]);
                var a4 = Int32.Parse(input[3]);
                var a5 = Int32.Parse(input[4]);
                var a6 = Int32.Parse(input[5]);
                var birthDate = new CustomDateTime(a1, a2, a3, a4, a5, a6);
                input = Console.ReadLine().Split(' ');
                var b1 = Int32.Parse(input[0]);
                var b2 = Int32.Parse(input[1]);
                var b3 = Int32.Parse(input[2]);
                var b4 = Int32.Parse(input[3]);
                var b5 = Int32.Parse(input[4]);
                var b6 = Int32.Parse(input[5]);
                var unit = Console.ReadLine();
                var currentDate = new CustomDateTime(b1, b2, b3, b4, b5, b6);

                if (unit == "Year")
                {
                    var currentFraction = FractionInYear(currentDate);
                    var birthFraction = FractionInYear(birthDate);
                    var isFullYear = currentFraction >= birthFraction
                        ? 1
                        : 0;
                    Console.WriteLine(b1 - a1 - 1 + isFullYear);
                }
                else if (unit == "Month")
                {
                    var currentFraction = FractionInMonth(currentDate);
                    var birthFraction = FractionInMonth(birthDate);
                    var isFullMonth = currentFraction >= birthFraction
                        ? 1
                        : 0;
                    Console.WriteLine((b1 - a1) * 12 + b2 - a2 - 1 + isFullMonth);
                }
                else if (unit == "Day")
                {
                    var birthTotalSeconds = ToSeconds(birthDate);
                    var currentTotalSeconds = ToSeconds(currentDate);
                    var diffSeconds = currentTotalSeconds - birthTotalSeconds;
                    Console.WriteLine(diffSeconds / DAY_SECONDS);
                }
            }
        }
    }
}