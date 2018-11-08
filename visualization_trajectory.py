import scipy.io
import numpy as np
import cv2
import os

# deteil about DukeMTMCT video information
tail_colors = [(0, 0, 1), (0, 1, 0), (0, 0, 0)]
start_time = [5543, 3607, 27244, 31182, 1, 22402, 18968, 46766]
NumFrames = [359580, 360720, 355380, 374850, 366390, 344400, 337680, 353220]
PartFrames = [[38370, 38370, 38400, 38670, 38370, 38400, 38790, 38370],
              [38370, 38370, 38370, 38670, 38370, 38370, 38640, 38370],
              [38370, 38370, 38370, 38670, 38370, 38370, 38460, 38370],
              [38370, 38370, 38370, 38670, 38370, 38370, 38610, 38370],
              [38370, 38370, 38370, 38670, 38370, 38400, 38760, 38370],
              [38370, 38370, 38370, 38700, 38370, 38400, 38760, 38370],
              [38370, 38370, 38370, 38670, 38370, 38370, 38790, 38370],
              [38370, 38370, 38370, 38670, 38370, 38370, 38490, 38370],
              [38370, 38370, 38370, 38670, 38370, 37350, 28380, 38370],
              [14250, 15390, 10020, 26790, 21060, 0, 0, 7890]]
start_sequence = 127720
end_sequence = 187540


def load_mat():
    trajectory = scipy.io.loadmat('D:/Code/DeepCC/DeepCC/experiments/demo/L3-identities/L3Final_trajectories.mat')
    data = trajectory['trackerOutputL3']
    return data


data = load_mat()


def calucate_part(icam, frame):
    sum_frame = 0
    for part_num in range(0, 10):
        previs_sum = sum_frame
        sum_frame += PartFrames[part_num][icam - 1]
        if sum_frame >= frame+1:
            return part_num, frame - previs_sum


def show_video(icam, startFrame, endFrame):
    #   only show video
    part_cam, part_frame = calucate_part(icam, startFrame)
    filename = 'D:/Code/DukeMTMC/videos/camera' + str(icam) + '/0000' + str(part_cam) + '.MTS'
    cap = cv2.VideoCapture(filename)
    part_cam_previous = part_cam
    cap.set(1, part_frame)
    for frame_num in range(startFrame, endFrame):
        part_cam, part_frame = calucate_part(icam, frame_num)
        if part_cam == part_cam_previous:
            ret, frame_img = cap.read()
            frame_img = draw_bb(icam, frame_num, frame_img)
            frame_img = cv2.resize(frame_img, (640, 360))
            cv2.imshow("video", frame_img)
            cv2.waitKey(1)
            print(str(frame_num) + 'yes')
        else:
            filename = 'D:/Code/DukeMTMC/videos/camera' + str(icam) + '/0000' + str(part_cam) + '.MTS'
            cap = cv2.VideoCapture(filename)
            ret, frame_img = cap.read()
            frame_img = draw_bb(icam, frame_num, frame_img)
            frame_img = cv2.resize(frame_img, (640, 360))
            cv2.imshow("video", frame_img)
            cv2.waitKey(1)
            part_cam_previous = part_cam
            print(str(frame_num) + 'no')
    cap.release()
    cv2.destroyAllWindows()


def draw_bb(icam, frame, img):
    find_ind = [i for i in range(len(data)) if data[i][0] == icam and data[i][1] == frame]
    for i in find_ind:
        left_x = int(data[i][3])
        left_y = int(data[i][4])
        right_x = int(data[i][3] + data[i][5])
        right_y = int(data[i][4] + data[i][6])
        cv2.rectangle(img, (left_x, left_y), (right_x, right_y), (255, 255, 0), 3)
        cv2.circle(img, (int(data[i][3] + data[i][5]/2), right_y), 15, (255, 0, 0), -1)

    return img


def show_video_old(icam, startFrame, endFrame):
    #   only show video
    for frame_num in range(startFrame, endFrame):
        part_cam, part_frame = calucate_part(icam, frame_num)
        filename = 'D:/Code/DukeMTMC/videos/camera' + str(icam) + '/0000' + str(part_cam) + '.MTS'
        cap = cv2.VideoCapture(filename)
        cap.set(1, part_frame)
        ret, frame = cap.read()
        frame = cv2.resize(frame, (640, 360))
        cv2.imshow("video", frame)
        cv2.waitKey(1)
    cap.release()
    cv2.destroyAllWindows()


def get_frame_image(icam, frame):
    #   get frame image
    part_cam, part_frame = calucate_part(icam, frame)
    filename = 'D:/Code/DukeMTMC/videos/camera' + str(icam) + '/0000' + str(part_cam) + '.MTS'
    cap = cv2.VideoCapture(filename)
    cap.set(1, part_frame)
    ret, frame = cap.read()
    return frame


def main():
    #   load data from L3Final_trajectories.mat
    show_video(5, 127720, 127820)


if __name__ == '__main__':
    main()
