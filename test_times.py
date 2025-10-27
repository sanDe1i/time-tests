# test_times.py
from times import compute_overlap_time, time_range
import pytest

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00", "2010-01-12 10:37:00"),
                ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected


def test_non_overlapping_ranges():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00")
    r2 = time_range("2020-01-01 12:00:00", "2020-01-01 13:00:00")
    assert compute_overlap_time(r1, r2) == []


def test_multiple_intervals_each():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00", 2, 60)
    r2 = time_range("2020-01-01 10:30:00", "2020-01-01 11:30:00", 2, 60)
    overlaps = compute_overlap_time(r1, r2)
    assert all("2020-01-01 10:30:00" <= s < e <= "2020-01-01 11:00:00" for s, e in overlaps)


def test_touching_ranges():
    r1 = time_range("2020-01-01 10:00:00", "2020-01-01 11:00:00")
    r2 = time_range("2020-01-01 11:00:00", "2020-01-01 12:00:00")
    # End of r1 == Start of r2 → no overlap
    assert compute_overlap_time(r1, r2) == []

def test_time_range_error():
     with pytest.raises(ValueError):
        time_range("2020-01-01 10:00:00", "2020-01-01 09:00:00")