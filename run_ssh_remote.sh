#!/bin/sh

alias="ailab"
local_ssh_port=22222

create_ssh_script="ssh -o 'StrictHostKeyChecking no' -R $alias:22:localhost:$local_ssh_port teleport.anhdh.com"
script="#!/bin/sh\n\nsleep 10\n$create_ssh_script"

sudo echo script >> /usr/local/sbin/startup.sh
sudo cp ./ssh-remote.service /etc/systemd/system/ssh-remote.service

sudo systemctl daemon-reload
sudo systemctl start ssh-remote