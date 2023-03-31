import polars as pl

from urllib import request
from os import path, makedirs

from src.spell import generate_pattern
from src.convert import convert_to_minutes

URL = "https://bnlf-tests.s3.eu-central-1.amazonaws.com/recipes.json"
FOLDER = 'data'
LOCAL_FILE = "recipes.json"

KEYWORD = 'Chilie'


def download(url: str, folder: str, filename: str) -> str:
    if not path.exists(folder):
        makedirs(folder)
    filepath = f'{folder}/{filename}'
    request.urlretrieve(url, filepath)
    return filepath


def retrieve(keyword: str, filepath: str) -> pl.DataFrame:
    qp = pl.scan_ndjson(filepath)

    qp = (
            qp
            .filter(pl.col('ingredients')
                    .str.to_lowercase()
                    .str.contains(generate_pattern(keyword))
                )
        )

    qp = (
            qp
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

    qp = qp.unique()

    return qp.collect()


def average_by_difficulty(df: pl.DataFrame) -> pl.DataFrame:
    return (
            df
            .filter(pl.col('totalTime').is_not_null())
            .groupby('difficulty')
            .agg(
                pl.mean('totalTime').round(2).alias('AverageTotalTime')
            )
    )


def main():
    print(f'Downloading {LOCAL_FILE}..')
    filepath = download(URL, FOLDER, LOCAL_FILE)

    print(f'Transforming & saving data as {KEYWORD}.csv..')
    df = retrieve(KEYWORD, filepath)
    df.write_csv(f'{FOLDER}/{KEYWORD}.csv', separator='|')

    print('Transforming & saving data as Results.csv..')
    grouped_df = average_by_difficulty(df)
    grouped_df.write_csv(f'{FOLDER}/Results.csv', separator='|')


if __name__ == '__main__':
    main()
