.nr PI 0n
.nr PS 12.2p
.nr VS 2.8n
.nr PD 0.5v
.nr HM 4v
.defcolor blue rgb #000080

.ds header Rasmus Winther\t13. Maj
.LH
.ta T 5.4i
\*[header]

.TL
OfficeHub programmerings test

\l'25'
.SH
Generelle setup
.PP
Programmet er skrevet i Python, jeg har skrevet det med så få ekstra moduler som muligt så du ikke behøver at installere alt muligt. Det eneste kan dog være regex modulet jeg har  brugt. Når scriptet er blivet kørt bliver outputtet lagt i en af de tilhørende folders. Der ligger også en fil med testene til den funktion, hvor flere kan blive sat ind.
.SH
How to run
.PP
For at køre scripet skal kommandoen køres:

.B
.ce
python3 functions.py

.SH
Særlige overvejelser
.PP
Generelt kunne simple mynstre findes rimelig let med regex og resultatet hentes. Den eneste undtagelse var den sidste funktion om kontakt infomation, da navner kan have uendelig mange forskellige kombinationer og i eksemplerne også har et stort overlap med titel. Det kunne løses bedre ved brug af NLP funktioner i NLTK biblioteket. Det kunne fx. være en Named entity recognition model.
.PP
- Rasmus winther
