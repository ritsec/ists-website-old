#!/bin/bash

if [ -z "$1" ]
then
  echo "Please provide a commit message"
  exit 1
fi

yarn build
git add build && git commit -m $1
git subtree push --prefix build origin gh-pages