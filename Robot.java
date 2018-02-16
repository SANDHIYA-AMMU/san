package robot;
import java.util.Scanner;
import java.io.*;
class Robot {
    int col;
    int row;
    char direction;   //("Enter e/w/n/s:")
    int initial_posx,initial_posy,n;
    
char[]  s=new char[10];
public static void main(String[] args) throws IOException {
    Robot f=new Robot();
f.getdata();
for(int i=0;i<f.n;i++)
{
    if(f.s[i]=='m')
    {
        f.move();
    }
    else if(f.s[i]=='r'){
        f.rotate();
    }
}

System.out.println("The final position of robot after all moves is  "+f.initial_posx+","+f.initial_posy);
    }
public void getdata()
{
    
Scanner reader = new Scanner(System.in);
System.out.println("Enter row");
 row=reader.nextInt();
System.out.println("Enter col");
    col=reader.nextInt();
System.out.println("Enter initial_posx");
    initial_posx=reader.nextInt();
    System.out.println("Enter initial_posy");
    initial_posy=reader.nextInt();
System.out.println("Enter the direction (n/s/e/w):");
   direction = reader.next().charAt(0);
   System.out.println("Enter number of instructions");
   n=reader.nextInt();
   for(int i=0;i<n;i++){
       s[i]=reader.next().charAt(0);

       
   }
    
}
    public void move()
    {
        
        switch(direction)
        {
            case 'n':if((initial_posx-1)!=0)  initial_posx=initial_posx-1;break;    
            case 's':if((initial_posx+1)<row)  initial_posx=initial_posx+1;break;
            case 'w':if((initial_posy-1)!=0)  initial_posy=initial_posy-1;break;
            case 'e':if((initial_posy+1)< col) initial_posy=initial_posy+1;break;
            default:
                System.out.println("Invalid move");       
        }
        
    }
    public void rotate()
    {
        switch(direction)
        {
            case 'n':direction='e';break;    
            case 's':direction='w';break;
            case 'w':direction='n';break;
            case 'e':direction='s';break;
            default:
                System.out.println("Invalid rotate cmd");       
        }
        
    }
}
