using System.Collections;

public class IOManager : IDisposable
{
    private Boolean _disposed;
    private IEnumerator<String> _tokens;
    private const int bufferSize = 131072;
    private StreamReader _inputReader;
    public static StreamReader StandardInput = new(new
        BufferedStream(Console.OpenStandardInput(), bufferSize));
    public static StreamWriter StandardOutput = new(new
        BufferedStream(Console.OpenStandardOutput(), bufferSize));
    public static StreamWriter StandardError = new(new
        BufferedStream(Console.OpenStandardError(), bufferSize));


    public IOManager(String inputFileName = null)
    {
        if (inputFileName != null)
        {
            var fileStream = new FileStream(inputFileName, FileMode.Open, FileAccess.Read);
            var bufferedStream = new BufferedStream(fileStream);
            _inputReader = new StreamReader(bufferedStream);
        }
        else
        {
            _inputReader = StandardInput;
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
        if (_inputReader != StandardInput)
        {
            _inputReader.Dispose();
        }
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
        PrintWithOptions(StandardOutput, args, sep, end);
    }

    public void EPrint(String sep = " ", String end = "\n", params Object[] args)
    {
        PrintWithOptions(StandardError, args, sep, end);
    }

    public void FPrint(String file, String sep = " ", String end = "\n", params Object[] args)
    {
        using (var fileStream = new FileStream(file, FileMode.OpenOrCreate, FileAccess.Write))
        using (var bufferedStream = new BufferedStream(fileStream))
        using (var writer = new StreamWriter(bufferedStream) { AutoFlush = true })
        {
            PrintWithOptions(writer, args, sep, end);
        }
    }

    private void PrintWithOptions(StreamWriter writer, Object[] args, String sep, String end)
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
        writer.Flush();
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