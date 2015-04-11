namespace ConsoleApplication1
{
	class Program
	{
		public static void Main(string[] args)
		{
			SerialPort sp = new SerialPort("/dev/ttyAMA0", 115200, Parity.None, 8, StopBits.One);
			sp.Open();
			for (int index = 0; index < 10; index++)
			{
				string result = string.Format("{0} Testing", index);
				sp.Write(result);
			}
			sp.Close();
		}
	}
}
