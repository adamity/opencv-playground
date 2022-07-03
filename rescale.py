import cv2 as cv


def rescaleFrame(frame, scale=0.5):
    # Images, videos and Live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)


# Reading images
# img = cv.imread('photos/cat_large.jpg')
# img_resized = rescaleFrame(img, 0.2)

# cv.imshow('Cat Resized', img_resized)

# cv.waitKey(0)

# Reading videos
# capture = cv.VideoCapture('videos/cat.mp4')

# while True:
#     isTrue, frame = capture.read()

#     frame_resized = rescaleFrame(frame)

#     cv.imshow('Video Resized', frame_resized)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()

# Live video
# capture = cv.VideoCapture(0)

# while True:
#     isTrue, frame = capture.read()

#     cv.imshow('Live Video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()
