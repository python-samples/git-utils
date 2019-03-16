#!/usr/bin/env python

# requires GitPython pip package to be installed

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
            except Exception as e:
                print("   - failed pulling! The error message was: " + str(e))
        else:
            repo = "https://git-url/scm/" + folder + ".git"
            print(repo)
            try:
                git.Git(k).clone(repo)
            except Exception as e:
                print("   - failed cloning! The error message was: " + str(e))
