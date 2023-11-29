import cv2
import mediapipe as mp

hand_detector = mp.solutions.hands.Hands(max_num_hands=1)


def get_skeleton(frame):
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks

    return hands
