#Use of find and slice funtion

xt = "X-DSPAM-Confidence:    0.8475";
lx=text.find(":")
nl=text[lx+1:]
print(float(nl))