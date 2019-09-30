apt-get update && apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null
mkdir -p /var/run/sshd
sudo echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
sudo echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
sudo echo "export LC_ALL=C.UTF-8" >> /root/.bashrc
sudo /usr/sbin/sshd -D &
