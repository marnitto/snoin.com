import pathlib
import sys

from snoin.config import load
from snoin.web.app import app

__all__ = 'app', 'config', 'config_file'

config_file = pathlib.Path('/home/snoin/snoin.com/snoin.cfg.py')
if not config_file.exists():
    print('config file is missing', file=sys.stderr)
    raise SystemExit(1)

config = load(config_file)

app.config.update(config)
