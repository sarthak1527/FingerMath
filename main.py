import os
import cv2
import mediapipe as mp
from mediapipe.tasks.python import vision
from mediapipe.tasks.python import BaseOptions

# ----------------------------
# Load model
# ----------------------------
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "hand_landmarker.task"
)

options = vision.HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    num_hands=2,
    min_hand_detection_confidence=0.3,
    min_hand_presence_confidence=0.3,
    min_tracking_confidence=0.3,
)

detector = vision.HandLandmarker.create_from_options(options)

# ----------------------------
# Camera
# ----------------------------
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

FINGER_TIPS = [4, 8, 12, 16, 20]


def finger_in_box(fx, fy, box):
    x, y, w, h = box
    return x <= fx <= x + w and y <= fy <= y + h


while True:

    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.flip(frame, 1)

    h, w = frame.shape[:2]

    # Bigger boxes
    BOXES = [
    ((120, 120, 220, 260), "BOX 1", (255, 0, 0)),
    ((760, 120, 220, 260), "BOX 2", (0, 0, 255)),
     ]

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    mp_image = mp.Image(
        image_format=mp.ImageFormat.SRGB,
        data=rgb
    )

    result = detector.detect(mp_image)

    total = 0

    # Draw boxes
    for box, label, color in BOXES:

        x, y, bw, bh = box

        cv2.rectangle(frame, (x, y), (x + bw, y + bh), color, 3)

        cv2.putText(
            frame,
            label,
            (x + 20, y + 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            3,
        )

        count = 0

        if result.hand_landmarks:

            for hand in result.hand_landmarks:

                for tip in FINGER_TIPS:

                    lm = hand[tip]

                    fx = int(lm.x * w)
                    fy = int(lm.y * h)

                    cv2.circle(frame, (fx, fy), 8, (0, 255, 0), -1)

                    if finger_in_box(fx, fy, box):
                        count += 1

        total += count

        cv2.putText(
            frame,
            str(count),
            (x + 130, y + 260),
            cv2.FONT_HERSHEY_DUPLEX,
            4,
            color,
            5,
        )

    # Total
    cv2.putText(
        frame,
        f"TOTAL = {total}",
        (350, 670),
        cv2.FONT_HERSHEY_DUPLEX,
        2,
        (255, 255, 255),
        4,
    )

    # Number of hands
    hands_detected = len(result.hand_landmarks) if result.hand_landmarks else 0

    cv2.putText(
        frame,
        f"Hands: {hands_detected}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 255, 255),
        2,
    )

    cv2.imshow("Finger Math", frame)

    key = cv2.waitKey(1)

    if key == 27:
        break

detector.close()
cap.release()
cv2.destroyAllWindows()