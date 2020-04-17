build:
	pandoc -s -f markdown -H header.html cv.md --metadata pagetitle=CV -o cv.html
	cat cv.md | \
		sed 's/<\/*details>//g; s/<\/*summary>//g; s/<h2>/## /g; s/<\/h2>//g; s/<h3>/## /g; s/<\/h3>//g' | \
		pandoc -s -f markdown --metadata pagetitle=CV --metadata linkcolor=blue --metadata geometry:margin=1in -o cv.pdf
