#!/usr/bin/env python3

import os
import yaml
import git

with open("repos.yml", 'r') as stream:
    repos_data = yaml.load(stream)

for k, v in repos_data.items():
    if not os.path.isdir(k):
        os.mkdir(k)
    for repo in v:
        folder = k + "/" + repo
        print(folder)
        if os.path.isdir(folder):
            try:
                g = git.cmd.Git(folder)
                g.pull()
            except:
                print("   - failed pulling!")
        else:
            repo = "https://git-url/scm/" + folder + ".git"
            try:
                git.Git(k).clone(repo)
            except:
                print("   - failed cloning!")
