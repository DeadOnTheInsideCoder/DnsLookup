import socket
import sys


def GetArguments():

   global host
   global path
   global Write
   try:
     
       host = sys.argv[1]
       
   except IndexError:
     
      try:
        
       host = str(input("[?]Host >>"))
       
      except KeyboardInterrupt:
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()
      except EOFError:
        sys.exit()
      except Exception as e:
       print("[!]Error :",str(e))    
   except Exception as e:
     print("[!]Error :",str(e))
     
   try:

     
     path = sys.argv[2]
     Write = True

   except IndexError:
     
     try:
       
      path = str(input("[?]Path >>"))
      if path == "":
        
         Write = False

      else:

        Write = True

        
     except KeyboardInterrupt:
       
        print("[!]You pressed ctr+x")
        print("[*]Exiting...")
        sys.exit()
        
     except EOFError:
       
        sys.exit()
        
     except Exception as e:
       
       print("[!]Error :",str(e))
       sys.exit()
       
   except Exception as e:
     
     print("[!]Error :",str(e))
     sys.exit()


def Lookup():

    global host
    global output
    ipv4 = socket.gethostbyname(host)
    ipv6 = socket.getaddrinfo(host,None,socket.AF_INET6)
    ipv6 = ipv6[0][4][0]
    info = {'host':host,'ipv4':ipv4,'ipv6':ipv6}
    output = "\nHost:     "+str(info['host'])+"\n"+"Ipv4:     "+str(info['ipv4'])+"\n"+"Ipv6:     "+str(info['ipv6'])+"\n"
    print(output)

    
def WriteOut():

    global path
    global Write
    global output

    if Write == True:
      
      try:
        
       file = open(path,"a")
       file.write(output)
       file.close()

      except FileNotFoundError:

        print("[!]Path doesn't exist.")
        sys.exit()

      except Exception as e:

        print("[!]Error: ",str(e))

    
    elif Write == False:

  
       sys.exit()


       
def dnslookup():
   
    GetArguments()
    Lookup()
    WriteOut()
    
dnslookup()
