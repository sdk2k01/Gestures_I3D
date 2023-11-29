import cv2
import mediapipe as mp

BaseOptions = mp.tasks.BaseOptions
GestureRecognizer = mp.tasks.vision.GestureRecognizer
GestureRecognizerOptions = mp.tasks.vision.GestureRecognizerOptions
GestureRecognizerResult = mp.tasks.vision.GestureRecognizerResult
VisionRunningMode = mp.tasks.vision.RunningMode


def print_result(
    result: GestureRecognizerResult, output_image: mp.Image, timestamp_ms: int
):
    print("gesture recognition result: {}".format(result))


options = GestureRecognizerOptions(
    base_options=BaseOptions(
        model_asset_path="/Users/soumyadeep/Gestures_I3D/assets/gesture_recognizer.task"
    ),
    running_mode=VisionRunningMode.LIVE_STREAM,
    result_callback=print_result,
)


if __name__ == "__main__":
    video_capture = cv2.VideoCapture(0)

    with GestureRecognizer.create_from_options(options) as recognizer:
        while True:
            # Grab a single frame of video
            ret, frame = video_capture.read()
            frame = cv2.flip(frame, 1)

            mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)

            recognizer.recognize_async(
                mp_image, str(video_capture.get(cv2.CAP_PROP_POS_MSEC))
            )

            # Display the resulting image
            cv2.imshow("Video", frame)

            # Hit 'q' on the keyboard to quit!
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
