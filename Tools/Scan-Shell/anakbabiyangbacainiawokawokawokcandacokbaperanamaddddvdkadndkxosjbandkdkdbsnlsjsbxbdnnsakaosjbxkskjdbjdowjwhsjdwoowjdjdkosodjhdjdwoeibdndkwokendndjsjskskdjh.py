#!/usr/bin/python
# PENULIS OLEH MR-FUKURO 
#RECODE ITU TIDAK MEMBUAT MU JADI PENCIPTA KODE ^_^
#YA TUHAN SAYA BERSUMPAH, SEMOGA SAYA MANDUL 7 TURUNAN JIKA RECODE SCRIPT INI,..
#HAYOLOH UDAH SUMPAH, WMWKWK
#RECODE? MANDUL LAH KAU!! 
# ==== (((- + - COLOR - + -))) ==== #
M = '\033[1;31m' #RED
H = '\033[1;32m' #GREEN
K = '\033[1;33m' #YELLOW 
U = '\033[1;34m' #PURPLE 
P = '\033[1;35m' #PINK 
C = '\033[1;36m' #CYAN 
W = '\033[1;37m' #WHITE

from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import argparse
import sys
import time

global starttime

class ZeroScann():

    def __init__(self):
        self.scan()
        
    def scan(self):
        # argument parser like shit
        parser = argparse.ArgumentParser(prog="--", description="Simple Find Shell in Website")
        parser.add_argument("-u", dest="domain", help="your url")
        parser.add_argument("-w", dest="wordlist", help="your wordlsit")
        args = parser.parse_args()
        if not args.domain:
            sys.exit(""+W+"usage: - - ")
        if not args.wordlist:
            sys.exit(""+W+"usage: - - ")
            
        # handle url website format
        site = args.domain
        print(""+W+"Start Scan!... ")
        print(""+W+"Mohon Tunggu Sebentar...") 
        time.sleep(3)
        if not site.startswith("http://"):
            site = "http://"+site
        if not site.endswith("/"):
            site = site+"/"
        # load wordlist
        try:
            pathlist = args.wordlist
            wlist = open(pathlist, "r")
            wordlist = wlist.readlines()
        except FileNotFound as e:
            print(""+M+" - - ")
            exit()
        finally:
            try:
                wlist.close()
            except:
                print(""+W+"Close - - ")
        # user-agent
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
        #list to hold the results we find
        found = []
        # respon code
        resp_codes = {403 : "403 forbidden", 401 : "401 unauthorized"}
        # loop with join pathlist
        starttime = time.time()
        for psx in wordlist:
            try:
                psx = psx.replace("\n", "")
                url = site+psx
                req = Request(url, headers={"User-Agent": user_agent})
                time.sleep(0.1)
                try:
                    connection = urlopen(req)
                    print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[92mFound :","\033[0m/"+psx)
                    found.append(url)
                    
                except HTTPError as e:
                    if e.code == 404:
                        print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[91mError :","\033[0m/"+psx)
                    else:
                        print("\033[96m[\033[90m{0}\033[96m]".format(time.strftime("%H:%M:%S")),"\033[92mInfo :","\033[33m/"+psx,"\033[92mstatus:\033[33m",resp_codes[e.code])
                        
                except URLError as e:
                    sys.exit("\033[31m[!] Upss, Cek Koneksi Jaringan Kamu")
                except Exception as er:
                    
                    print("\033[93m[!] \033[0mExit Program")
                    time.sleep(3)
                    exit()
            except KeyboardInterrupt as e:
                print(""+C+"CTRL+C Terdeteksi")
                print("\033[96m[!] \033[0mExit Program")
                time.sleep(2)
                exit()
        
        if found:
            print(""+C+"_::"+H+"Result Found"+C+"::_"+H+" ")
            print("\n".join(found))
            print("\033[96m[?] \033[0mTime Elasped: \033[35m%.2f\033[0m Seconds" % float(time.time()-starttime))
        else:
            print("\n\033[96m[!] \033[0mCould Not Find Any Admin")
            print("\033[96m[?] \033[0mTime Elasped: \033[33m%.2f\033[0m Seconds" % float(time.time()-starttime))
                
    def banner():
        # just the screen display like this
        info = """\033[1;32m
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
■ Tools Type : Scanner Shell  ■
■ Author Coding By : MrFukuro ■
■ Version : 1.8               ■
■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■
              """
        return info
    print(banner())
                
if __name__ == '__main__':
    ZeroScann()
