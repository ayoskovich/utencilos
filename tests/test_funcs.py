import random
import pandas as pd

from utencilos.general import checkin, squish, filter_random

def test_checkin(capsys):
    start_df = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
    output = (
        start_df.pipe(checkin, "before filtering")
        .loc[lambda x: x["a"] == 1]
        .pipe(checkin, "after filtering")
    )
    captured = capsys.readouterr()
    out_text = "(3, 2): before filtering\n(1, 2): after filtering\n"
    assert captured.out == out_text
    assert output.shape == (1, 2)

def test_filter_random():
    random.seed(1234)
    df_input = pd.DataFrame(
        columns=['grp', 'val'],
        data=[
            ('a', 15),
            ('a', 20),
            ('b', 100)
        ]
    )
    expected_output = pd.DataFrame(
        columns=['grp', 'val'],
        data=[
            ('a', 15),
            ('a', 20)
        ]
    )
    actual_output = df_input.pipe(filter_random, 'grp')
    pd.testing.assert_frame_equal(actual_output, expected_output)

def test_squish():
    df_input = pd.DataFrame(
        columns=['index_var', 'a_1', 'a_2', 'b_1', 'b_2'],
        data=[
            (1, 2, 3, 4, 5),
            (10, 20, 30, 40, 50)
        ]
    )
    expected_output = pd.DataFrame(
        columns=['group', 'value'],
        data=[
            ('a', [2, 20, 3, 30]),
            ('b', [4, 40, 5, 50]),
        ]
    )

    actual_output = squish(df_input, 'index_var')
    pd.testing.assert_frame_equal(actual_output, expected_output)