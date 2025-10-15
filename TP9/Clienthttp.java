import java . io . * ;
import java . net . * ;

public class Clienthttp
{
	public static void main( String args[] ) throws Exception 
	{
		Socket socket = new Socket( "localhost", 80 );
		OutputStreamWriter osw = new OutputStreamWriter( socket.getOutputStream() );
		IntputStreamReader isw = new IntputStreamReader( socket.getIntputStream() );
		
		BufferedWriter bufOut = new BufferedWriter( osw );
		BufferedReader bufInt = new BufferedReader( isw );
		
		String request = "Get / HTTP/1.0\r\n\r\n"; // requete HTTP
		bufOut.write( request, 0, request.length() );
		bufOuf.flush();
		
		String line = bufIn.readLine(); 
		while( line != null ) {
			System.out.println( line );
			line = bufIn.readLine();
			}
		bufIn.close();
		bufOut.close();
		socket.close();
	}
}
