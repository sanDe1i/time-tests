# times.py
import datetime

def time_range(start_time, end_time, number_of_intervals=1, gap_between_intervals_s=0):
    start_time_s = datetime.datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time_s = datetime.datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    if start_time_s >= end_time_s:
        raise ValueError(f"end_time ({end_time}) must be after start_time ({start_time})")

    total_duration = (end_time_s - start_time_s).total_seconds()
    interval_duration = (total_duration - (number_of_intervals - 1) * gap_between_intervals_s) / number_of_intervals

    sec_range = []
    for i in range(number_of_intervals):
        s = start_time_s + datetime.timedelta(seconds=i * (interval_duration + gap_between_intervals_s))
        e = s + datetime.timedelta(seconds=interval_duration)
        sec_range.append((s.strftime("%Y-%m-%d %H:%M:%S"), e.strftime("%Y-%m-%d %H:%M:%S")))

    return sec_range


def compute_overlap_time(range1, range2):
    fmt = "%Y-%m-%d %H:%M:%S"
    overlap_time = []
    for start1, end1 in range1:
        s1, e1 = datetime.datetime.strptime(start1, fmt), datetime.datetime.strptime(end1, fmt)
        for start2, end2 in range2:
            s2, e2 = datetime.datetime.strptime(start2, fmt), datetime.datetime.strptime(end2, fmt)
            low = max(s1, s2)
            high = min(e1, e2)
            if low < high:
                overlap_time.append((low.strftime(fmt), high.strftime(fmt)))
    return overlap_time
