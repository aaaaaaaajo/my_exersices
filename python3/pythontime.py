from datetime import datetime

# Getting the current date and time
dt = datetime.now()

# getting the timestamp
ts = datetime.timestamp(dt)

print("Date and time is:", dt)
print("Timestamp is:", ts)