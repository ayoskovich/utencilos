import pandas as pd

def checkin(df: pd.DataFrame, msg=None) -> pd.DataFrame:
    """ Prints a message. To be used in a pipeline.
    
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