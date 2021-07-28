import cv2, os, time
from numpy import asarray
from PIL import Image
from mtcnn.mtcnn import MTCNN

detector = MTCNN()

def crop(img, results,face):
    x1, y1, width, height = results[face]["box"]
    x2, y2 = x1+width, y1+height
    cropped_face = img[y1:y2, x1:x2]
    face_image = Image.fromarray(cropped_face)
    face_image = face_image.resize((224,224))
    face_array = asarray(face_image)
    return face_array

def face_crop_in_image(faces_image_path, faces_folder_path):
    img = cv2.imread(faces_image_path)
    results = detector.detect_faces(img)
    print("[PLEASE WAIT]")
    start_time = time.time()
    for i in range(len(results[0:])):
        face_array = crop(img, results, i)
        cv2.imwrite(f"{faces_folder_path}/{i}.jpg", face_array)
    print(f"[FINISHED] [TIME: {time.time() - start_time :.2f} seconds]")

def face_crop_in_multi_images(multi_images_folder_path, faces_folder_path):
    all_img = os.listdir(f'{multi_images_folder_path}/.')
    cropped_face_number = 0
    print("[PLEASE WAIT]")
    start_time = time.time()
    for i in range(len(all_img)):
        img = cv2.imread(f'{multi_images_folder_path}/{all_img[i]}')
        results = detector.detect_faces(img)
        for j in range(len(results[0:])):
            face_array = crop(img, results, j)
            cv2.imwrite(f"{faces_folder_path}/{cropped_face_number}.jpg", face_array)
            cropped_face_number += 1
    print(f"[FINISHED] [TIME: {time.time() - start_time :.2f} seconds]")

def face_crop_in_video(cam_id, faces_folder_path, sleep_time):
    video = cv2.VideoCapture(int(cam_id))
    while True:
        ret, img = video.read()
        results = detector.detect_faces(img)
        print("[PLEASE WAIT]")
        start_time = time.time()
        for i in range(len(results[0:])):
            face_array = crop(img, results, i)
            cv2.imwrite(f"{faces_folder_path}/{i}.jpg", face_array)
            time.sleep(int(sleep_time))
        video.release()
        print(f"[FINISHED] [TIME: {time.time() - start_time :.2f} seconds]")

