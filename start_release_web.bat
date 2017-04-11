cd srcs
set module=index
python -m bottle -s paste -b 0.0.0.0:9797 --reload %module%
pause