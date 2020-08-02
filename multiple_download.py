from pytube import YouTube

# where to save
SAVE_PATH = "F:/"  # to_do

# link of the video to be downloaded
link = ["https://youtu.be/egFdYDxeftE",
        "https://www.youtube.com/watch?v=uSY8RO2C1pw"
        ]


# Video information
def video_info(yt_link):
    my_video = YouTube(yt_link)

    # Title of the Video

    print("Title: " + my_video.title)

    # Length of the Video in Seconds

    print("Duration: " + str(my_video.length))

    # URL of the Thumbnail of the video

    print("Thumbnail Link: " + my_video.thumbnail_url)

    # Description of the Video

    # print("Description: " + my_video.description)

    # Total Views of the Video

    print("Views: " + str(my_video.views))

    # Age Restricted Content

    print("Age Restricted: " + str(my_video.age_restricted))

    # ID of the Video

    print("Video ID: " + str(my_video.video_id))


for i in link:
    try:
        # object creation using YouTube which was imported in the beginning
        yt = YouTube(i)

        # you can check if the video supports 720p resolution (OR any other resolution you want)
        # and if yes you can download that
        # Here I am interested in 720p so I have given res as 720p
        webm_streams = yt.streams.filter(res="720p").first()

        if webm_streams is not None:
            print("downloading 720p")
            stream = yt.streams.filter(res="720p").first()
        else:
            print("downloading regular or first supported")
            stream = yt.streams.first()

        stream.download(SAVE_PATH)
        myVideoStreams = yt.streams
        print('Task Completed!')
        video_info(i)
        print("---------video information End---------\n\n")
    except Exception as e:
        print(e)
    except:
        print("Connection Error")  # to handle exception