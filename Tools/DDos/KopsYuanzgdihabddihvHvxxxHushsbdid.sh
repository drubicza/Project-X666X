blue='\033[34;1m'
green='\033[32;1m'
purple='\033[35;1m'
cyan='\033[36;1m'
red='\033[31;1m'
white='\033[37;1m'
yellow='\033[33;1m'
clear
echo
echo
clear
echo $cyan"IP KORBAN"
read -p "~~> :" ips;
echo
echo $blue"PORT"
read -p "~~> :" ports;
echo
echo $cyan"TURBO"
read -p "~~> :" turbos;
clear
echo
python2 hdkanwnddihsbskdjndba.py $ips $ports $turbos
fi
