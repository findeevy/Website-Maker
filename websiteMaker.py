import webbrowser
#Import webbrowser library so we can open user's website.
print("Welcome to the Website Maker by Fin Deevy")

#Set the stage of the program to 0.
i = 0

#Create empty website.
websiteFile=""

if(input("Do you want to create a website (y/n):")=="y"):
    i = 1

#Loop through stages 1-4, which will allow user to set the contents, file and website name, and styling.  
while i>0:
    
    if(i==1):
        #Set title of website.
        websiteFile = websiteFile+"<html>\n<title>"+str(input("Title of Website:"))+"</title>"
        i=2
        
    if(i==2):
        #Set contents of website.
        j=str(input("What do you want to add to your website?\n1) Header\n2) Text\n3) Link\n4) Image\n5) Line Break\n6) Go To Style\n"))
        if(j=="1"):
            websiteFile = websiteFile+"\n<h1>"+str(input("Header:"))+"</h1>"
        elif(j=="2"):
            websiteFile = websiteFile+"\n<p>"+str(input("Text:"))+"</p>"
        elif(j=="3"):
            websiteFile = websiteFile+"\n<a href='"+str(input("Link Location:"))+"' target='_blank'>"+str(input("Link Text:"))+"</a>"
        elif(j=="4"):
            websiteFile = websiteFile+"\n<img src='"+str(input("Image File Location:"))+"'>"
        elif(j=="5"):
            websiteFile = websiteFile+"\n<br>"
        elif(j=="6"):
            i=3
        else:
            print("Not valid.")
            break
            
    elif(i==3):
        #Set style (color and alignment) of website.
        j=str(input("What do you want to style about your website?\n1) Color\n2) Alignment\n3) Go To File Name\n"))
        websiteFile = websiteFile+"<style>"
        if(j=="1"):
            websiteFile = websiteFile+"\nbody {background-color:"+str(input("Background Color:"))+";}"
            websiteFile = websiteFile+"\nh1 {color:"+str(input("Header Color:"))+";}"
            websiteFile = websiteFile+"\np {color:"+str(input("Text Color:"))+";}"
            websiteFile = websiteFile+"\na {color:"+str(input("Link Color:"))+";}"
        elif(j=="2"):
            if(input("Do you want to center align your website (y/n):")=="y"):
                websiteFile = websiteFile+"\nbody { width: 800px; margin: 0 auto; }"
        elif(j=="3"):
            websiteFile = websiteFile+"</style>"
            i=4
        else:
            print("Not valid.")
            break
            
    elif(i==4):
        #Set file name of website.
        websiteFile = websiteFile+"</body>\n</html>"
        name=str(input("Name of Website File:"))+".html"
        f = open(name, "w")
        f.write(websiteFile)
        f.close()
        print("Your website is complete!")
        #Use the webbrowser library to show user their site.
        if(input("Do you want to open your website (y/n):")=="y"):
            webbrowser.open(name)    
        #End program.
        print("Thank you!")
        break
