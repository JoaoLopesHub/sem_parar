from base64 import encode
import paramiko
from paramiko import SSHClient
import time
from datetime import datetime

execucao = open("c:/Users/joao.lopes/Documents/automacao/log1.txt",'a')

def carregar_postos(arquivo):
    postos = open(arquivo,'r',encoding='UTF-8')
    lista_postos = postos.read()
    lista_postos = lista_postos.split('\n')
    qt=0
    for postos in lista_postos:

        ip = postos
        qt+=1
        try:

            class SSH:
                def __init__(self):
                    self.ssh = SSHClient()
                    self.ssh.load_system_host_keys()
                    self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                    self.ssh.connect(hostname= str(ip),port='22',username='pi',password='SemParar')

            Ssh = SSH()

            ###############     Coleta GAMIFICATION     ######################

        
            
            stdin,stdout,stderr = Ssh.ssh.exec_command("cat /etc/abastece/lado1/gamification.json | grep 'active'")
            retorno_lado1 = stdout.read()
            retorno_lado1 = retorno_lado1.split('\n'.encode())

            stdin,stdout,stderr = Ssh.ssh.exec_command("cat /etc/abastece/lado2/gamification.json | grep 'active'")
            retorno_lado2 = stdout.read()
            retorno_lado2 = retorno_lado2.split('\n'.encode())

            execucao.write("Versão Gamification do posto," + str(ip) + "," + str(retorno_lado1) + "," + str(retorno_lado2) + "," '\n')

            print ("Lendo linha: ",qt," Host Analisado :",ip," Status :",retorno_lado1,retorno_lado2)
            

            ###############     ALTERAR GAMIFICATION     ######################

            '''
            co = 'sed -i'  
            mm = 's/"active": true,/"active": false,/g'
            an = '/etc/abastece/lado1/gamification.json'

            command = co + " '" + mm + "' " + " " + an

            stdin,stdout,stderr = Ssh.ssh.exec_command(command, get_pty=True)
            retorno_lado1 = stdout.read()
            retorno_lado1 = retorno_lado1.split('\n'.encode())
            
            co = 'sed -i'  
            mm = 's/"active": true,/"active": false,/g'
            an = '/etc/abastece/lado2/gamification.json'

            command = co + " '" + mm + "' " + " " + an

            stdin,stdout,stderr = Ssh.ssh.exec_command(command, get_pty=True)
            retorno_lado2 = stdout.read()
            retorno_lado2 = retorno_lado2.split('\n'.encode())
            
            execucao.write("Versao abastede do posto," + str(ip) + "," + str(retorno_lado1) + "," + str(retorno_lado2) + "," '\n')
            
            print("Total_Linhas: ",qt," Ip_Servidor :",ip)
            '''
            

            ###############     ALTERAR IFPISTA     ######################

            '''   
            co = 'sed -i'  
            mm = 's/rssiE=.*/rssiE=55/g'
            an = '/var/abastece/SLT/configpista/ifpistas.ini'
            command = co + " '" + mm + "' " + " " + an
            #stdin,stdout,stderr = Ssh.ssh.exec_command(command, get_pty=True)
            retorno = stdout.read()
            retorno = retorno.split('\n'.encode())
            
            execucao.write("Versao abastede do posto," + str(ip) + "," + str(retorno) + "," '\n')
            
            '''

            ###############     COLETA VERSÕES ABASTECE     ######################

            '''

            ###### SATURNO

            stdin,stdout,stderr = Ssh.ssh.exec_command("ls /var/abastece/SLT/saturno3")
            retorno_Sat = stdout.read()
            retorno_Sat = retorno_Sat.split('\n'.encode())

            ####### ABASTECE
            
            stdin,stdout,stderr = Ssh.ssh.exec_command("dpkg -l abastece | grep -E abastece | cut -c20-30")
            retorno_abastece = stdout.read()
            retorno_abastece = retorno_abastece.split('\n'.encode())
            
            ###### ARQUITETURA

            stdin,stdout,stderr = Ssh.ssh.exec_command("arch")
            retorno_arch = stdout.read()
            retorno_arch = retorno_arch.split('\n'.encode())

            print (retorno_arch,retorno_abastece,retorno_Sat)

            execucao.write("Versao abastede do posto," + str(ip) + "," + str(retorno_arch) + "," + str(retorno_abastece) + "," + str(retorno_Sat) + "," '\n')

            '''

            ###############     COLETA VERSÃO FORSETI     ######################

            '''

            #stdin,stdout,stderr = Ssh.ssh.exec_command("dpkg -l forseti | grep -E forseti | cut -c20-30")
            retorno = stdout.read()
            retorno = retorno.split('\n'.encode())

            execucao.write("Versão forseti do posto," + str(ip) + "," + str(retorno) + "," '\n')

            '''

            ###############     COLETA ALEATORIA     ######################

            #stdin,stdout,stderr = Ssh.ssh.exec_command("dpkg -l forseti | grep -E forseti | cut -c20-30")
            #stdin,stdout,stderr = Ssh.ssh.exec_command("cat /usr/bin/autoStartAbastece.sh | grep 'presveic'")
            #stdin,stdout,stderr = Ssh.ssh.exec_command("cat /var/abastece/imagens/VERSION")
            #stdin,stdout,stderr = Ssh.ssh.exec_command("cat /var/abastece/SLT/configpista/ifpistas.ini | grep 'rssiE' | cut -c7-8")
            #stdin,stdout,stderr = Ssh.ssh.exec_command("ls /var/validaabastece/tmp/APL_ABASTECE_2209134_Final.pac")
            #retorno = stdout.read()
            #retorno = retorno.split('\n'.encode())

            #execucao.write("Versão Telas do posto," + str(ip) + "," + str(retorno) + "," '\n')
            
        except:

            execucao.write("erro na coleta da versão," + str(ip) + "," + str(stderr.read()) + "," '\n')

carregar_postos('c:/Users/joao.lopes/Documents/automacao/postos1.txt')
