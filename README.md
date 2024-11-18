# CV

This is a Markdown version of my CV. I got tired of updating a Google Docs / Word document. Any change triggers deployment into https://aleksic.dev website without any red tape.

What it does:

1. uses `pandoc` to generate HTML and PDF
1. triggers deployment to web site on commit via GH workflow

## Mac

To build PDF you need: 

```
brew install pandoc
brew cask install basictex
```

## Linux

Look at the file `.github/workflows/main.yml` to see what are preconditions on an Ubuntu box
