#!/usr/bin/env bash
# exit on error
set -o errexit

# 1. Build React Frontend (BotivateScanner)
echo "--- BUILDING REACT FRONTEND ---"
cd BotivateScanner
npm install
npm run build
cd ..

# 2. Setup Frontend Directory
# My FastAPI backend expects BotivateScanner/dist to exist or be mapped.
# In main.py, let's verify where it expects it.
echo "--- INSTALLING PYTHON DEPENDENCIES ---"
pip install -r requirements.txt

echo "--- BUILD COMPLETE ---"
