from datetime import datetime


def find_overlap(*events):
    data_format = "%H:%M"
    event_times = [(datetime.strptime(start, data_format), datetime.strptime(end, data_format)) for start, end in
                   events]

    overlap_start = max(start for start, _ in event_times)
    overlap_end = min(end for _, end in event_times)

    if overlap_start < overlap_end:
        print(True)
        print(
            f'The events overlap from from {overlap_start.strftime(data_format)} to {overlap_end.strftime(data_format)}')
    else:
        print(False)
        print('The events do not overlap.')


"""
Examples for Outputs
"""

# find_overlap(["02:15", "04:00"], ["04:00", "06:00"], ["03:30", "05:00"])
# find_overlap(["01:00", "02:35"], ["01:25", "06:00"], ["02:00", "02:45"])
# find_overlap(["10:15", "11:15"], ["14:30", "16:40"])
