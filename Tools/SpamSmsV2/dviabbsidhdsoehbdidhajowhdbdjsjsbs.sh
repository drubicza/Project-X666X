GREEN=$(tput setaf 2)
WHITE=$(tput setaf 7)
CYAN=$(tput setaf 6)
RED=$(tput setaf 1)
YELLOW=$(tput setaf 3)
NORMAL=$(tput sgr0)
function finish() {
exit
}
LIMITATOR=15
trap finish SIGINT
function nebanner(){
clear
toilet -f future "  SPAM SMS V2 " | lolcat
echo
}
function negetgan(){
bypass=$(curl -s 'http://sms.payuterus.biz/alpha/index.php?a=keluar' \
-H 'Connection: keep-alive' \
-H 'Pragma: no-cache' \
-H 'Cache-Control: no-cache' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
-H 'Referer: http://sms.payuterus.biz/alpha/send.php' \
-H 'Accept-Encoding: gzip, deflate' \
-H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \
-H 'Cookie: _ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1' --compressed --insecure | grep "value" | grep "name" | grep -oP 'value="\K[^"]+')
okeey1=$(curl -s 'http://sms.payuterus.biz/alpha/index.php?a=keluar' \
-H 'Connection: keep-alive' \
-H 'Pragma: no-cache' \
-H 'Cache-Control: no-cache' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
-H 'Referer: http://sms.payuterus.biz/alpha/send.php' \
-H 'Accept-Encoding: gzip, deflate' \
-H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \
-H 'Cookie: _ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035; _gat=1' --compressed --insecure | grep "span" | grep -Po "\d \S \d")
if [[ $okeey1 =~ "+" ]]; then
ok=`expr $okeey1 | bc`
elif [[ $okeey =~ "-" ]]; then
ok=`expr $okeey1 | bc`
elif [[ $okeey1 =~ "/" ]]; then
ok=`expr $okeey1`
fi
okeey=$(curl -s "http://sms.payuterus.biz/alpha/send.php" \
-H 'Connection: keep-alive' \
-H 'Pragma: no-cache' \
-H 'Cache-Control: no-cache' \
-H 'Origin: http://sms.payuterus.biz' \
-H 'Upgrade-Insecure-Requests: 1' \
-H 'Content-Type: application/x-www-form-urlencoded' \
-H 'User-Agent: Mozilla/5.0 (Linux; Android 4.4.2; Nexus 4 Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.114 Mobile Safari/537.36' \
-H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
-H 'Referer: http://sms.payuterus.biz/alpha/' \
-H 'Accept-Encoding: gzip, deflate' \
-H 'Accept-Language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7' \
-H 'Cookie: _ga=GA1.2.131924726.1560439960; PHPSESSID=jjrqqaakmfcgfgbtjt8tve5595; _gid=GA1.2.1969561921.1561024035' --data "nohp=$now&pesan=$psn&captcha=$ok&key=$bypass" --compressed --insecure | grep -o 'value="[^"]*"')
if [[ $okeey =~ "SMS Gratis Telah Dikirim" ]]; then
echo "${WHITE}[${GREEN}✓${WHITE}]${GREEN} SMS BERHASIL DI KIRIM"
else
echo "${WHITE}[${RED}✘${WHITE}]${RED} SMS GAGAL DI KIRIM! "
echo "${WHITE}[${GREEN}✓${WHITE}]${GREEN} HARAP GANTI ISI PESAN ${WHITE}-${RED}$psn${WHITE}-"
echo "${WHITE}[${YELLOW}✚${WHITE}]${CYAN} JIKA INGIN PESAN YANG SAMA HARAP TUNGGU 15 MENIT LAGI!"
fi
}
nebanner
echo -en "MASUKKAN NOMOR TERGET : " | lolcat; read now
echo -en "MASUKKAN ISI PESAN : " | lolcat; read psn
for x in okeey; do
((thread=thread%LIMITATOR)); ((thread++==0)) && wait
negetgan "$now" "$psn" "$okeey"
done
wait
