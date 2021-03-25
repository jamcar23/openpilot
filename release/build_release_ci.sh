#!/usr/bin/env bash

# TARGET_DIR="$1"
# BRANCH="$2"

mkdir "$TARGET_DIR"

cp -pR --parents $(cat release/files_common) "$TARGET_DIR"

cd "$TARGET_DIR"

mkdir -p panda/board/obj
touch panda/board/obj/.placeholder

echo "!board/obj/.placeholder" >> panda/.gitignore

SELFDRIVE_VERSION_FILE = selfdrive/common/version.h
OP_VERSION=$(head -1 $SELFDRIVE_VERSION_FILE | cut -d '"' -f 2)
VERSION="$(date +%y.%m.%d.%H%M)"
echo "#define COMMA_VERSION \"$VERSION\"" > $SELFDRIVE_VERSION_FILE
echo "#define OPENPILOT_VERSION \"$OP_VERSION\"" >> $SELFDRIVE_VERSION_FILE

git init
git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"
git remote add origin https://github.com/jamcar23/openpilot.git
git checkout --orphan "$BRANCH"
git add -A

cp ../.pre-commit-config.yaml .pre-commit-config.yaml
pre-commit run --all

git commit -am "release: $VERSION"
