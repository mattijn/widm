import face_recognition
import cv2

frame_skip = 10

# Load some sample pictures and learn how to recognize them.
image_1 = face_recognition.load_image_file("img/2023/anke.png")
face_encoding_1 = face_recognition.face_encodings(image_1)[0]

image_2 = face_recognition.load_image_file("img/2023/annick.png")
face_encoding_2 = face_recognition.face_encodings(image_2)[0]

image_3 = face_recognition.load_image_file("img/2023/daniel.png")
face_encoding_3 = face_recognition.face_encodings(image_3)[0]

image_4 = face_recognition.load_image_file("img/2023/froukje.png")
face_encoding_4 = face_recognition.face_encodings(image_4)[0]

image_5 = face_recognition.load_image_file("img/2023/jurre.png")
face_encoding_5 = face_recognition.face_encodings(image_5)[0]

image_6 = face_recognition.load_image_file("img/2023/nabil.png")
face_encoding_6 = face_recognition.face_encodings(image_6)[0]

image_7 = face_recognition.load_image_file("img/2023/ranomi.png")
face_encoding_7 = face_recognition.face_encodings(image_7)[0]

image_8 = face_recognition.load_image_file("img/2023/sander.png")
face_encoding_8 = face_recognition.face_encodings(image_8)[0]

image_9 = face_recognition.load_image_file("img/2023/sarah.png")
face_encoding_9 = face_recognition.face_encodings(image_9)[0]

image_10 = face_recognition.load_image_file("img/2023/soy.png")
face_encoding_10 = face_recognition.face_encodings(image_10)[0]

known_faces = [
    face_encoding_1,
    face_encoding_2,
    face_encoding_3,
    face_encoding_4,
    face_encoding_5,
    face_encoding_6,
    face_encoding_7,
    face_encoding_8,
    face_encoding_9,
    face_encoding_10
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0
p6 = 0
p7 = 0
p8 = 0
p9 = 0
p10 = 0

# Loading video for face detection
eps = "S23E01"

# Create an output movie file (make sure resolution/frame rate matches input video!)
fourcc = cv2.VideoWriter_fourcc(*"XVID")
output_movie = cv2.VideoWriter(f"episodes/{eps}_tracked_frameskip_{frame_skip}.avi",
                               fourcc, 25, (960, 540))

video_capture = cv2.VideoCapture(f"episodes/{eps}.mp4")
length = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
print(length)

frame_count = 0
a = False

while video_capture.isOpened():
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Bail out when the video file ends
    if not ret:
        video_capture.release()
        break

    # We will search face in every X frames to speed up process.
    frame_count += 1
    if frame_count % 500 == 0:
        print("{}/{}".format(frame_count, length))
    if frame_count % frame_skip == 0:
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Find all the faces and face encodings in the current frame of video
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

        face_names = []
        for face_encoding in face_encodings:
            # See if the face is a match for the known face(s)
            match = face_recognition.compare_faces(known_faces, face_encoding,
                                                   tolerance=0.50)

            # If you had more than 2 faces, you could make this logic a lot prettier
            # but I kept it simple for the demo
            name = None
            if match[0]:
                p1 += 1
                name = "Anke"
            elif match[1]:
                p2 += 1
                name = "Annick"
            elif match[2]:
                p3 += 1
                name = "Daniel"
            elif match[3]:
                p4 += 1
                name = "Froukje"
            elif match[4]:
                p5 += 1
                name = "Jurre"
            elif match[5]:
                p6 += 1
                name = "Nabil"
            elif match[6]:
                p7 += 1
                name = "Ranomi"
            elif match[7]:
                p8 += 1
                name = "Sander"
            elif match[8]:
                p9 += 1
                name = "Sarah"
            elif match[9]:
                p10 += 1
                name = "Soy"

            face_names.append(name)

        for (top, right, bottom, left), name in zip(face_locations, face_names):
            if not name:
                continue

            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255),
                          cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255),
                        1)

        output_movie.write(frame)

cv2.destroyAllWindows()

stat_eps = {"anke": p1, "annick": p2, "daniel": p3, "froukje": p4, "jurre": p5,
            "nabil": p6, "ranomi": p7, "sander": p8, "sarah": p9, "soy": p10}

print(stat_eps)

print(sorted(stat_eps.items(), reverse=True, key=lambda item: item[1]))
