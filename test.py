import webbrowser
#import mechanize

start = raw_input("What timeframe do you want to start with? (Military Time MM/DD/YY HH::MM:SS) ")
type(start)
finish = raw_input("What timeframe do you want to finish with? (Military Time MM/DD/YY HH::MM:SS) ")

webbrowser.open('http://itsm.gm.com')
print("Looking for tickets in between " + start + " & " + finish)
#with urllib.request.urlopen('http://itsm.gm.com') as response:
    #html - response.read()


