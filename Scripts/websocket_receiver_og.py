#orginal web socket file that gets the live streeam from meta glasses

import asyncio
import websockets
import numpy as np
import cv2
import time

frame_count = 0
last_time = time.time()

async def handler(websocket):
    global frame_count, last_time

    print("Android connected!")

    async for message in websocket:
        jpg = np.frombuffer(message, dtype=np.uint8)
        frame = cv2.imdecode(jpg, cv2.IMREAD_COLOR)

        if frame is None:
            continue

        frame_count += 1

        now = time.time()
        elapsed = now - last_time

        if elapsed >= 1:
            fps = frame_count / elapsed
            print(f"Receiving FPS: {fps:.2f}")
            frame_count = 0
            last_time = now

        cv2.imshow("Meta Stream", frame)

        if cv2.waitKey(1) == 27:
            break


async def main():
    async with websockets.serve(handler, "0.0.0.0", 8765):
        print("Waiting for Android connection...")
        await asyncio.Future()

asyncio.run(main())