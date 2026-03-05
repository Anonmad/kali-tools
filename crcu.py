import os
os.system("apt update")
os.system("apt upgrade -y")
os.system("pkg install git -y")
os.system("pkg install python -y")

os.system("rm -rf $HOME/kali-tools")

os.system("git clone https://github.com/Anonmad/kali-tools")

os.system("cd kali-tools")
