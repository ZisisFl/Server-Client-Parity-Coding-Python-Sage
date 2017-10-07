import socket
from sage.all import*

def Main():
    host = '127.0.0.1'
    port = 51000
    final_list = []

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)##socket creation
    s.bind((host,port))

    print "Server Started."

    f_field = s.recv(1024)#fuction to recieve data with limit 1024bytes
    print "Size of Finite Field = " + str(f_field)
    f_field = sage_eval(f_field)#sage's fuction to turn data into sage object

    n_bits = s.recv(1024)
    print "Number of bits for each codeword = " + str(n_bits)
    n_bits = sage_eval(n_bits)

    min_d = s.recv(1024)
    print "Code's minimum distance = " + str(min_d)
    min_d = sage_eval(min_d)

    error_weigth = s.recv(1024)
    print "Weight of noise =" + str(error_weigth)
    error_weigth = sage_eval(error_weigth)

    list_noise = s.recv(1024)
    list_noise = sage_eval(list_noise)
    print "List of codewords as sage object =" ,list_noise

    serverC = codes.ParityCheckCode(GF(param1), param2)#creation of parity check code once again
    serverC = severC.dual_code()#use of dual code
    for i in range(0,20):
        final_list = vector(GF(f_field), list_noise[i])
        serverC_decoded = serverC.decode_to_code(final_list)

    print final_list

    print "Codewords with noise decoded"
    c.close()

if __name__ == '__main__':
    Main()
