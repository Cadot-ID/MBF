# -*- coding: utf-8 -*-
import os, sys
import random
import sys
import time
def TheX (s):
        for c in s + '\n':
                sys.stdout.write(c)
                sys.stdout.flush()
                time.sleep(1./1820)
os.system ('clear')
TheX( "\033[37;1m        _______________________________________")
TheX( "       |,-------------------O-----------------,|")
TheX( "       ||\033[36;1mimport\033[37;1m os,random,sys,time            ||")
TheX( "       ||\033[34;1mdef\033[37;1m kntl (s):                        ||")
TheX( "\033[37;1m       ||       for c in s + '/n':            ||")
TheX( "       ||            sys.stdout.write(c)      ||")
TheX( "       ||            sys.stdout.flush()       ||")
TheX( "       ||            time.sleep(1./1820)      ||")
TheX( "\033[37;1m       ||kntl( \033[32;1m'selamat datang master'\033[37;1m)       ||")
TheX( "       ||_____________________________________||")
TheX( "\033[32;1m       |)____________|__________|_____________(|")
TheX( "\033[32;1m      /______|_______|\x1b[00m\033[41m Cadot-ID \033[00m\033[32;1m|______|________\"")
TheX( "\033[37;1m     / _| _| _| _| _| _| _| _| _| _| _| _| _| _| \"")
TheX( "    / ___| _| _| _| _| _| _| _| _| _| _| _|  |  | \"")
TheX( "   / ___| _| _| _| _| _| _| _| _| _| _| _| ______| \"")
TheX( "  / __| _| _| _| _| _| _| _| _| _| _| _| _| _| ___| \"")
TheX( " / _| _| _| _| ________________________| _| _| _| _| \"")
TheX( "|-----------------------------------------------------|")
TheX( ":-----------------------------------------------------:")
print
print ("\033[1;32mMasukkan Username & Password")

username = 'LWHFAC'

password = 'XJ3M72'



def restart():

        ngulang = sys.executable

        os.execl(ngulang, ngulang, *sys.argv)



def main():

        uname = raw_input("username : ")

        if uname == username:

                pwd = raw_input("password : ")



                if pwd == password:

                        print "\033[1;32mAlhamdulilah  masuk juga..",
                        os.system('python http://owmaoabsiamaoansusosnauis')
                        sys.exit()



                else:

                        print "\033[1;32m password salah\033[00m"

                        os.system('xdg-open https://wa.me/6289660267608?text=Hello%20bro%20Iam%20an%20MBF%20user,%20give%20me%20the%20password😄')
                        os.system('clear')

                        restart()



        else:

                print "\033[1;32mUsername salah\033[00m"

                os.system('xdg-open https://wa.me/6289660267608?text=Hello%20bro%20Iam%20an%20MBF%20user,%20give%20me%20the%20password😄')
                os.system('clear')
                restart()



try:

        main()

except KeyboardInterrupt:

        os.system('clear')

        restart()
