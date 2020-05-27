import requests
from bs4  import BeautifulSoup
from pytube import YouTube
import os

def output_log(log, output_file):
    LOCAL = os.getcwd()
    data = open(LOCAL + '\\' + output_file, "w", encoding = "utf-8")
    for line in log:
        data.write(line)
        data.write("\n\n\n\n")
    data.close()

def yt_search(search_key = ""):
    class parsed():
        def __init__(self,til,url):
            title = til
            url = url

    print_list = parsed()

    #request = requests.get("https://www.youtube.com/results?search_query={}".format(search_key))
    request = requests.get("https://www.youtube.com/results?search_query={}".format("吳宗憲"))
    content = request.content
    soup = BeautifulSoup(content, "html.parser")

    for all_mv in soup.select(".yt-lockup-video"):
        data = all_mv.select("a[rel='spf-prefetch']")
        print_list.title.append(str(data[0].get("title")))
        print_list.url.append("https://www.youtube.com{}".format(data[0].get("href")))

    return print_list
    #output_log(print_list, 'log2.txt')


# on_progress_callback takes 4 parameters.
def progress_Check(chunk = None, file_handle = None, remaining = None):
    #Gets the percentage of the file that has been downloaded.
   contentSize = file_size
   size = contentSize - remaining
   print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
   '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')
 
#Grabs the file path for Download
def file_path():
    home = os.path.expanduser('~')
    download_path = os.path.join(home, 'Downloads')
    return download_path
 
def yt_download(yt_url = ""):

    # Searches for the video and sets up the callback to run the progress indicator. 
    try:
        video = YouTube(yt_url, on_progress_callback=progress_Check)
    except:
        print("ERROR. Check your:\n  -connection\n  -url is a YouTube url\n\nTry again.")
        return -30

    #Get the first video type - usually the best quality.
    video_type = video.streams.filter(progressive = True, file_extension = "mp4").first()

    #Gets the title of the video
    title = video.title

    #Prepares the file for download
    print ("Fetching: {}...".format(title))
    global file_size
    file_size = video_type.filesize
    #Starts the download process
    video_type.download(file_path())

    print ("Ready to download another video.\n\n")
    return 0

#########################################################################
# main()
class gotot_lablel(Exception): pass

file_size = 0
yt_cnt = cnt = rc= 0
print("Your video will be saved to: {}".format(file_path()))
#yt_parsed = yt_search()

while (rc != 0):
    # check syntax

    # search youtube
    yt_parsed = [parsed(["0","1",["1"),parsed(["1"],["2"),parsed(["-99"],["-99")]
    yt_parsed = {["0","1"],["1","2","-99"]}
    #yt_parsed = yt_search()

    # parse URL
    ### YS_function()
    #yt_url = input("Your YouTube URL: ")
    yt_url = yt_parsed[0]
    try:
        if (yt_url == "-99"):
            print("\nGOT end sign, stop download\n")
            rc = -99
            raise gotot_lablel()

        print(yt_url)
        print ("Accessing YouTube URL...")

        # download youtube
        rc = yt_download(yt_url)
        cnt = cnt + 1

    except gotot_lablel:
        # SW recovery flow
        print("rc:" + str(rc) + "\n")

if (cnt != yt_cnt):
    print("Download FAIL !!")