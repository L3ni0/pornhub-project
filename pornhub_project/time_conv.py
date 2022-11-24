def str_to_seconds(duration: str) -> int:
    duration = duration.split(':')
    times = [3600,60,1]

    int_time = 0
    for i in range(1,len(duration)+1):
        int_time += int(duration[-i]) * times[-i]

    return int_time

    