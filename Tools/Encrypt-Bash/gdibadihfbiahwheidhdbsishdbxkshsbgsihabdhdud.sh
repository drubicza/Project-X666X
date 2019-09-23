clear
toilet -f future "  BASH ENCRYPT " | lolcat
echo
echo ""
echo "[!] MASUKKAN FILE DI INTERNAL" | lolcat
echo "EX : /sdcard/script.sh" | lolcat
echo
echo "_::MASUKKAN FILE YANG INGIN DI ENCRYPT::_" | lolcat
echo "EX : script.sh " | lolcat
read file
echo
echo "_::MASUKAN NAMA HASILNYA::_" | lolcat
echo "EX : hasilenc.sh" | lolcat
read output
echo
bash-obfuscate /sdcard/$file -o /sdcard/$output
echo "SCRIPT BERHASIL DI ENCRYPT | SILAHKAN LIHAT DI /sdcard/$output" | lolcat
echo ""
