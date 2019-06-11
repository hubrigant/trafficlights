#!/usr/bin/env python3
# from traffic import *
from traffic.intersections.queue import Queue

left_queue_a = Queue(queue_id="LeftA", max_queue_depth=100)
left_queue_b = Queue(queue_id="LeftB", max_queue_depth=100)
left_funnel = Queue(queue_id="LeftFunnel", max_queue_depth=8)

right_queue_a = Queue(queue_id="RightA", max_queue_depth=100)
right_queue_b = Queue(queue_id="RightB", max_queue_depth=100)
right_funnel = Queue(queue_id="RightFunnel", max_queue_depth=8)

left_queue_a.fill()
left_queue_b.fill()
right_queue_a.fill()
right_queue_b.fill()

while(len(left_queue_a) and len(left_queue_b) and len(left_funnel) and
      len(right_queue_a) and len(right_queue_b) and len(right_funnel)):
    print("Looping")
