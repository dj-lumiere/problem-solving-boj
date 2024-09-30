using System.Collections;

public class IOManager : IDisposable
{
    private Boolean _disposed;
    private TextReader _inputReader;
    private IEnumerator<String> _tokens;

    public IOManager(String inputFileName = null)
    {
        if (inputFileName != null)
        {
            _inputReader = new StreamReader(inputFileName);
        }
        else
        {
            _inputReader = Console.In;
        }

        InitializeTokens();
    }

    public void Dispose()
    {
        Dispose(true);
        GC.SuppressFinalize(this);
    }

    private void InitializeTokens()
    {
        var content = _inputReader.ReadToEnd();
        _inputReader.Dispose();
        var tokensArray = content.Split((Char[])null, StringSplitOptions.RemoveEmptyEntries);
        _tokens = ((IEnumerable<String>)tokensArray).GetEnumerator();
    }

    public String Input()
    {
        if (_tokens.MoveNext())
        {
            return _tokens.Current;
        }

        Dispose();
        return null;
    }

    public void Print(String sep = "\n", String end = "\n", params Object[] args)
    {
        PrintWithOptions(Console.Out, args, sep, end);
    }

    public void EPrint(String sep = " ", String end = "\n", params Object[] args)
    {
        PrintWithOptions(Console.Error, args, sep, end);
    }

    public void FPrint(TextWriter file, String sep = " ", String end = "\n", params Object[] args)
    {
        PrintWithOptions(file, args, sep, end);
    }

    private void PrintWithOptions(TextWriter writer, Object[] args, String sep, String end)
    {
        var flattenedArgs = new List<String>();
        foreach (var arg in args)
        {
            if (arg is IEnumerable enumerable && !(arg is String))
            {
                foreach (var item in enumerable)
                {
                    flattenedArgs.Add(item.ToString());
                }
            }
            else
            {
                flattenedArgs.Add(arg?.ToString());
            }
        }

        var output = String.Join(sep, flattenedArgs);
        writer.Write(output + end);
    }

    protected virtual void Dispose(Boolean disposing)
    {
        if (!_disposed)
        {
            if (disposing)
            {
                if (_inputReader != null)
                {
                    _inputReader.Dispose();
                    _inputReader = null;
                }
            }

            _disposed = true;
        }
    }

    ~IOManager()
    {
        Dispose(false);
    }
}

internal class Program
{
    private static void Main(String[] args)
    {
        using (var io = new IOManager())
        {
            var answers = new List<String>();
            var t = Int32.Parse(io.Input());
            for (var hh = 1; hh <= t; hh += 1)
            {
                var a = Int32.Parse(io.Input());
                var b = Int32.Parse(io.Input());
                answers.Add($"{a + b}");
            }

            io.Print("\n", "\n", answers);
        }
    }
}