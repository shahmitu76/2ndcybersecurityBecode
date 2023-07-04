# Let's go Phishing

- Mode : Solo
- Duration : 4 days


## Challenge

- Bob has a dog (a bull terrier) named "Shimi". Bob really loves his dog. 
- Alice is a fan of Mécanique. She has two vintage cars and often likes to parade around with her ancestral objects.
- Your mission will be to obtain Alice's or Bob's password

# I Chose to take Bob's challenge

Prerequisites:
1. VSCodium- Text editor 
 

## Downloading VSCodium
1. Go to command prompt on windows
2. write this command

| winget install vscodium   |  

## Step1:
* Create a folder called web-projects. I created in c:/github/
* Now I will create:test-site folder inside web-projects
* index1.html: This file will generally contain your homepage content, that is, the text and images that people see when they first go to your site. Using your text editor, create a new file called index1.html and save it just inside your test-site folder.
* images folder: This folder will contain all the images that you use on your site. Create a folder called images, inside your test-site folder.
* styles folder: This folder will contain the CSS code used to style your content (for example, setting text and background colors). Create a folder called styles, inside your test-site folder.

## Step2:
* Writing HTML script in index1.html
* Here are the screenshots of index1.html
 ![clipboard](https://i.imgur.com/UYsqQy9.png)

![clipboard](https://i.imgur.com/WRjjx1B.png)
This will create a very basic html file if it was not for style/style.css

* Basic HTML page without image and css file which gives it a texture

![clipboard](https://i.imgur.com/C2i1zV4.png)


## Step3:
* To add texture and look to our HTML file we make styles.css file
* ![clipboard](https://i.imgur.com/rImlzF7.png)
* ![clipboard](https://i.imgur.com/KHlCtGs.png)
 Now, this file is the real designer of our html page

* Adding an image and css file to our html page:

![clipboard](https://i.imgur.com/DcNV7rM.png)
![clipboard](https://i.imgur.com/ZFSKqf1.png)


!! You see a huge difference
## Step4:
* I have added one more functionality :
 When someone clicks on the link "I am a Dog lover", it takes it to another html page called formwebhook.html. I have saved it directly in test-site folder. This will take the user to a new page asking him to fill his credentials. Once filled and clicked on the submit button, his email and password will be taken by webhook.site url as I have used 
 
 <--form action="webhook.site url" method="post">
 
 ![clipboard](https://i.imgur.com/ht3rcQa.png)
 
 
## Step5:
Now to add some texture and colour to our form page, I have added one more css file called formstyle.css in styles folder.
![clipboard](https://i.imgur.com/mbmidJe.png)
 This is how our second page looks after adding .css file to the second html page.

![clipboard](https://i.imgur.com/mAFD0ts.png)


 # And there you have a phishing page stealing the credentials of Bob!
 
 ![clipboard](https://i.imgur.com/YXX6vl9.png)


## Resources

- [MDN HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
- [MDM Form](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)
- [MDN CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS)
- [Cheatsheet Html](https://learnxinyminutes.com/docs/html/)
- [Cheatsheet CSS](https://learnxinyminutes.com/docs/css/)

## Hint
- [Webhook](https://webhook.site/)
 