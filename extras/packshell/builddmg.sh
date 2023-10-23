#!/bin/sh
# Create a folder (named dmg) to prepare our DMG in (if it doesn't already exist).
mkdir -p dist/dmg
# Empty the dmg folder.
rm -r dist/dmg/*
# Copy the app bundle to the dmg folder.
cp -r "dist/markup.app" dist/dmg
# If the DMG already exists, delete it.
test -f "dist/markup.dmg" && rm "dist/markup.dmg"
create-dmg \
  --volname "markup" \
  --window-pos 200 120 \
  --icon "markup.app" 175 120 \
  --hide-extension "markup.app" \
  --app-drop-link 425 120 \
  "dist/markup.dmg" \
  "dist/dmg/"
