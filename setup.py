import os
import sys
import subprocess
import string
import random
 
bashfile=''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
bashfile=os.getcwd() +'/'+ bashfile+'.sh'
 
f = open(bashfile, 'w')
s = """export APP_NAME="main.py"
export WORKSPACE=`pwd`
# Create/Activate virtualenv
python3 -m venv env

if [ -d "./env" ];then
  echo "[info] Ctrl+d to deactivate"
  bash -c ". env/bin/activate;pip install -r requirements.txt
 exec /usr/bin/env bash --rcfile <(echo 'PS1=\\"(env)\\${PS1}\\"') -i"
fi

# Install Requirements
#pip3 install -r requirements.txt
"""
f.write(s)
f.close()
os.chmod(bashfile, 0o755)
bashcmd=bashfile
for arg in sys.argv[1:]:
  bashcmd += ' '+arg
subprocess.call(bashcmd, shell=True)



#if [ -d "./env" ];then
#  echo "[info] Ctrl+d to deactivate"
#  bash -c ". env/bin/activate; exec /usr/bin/env bash --rcfile <(echo 'PS1=\"(env)\${PS1}\"') -i "
#fi
 
