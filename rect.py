import cv2
import numpy as np
 
# Create a VideoCapture object
capl = cv2.VideoCapture("/home/user/NeoAeroIntern/PushBroom/LeftStereo.avi")
capr = cv2.VideoCapture("/home/user/NeoAeroIntern/PushBroom/RightStereo.avi")

frame_width=752
frame_height=480
cameraMatrix1=np.array([[454.812772, 0, 397.120001],
				[0, 452.989403, 228.597388],
				[0,0,1]])
cameraMatrix2=np.array([[458.719606, 0, 372.365934],
				[0, 455.914300, 263.726870],
				[0,0,1]])
distCoeffs1=np.array([-0.380800, 0.114514, -0.004890, -0.001906, 0.000000])
distCoeffs2=np.array([-0.394637, 0.134148, -0.001294, -0.001776, 0.000000])
imageSize=np.array([752,480])
R = np.array([[0.999935, -0.002227, -0.011225],
	[0.002210, 0.999996, -0.001530],
	[0.011228, 0.001505, 0.999936]])
T = np.array([-0.11570308541861062,0.0015164440398994998,0.003499626050482985])
R1 = np.zeros((3,3))
R2 = np.zeros((3,3))
P1 = np.zeros((3,4))
P2 = np.zeros((3,4))
Q = np.zeros((4,4))
cv2.stereoRectify(cameraMatrix1, distCoeffs1,cameraMatrix2, distCoeffs2, (752,480), R, T, R1, R2, P1, P2, Q=None, flags=0, alpha=-1, newImageSize=(752, 480)) 
newcameraMatrix1 = P1[:,:-1]
newcameraMatrix2 = P2[:,:-1]
map1x, map1y = cv2.initUndistortRectifyMap(cameraMatrix1, distCoeffs1, R1, newcameraMatrix1, (752,480), cv2.CV_32FC1)
map2x, map2y = cv2.initUndistortRectifyMap(cameraMatrix2, distCoeffs2, R2, newcameraMatrix2, (752,480), cv2.CV_32FC1)
 
# Check if camera opened successfully
if (capl.isOpened() == False): 
  print("Unable to read camera feed left")
if (capr.isOpened() == False): 
  print("Unable to read camera feed right")
# Default resolutions of the frame are obtained.The default resolutions are system dependent.
# We convert the resolutions from float to integer.
frame_width = int(capl.get(3))
frame_height = int(capl.get(4))
 
# Define the codec and create VideoWriter object.The output is stored in 'outpy.avi' file.
outl = cv2.VideoWriter('outpyleft.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
outr = cv2.VideoWriter('outpyright.avi',cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
 
while(True):
  retl, framel = capl.read()
  retr, framer = capr.read()
 
  if retl == True and retr==True: 
    
    dst1 = cv2.remap(framel, map1x, map1y, cv2.INTER_LINEAR)
    dst2 = cv2.remap(framer, map2x, map2y, cv2.INTER_LINEAR)
    # Write the frame into the file 'output.avi'
    outl.write(dst1)
    outr.write(dst2)
 
    # Display the resulting frame    
    cv2.imshow('framel',framel)    
    cv2.imshow('framer',framer)
 
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
 
  # Break the loop
  else:
    break 
 
# When everything done, release the video capture and video write objects
capl.release()
outl.release()
capr.release()
outr.release()
# Closes all the frames
cv2.destroyAllWindows() 