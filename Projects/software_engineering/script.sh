#!/bin/bash
# Release build script: copies selected files from source/ to build/

echo 'Welcome to the Build Script!"
echo "Preparing to create a fresh build…"

# Ensure expected directories exist
mkdir -p build
if [ ! -d "source" ]; then
  echo " Error: 'source' directory not found. Exiting."
  exit 1
fi

# 3) Read first line of changelog for version line like: ## 1.1.1
firstline=$(head -n 1 source/changelog.md 2>/dev/null)
if [ -z "$firstline" ]; then
  echo " Error: Couldn't read first line from source/changelog.md. Exiting."
  exit 1
fi

# 4) Split first line into an array
read -a splitfirstline <<< "$firstline"

# 5) Extract version (index 1 after '##')
version="${splitfirstline[1]}"

echo "You are building version: $version"
echo "Have you updated source/changelog.md with the correct release version?"
echo -n "Enter 1 to continue, 0 to exit: "

# 6) Capture user input
read versioncontinue

# 7) Continue or exit
if [ "$versioncontinue" -eq 1 ] 2>/dev/null; then
  echo "OK  Starting copy…"

  # 8–10) Copy files except secretinfo.md
  for filename in source/*; do
    echo "Found: $filename"
    if [ "$filename" = "source/secretinfo.md" ]; then
      echo "   ➜ Skipping secret file: $filename"
    else
      echo "   ➜ Copying to build/: $filename"
      cp -f "$filename" build/
    fi
  done

  # 11) Change into build and then back
  echo "Finalizing…"
  pushd build >/dev/null || { echo " Could not enter build/"; exit 1; }

  # 12) List files in build directory with version reference
  echo " Build contents for version $version:"
  ls -lah

  popd >/dev/null

  echo " Build complete!"
else
  echo "Please come back when you are ready."
fi
