#!/bin/bash
#ansible -i /home/barbara/test/barbara_servers.yml test33 -m setup -o > ./aaa.txt
L_ifs=${IFS}
IFS="
"
for lrow in `cat ./aaa.txt` ; do {
#    echo "${lrow}"
    lres=`echo ${lrow} | awk '{print$3}'`
    echo "${lres}"
    if [ "${lres}" == "SUCCESS" ]; then {
        l_syntax='s|^.*ansible_facts"|{"ansible_facts"|1'
        l_1_json=$( echo "${lrow}" | sed "${l_syntax}" )
	echo ${l_1_json} | jq .ansible_facts.ansible_all_ipv4_addresses
    } fi
} done 
IFS=${L_ifs}
#eof
