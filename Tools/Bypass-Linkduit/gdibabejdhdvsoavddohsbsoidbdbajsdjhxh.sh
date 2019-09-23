getconten(){
test=$(curl --silent -i "${uz}" -A "$agent" --location | grep 'set-cookie:' |  grep -Po '(?<=PHPSESSID=)[^,]*' | gawk '{print $1}')
test1=$(curl --silent -i "${uz}" -A "$agent" --location | grep 'set-cookie:' |  grep -Po '(?<=__cfduid=)[^,]*' | gawk '{print $1}')
ngett=$(curl "${uz}" --silent --compressed \
-H 'authority: linkduit.net' \
-H 'upgrade-insecure-requests: 1' \
-A 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36' \
-H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' \
-H 'accept-language: id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7')
coba=$(echo -e "$ngett" | grep -Po '(?<=href=").*?(?=")')
gettt=$(echo -e "${coba}" | grep '/get/')
vari="https://linkduit.net${gettt}"
getx=$(printf "$vari")
cobax=$(curl --silent "${getx}" -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36" --compressed \
-H "upgrade-insecure-requests: 1" \
-H 'authority: linkduit.net' \
-H "accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3" \
-H "cookie: __cfduid=$test1 PHPSESSID=$test")
ss=$(shuf -e "${cobax}" | grep -Po 'URL=[^"]*' | gawk -F "=" '{print $2}')
echo "_::LINK ASLI::_" | lolcat
echo ${ss[*]}
}
clear
toilet -f future "  BYPASS LINKDUIT " | lolcat
echo
echo "_::MASUKKAN LINK::_" | lolcat
read uz
echo
getconten
