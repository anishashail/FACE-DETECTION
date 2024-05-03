import cv2

#Using the haar cascade algorithm to load a pre-trained dataset in the code
face_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#Asking the user for choice
choice = input("Press \n1 - Detect faces in image\n2 - Detect faces in real time video\n3 - Detect faces in recorded video\n")

#Detecting faces in an image
if choice =='1':

    #Reading the image with opencv
    image = cv2.imread('group.jpg')

    #Converting the image into grayscale
    grayscale_image = cv2.cvtColor(image , cv2.COLOR_BGR2GRAY)

    #Detect faces
    faces_coordinates = face_data.detectMultiScale(grayscale_image , 1.3 , 5)

    #Making a rectangle around the faces in the image
    for (x , y , w , h) in faces_coordinates:
        cv2.rectangle(image , (x , y) , (x + w , y + h) , ( 255 , 0 , 0 ) , 2)

    #Showing the image on the screen
    cv2.imshow('face_detector' , image)
    cv2.waitKey()
    
#Detecting faces in real time video
elif choice == '2':

    #To capture video from the webcam
    video = cv2.VideoCapture(0)

    #Iterating over the frames captured
    while True:
        
        #Reading the current frame
        frame_read , current_frame = video.read()

        #Converting the frame into grayscale
        grayscale_frame = cv2.cvtColor(current_frame , cv2.COLOR_BGR2GRAY)

        #Detect faces
        faces_coordinates = face_data.detectMultiScale(grayscale_frame , 1.3 , 5)

        #Making a rectangle around the faces in the image
        for (x , y , w , h) in faces_coordinates:
            cv2.rectangle(current_frame , (x , y) , (x + w , y + h) , ( 255 , 0 , 0 ) , 2)

        #Showing the frame on the screen
        cv2.imshow('face_detector' , current_frame)

        #Exiting if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Release the capture
    video.release()

#Detecting faces in recorded video        
elif choice == '3':

    #To capture the recordedvideo 
    video = cv2.VideoCapture('recorded1.mp4')

    #Iterating over the frames captured
    while True:
        
        #Reading the current frame
        frame_read , current_frame = video.read()

        #Converting the frame into grayscale
        grayscale_frame = cv2.cvtColor(current_frame , cv2.COLOR_BGR2GRAY)

        #Detect faces
        faces_coordinates = face_data.detectMultiScale(grayscale_frame , 1.3 , 5)

        #Making a rectangle around the faces in the image
        for (x , y , w , h) in faces_coordinates:
            cv2.rectangle(current_frame , (x , y) , (x + w , y + h) , ( 255 , 0 , 0 ) , 2)

        #Showing the frame on the screen
        cv2.imshow('face_detector' , current_frame)

        #Exiting if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    #Release the capture
    video.release()

else :
    print ("Wrong Choice")
