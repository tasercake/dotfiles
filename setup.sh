#!/bin/sh
# .bashrc
cp -L ~/.bashrc .
rm ~/.bashrc
ln -s dotfiles/.bashrc ~/.bashrc

# OpenSSH Server
sudo apt update
sudo apt install openssh-server
sudo systemctl status ssh
sudo ufw allow ssh
