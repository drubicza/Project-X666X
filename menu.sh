#!/usr/bin/bash

cmd () {
    cd "Tools/$1"
    case $(echo "$2" | awk -F'.' '{print $NF}') in
    sh) bash "$2"
        ;;
    py) python2 "$2"
        ;;
    php) php "$2"
        ;;
    *)  echo "File tidak diketahui!"
        ;;
    esac
}

case $((RANDOM % 3)) in
0)  echo """
┈┏━━━━━━┓
┈┈▏╱╱╱╱▕
┈┈┣━┳━┳┫
┈━╋━┻━┻╋━
┈╭┫▊┃┃▊┣╮┈╭╯
┈┃┃▔╰╯▔┃┃╭╯
┈╰┫┏━━▂▂▂█
┈┈╭╰━━╯╮
┈┈╭╭╭╯╮╮
╱▔▕▔╲╱▔▏▔╲
▏┃▕▁╱╲▁▏┃▕
¯¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿ '̿̿̿̿̿̿\̵͇̿̿\=(•̪̀●́)=o/̵͇̿̿/'̿̿ ̿ ̿̿¯¯̿̿¯̿̿'̿̿̿̿̿̿̿'̿̿'̿̿̿̿̿'̿̿̿)͇̿̿)̿̿̿̿
""" | lolcat
    ;;
1)  echo """
╯▅╰╱▔▔▔▔▔▔▔╲╯╯☼
▕▕╱╱╱╱╱╱╱╱╱╲╲╭╭
▕▕╱╱╱╱╱╱╱╱┛▂╲╲╭
╱▂▂▂▂▂▂╱╱┏▕╋▏╲╲
▔▏▂┗┓▂▕▔┛▂┏▔▂▕▔
▕▕╋▏▕╋▏▏▕┏▏▕╋▏▏
▕┓▔┗┓▔┏▏▕┗▏┓▔┏▏
""" | lolcat
    ;;
2)  echo """
╭━━━━━━━╮
┃       ● ══    ┃
┃███████┃
┃███████┃
┃███████┃╔══╗
┃███████┃║██║
┃███████┃║(O)║♫ ♪ ♫ ♪
┃███████┃╚══╝
┃███████┃▄ █ ▄ █ ▄ ▄ █ ▄ █ ▄ █
┃███████┃Min- - - - - - - - - - - -●Max
┃         ○        ┃
╰━━━━━━━╯
""" | lolcat
    ;;
esac

cat <<__EOL__
[i] Menu tools:
     1. Spam SMS v1
     2. Spam SMS v2
     3. Spam Call
     4. DDoS
     5. WebDav
     6. Script Deface
     7. Scan SQLi
     8. Hack FB
     9. Tombol Termux
    10. Encrypt Text
    11. Youtube Downloader
    12. Scan Admin
    13. Scan Shell
    14. Install Metasploit
    15. Bypass Linkduit
    16. Jadwal Sholat
    17. Virus Download
__EOL__
read -p "[?] Masukkan pilihan: " perantara

case $perantara in
1)  cmd "SpamSmsV1" Makfjoshdbifbjsisbdbdkiabwbddxhsjschjsd.sh
    ;;
2)  cmd "SpamSmsV2" dviabbsidhdsoehbdidhajowhdbdjsjsbs.sh
    ;;
3)  cmd "SpamCall" godbekowhddoaheoejdhdaowjhdhdoa.php
    ;;
4)  cmd "DDos" KopsYuanzgdihabddihvHvxxxHushsbdid.sh
    ;;
5)  cmd "Webdav" LopLopYYyyXxxShJxCxcxcBabybkBabyksXcvXcv.sh
    ;;
6)  cmd "Script-Deface" vosjsbeoidbosobsidhchoabsbdhc.py
    ;;
7)  cmd "Scan-Sqli" hdooanwpwjdbxoabsisodbbxosbsd.py
    ;;
8)  cmd "Hack-Fb" ksbwoowbdosjjapwndkxpabejdoahwdii.py
    ;;
9)  cmd "Tombol-Termux" dhisiwbwodidbdoajbsndidjxkshdiajbejd.py
    ;;
10) cmd "Encrypt-Text" __Encrypt__.php
    ;;
11) cmd "Yt-Dl" XcxcxcxcxcxcxcxcxcxcHhHhHh.sh
    ;;
12) cmd "Scan-Admin" psjdnoxhaekidbcishejdihfjsiwbdbdhishd.sh
    ;;
13) cmd "Scan-Shell" Polosangfibashhdhksgiehdbdkshdvdxjjsbd.sh
    ;;
14) cmd "InstallMetasploit" vdoajneieibdoabekdkoxba9ehdnx.sh
    ;;
15) cmd "Bypass-Linkduit" gdibabejdhdvsoavddohsbsoidbdbajsdjhxh.sh
    ;;
16) cmd "Jadwal-Shalat" HhhhhXxxxzCccshdusvdusvsdhiavxvsjs.sh
    ;;
17) cmd "Virus-Download" sijsbakoahsldnsowjebdodnksjsbdjxbc.py
    ;;
*)  echo "Pilihan salah"
    ;;
esac
