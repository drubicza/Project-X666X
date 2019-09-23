red='\033[1;31m'
green='\033[1;32m'
yellow='\033[1;33m'
purple='\033[1;34m'
pink='\033[1;35m'
cyan='\033[1;36m'
white='\033[1;37m'
clear
figlet  "   YOUTUBE"  | lolcat
echo
echo "  MENU : " | lolcat
echo $white"  ____"
echo
echo "      1) DOWNLOAD VIDEO YOUTUBE MP4" | lolcat
echo $white"      ==============X=============="
echo "      2) DOWNLOAD MUSIK YOUTUBE MP3" | lolcat
echo $white"      ==============X=============="
echo $cyan"      X"$white")"$green" KELUAR" $yellow
echo
read -p "PILIH MENU : " auto
case $auto in
1) echo
echo "_::MASUKKAN LINK YOUTUBE::_" | lolcat
read link
youtube-dl -f mp4 $link
echo
ls
echo "CARA SIMPAN : | EX : $ cp 'VideoBokep *_*' /sdcard (Tanpa Tanda Dolar)" | lolcat
echo "JIKA SUDAH LIHAT DI PENYIMPANAN INTERNAL" | lolcat
;;
2) echo
echo "_::MASUKKAN LINK YOUTUBE::_" | lolcat
echo
read link
youtube-dl --extract-audio --audio-format mp3 $link
echo
ls
echo
echo "CARA SIMPAN | EX : $ cp 'SuaraMendesah *_*' /sdcard (Tanpa Tanda Dolar)" | lolcat
echo "JIKA SUDAH LIHAT DI PENYIMPANAN INTERNAL" | lolcat
;;
x) exit
;;
X) exit
;;
*) echo $red"CEK KEMBALI NOMOR YANG ANDA PILIH *_*"
esac
