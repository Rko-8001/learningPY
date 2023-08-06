import os
import shutil

from pytube import YouTube

def url_to_mp3(video_url: str):
    video_file = YouTube(video_url).streams.filter().get_audio_only().download() 
    
    mp4_name: str = video_file.split('\\')[-1]
    mp3_name: str = mp4_name[:-4] + '.mp3'
    os.rename(mp4_name, mp3_name)
    shutil.move(mp3_name, 'data/')
    
def main(): 
    try:
        print("Hooman. Careful Video shouldn't be age restricted. U parvat\n\n")
        url_to_mp3(input('Enter the video URL: '))
        print("\nCheck the data folder for the mp3 file..")
    except Exception as e:
        print(e)
        print('Hooman, you are not a coder.')

if __name__ == '__main__':
    main()
    

