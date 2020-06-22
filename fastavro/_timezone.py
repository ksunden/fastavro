from datetime import datetime, timezone


# used to compute timestamp for tz-aware datetime objects
# python >= 3.3 can use datetime.datetime.timestamp() instead
# SCOTT do we need these?
epoch = datetime(1970, 1, 1, tzinfo=timezone.utc)
epoch_naive = datetime(1970, 1, 1)
