build:
	pandoc -s -f markdown -c mini-default.min.css cv.md --metadata pagetitle=CV -o cv.html
