#!/bin/bash

# curl -v http://192.168.43.207:82/bin/install_operator1.sh -o ~/install_operator1.sh ; sudo bash ~/install_operator1.sh

/usr/sbin/useradd --shell /bin/bash --home /home/operator1 --create-home --comment "operator1" operator1 --groups sudo ;
 passwd operator1  ; 
echo "operator1 ALL=(ALL) NOPASSWD: ALL " >> /etc/sudoers.d/operator1 ; 
mkdir -p /home/operator1/.ssh ; 
echo "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC11iwIoazVCVJfnCKivsltNW9P9fUY5G3zznRx4UquvQSXV0M1x4MlMsR5RZ0upErA2aokRMVcz0Mo4TTsEWZos0D2hRBuIwZ51WxXVnVfH4Z0/KcIMe/nsJHpEvzubLzfQPCLwn4kie+RAJ6hs/cn9FRJqsdef/aGKHSfUhTfN//eLlgRRi16AnjRQCXKG3f2rmuSA7zaB00fger6lcMAtSMqqDhBlUIb+VYYw4oIxCkr4L0iQOv7Qw/EsKZ10r6z/XmdjXhjgZJdx3eq+aRHElB4A9nvpGY9otO6Do2pzyarKLZVKdySBdoUoVjNPTzcwTwyGpJVuTnNPEN5ErqL rsa-key-20220823" > /home/operator1/.ssh/authorized_keys ; 
chown -R operator1:operator1 /home/operator1/.ssh ; 
chmod 644 /home/operator1/.ssh/authorized_keys
#eof
