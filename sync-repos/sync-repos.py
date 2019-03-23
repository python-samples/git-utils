#!/usr/bin/env python

# requires GitPython pip package to be installed

import os
import yaml
import git

script_dir = os.path.dirname(__file__)
#work_dir=os.getcwd()

with open(os.path.join(script_dir,"repos.yml"), 'r') as stream:
    repos_data = yaml.load(stream)

server_url = repos_data['server_url']

for project, repos in repos_data['repos'].items():
    project_path = os.path.join(script_dir,project)
    if not os.path.isdir(project_path):
        os.mkdir(project_path)
    for repo in repos:
        repo_path = os.path.join(project_path,repo)
        print(repo_path)
        if os.path.isdir(repo_path):
            try:
                os.system('cd "' + repo_path + '" && git branch -r | grep -v \'\->\' | while read remote; do git branch --track "${remote#origin/}" "$remote"; done')
                os.system('cd "' + repo_path + '" && git fetch --all')
                os.system('cd "' + repo_path + '" && git pull --all')
#                g = git.cmd.Git(folder)
#                g.pull()
            except Exception as e:
                print("   - failed pulling! The error message was: " + str(e))
        else:
            repository = server_url + project + "/" + repo + ".git"
            print(repository)
            try:
                git.Git(project_path).clone(repository)
            except Exception as e:
                print("   - failed cloning! The error message was: " + str(e))
