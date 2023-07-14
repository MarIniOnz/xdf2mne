import os
import pyxdf
import mne
from xdf2mne import streams2raw

import logging

logger = logging.getLogger(__name__)

filename = "2023-06-03_finger_discrimination_pilot_jan\Task_1_16.xdf"
filepath = os.path.join("data", filename)

streams, fileheader = pyxdf.load_xdf(filepath, dejitter_timestamps=True)

##
stream = streams[3]
marker_stream = streams[1]

raw, events, event_id = streams2raw(stream, marker_streams=[marker_stream])

print(f"raw contains the following annotations: {raw.annotations}")
# The events array is redundant with annotations, you can do
events_from_annotations = mne.annotations.events_from_annotations(raw, event_id)
# and should receive the same array as events
