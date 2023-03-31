# Python task

1. Navigate to folder:
`recipes-etl`
1. Set up virtual environment (optional):
`$ python3.10 -m venv .venv`
`$ source .venv/bin/activate`
1. Install requirements with:
`$ pip install -r requirements.txt`
or just
`$ pip install polars`
1. Launch the script `main.py`:
`$ python3.10 main.py`
1. You can find the results in the folder `data`.
```
.
├── data
│   ├── Chilie.csv
│   ├── Results.csv
│   └── recipes.json
├── main.py
├── notebooks
│   ├── etl.sync.ipynb
│   └── etl.sync.py
├── requirements.txt
├── src
│   ├── __init__.py
│   ├── convert.py
│   └── spell.py
└── test
    ├── __init__.py
    ├── test_convert.py
    └── test_spell.py
```

6. You can also run unittests:
`$ python3.10 -m unittest discover -v`
