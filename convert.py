from obsidian_to_hugo import ObsidianToHugo
import os

cvter = ObsidianToHugo(
    obsidian_vault_dir = os.path.abspath(os.path.join(os.getcwd(), "./")),
    hugo_content_dir = os.path.abspath(os.path.join(os.getcwd(), "/Source/blog/content"))
)

cvter.run()

os.popen("hugo -s T:/Source/blog")

from datetime import datetime, timedelta
now_time = datetime.now()
utc_time = now_time - timedelta(hours=8)  # 减去8小时
utc_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")

os.system("hugo -s T:/Source/blog")
os.system("git -C T:/Source/blog/public add .")
os.system("git -C T:/Source/blog/public commit -m \"{}\"".format(utc_time))
os.system("git -C T:/Source/blog/public push")
