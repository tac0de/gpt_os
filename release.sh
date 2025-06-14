#!/bin/bash

# usage: ./release.sh 0.2

VERSION=$1

if [ -z "$VERSION" ]; then
  echo "❌ Usage: ./release.sh <version>"
  exit 1
fi

# Update version in setup.cfg (if it exists)
if [ -f setup.cfg ]; then
  echo "🔧 Updating setup.cfg to version $VERSION"
  sed -i '' "s/^version = .*/version = $VERSION/" setup.cfg
fi

# Optional: auto-add and commit changes
git add .
git commit -m "chore: release v$VERSION"
git tag v$VERSION -m "Release GPT OS v$VERSION"
git push origin main
git push origin v$VERSION

echo "✅ Released GPT OS v$VERSION"
