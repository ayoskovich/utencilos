import random
from typing import Union, Callable
import pandas as pd


def checkin(df: pd.DataFrame, msg: str = None) -> pd.DataFrame:
    """Prints a message. To be used in a pipeline.

    Example
    -------
    .. code-block:: python

        (
            mydf
            .pipe(checkin, 'Starting pipeline')
            .loc[lambda x: x['A'] == 'b']
            .pipe(checkin, 'After filtering')
        )
    """
    msg = f"{df.shape}: {msg or ''}"
    print(msg)
    return df


def squish(
    df: pd.DataFrame, index_var: Union[str, list[str]], col_sep: str = "_"
) -> pd.DataFrame:
    """Combines columns horizontally. Assumes the columns end with an index.
    
    Example
    -------
    .. code-block:: python

        pd.DataFrame({'a': ['yaya!']})
    """
    if not isinstance(index_var, list):
        index_var = [index_var]
    return (
        df.melt(id_vars=index_var, value_name="value", var_name="variable")
        .assign(group=lambda x: x["variable"].apply(lambda x: x.split(col_sep)[-2]))
        .groupby(["group"])["value"]
        .apply(lambda x: list(x))
        .reset_index()
    )


def filter_random(df: pd.DataFrame, col: str) -> pd.DataFrame:
    """Returns the dataframe filtered to a random value of col."""
    val = random.choice(df[col])
    return df.loc[lambda x: x[col] == val]

def create_column(df: pd.DataFrame, colname: str, func: Callable, *args, **kwargs) -> pd.DataFrame:
    """ Creates a new column using a function that takes column names as strings.
    
    Example
    -------
    
    .. code-block:: python

        create_column(df, 'sum_total', sum, 'a', 'b', 'c')
        create_column(df, 'sum_total', sum('a', 'b', 'c'))
    """
    return (
        df
        .assign(newcol = lambda x: x.apply(lambda x: func(*args, **kwargs), axis=1))
        .rename(columns={'newcol': colname})
    )