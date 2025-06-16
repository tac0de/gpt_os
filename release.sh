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

# 📜 Get all commit messages since last tag
LAST_TAG=$(git describe --tags --abbrev=0 2>/dev/null)
if [ -z "$LAST_TAG" ]; then
  COMMIT_LOG=$(git log --pretty=format:"- %s")
else
  COMMIT_LOG=$(git log --pretty=format:"- %s" "$LAST_TAG"..HEAD)
fi

if [ -z "$COMMIT_LOG" ]; then
  COMMIT_LOG="- No significant changes"
fi

# CHANGELOG update
if [ "$DRY_RUN" = false ]; then
  echo "📝 Updating CHANGELOG.md"

  # delete existing section for this version
  sed -i '' "/## \[v$VERSION\]/,/^## /d" CHANGELOG.md

  printf "\n## [v%s] - %s\n### Changes\n%s\n\n" "$VERSION" "$(date +%Y-%m-%d)" "$COMMIT_LOG" >> CHANGELOG.md
else
  echo "🧪 Dry run complete. No changes made."
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
