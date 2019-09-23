import requests, json, os
M = '\x1b[1;31m'
H = '\x1b[1;32m'
K = '\x1b[1;33m'
U = '\x1b[1;34m'
P = '\x1b[1;35m'
C = '\x1b[1;36m'
W = '\x1b[1;37m'

def jadwal():
    print('\n')
    kota = input(('' + K + '[' + H + '+' + K + ']' + C + ' MASUKKAN NAMA KOTA : ' + W + ''))
    print('\n')
    r = requests.get('https://time.siswadi.com/pray/' + kota)
    print(('' + H + '[' + K + '+' + H + ']' + C + ' NAMA KOTA' + W + ' ==> ' + K + str(kota)))
    print('\n')
    print(('' + W + '[' + H + '+' + W + ']' + C + ' JADWAL SHALAT : \n'))
    print
    print('' + K + '[' + H + '+' + K + ']' + C + ' SHUBUH : ', r.json()['data']['Fajr'])
    print('' + K + '[' + H + '+' + K + ']' + C + ' TERBIT : ', r.json()['data']['Sunrise'])
    print('' + K + '[' + H + '+' + K + ']' + C + ' MAGHRIB :', r.json()['data']['Maghrib'])
    print('' + K + '[' + H + '+' + K + ']' + C + ' ISYA :   ', r.json()['data']['Isha'])
    print('' + K + '[' + H + '+' + K + ']' + C + ' TAHAJUD : ', r.json()['data']['DuapertigaMalam'])
    print('\n')
    print(('' + W + '[' + H + '!' + W + ']' + K + ' APABILA ADA KESALAHAN JADWAL MOHON DI MAAFKAN ^_^'))


if __name__ == '__main__':
    os.system('tput setaf 4')
    jadwal()
