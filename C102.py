import dropbox
import cv2
import time
import random

startTime=time.time()
def TakeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=videoCaptureObject.read()
        imageName='img'+str(number)+'.png'
        cv2.iamrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    print('snapshot taken')
    videoCaptureObject.release()
    cv2.destroyAllWindows

def uploadFile(imageName):
    accessToken='PlpHe8BxAB8AAAAAAAAAAeUNH6x_UN44fgsoNus8pTXuJMbwuG67TciM1SOZtZhy'
    file=imageName
    filefrom=file
    fileto='/newfolder/'+imageName
    dbx=dropbox.Dropbox(accessToken)
    with open(filefrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print('file uploaded')

def main():
    while(True):
        if((time.time()-startTime)>=300):
            name=TakeSnapshot()
            uploadFile(name)

main()