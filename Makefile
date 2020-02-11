build:
	pandoc -s -f markdown -H mini-default.min.css cv.md --metadata pagetitle=CV -o cv.html
