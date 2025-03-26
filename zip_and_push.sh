#!/bin/bash

MODULE_NAME="Module_2_Exploring_Data_World"
ZIP_NAME="${MODULE_NAME}.zip"
REPO_NAME="spg-${MODULE_NAME// /_ | tr '[:upper:]' '[:lower:]'}"

echo "📦 Zipping folder..."
zip -r $ZIP_NAME $MODULE_NAME > /dev/null

echo "✅ Zipped: $ZIP_NAME"

# Create Git repo if not already present
if [ ! -d ".git" ]; then
  echo "🌀 Initializing Git repo..."
  git init
  git remote add origin https://github.com/YOUR_USERNAME/$REPO_NAME.git
fi

# Move into the folder
cd $MODULE_NAME

echo "📁 Committing changes..."
git add .
git commit -m "🚀 Added $MODULE_NAME full assistant package"

echo "🚀 Pushing to GitHub..."
git push -u origin main

echo "✅ All done!"
