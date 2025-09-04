#!/bin/zsh

BASE_DIR="$(dirname "$0")"
VENV="$HOME/.venvs/global"

if [[ -f "$BASE_DIR/bulk2avif.pyw" ]]; then
  SCRIPT="$BASE_DIR/bulk2avif.pyw"
  BACKGROUND=true
elif [[ -f "$BASE_DIR/bulk2avif.py" ]]; then
  SCRIPT="$BASE_DIR/bulk2avif.py"
  BACKGROUND=false
else
  echo "❌ No bulk2avif.py / bulk2avif.pyw in $BASE_DIR"
  exit 1
fi

source "$VENV/bin/activate"

if [[ $BACKGROUND == true ]]; then
  nohup python "$SCRIPT" "$@" > /dev/null 2>&1 &
else
  python "$SCRIPT" "$@"
fi
