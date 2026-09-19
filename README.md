cd ~
mkdir agent-harness-demo && cd agent-harness-demo
git init -b main
python3 -m venv .venv
source .venv/bin/activate
pip install pytest ruff
