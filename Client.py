import socket
from sage.all import*

def Main():
    host = '127.0.0.1'
    port = 51001
    server = ('127.0.0.1',51000)

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)#socket creation
    s.bind((host, port))

    f_field = raw_input("Give size of finite field" " \n ->")
    s.sendto(f_field, server)#fuction used to send data through socket

    n_bits = raw_input("Give number of bits for each codeword" " \n ->")
    s.sendto(n_bits, server)


    if (f_field in Primes()) == true: #checks if input is Prime number
        C = codes.ParityCheckCode(GF(f_field), n_bits) #if it is true creates code
        min_d = C.minimum_distance()#sage's fuction to find hamming distance
        s.sendto(min_d, server)
        err_det = C.minimum_distance()-1
        err_cor = (C.minimum_distance()-1)/2
        print "Code's minimum distance is :",min_d
        print "Code can detect up to",err_det, "errors"
        print "Code can correct up to",int(err_cor), "errors"
    else:
        print "The parameters you gave do not respond to a parity-check code"
        quit()#terminates script


    error_weigth = raw_input("Give weight of noise" " \n ->")
    s.sendto(error_weigth, server)


    if C is not None:
        if C.dual_code() is not None:
            C=C.dual_code()
            noise = channels.StaticErrorRateChannel(c.ambient_space(), error_weigth)#creates noise based on the error weight user chose
        else:
            noise = channels.StaticErrorRateChannel(c.ambient_space(), error_weigth)

        for i in range(0,20):
            random_cword = C.random_element()#random codeword
            cword_noise = noise.transmit(random_cword)#random codeword with noise
            cwords_to_send.append(cword_noise)
            s.send(repr(cwords_to_send))

        print cwords_to_send
    s.close()
if __name__ == '__main__':
    Main()
