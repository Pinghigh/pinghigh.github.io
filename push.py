#!/bin/python
from obsidian_to_hugo import ObsidianToHugo
import os

hugo_dir = "../../../Source/blog"

cvter = ObsidianToHugo(
    obsidian_vault_dir = os.path.abspath(os.path.join(os.getcwd(), "./")),
    hugo_content_dir = os.path.abspath(os.path.join(os.getcwd(), "../../../Source/blog/content"))
)

cvter.run()

from datetime import datetime, timedelta
now_time = datetime.now()
utc_time = now_time # 减去8小时
utc_time = utc_time.strftime("%Y-%m-%d %H:%M:%S")

os.system(f"hugo -s {hugo_dir}")
os.system(f"git -C {hugo_dir}/public add .")
os.system(f"git -C {hugo_dir}/public commit -m \"{utc_time}\"")
os.system(f"git -C {hugo_dir}/public push")
