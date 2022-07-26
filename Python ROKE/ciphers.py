phrase = """
M LEH MQEKMRIH XLEX WLIVPSGO LSPQIW ASYPH EX SRGI LEZI LYVVMIH MRXS XLI LSYWI ERH TPYRKIH MRXS E WXYHC SJ
XLI QCWXIVC. RSXLMRK ETTIEVIH XS FI JYVXLIV JVSQ LMW MRXIRXMSR. AMXL ER EMV SJ RSRGLEPERGI ALMGL, YRHIV XLI 
GMVGYQWXERGIW, WIIQIH XS QI XS FSVHIV YTSR EJJIGXEXMSR, LI PSYRKIH YT ERH HSAR XLI TEZIQIRX, ERH KEDIH ZEGERXPC
EX XLI KVSYRH, XLI WOC, XLI STTSWMXI LSYWIW ERH XLI PMRI SJ VEMPMRKW. LEZMRK JMRMWLIH LMW WGVYXMRC, LI TVSGIIHIH
WPSAPC HSAR XLI TEXL, SV VEXLIV HSAR XLI JVMRKI SJ KVEWW ALMGL JPEROIH XLI TEXL, OIITMRK LMW ICIW VMZIXIH YTSR XLI
KVSYRH. XAMGI LI WXSTTIH, ERH SRGI M WEA LMQ WQMPI, ERH LIEVH LMQ YXXIV ER IBGPEQEXMSR SJ WEXMWJEGXMSR. XLIVI AIVI
QERC QEVOW SJ JSSXWXITW YTSR XLI AIX GPECIC WSMP, FYX WMRGI XLI TSPMGI LEH FIIR GSQMRK ERH KSMRK SZIV MX, M AEW
YREFPI XS WII LSA QC GSQTERMSR GSYPH LSTI XS PIEVR ERCXLMRK JVSQ MX. WXMPP M LEH LEH WYGL IBXVESVHMREVC IZMHIRGI
SJ XLI UYMGORIWW SJ LMW TIVGITXMZI JEGYPXMIW, XLEX M LEH RS HSYFX XLEX LI GSYPH WII E KVIEX HIEP ALMGL AEW
LMHHIR JVSQ QI.
"""

phrase = phrase.replace(" ", "").replace(",", "").replace(".", "").replace("\n", "")
letter_dict = {}

for letter in phrase:
    if letter in letter_dict.keys():
        letter_dict[letter] += 1
    else:
        letter_dict[letter] = 1

print(letter_dict)

for key in sorted(letter_dict.keys()):
    print(f"{key} appears {letter_dict[key]} times")
