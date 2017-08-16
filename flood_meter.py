from datetime import datetime


class FloodMeter:

    def __init__(self):
      self._message_timestamps = []

    def check_message(self):
      self._message_timestamps.append(datetime.utcnow())

    @property
    def flood_rate(self):
        now = datetime.utcnow()

        self._message_timestamps = [t for t in self._message_timestamps
                                    if (now - t).seconds <= 60]

        return len(self._message_timestamps)
