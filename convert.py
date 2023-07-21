#!/bin/python
from obsidian_to_hugo import ObsidianToHugo
import os

hugo_dir = "../../../Source/blog"

cvter = ObsidianToHugo(
    obsidian_vault_dir = os.path.abspath(os.path.join(os.getcwd(), "./")),
    hugo_content_dir = os.path.abspath(os.path.join(os.getcwd(), "../../../Source/blog/content"))
)

cvter.run()