# tests/test_utils.py
import pandas as pd
import pytest
from app.utils import summary_stats, line_chart, box_chart

# --------- Sample Data for Testing ---------
@pytest.fixture
def sample_df():
    data = {
        "Timestamp": pd.date_range("2025-01-01", periods=5, freq="D"),
        "GHI": [100, 150, 200, 250, 300],
        "DNI": [50, 75, 100, 125, 150],
        "DHI": [25, 35, 45, 55, 65],
        "Tamb": [20, 21, 22, 23, 24],
        "RH": [30, 40, 50, 60, 70],
        "Country": ["TestLand"]*5
    }
    return pd.DataFrame(data)

# --------- Tests for summary_stats ---------
def test_summary_stats(sample_df):
    stats = summary_stats(sample_df, "GHI")
    assert stats["Mean"] == 200
    assert stats["Median"] == 200
    assert stats["Std Dev"] > 0

# --------- Tests for line_chart ---------
def test_line_chart(sample_df):
    fig = line_chart(sample_df, "GHI", "TestLand")
    assert fig is not None
    assert fig.data[0].y.tolist() == [100, 150, 200, 250, 300]

# --------- Tests for box_chart ---------
def test_box_chart(sample_df):
    fig = box_chart(sample_df, "GHI")
    assert fig is not None
    assert "TestLand" in fig.data[0].name
