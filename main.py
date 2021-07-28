from utils import *
from configparser import ConfigParser
import argparse

config_object = ConfigParser()
config_object.read("config.conf")

crop_mode = config_object["SETTINGS"]["crop_mode"]
cam_id = config_object["SETTINGS"]["cam_id"]
sleep_time = config_object["SETTINGS"]["sleep_time"]
faces_folder_path = config_object["PATH"]["faces_folder_path"]
faces_image_path = config_object["PATH"]["faces_image_path"]
multi_images_folder_path = config_object["PATH"]["multi_images_folder_path"]

def main(args):
    if args.mode == "cii":
        face_crop_in_image(args.fip, args.ffp)

    elif args.mode == "cimi":
        face_crop_in_multi_images(args.mifp, args.ffp)
    
    elif args.mode == "civ":
        face_crop_in_video(args.ci, args.ffp, args.st)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Face crop in image')
    parser.add_argument('--mode', default=crop_mode, type=str, help='crop in image: cii, crop in multi images: cimi, crop in video: civ')
    parser.add_argument('--ffp', default=faces_folder_path, type=str, help='faces folder path')
    parser.add_argument('--fip', default=faces_image_path, type=str, help='face imges path')
    parser.add_argument('--st', default=sleep_time, type=str, help='sleep time')
    parser.add_argument('--mifp', default=multi_images_folder_path, type=str, help='multi face images path')
    parser.add_argument('--ci', default=cam_id, type=str, help='camera id')
    args = parser.parse_args()
    main(args)