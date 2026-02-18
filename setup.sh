# create venv
if [ ! -d $PWD/.venv ]; then
  python3 -m venv .venv
  $PWD/.venv/bin/pip install -r requirements.txt
fi

alias azemu='$PWD/.venv/bin/python $PWD/run.py'
