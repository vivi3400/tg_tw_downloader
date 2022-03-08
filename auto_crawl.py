import uiautomator2 as u2
import time
import random
import download
import os

def swipe_up():
    d.swipe(0.5, 0.7, 0.5, 0.4)

def share_url():

    try:
        if d(resourceId="com.twitter.android:id/inline_twitter_share").info['bounds']['top'] > 350\
                and d(resourceId="com.twitter.android:id/inline_twitter_share").info['bounds']['bottom'] <2000:

            d(resourceId="com.twitter.android:id/inline_twitter_share").click()

            # print('normal links')
        else:
            print('outside the boundry')
            d.swipe(0.5,0.25,0.5,0.4,steps=50)

            if d(resourceId="com.twitter.android:id/inline_twitter_share").info['bounds']['top'] > 350\
                and d(resourceId="com.twitter.android:id/inline_twitter_share").info['bounds']['bottom'] <2000:

                d(resourceId="com.twitter.android:id/inline_twitter_share").click()
                d(resourceId="com.twitter.android:id/carousel_item_title", text="Copy Link").click(timeout=30)

            return

        d(resourceId="com.twitter.android:id/carousel_item_title", text="Copy Link").click(timeout=30)
    except:
        pass

if __name__ == '__main__':
    d = u2.connect("f2c72deb")

    folder = "2_guanzhang"
    txt = folder+".txt"

    # folder_path = os.path.join(os.getcwd(),folder)
    # try:
    #     os.makedirs(folder_path)
    # except:
    #     pass

    for i in range(100):
        print('currently crawing',str(i))
        swipe_up()
        # r_time = random.randint(1, 3)
        # time.sleep(r_time)
        share_url()

        print(d.clipboard)
        # download.down_img(d.clipboard,folder_path)
        f1 = open(txt, 'a')
        f1.write(d.clipboard + '\n')
        f1.close()
