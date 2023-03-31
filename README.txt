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

# SQL task
I have been using `mysql` db in order to make sure that syntax of my queris is correct, which I also added.
You also can run those with in the `db` folder:
`$ docker compose up`
and additionaly there is available db adminer at `http://localhost:8080/`

## Notes:
Please take into account that I have to spend some time clarifying certain questions, which were jamming me
so I decided not to do all 8 sql quesions.
