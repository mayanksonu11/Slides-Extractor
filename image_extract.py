import cv2
import time

file_name = "class1.mp4"

vidObj = cv2.VideoCapture(file_name)
# Used as counter variable
count = 0
# checks whether frames were extracted
success = 1

def compare(prev,curr):
	# cv2.imshow("prev",prev)
	# cv2.imshow("curr",curr)
	prev = cv2.cvtColor(prev, cv2.COLOR_BGR2GRAY)	
	curr = cv2.cvtColor(curr, cv2.COLOR_BGR2GRAY)	

	h = prev.shape[0]
	w = prev.shape[1]
	similarity = 0 
	dissimilarity = 0
	total = 0
	# time.sleep(5)
	for i in range(h):
		for j in range(w):
			if prev[i,j] >= 30 and curr[i,j] >= 30:
				total += 1
			if abs(prev[i,j]-curr[i,j])>=40 and curr[i,j] <=20:
				dissimilarity += 1
	cv2.destroyAllWindows()
	return similarity/total, dissimilarity/total


while success:

    # vidObj object calls read
    # function extract frames
    success, image = vidObj.read()
    tmp = cv2.resize(image, (0,0), fx=0.25, fy=0.25) 
    if count==0:
    	prev = tmp
    	prev_temp = image
    # cv2.imshow("prev",prev)
    # cv2.imshow("image",image)
	
    count += 1
    if count%15!=1:
    	continue
    similarity, dissimilarity = compare(prev,tmp)
    print(dissimilarity)
    if dissimilarity>=0.9:
    	cv2.imwrite("images/frame%d.jpg" % (count/30), prev_temp)
    	# prev = tmp
    prev_temp = image
    prev = tmp
    # Saves the frames with frame-count
    # if count%150 == 0: