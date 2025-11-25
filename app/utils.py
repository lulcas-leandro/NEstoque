from datetime import timezone

def to_local_time(utc_dt, local_tz):
    if utc_dt is None:
        return None
    
    if utc_dt.tzinfo is None:
        utc_dt = utc_dt.replace(tzinfo=timezone.utc)
    
    return utc_dt.astimezone(local_tz)
