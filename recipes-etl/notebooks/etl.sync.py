# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.3.4
#   kernelspec:
#     display_name: hf
#     language: python
#     name: hf
# ---

# %%
from urllib import request
from os import path, makedirs

# %%
URL = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
FOLDER = '../data'
LOCAL_FILE = f"{FOLDER}/recipes.json"

if not path.exists(FOLDER):
    makedirs(FOLDER)

request.urlretrieve(URL, LOCAL_FILE)

# %%
import polars as pl

pl.Config.set_fmt_str_lengths(300)
# %%
df = pl.read_ndjson(LOCAL_FILE).drop(['url', 'image'])
df.head()

# %%
df.estimated_size(unit='mb')

