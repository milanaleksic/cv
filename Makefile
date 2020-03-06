build:
	pandoc -s -f markdown -H header.html cv.md --metadata pagetitle=CV -o cv.html
