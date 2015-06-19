using System.IO.Ports;
using System;

namespace ConsoleApplication1
{
	class Program
	{
		public static void Main(string[] args)
		{
			SerialPort sp = new SerialPort("/dev/ttyACM0", 115200, Parity.None, 8, StopBits.One);
			sp.Open();
			//byte buff[];
			int input;
			
			for (int index = 0; index < 10; index++)
			{
				//string result = string.Format("{0} Testing", index);
				//sp.Write(result);
				input = sp.ReadChar();
				Console.Write("Recieved: ");
				Console.WriteLine(input);
			}
			
			sp.Close();
		}
	}
}
