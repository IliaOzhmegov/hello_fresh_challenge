import polars as pl

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
