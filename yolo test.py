import sys
import cv2
import argparse
sys.path.append('/home/robot-ros/yolov5')
import detect


def webcam_detect(
    weights='/home/robot-ros/ros2_ws/src/Het-cone/bestbest1.pt',
    img_size=[640, 640],
    conf=0.4,
    device='',
    augment=True,
    view_img=True
):
    source = '1'
    vid_stride = 1

    # ทดสอบเปิดกล้องก่อน
    cap = cv2.VideoCapture(int(source))
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

    if not cap.isOpened():
        print("cannot cam")
        return

    cap.release()  
    parser = argparse.Namespace(
        weights=weights,
        source=source,
        data='data/coco128.yaml',
        imgsz=img_size,
        conf_thres=conf,
        iou_thres=0.45,
        max_det=1000,
        device=device,
        view_img=view_img,
        save_txt=False,
        save_conf=False,
        save_crop=False,
        nosave=False,
        classes=None,
        agnostic_nms=False,
        augment=augment,
        visualize=False,
        update=False,
        project='runs/detect',
        name='exp',
        exist_ok=False,
        line_thickness=3,
        hide_labels=False,
        hide_conf=False,
        half=False,
        dnn=False,
        vid_stride=vid_stride,
        save_format=0,
        save_csv=False,
    )
    detect.main(parser)


if __name__ == "__main__":
    webcam_detect()
