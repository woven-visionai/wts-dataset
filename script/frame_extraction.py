import cv2 

def processing(video_path):
  
  vidcap = cv2.VideoCapture(video_path)
  fps = vidcap.get(cv2.CAP_PROP_FPS)

  readable,image = vidcap.read()
  count = 0

  while readable:
    cv2.imwrite("frame%d.jpg" % count, image)
    if fps == 60:
      count += 1 
      cv2.imwrite("frame%d.jpg" % count, image)
    readable,image = vidcap.read()
    count += 1
        
if __name__ == '__main__':
    
    video_path = 'path/to/../20230707_12_SN17_T1_Camera1_0.mp4'
    processing(video_path)
