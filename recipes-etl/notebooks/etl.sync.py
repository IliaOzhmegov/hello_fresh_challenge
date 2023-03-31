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

# %%
ingredient = "chilie"

# Common misspellings
n_grams = [
        {},
        {
            "v": "[v|f]",
            "w": "[w|u]",
            "s": "[s|z]",
            "y": "[y|i]",
            "x": "[x|ks]"
            },
        {
            "ei": "[ei|ie|e|i]",
            "ie": "[ei|ie|i|e]",
            "ck": "[ck|c|k]",
            "ph": "[ph|f]"
            }
        ]

n = len(ingredient) - 2
for i in range(n, 0, -1):
    two_chars = ingredient[i:i+2]
    if two_chars in n_grams[2]:
        ingredient = ingredient[:i] + n_grams[2][two_chars] + ingredient[i+2:]
ingredient

# %%
space = r'\s?'
pattern = space + ingredient + space
print(pattern)

# %%
(
    df
    .filter(pl.col('ingredients')
            .str.to_lowercase()
            .str.contains(pattern)
    )
    .shape
)


# %%
pl.Config.set_tbl_rows(42)
(
    df
    .select(
        pl.col('cookTime'),
        pl.col('cookTime').str.extract(r'PT(\d*)H').cast(pl.UInt32).alias('cooking H'),
        pl.col('cookTime').str.extract(r'(\d*)M')  .cast(pl.UInt32).alias('cooking M')
    )
    .with_columns(
        pl.when(pl.col('cooking H').is_not_null() | pl.col('cooking M').is_not_null())
        .then(
            pl.col('cooking H').fill_null(0)*60 + pl.col('cooking M').fill_null(0)
        )
        .otherwise(
            pl.col('cooking M')
        )
        .alias('cooking time')

    )
    .unique()
)


# %%
def convert_to_minutes(df: pl.DataFrame, col: str, alias=None) -> pl.DataFrame:
    if alias is None:
        alias = col
    return (
            df
            .with_columns(
                (pl.col(col).str.extract(r'PT(\d*)H')
                 .cast(pl.UInt32)*60).alias(col+'_H'),
                pl.col(col).str.extract(r'(\d*)M')
                .cast(pl.UInt32).alias(col+'_M')
            )
            .with_columns(
                pl.coalesce(
                    pl.col(col+'_H') + pl.col(col+'_M'),
                    pl.col(col+'_H'),
                    pl.col(col+'_M')
                )
                .alias(alias)
            )
            .select(pl.exclude([col+'_H', col+'_M']))
    )


# %%
df = (
    df
    .pipe(convert_to_minutes, col='cookTime', alias='cookTime_mins')
    .pipe(convert_to_minutes, col='prepTime', alias='prepTime_mins')

    .with_columns(
        pl.coalesce(
            pl.col('cookTime_mins') + pl.col('prepTime_mins'),
            pl.col('cookTime_mins'),
            pl.col('prepTime_mins')
        )
        .alias('totalTime'),  # minutes
    )

    .with_columns(
        pl.when(pl.col('totalTime') > 60).then('Hard')
        .when(pl.col('totalTime') > 30)  .then('Medium')
        .when(pl.col('totalTime') > 0)   .then('Easy')
        .otherwise('Unknown')
        .alias('difficulty')
    )

    .select(pl.exclude(['cookTime_mins', 'prepTime_mins']))
)

# %%
(
    df
    .filter(pl.col('totalTime').is_not_null())
    .groupby('difficulty')
    .agg(
        pl.mean('totalTime').round(2).alias('AverageTotalTime')
    )
)

# %%
