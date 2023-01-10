def str_to_seconds(duration: str) -> int:
    duration = duration.split(':')
    times = [3600,60,1]

    int_time = 0
    for i in range(1,len(duration)+1):
        int_time += int(duration[-i]) * times[-i]

    return int_time

def sec_to_time(seconds):
    return f'{seconds//3600}h:{(seconds//60)%60}m:{seconds%60}s'

def time_to_sec(text):
    text = text.replace('h','').replace('m','').replace('s','').split(':')
    return int(text[0])*3600 + int(text[1])*60 + int(text[2])
