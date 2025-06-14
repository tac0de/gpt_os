#!/bin/bash

VERSION=$1
MODE=$2  # e.g. --dry-run or --force

if [ -z "$VERSION" ]; then
  echo "❌ Usage: ./release.sh <version> [--dry-run|--force]"
  exit 1
fi

DRY_RUN=false
FORCE=false

if [ "$MODE" == "--dry-run" ]; then
  DRY_RUN=true
elif [ "$MODE" == "--force" ]; then
  FORCE=true
fi

# 🔍 Detect uncommitted changes
if [ "$FORCE" = false ] && [[ -n $(git status --porcelain) ]]; then
  echo "❌ You have uncommitted changes. Commit or stash before releasing. Use --force to override."
  exit 1
fi

# ❌ Prevent duplicate tags
if [ "$FORCE" = false ] && git rev-parse "v$VERSION" >/dev/null 2>&1; then
  echo "❌ Tag v$VERSION already exists. Use --force to override."
  exit 1
fi

echo "📦 Releasing GPT OS v$VERSION"

# 🧠 Update setup.cfg
if [ -f setup.cfg ]; then
  echo "🔧 Updating setup.cfg to version $VERSION"
  sed -i '' "s/^version = .*/version = $VERSION/" setup.cfg
fi

# 📜 Auto-fill CHANGELOG.md using filtered git log
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null)
if [ -z "$LAST_TAG" ]; then
  COMMIT_LOG=$(git log --oneline)
else
  COMMIT_LOG=$(git log --oneline "$LAST_TAG"..HEAD)
fi

# 🧹 Filter meaningful commit messages
FILTERED_LOG=$(echo "$COMMIT_LOG" | grep -vE 'jekyll|gh-pages|workflow|LICENSE|README|generate_readme')

if [ -n "$FILTERED_LOG" ]; then
  echo "📝 Updating CHANGELOG.md"

  # Remove any pre-existing duplicate for this version
  sed -i '' "/## \[v$VERSION\]/,/^## /d" CHANGELOG.md

  CHANGELOG_ENTRY=$'\n'"## [v$VERSION] - $(date +%Y-%m-%d)"$'\n'"### Changes"$'\n'"$FILTERED_LOG"$'\n'

  echo "$CHANGELOG_ENTRY" >> CHANGELOG.md
else
  echo "⚠️ No significant changes to log for v$VERSION"
fi

# 💡 Dry run output
if [ "$DRY_RUN" = true ]; then
  echo "🧪 Dry run complete. No changes made."
  exit 0
fi

echo "📄 Updating README.md..."
python3 scripts/generate_readme.py > README.md

# ✅ Commit + Tag + Push
git add .
git commit -m "chore(release): v$VERSION"
git tag -f v$VERSION -m "Release GPT OS v$VERSION"
git push origin main
git push --force origin v$VERSION

echo "✅ Released GPT OS v$VERSION"
