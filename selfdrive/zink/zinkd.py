#!/usr/bin/env python3

import os
import queue
import time
import threading
import zmq
from typing import Any
from jsonrpc import dispatcher

from selfdrive.swaglog import cloudlog

HANDLER_THREADS = int(os.getenv('HANDLER_THREADS', "4"))

dispatcher["echo"] = lambda s: s
payload_queue: Any = queue.Queue()
response_queue: Any = queue.Queue()

def do_long_poll(rep_socket):
  end_event = threading.Event()

  threads = [
    threading.Thread(target=zmq_recv, args=(rep_socket, end_event)),
    threading.Thread(target=zmq_send, args=(rep_socket, end_event)),
  ] + [
    threading.Thread(target=rpc_handler, args=(end_event,))
    for x in range(HANDLER_THREADS)
  ]

  for thread in threads:
    thread.start()
  try:
    while not end_event.is_set():
      time.sleep(0.1)
  except (KeyboardInterrupt, SystemExit):
    end_event.set()
    raise
  finally:
    for thread in threads:
      thread.join()

def rpc_handler(end_event):
  pass

def zmq_recv(rep_socket, end_event):
  while not end_event.is_set():
    try:
      data = rep_socket.recv()
      payload_queue.put_nowait(data)
    except Exception:
      cloudlog.exception("zinkd.zmq_recv.exception")
      end_event.set()


def zmq_send(rep_socket, end_event):
  while not end_event.is_set():
    try:
      response = response_queue.get(timeout=1)
      rep_socket.send(response.json)
    except queue.Empty:
      pass
    except Exception:
      cloudlog.exception("zinkd.zmq_send.exception")
      end_event.set()

def main():
  context = zmq.Context()
  socket = context.socket(zmq.REP)
  socket.bind("tcp://*:5555")

  while True:
    try:
      do_long_poll(socket)
    except (KeyboardInterrupt, SystemExit):
      break
    except Exception:
      cloudlog.exception("zinkd.main.exception")


if __name__ == "__main__":
    main()
