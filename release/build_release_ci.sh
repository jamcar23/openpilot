#!/bin/bash -e

# TARGET_DIR="$1"
# BRANCH="$2"

mkdir "$TARGET_DIR"

cp -pR --parents $(cat release/files_common) "$TARGET_DIR"

cd "$TARGET_DIR"

mkdir -p panda/board/obj
touch panda/board/obj/.placeholder

echo "!board/obj/.placeholder" >> panda/.gitignore

VERSION="$(python ../tools/scripts/gen_changelog.py --export)"
echo "#define COMMA_VERSION \"$VERSION\"" > selfdrive/common/version.h

git init
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git remote add origin https://github.com/jamcar23/openpilot.git
git checkout --orphan "$BRANCH"
git add -A

cp ../.pre-commit-config.yaml .pre-commit-config.yaml
pre-commit run --all

git commit -am "release: $VERSION"
