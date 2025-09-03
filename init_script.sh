#!/bin/sh
### File            : init-script.sh 
### Description     : Configuring sources before upgrade ${ENVIRON}
### Author          : Varvara Yasko
### Version history :
### 20250903 1.0 Create basic idea for packer.
echo ${AWSENVIRON}
echo "<html><h1>the machine test-00</h1><body></body>${AWSENVIRON}</html>" > /var/www/nginx/index.html
#EOF
