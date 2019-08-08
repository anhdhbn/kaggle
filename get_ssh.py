# Setup sshd
! apt-get install -qq -o=Dpkg::Use-Pty=0 openssh-server pwgen > /dev/null

# Set root password
! echo root:$password | chpasswd
! mkdir -p /var/run/sshd
! echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
! echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
! echo "LD_LIBRARY_PATH=/usr/lib64-nvidia" >> /root/.bashrc
! echo "export LD_LIBRARY_PATH" >> /root/.bashrc
! echo "export LC_ALL=C.UTF-8" >> /root/.bashrc

# Run sshd
get_ipython().system_raw('/usr/sbin/sshd -D &')

# Print root password
import os
os.system("echo 'Root alias: {}'".format(password))
os.system("echo 'Root password: {}'".format(password))
os.system("echo 'Port: {}'".format(port))

print('Root alias: {}'.format(password))
print('Root password: {}'.format(password))
print('Port: {}'.format(port))

# Create tunnel
! ssh -o "StrictHostKeyChecking no"  -R $password:$port:localhost:22 teleport.anhdh.com
