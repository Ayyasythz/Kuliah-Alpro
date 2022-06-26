video_upload = [
    {'Video' : 4, 'Likes' : 2100, 'Comments' : 300},
    {'Likes' : 1300, 'Comments' : 200, 'Shares' : 100},
    {'Video' : 5, 'Likes' : 330, 'Comments' : 80, 'Shares' : 30},
    {'Comments' : 300, 'Shares' : 20}
]

jumlah_like = 0
upload = 1
for post in video_upload:
    print(f"Upload ke - {upload}")
    upload += 1
    try:
        jumlah_like += post["Likes"]
        like = post['Likes']
    except KeyError:
        print("Post Ini tidak Memiliki Likes")
    else:
        print(f"Post ini memiliki {like} Likes")


print(f"Jumlah Total Likes adalah {jumlah_like}")