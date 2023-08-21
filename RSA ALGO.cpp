#include<iostream>
using namespace std;
int main()
{
   long int p;
   long int q;
   bool is_prime;
   bool i_prime;

   do
   {
   
    cout<<"Enter P = ";
    cin>>p;
   
if(p==0 || p==1)
          is_prime=false;
 
    for(int i = 2; i <= p/2; i++)  
   {  
      is_prime=true;
      if(p % i == 0)  
      {  
          is_prime=false;
          break;  
      }  
   }
      if (is_prime)
          cout << "Number is Prime."<< endl;  
      else
     cout<<"Number is not Prime."<<endl;
   
   }while (!is_prime);
   

	do
   {
   
    cout<<"Enter Q = ";
    cin>>q;
   
if(q==0 || q==1)
          i_prime=false;
 
    for(int i = 2; i <= q/2; i++)  
   {  
   	  i_prime=true;
      if(q % i == 0)  
      {  
          i_prime=false;
          break;  
      }  
   }
      if (i_prime)
          cout << "Number is Prime."<< endl;  
      else
     cout<<"Number is not Prime."<<endl;
   
   }while (!i_prime);

    long int n=p*q;
   
      cout<<"\n"<<"n = p*q = "<<n<<endl;

    int totient = (p-1)*(q-1);
   
     cout<<"\n"<<"Totient = "<< totient << endl;

 
    int e;   //Public Key
   
    do
    {

    cout<<"Enter values of e which is the pubic key = ";
    cin>>e;
    if( e>totient || e%2==0 )
     {
      cout<<"\nEntered value of e must be less then totient and not an even number."<<endl<<endl;
     }
    else
      cout<<endl;
 
}while(e>totient || e%2==0 );

     
    long int d;  //Private key
    float f;
     
    for(float i=1;i<e;i++)
    {
      f=((i*totient)+1)/e;
     
      if(f==static_cast<int>(f))
      {
        d=f;
  cout<<"Private Key = "<<d<<endl;
      }
    }
 
    int length;
   
    cout<<"\nEnter length of string = ";
    cin>>length;
   
    cout<<"\nEnter String = ";
    char msg[length];
   
    for(int i=0;i<length;i++)
    {
      cin>>msg[i];  
    }
      cout<<"\nOriginal message that you want to encrypt = ";
    for(int i=0;i<length;i++)
    {
      cout<<msg[i];
    }
      cout<<endl;

cout<<"\nTo encrypt message using RSA algoritm"<<endl;

    cout<<"\nFormula :     Cipher Text = m * e mod n         where m = Length of String "<<endl;
 
    long int cipher;

    cipher =  (length * e) % n;
   
    cout<<"Cipher Key = "<< cipher <<endl;

    cout<<"\nTo decrypt message using RSA algoritm."<<endl;

    cout<<"\nFormula :     Plain Text  = c * d mod n         where d = Private Key & c = Cipher Key "<<endl;

    long int decipher;

    decipher =  (cipher * d ) % n;
   
    cout<<"Plain Text Key = "<< decipher << endl;

    int j;
  do
  {

      cout << "\nPlease choose following options : \n";
      cout << "1 = Encrypt the string.\n";
      cout << "2 = Decrypt the string.\n";
      int x;
   
      int pub_key,pri_key;
      cin >> x;
     
    switch(x)
   {
      case 1:
      cout<<"\nEnter public key to encrypt message = ";
      cin>>pub_key;
     
      if(pub_key==e)
      {
         for(int i = 0; (i < length && msg[i] != '\0');  i++)
            msg[i] = msg[i] + cipher;
           
         cout << "\nEncrypted string = " << msg << endl;
         break;
      }
      else
      {
        cout<<"Invalid Key."<<endl;
        break;
      }
     
      case 2:
      cout<<"Enter private key to decrypt message = ";
      cin>>pri_key;
     
      if(pri_key==d)
      {
         for(int i = 0; (i < length && msg[i] != '\0'); i++)
            msg[i] = msg[i] - cipher;

         cout << "\nDecrypted string = " << msg << endl;
         break;
      }
      else
      {
        cout<<"invalid Key."<<endl;
        break;
      }
     
      default:
         cout << "\nInvalid Input!!!\n";
   }
   
   cout<<"Press 1 to run again."<<endl;
   cout<<"Press 2 to exit."<<endl;
   cin>>j;
   
  } while(j!=2);
   
    system("pause");
    return 0;
}
