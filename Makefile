build:
	pandoc -s -f markdown -H header.html cv.md --metadata pagetitle=CV -o cv.html
	pandoc -s -f markdown cv.md --metadata pagetitle=CV --metadata linkcolor=blue -o cv.pdf
