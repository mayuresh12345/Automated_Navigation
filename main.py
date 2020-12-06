import matplotlib.pyplot as plt
import cv2
import os
from os.path import join, basename
from collections import deque
from detect_lanes import color_frame_pipeline


if __name__ == '__main__':

    resize_h, resize_w = 540, 960

    verbose = True
    if verbose:
        plt.ion()
        figManager = plt.get_current_fig_manager()
        figManager.window.showMaximized()

    cap = cv2.VideoCapture('input_video/laneVideo.mp4')
    out = cv2.VideoWriter('output_video/laneVideo.mp4',fourcc=cv2.VideoWriter_fourcc(*'DIVX'),fps=20.0, frameSize=(resize_w, resize_h))
    frame_buffer = deque(maxlen=10)
    while cap.isOpened():
    	ret, color_frame = cap.read()
    	if ret:
    		color_frame = cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB)
    		color_frame = cv2.resize(color_frame, (resize_w, resize_h))
    		frame_buffer.append(color_frame)
    		blend_frame = color_frame_pipeline(frames=frame_buffer, solid_lines=True, temporal_smoothing=True)
    		out.write(cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR))
    		cv2.imshow('detected_lanes',cv2.cvtColor(blend_frame, cv2.COLOR_RGB2BGR))
    		if cv2.waitKey(1) & 0xFF == ord('q'):
    			break
    	else:
    		break
    cap.release()
    out.release()
    cv2.destroyAllWindows()



