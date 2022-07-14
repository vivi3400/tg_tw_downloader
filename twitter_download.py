import requests
from urllib.request import urlretrieve
import json
import os
import time
import random

def down_img(resourcd_id,folder):

    # p = "https://api.twitter.com/1.1/statuses/show.json?id="+str(resourcd_id)

    p = f"https://api.twitter.com/1.1/statuses/show/{resourcd_id}.json?tweet_mode=extended"

    print(p)
    headers = {
        "Authorization":"Bearer AAAAAAAAAAAAAAAAAAAAABXsygAAAAAAmJuTUyoBiQiFqw9KIVOZPoELi%2FM%3DPau8s2HiUxM9v3eiOtJQu3bdKcCbaHyw5le0yH1LLhfJh6580X"
    }

    p_res = requests.get(p,headers=headers)

    data = json.loads(p_res._content)

    print(data)

    try:
        media_data = (data["extended_entities"])
    except:

        return
    print('media data ',media_data)

    for media in media_data['media']:

        if ("video_info" in media):

            video_all_quality = (media["video_info"]['variants'])

            bitrate = []

            for video in video_all_quality:
                # print(video)
                if "bitrate" in video:
                    bitrate.append(video["bitrate"])
                    # print(video["bitrate"])
                else:
                    bitrate.append(-1)

            print(bitrate)
            print(max(bitrate))

            max_bitrate_index = (bitrate.index(max(bitrate)))

            video_url = (video_all_quality[max_bitrate_index]["url"])
            try:
                urlretrieve(video_url, folder+str(resourcd_id)+".mp4")
            except:
                pass

        else:
            img_url = (media["media_url_https"])
            img_name = (img_url.split("/")[-1])
            try:
                urlretrieve(img_url, folder+img_name)
            except:
                pass

if __name__ == '__main__':

    txt_name = "noteFromPhone"
    folder_name = "Apr6"
    folder_path = os.path.join(os.getcwd(),folder_name)
    try:
        os.makedirs(folder_path)
    except:
        pass

    read_file = os.path.join(os.getcwd(),txt_name+".txt")

    f1= open(read_file,"r")
    lines = f1.readlines()
    for line in lines:
        resourcd_id = (line.split("/")[-1].split("?")[0])
        print("current progress is",lines.index(line))
        print("current progres is ",round(float(((lines.index(line))/float(len(lines)))*100),3),"%")
        # if lines.index(line)<52:
        #     continue
        print('rescource id is  ', resourcd_id)
        down_img(resourcd_id,folder_path+"/")
        time.sleep(random.randint(1,2))