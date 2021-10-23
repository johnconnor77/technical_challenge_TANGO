import datetime


def delta_time(end_time, start_time):
    """
        Function that calculates the difference between two given dates
        :param end_time: where appointment finish
        :param start_time: where appointment begins
        :return: the amount of time between dates as a timedelta type
    """
    date = datetime.date(1, 1, 1)
    datetime1 = datetime.datetime.combine(date, start_time)
    datetime2 = datetime.datetime.combine(date, end_time)
    time_elapsed = datetime2 - datetime1
    return time_elapsed


def check_time(time):
    """
        Function that checks if a given time is on hour or half hour as required
    """
    if time.minute == 0 or time.minute == 30:
        return True
    return False
