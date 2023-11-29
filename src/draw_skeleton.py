import cv2
import pyautogui
import mediapipe as mp
import jointsformer as jf
import torch

def capture():
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
    drawing_utils = mp.solutions.drawing_utils


    screen_width, screen_height = pyautogui.size()
    index_y = 0
    framelist = []
    while True:
        _, frame = cap.read()
        frame = cv2.flip(frame, 1)
        frame_height, frame_width, _ = frame.shape
        # Resize the image
        frame = cv2.resize(frame, (224, 224))
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = hand_detector.process(rgb_frame)
        hands = output.multi_hand_landmarks

        if hands:
            for hand in hands:
                drawing_utils.draw_landmarks(frame, hand, mp.solutions.hands.HAND_CONNECTIONS)
                landmarks = hand.landmark

                framelist.append(frame)
                if len(framelist)==4:
                    tensor = jf.preprocess(frame_list= framelist)
                    jf.predict(tensor_input=tensor)
                    framelist.clear()

                # # Print the coordinates of each landmark
                # for id, landmark in enumerate(landmarks):
                #     x = int(landmark.x * frame_width)
                #     y = int(landmark.y * frame_height)
                #     print(f"Landmark {id}: ({x}, {y})")

        cv2.imshow('frame', frame)

        # observe the keypress by the user
        keypress = cv2.waitKey(1) & 0xFF

        # if the user pressed "q", then stop looping
        if keypress == ord("q"):
            # free up memory
            cap.release()
            cv2.destroyAllWindows()
            break
