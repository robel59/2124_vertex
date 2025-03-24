import subprocess
import os
import sys
from pathlib import Path
cwd = Path.cwd()
repo_name=cwd.name
subprocess.run(["git", "init"])
subprocess.run(["git" ,"add" ,"."])
subprocess.run(["git","commit","-m"," 'default'"])
subprocess.run(["gh", "repo", "create" ,repo_name, "--public"])
subprocess.run(["git", "remote", "add", repo_name, 'https://github.com/robel59/'+repo_name])

subprocess.run(["git","push"])
subprocess.run([
    "gh", "api",
    "--method", "POST",
    "-H", "Accept: application/vnd.github+json",
    "-H", "X-GitHub-Api-Version: 2022-11-28",
    f"/repos/robel59/{repo_name}/pages",
    "-f", "source[branch]=master",
    "-f", "source[path]=/root"
], check=True)
