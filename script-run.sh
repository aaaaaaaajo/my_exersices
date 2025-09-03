#!/bin/bash

### File            : script-run.sh 
### Description     : Configuring sources before upgrade ${ENVIRON}
### Author          : Varvara Yasko
### Version history :
### 20250903 1.0 Create basic idea for packer.


export VERSION="33"
export ENVIRON="aws_stage"
export AWS_ENV_REGION="eu-central-1"


export AWS_ACCESS_KEY_ID="----------------VSS6"
export AWS_SECRET_ACCESS_KEY="B0-----------------------------------/9M"
export AWS_AMI_TAG_NAME="aws-${ENVIRON}-${VERSION}"

ls_json="linux.json"

packer validate ./${ls_json}
l_ret=${?} ; echo "l_ret=${l_ret}"
packer build -on-error=ask  ./${ls_json}
l_ret=${?} ; echo "l_ret=${l_ret}"
