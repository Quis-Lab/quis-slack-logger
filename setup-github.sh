#!/bin/bash

# Script to push Slack Logger to GitHub
# Make sure you've created the repository on GitHub first!

echo "🚀 Setting up GitHub repository for Slack Error Logger"
echo ""

# Check if remote already exists
if git remote | grep -q origin; then
    echo "⚠️  Remote 'origin' already exists:"
    git remote -v
    read -p "Do you want to update it? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        read -p "Enter your GitHub username: " GITHUB_USERNAME
        read -p "Enter repository name (default: quis-slack-logger): " REPO_NAME
        REPO_NAME=${REPO_NAME:-quis-slack-logger}
        git remote set-url origin "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
    else
        echo "Using existing remote"
    fi
else
    read -p "Enter your GitHub username: " GITHUB_USERNAME
    read -p "Enter repository name (default: quis-slack-logger): " REPO_NAME
    REPO_NAME=${REPO_NAME:-quis-slack-logger}
    git remote add origin "https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"
fi

echo ""
echo "📦 Pushing code to GitHub..."
git push -u origin main

echo ""
echo "🏷️  Creating version tag v1.0.0..."
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0

echo ""
echo "✅ Done! Your package is now on GitHub!"
echo ""
echo "📝 To use in other projects, add to requirements.txt:"
echo "   git+https://github.com/${GITHUB_USERNAME}/${REPO_NAME}.git@v1.0.0"
echo ""

