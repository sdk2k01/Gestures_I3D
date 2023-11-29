from queue import Queue

import cv2
import mediapipe as mp

from src.utils import get_skeleton

if __name__ == "__main__":
    drawing_utils = mp.solutions.drawing_utils

    # Get a reference to webcam #0 (the default one)
    video_capture = cv2.VideoCapture(0)

    process_this_frame = 0.0
    frame_queue = Queue()

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()
        frame = cv2.flip(frame, 1)

        if process_this_frame == 1:
            # Detect Hand Skeleton
            skel = get_skeleton(frame)
            if skel:
                hand = skel[0]
                landmarks = hand.landmark
                frame_queue.put(landmarks)
                drawing_utils.draw_landmarks(
                    frame, hand, mp.solutions.hands.HAND_CONNECTIONS
                )

            process_this_frame = 0

        process_this_frame += 0.2  # (Processes 1 in 5 frames)

        # Display the resulting image
        cv2.imshow("Video", frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
