from pytube import YouTube
import os
# ask for the link from user
# download any video from youtube by only entering url
# dependencies for python3:
# pip3 install os_sys
# pip3 install pytube
link = input("Enter the link of YouTube video you want to download:  ")
isAudio = input("Want to download only audio? Enter Y if yes: ")
yt = YouTube(link)
# #Showing details
print("Title: ", yt.title)
print("Number of views: ", yt.views)
print("Length of video: ", yt.length)
print("Rating of video: ", yt.rating)
if isAudio == "y" or isAudio == "Y":
    video = yt.streams.filter(only_audio=True).first()
    destination = './downloads/'
    # # download the file
    out_file = video.download(output_path=destination)
    print(out_file)
    #
    # save the file
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)
else:
    video = yt.streams.get_highest_resolution()
    # # result of success
    print(video.title + " has been successfully downloaded.")
    # Starting download
    print("Downloading...")
    video.download()
    print("Download completed!!")
