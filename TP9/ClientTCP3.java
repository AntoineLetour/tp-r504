import java . io . * ;
import java . net . * ;

public class ClientTCP3
{
	public static void main( String args[] ) throws Exception 
	{
	Socket socket = new Socket( "localhost", 2016 );
// envoi au serveur
	DataOutputStream dOut = new DataOutputStream( socket.getOutputStream() );
	dOut.writeUTF( args[0] );

// attente que le serveur me renvoie la chaine inversée$	
	DataInputStream dIn = new DataInputStream ( socket.getInputStream());
	String msg = dIn.readUTF();
	System.out.println( "Message: " + msg);
	socket.close();
	}
}
