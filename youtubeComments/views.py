from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
# Create your views here.
class data:
    def __init__(self):
        self.comment = []
        self.count = 20
        self.summarize = False
        self.summary1 = "Amazing Playlist scared of mathematical part of ML, DL. classifying attacks intrusion detection. Best teacher perfectos videos enough for interview. wrong min max scaler tomato leaf disease classification best architecture revision before interview never disappoint great work Thankyou sir community session for CNN and RNN suggest deep learning after completing"


    def fetch(self):
        from googleapiclient.discovery import build

        api_key = 'AIzaSyB-SYV_r4VqEO55M97b6Kso013iE25j9Xo'

        youtube = build('youtube', 'v3', developerKey=api_key)

        video_id = 'SH8D4WJBhms'
        # video_id = '3MFIpkeb-X0'

        comments = []
        nextPageToken = None

        while True:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                maxResults=100, 
                pageToken=nextPageToken
            ).execute()

            for item in results['items']:
                comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                comments.append(comment)

            nextPageToken = results.get('nextPageToken')

            if nextPageToken is None:
                break
        self.comment = comments
    # def summary(self):
        


        

obj = data()
obj.fetch()
# obj.summary()
def index(request):
    load = loader.get_template('home.html')
    context = {
            'comment': obj.comment[:20],
            'summarize' : obj.summarize,
            'content': obj.summary1

        }
    return HttpResponse(load.render(context,request))
def refresh(request):
    obj.fetch()
    return redirect('/')

def summarize(request):
    obj.summarize = True
    return redirect('/')

def clssummarize(request):
    obj.summarize = False
    return redirect('/')
    


