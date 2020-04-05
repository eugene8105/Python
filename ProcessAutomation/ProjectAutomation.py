import subprocess
import requests
import sys

# Notice that you username and token are required here
r = requests.post(
  "https://api.github.com/users/<username>/repos?access_token=<generated token>", 
  data={
  "name": "Test 1",
  "description": "This is your first repository",
  "homepage": "https://github.com",
  "private": false,
  "has_issues": true,
  "has_projects": true,
  "has_wiki": true
})

if r.status_code != 200:
  sys.exit()