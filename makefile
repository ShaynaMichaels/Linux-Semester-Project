all: scatterPlot.pdf

Anames_Obama: Ambass.py
	python3 Ambass.py

Anames_Bush2: Ambass.py
	python3 Ambass.py

Anames_Clinton: Ambass.py
	python3 Ambass.py

Anames_Bush: Ambass.py
	python3 Ambass.py

Anames_Reagan: Ambass.py
	python3 Ambass.py


matches_Obama: FECanalysis.py Anames_Obama Anames_Bush2 Anames_Clinton Anames_Bush Anames_Reagan indiv00.zip.txt indiv02.zip.txt indiv04.gz indiv06.gz indiv08.gz indiv10.gz indiv12.gz indiv14.gz indiv16.gz indiv22.zip.txt indiv80.zip.txt indiv82.zip.txt indiv84.zip.txt indiv86.zip.txt indiv88.zip.txt indiv90.zip.txt indiv92.zip.txt indiv94.zip.txt indiv96.zip.txt indiv98.zip.txt
	python3 FECanalysis.py
matches_Bush2: FECanalysis.py Anames_Obama Anames_Bush2 Anames_Clinton Anames_Bush Anames_Reagan indiv00.zip.txt indiv02.zip.txt indiv04.gz indiv06.gz indiv08.gz indiv10.gz indiv12.gz indiv14.gz indiv16.gz indiv22.zip.txt indiv80.zip.txt indiv82.zip.txt indiv84.zip.txt indiv86.zip.txt indiv88.zip.txt indiv90.zip.txt indiv92.zip.txt indiv94.zip.txt indiv96.zip.txt indiv98.zip.txt
	python3 FECanalysis.py
matches_Clinton: FECanalysis.py Anames_Obama Anames_Bush2 Anames_Clinton Anames_Bush Anames_Reagan indiv00.zip.txt indiv02.zip.txt indiv04.gz indiv06.gz indiv08.gz indiv10.gz indiv12.gz indiv14.gz indiv16.gz indiv22.zip.txt indiv80.zip.txt indiv82.zip.txt indiv84.zip.txt indiv86.zip.txt indiv88.zip.txt indiv90.zip.txt indiv92.zip.txt indiv94.zip.txt indiv96.zip.txt indiv98.zip.txt
	python3 FECanalysis.py
matches_Bush: FECanalysis.py Anames_Obama Anames_Bush2 Anames_Clinton Anames_Bush Anames_Reagan indiv00.zip.txt indiv02.zip.txt indiv04.gz indiv06.gz indiv08.gz indiv10.gz indiv12.gz indiv14.gz indiv16.gz indiv22.zip.txt indiv80.zip.txt indiv82.zip.txt indiv84.zip.txt indiv86.zip.txt indiv88.zip.txt indiv90.zip.txt indiv92.zip.txt indiv94.zip.txt indiv96.zip.txt indiv98.zip.txt
	python3 FECanalysis.py
matches_Reagan: FECanalysis.py Anames_Obama Anames_Bush2 Anames_Clinton Anames_Bush Anames_Reagan indiv00.zip.txt indiv02.zip.txt indiv04.gz indiv06.gz indiv08.gz indiv10.gz indiv12.gz indiv14.gz indiv16.gz indiv22.zip.txt indiv80.zip.txt indiv82.zip.txt indiv84.zip.txt indiv86.zip.txt indiv88.zip.txt indiv90.zip.txt indiv92.zip.txt indiv94.zip.txt indiv96.zip.txt indiv98.zip.txt
	python3 FECanalysis.py

sortedMatches_Obama: sortMatches.awk matches_Obama
	gawk -f sortMatches.awk
sortedMatches_Bush2: sortMatches.awk matches_Bush2
	gawk -f sortMatches.awk
sortedMatches_Clinton: sortMatches.awk matches_Clinton
	gawk -f sortMatches.awk
sortedMatches_Bush: sortMatches.awk matches_Bush
	gawk -f sortMatches.awk
sortedMatches_Reagan: sortMatches.awk matches_Reagan
	gawk -f sortMatches.awk

finalFile: converter.py sortedMatches_Obama sortedMatches_Clinton sortedMatches_Bush sortedMatches_Bush2 sortedMatches_Reagan cm00.zip.txt cm02.zip.txt cm04.zip.txt cm06.zip.txt cm08.zip.txt cm10.zip.txt cm12.zip.txt cm14.zip.txt cm22.zip.txt cm80.zip.txt cm82.zip.txt cm84.zip.txt cm86.zip.txt cm88.zip.txt cm90.zip.txt cm92.zip.txt cm94.zip.txt cm96.zip.txt cm98.zip.txt new_cn00.zip.txt new_cn02.zip.txt new_cn04.zip.txt new_cn06.zip.txt new_cn08.zip.txt new_cn10.zip.txt new_cn12.zip.txt new_cn14.zip.txt new_cn16.zip.txt new_cn22.zip.txt new_cn80.zip.txt new_cn82.zip.txt new_cn84.zip.txt new_cn86.zip.txt new_cn88.zip.txt new_cn90.zip.txt new_cn92.zip.txt new_cn94.zip.txt new_cn96.zip.txt new_cn98.zip.txt
	python3 converter.py

scatterPlot.pdf: plotter.py finalFile
	python3 plotter.py
