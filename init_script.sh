#!/bin/bash

### File            : init-script.sh
### Description     : Configuring sources before upgrade ${ENVIRON}
### Author          : Varvara Yasko
### Version history :
### 20250903 1.0 Create basic idea for packer.

echo ${AWSENVIRON}

# Создаем пользователя + группу
ls_user="deployer"
useradd --shell /bin/bash --home /home/${ls_user} --create-home ${ls_user} --comment "${ls_user}"

# Настраиваем права
echo "${ls_user} ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/${ls_user}

# Добавляем SSH ключи
mkdir -p /home/${ls_user}/.ssh
echo 'ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIOLK8IEAqChX4vnPjyCOVN4g7WmirWZZG9V3Nk8ZzIHN yasko
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBJeieBg44JxRIv8hsd0YA/qxsoLszGZ7U2pn86obcfUrxajDd3J9gFlEr8IzS9Q06zZSSAiigo8XlgVzsG7BfUs= laptop-myasko
ecdsa-sha2-nistp256 AAAAE2VjZHNhLXNoYTItbmlzdHAyNTYAAAAIbmlzdHAyNTYAAABBBC4qizdDQa0sil/11fpy+DRru1TG3ZiH0i846YdxU90CA6+ZGppQXJzfFf/futkqFO4UFEaIAJjhO0Cm4rv9IaY= deployer
' >> /home/${ls_user}/.ssh/authorized_keys

# Устанавливаем права доступа
chown -R ${ls_user}:${ls_user} /home/${ls_user}/.ssh
chmod 700 /home/${ls_user}/.ssh
chmod 600 /home/${ls_user}/.ssh/authorized_keys

###########
apt update
apt install -y curl wget mc bzip2 jq nginx net-tools
###########

# Выполняем команды
rm -f /etc/nginx/sites-enabled/default

cat > /etc/nginx/sites-enabled/my-nginx << 'EOF'
server {
    listen 80;

    root /var/www/nginx;
    index index.html index.htm;

    access_log /var/log/nginx/test-00-access.log;
    error_log /var/log/nginx/test-00-error.log;
}
EOF

mkdir -p /var/www/nginx/
echo "<html><h1>the machine test-00</h1><body></body>${AWSENVIRON}</html>" > /var/www/nginx/index.html
echo "<tilte>healtcheck</tilte>" > /var/www/nginx/healthcheck.html

# Перезапускаем nginx
systemctl restart nginx

curl -v http://127.0.0.1:80/healthcheck.html
curl -v http://127.0.0.1:80/index.html

#EOF
