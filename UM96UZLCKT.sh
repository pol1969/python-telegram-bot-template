export APP_NAME="main.py"
export WORKSPACE=`pwd`
# Create/Activate virtualenv
python3 -m venv env

if [ -d "./env" ];then
  echo "[info] Ctrl+d to deactivate"
  bash -c ". env/bin/activate;pip install -r requirements.txt
 exec /usr/bin/env bash --rcfile <(echo 'PS1=\"(env)\${PS1}\"') -i"
fi

# Install Requirements
#pip3 install -r requirements.txt
