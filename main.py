import time

import cv2
import torch
import Aim
import tools

if __name__ == '__main__':
    # 检查是否有可用的GPU设备
    device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
    print('使用设备：' + device.type)

    # 加载自瞄组件
    aim = Aim.Aim()

    # 加载YOLOv5模型
    model = torch.hub.load('ultralytics/yolov5', 'custom', path='./yolov5/yolov5s.pt').to(device)

    # cv2 窗口循环
    cv2.namedWindow('aim helper', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('aim helper', tools.get_capture_width(), tools.get_capture_height())
    while cv2.getWindowProperty('aim helper', cv2.WND_PROP_VISIBLE) > 0:
        # 记录执行时间
        start_time = time.time()

        # 截屏
        image = tools.screen_shot2()

        # 使用GPU进行预测
        if aim.is_open:
            results = model(image)

            # 处理预测结果
            # 获取预测结果的坐标和类别
            boxes = results.xyxy[0].cpu().numpy()
            class_ids = results.xyxy[0][:, -1].cpu().numpy().astype(int)

            # 在图像上绘制预测框和标签,并锁定预测目标
            for box, class_id in zip(boxes, class_ids):
                if class_id == 0:
                    x1, y1, x2, y2 = box[:4].astype(int)
                    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.putText(image, f'Class: {class_id}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

                    # 绝对目标
                    target_x = x1 + (x2 - x1) / 2
                    target_y = y1 + (y2 - y1) / 4

                    # 相对目标
                    Aim.move(target_x, target_y)

                    break

        # 显示截图
        cv2.imshow("aim helper", image)
        cv2.waitKey(1)

        # 统计执行时间后打印
        end_time = time.time()
        execution_time = end_time - start_time
        # print('FPS：' + str(1 / execution_time))

cv2.destroyAllWindows()
