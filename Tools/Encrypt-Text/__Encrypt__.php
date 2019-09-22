<?php
//Sengaja Ga Gua Encrypt Gan
//Biar Kalian Bisa Belajar
//Malah Jangan Di Recode
//Hargai Pembuatnya !! 

              //StartEnkodeMenu... 
$kuning = "\033[1;33m";
$ungu = "\033[1;34m";
$merah = "\033[1;31m";
$hijau = "\033[1;32m";
$pink = "\033[1;35m";
$cyan = "\033[1;36m";
$putih = "\033[1;37m";

    echo "$merah/$cyan>>>>>>>>>>$kuning|$cyan<<<<<<<<<<$merah\ \n";
    echo "$putih     Tools Encode$kuning     v1.7\n";
    echo "$merah/$cyan>>>>>>>>>>$kuning|$cyan<<<<<<<<<<$merah\ \n\n";
    echo "$putih<$cyan Tipe Enkode$putih>\n\n";
    echo "$putih  1) Encode Md5\n";
    echo "$putih  2) Encode Base64\n";
    echo "$putih  3) Encode Sha1\n";
    echo "$putih  4) Encode Md4\n";
    echo "$putih  5) Encode Semua Tipe\n";
    echo "$merah  x) Exit\n\n";
    echo "$putih<$merah/$cyan Tipe Enkode$putih>\n\n";
    echo "$kuning Pilih Tipe Enkode : ";
    switch(trim(fgets(STDIN,256)))
        {
            case 1:
                echo "$hijau Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN,256));
                echo "$cyan Hasil Encode Md5 : ",md5($kata)," \n";
                exit();
            case 2:
                echo "$hijau Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "$cyan Hasil Encode Base64 : ",base64_encode($kata),"\n";
                exit();
            case 3:
                echo "$hijau Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "$cyan Hasil Encode Sha1 : ",sha1($kata),"\n";
                exit();
            case 4:
                echo "$hijau Masukkan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                echo "$cyan Hasil Encode Md4 :",crypt('md4',$kata);
                exit();
            case 5:
                echo "$hijau Masukan Kata Yang Akan di Encode : ";
                $kata = trim(fgets(STDIN));
                foreach (hash_algos() as $v) {
                $r = hash($v, $kata, false);
                printf("%-12s %3d %s\n", $v, strlen($r), $r);
                }
                exit();
            case "x":
                exit();
        }
    //CloseEnkodeMenu... 
    fclose(STDIN);
?>
