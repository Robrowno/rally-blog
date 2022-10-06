# Rally Blog

The Rally Blog Website is a blog page about my rallying journey starting out as a driver and co-driver in the UK.

This is my first full-stack project, which contains blog posts about different Rally events I attend as a driver, co-driver or supporter. 

The aims of this website are:

1. To document my journey for readers
2. To inspire more people to take an interest in rallying and motorsport
3. To give readers different social media platforms to follow me on
4. To give readers to ability to use a contact form to contact me directly with queires 

As a full stack project, my personal aims out of this are to test my abilities in implementing Django in my fourth portfolio project for Code Institute, and to create a site which I will be eager to maintain and continue posting content on in future.

The website is deployed through Heroku, and the live link can be found here: ##################### 


---
## Website across different platforms






---

## Table of Contents
1. [Wireframes](#wireframes)
2. [User-Stories and Epics](#)
3. [UX Description](#ux-description)
4. [Technologies used](#technologies-used)
5. [Features](#features)
6. [Features to implement](#other-features-to-implement)
7. [Testing and Validation](#testing-and-validation)
8. [Bugs and Issues](#bugs-and-issues)
9. [Peer Reviews](#peer-reviews)
10. [Deployment](#deployment)
11. [Credits](#credits)

# Wireframes

I used Balsamiq to construct my wireframes, as it's a trustworthy way of mapping out my project ideas, which I have used on all of my prior projects as well.

## Home Page

![Home Page Wireframe](./static/images/readme-images/wireframe-home.png)

## Open Post

![Open Post Wireframe](./static/images/readme-images/wireframe-open-post.png)

## Different Devices

![Different Devices Wireframe](./static/images/readme-images/wireframe-devices.png)

## Create Account

![Account Registration Page](./static/images/readme-images/wireframe-create-account.png)

## Login

NOTE: During the designing of the Login page functionality, I decided to change to using the Username instead of the 
email address for Logging in to the website.
![Log in Page](./static/images/readme-images/wireframe-login.png)

## User Profile Page

![Profile Page](./static/images/readme-images/wireframe-profile-info.png)

## Edit Profile Page 

NOTE: Changed to having seperate inputs for First Name and Last Name.

![Edit Profile](./static/images/readme-images/wireframe-profile-edit.png)

## Forgot Password

NOTE: Title changed to reset and username is used to recover the password rather than the email address 
as originally planned here.

![Forgot Password Page](./static/images/readme-images/wireframe-forgot-password.png)

## Follow Me 

NOTE: Original Plan was to have large icons as links, seperated by a dividing cross, ended up going with Cards as I was happy with 
how the cards looked in the Index.html page and wanted to replicate something similar using Cards.
![Follow Me on Socials page](./static/images/readme-images/wireframe-followme.png)

## Contact Page

![Contact Page](./static/images/readme-images/wireframe-contact.png)

---

## Early Renderings

After creating my wireframes and getting my work environment set up to point where I was happy to start routing up urls, I decided to trial my templates/views to make sure I was happy with how my wireframes would look in practice.

Here is an example of my rendered home page early on in development:

![Early Development Home Page](./static/images/readme-images/wireframe-preview-render.png)

Here is an early example of my Follow-Me page, which I imagined as a 4 box grid with social media icons inside that, when clicked, direct you to my associated social media pages:

![Early Development Follow Me Page](./static/images/readme-images/followme-page-rendering.png)

Here is the very early stages of the Profile and Edit Profile pages - This is before any real fucntionality was in place for visiting different pages through the links or being able to retreive from or send data to the database: 

![Early Development Profile Page](./static/images/readme-images/early-profile-page-rendering.png)

![Early Development Edit Profile Page](./static/images/readme-images/early-edit-profile-rendering.png)


---

# User Stories and Epics

## User Stories:

- 
- 
- 
- 
- 
- 
- 
- 
- 

## Epics:

- 
- 
- 
- 
- 
- 




# Technologies Used

Technologies and Frameworks used to make this website include the following:

- HTML5 - a markup language used to structure the content on the site.
- CSS3 - a cascading stylesheet language used to style the site where needed (beyond Bootstrap's classes).
- Javascript - (Vanilla and JQuery) - a dynamic scripting language, used for applying logic, animating or updating content.
- Python v3.8 - an object oriented, high level programming language, on which the Django framework is based on.
- Django v3.2 Framework - a high level Python web framework, used for rapidly creating dynamic websites.
- Bootstrap v5.0 - a css framework used for rapidly creating/styling mobile-first websites.
- Git - a DevOps tool used for version control - used to add, commit and push my changes to the server.
- Balsamiq - a free wireframe service, where ideas can be visually interpreted for planning a project.
- Heroku - is a PaaS Cloud platform, used to host applications entirely in the cloud.
- Cloudinary - a free SaaS Cloud platform, used to store images/media
- Github - a cloud based service used for hosting repositories.
- Gitpod IDE - an open-source developer tool for remote development. Used for version control.
- Summernote - a free service for styling textareas in Django projects
- VSCode IDE - a code editor by Microsoft, used for local development. Used this for testing complicated features, such as the authentication module I used in this project.
- Google Chrome Browser - Used as my default browser for learning, working on github/gitpod and more.
- PostgreSQL - an open source and object-relational database system, used as my database of choice on Heroku.
- SendGrid API - a RESTful Application Programming Interface, used for sending emails and password resetting functionality.



---

# Features

My Rally Blog website consists of many features, that allow the user to interact with my site in differnt ways.

1. A Nav bar that contains links to:
    - A link that returns the user to the home page
    - A register/login page (This changes to Logout if the User is signed in)
    - A social media links page
    - A contact page with a form to fill out to get in touch
    - If the user has an account, they will also have access to a Profile page in the nav
    - Superusers/Admins will have a Manage link, which is exclusive to Superusers/Admins


2. A footer that contains font awesome icons with links to:
    - Facebook
    - Instagram
    - LinkedIn
    - Github

3. A Home Page that displays Blog post content which can be individually clicked on to open posts. When opened they display unique content to that specific blog post/article.

4. A Login Page, where users can log into their account. It also gives options to create an account if you don't have one or if you forget your password you can follow a link to reset it.

5. A Register Page, where users can create an account.

6. A Reset-Password Page, where users can reset their password. Also gives you options to go back to the Login or Registration pages.

7. A Follow Me page, with cards displaying social media links for the site user to visit and follow me on different social media platforms.

8. A Contact form page, where the site user can fill out a form to get in touch with a particular query they have in mind. The form asks for a name & surname, email, query-type and displays a text area to type out your message.

9. A User Profile Page, where Users can view stats about their likes and comments, or their info such as name and username on file.

10. An Edit Profile Page, where users can alter their Name, Username, Email. 

11. Being a Django site, there is also an admin page just for the site Admin/Author, where the admin can edit, create, delete and draft/publish content. The Admin page allows me to see more than just the content, I can view comments, user registration and contact forms sent to me from the admin panel.



# Features to implement

- 
- 
- 
- 
- 


# Testing and Validation

- Manual Testing:

- Automated Testing:


# Bugs and Issues

- I had an issue/bug where Posts were not displaying on the home page and the debug page that rendered was giving me mixed messages about there the issue was stemming from. After trying to clear the database using `python3 manage.py flush`, and being puzzled by the issue and tryign to find issues in my code for days, I decided to delete my database and and create a new one. I simply then added the new database url to my env.py file and mademigrations and migrated and it worked perfectly again. 

- There were one or two other occasions where it became necessary to delete my database to avoid bugs/issues during development. 

- I had an issue/bug where when developing the functionality of posting a form to the database through the contact page, option 3 (Other) in the select tag dropdown was throwing an error, whereas the other two options were posting to my database just fine. I asked about this on Slack and it was suggested to me by Dave Horrocks and Daisy McGirr that I should try using a CharField instead of a BooleanField, as this was likely causing the issue (as it's looking for values of just 0:False and 1:True) - I deleted any old records in my admin page and went about adjusting the Contact model in question and it worked as expected after making this change.

- At one point I was unable to get my Post content and title to render on the post detail page, I found this was due to me trying Post.title and post_view.title instead of post.title, as I had defined it in my context as "post": post_view.

- Styling the post detail page was another challenge, and one I found that actually had a very simple fix that I will always be checking for in future. In using bootstrap, and including many divs in my html structure, I often left out on or two closing div tags along the way, which would lead to unintended styling mistakes. This was particularly an issue with my comments section, where there was added complexity of the comments section being more dynamic. I was fixing the comments section styling when there were no comments, only to find that when a comment was made, the styling would go wrong again. And vice versa. When I went and double checked if there were any closing div tags missing after trying for ages and formatting the document, I noticed div tags missing.

- I struggled to get the edit profile functionlity working to begin with, as I kept getting integrity errors where the logic I had written was causing conflicts as I realised that it was attempting to create users that already existed after the user had been called, instead of updating the user's information. The mistake came from asigning user to User(), and I found out through playing around with the code, that I should have been assigning user = request.user. This was the root cause of the integrity error due to trying to accidentally create an existing user, rather than update it.

- I noticed an issue with how I originally did my comments in the post-detail template. I realised that in theory, you could keep adding comments and the page would keep scrolling down for an indefinite length in theory. Whilst I don't anticipate that large a quantity of comments, this would be a poor user experience in principle to have to scroll down a long way to read the comments. 
I decided to paginate the comments section to keep the comments section shorter. This prevents unesessary scrolling and keeps pages at a predictable height.



# Peer Reviews 

- Peer Reviews from the C.I Slack Community:

- Thoughts on the project from my mentor:

- Peer Reviews from the C.I London Community:


# Deployment

## Version Control:

- Version control was done through the Gitpod CLI, using the following key commands to push updated code to Github:
    - `git add ,` - to add all new files or file changes in preparation to commit in next step.
    - `git commit -m ""` - add your commit message inbetween the two quoatation marks, this explains the changes of your lastest version.
    - `git push` - this is the command that pushed your code up to your github repository.


## Forking a Github Repository:

- Instructions for forking a respositoty:
    - To fork a chosen repository, look towards the top right of the page, between the watch/unwatch tab and the star tab, and select the "Fork" tab.
    - By default, forks are named the same as the parent repository, however, you can change this as you see fit. You are also able to add an optional description.
    - Choose which branch you want to copy if you need to. Only the default branch is copied by default setting.
    - Click the green "Create Fork" button, and you will now have a forked repository to use.

## Locally Cloning a Github Repository:

- Instructions for cloning a repository:
    - To clone a repository, first you will need to select your chosen repository and look for the green "Code" button (located next to the "Go to file" and "Add file" buttons).
    - Next, copy the URL for the repository. By default this is a HTTPS link, however, you can copy an SSH key or by using the Github CLI.
    - After you have the URL, you are going to want to go to the terminal of your machine and cd (change directory) to the folder where you want to save your working directory to be.
    - In the terminal, type `git clone` followed by the url link you copied earlier.
    - Press enter and hopfully you will have successfully cloned the repository locally.
    - You will also need to make sure you have installed all the required packaged of the project. To do this, paste this code in to the terminal once your workspace is set up: `pip install -r requirements.txt`
    - You will also need to make an env.py file to run the project. Populate it with the required information, though make sure you include this file in the .gitignore file. The contents of the env.py file should NOT be made public.


### Github docs:
- For further reading, I would highly suggest the Github Docs: [Github Docs Link](https://docs.github.com/en/get-started/quickstart/fork-a-repo)

## Deployment through Heroku:

- Make sure you have a Heroku account before beginning with these steps.
- You should also have a Cloudinary account and means to send emails through an API such as SendGrid to use in production.

- Once logged in to Heroku, navigate to the personal dashboard and look for the 'New' dropdown button at top right hand corner of the page.
- In the drop down, select "Create new app - you will be taken to a page where you will be able to name the app and select a region. Once you have filled this information in, click the "Create app" button. Your app is now created.
- Access your Resources tab in your app's page, and go to setup your database in the add-ons. You will do this by searching for "Heroku Postgres" and Hobby Dev in the search bar and clicking add. 
- Next, you should navigate to the Settings tab to set up the config vars. Scroll down slightly to the button that reads "Reveal Config Vars" and click it to open it. We are going to need to add/remove the following information: 
    - DATABASE_URL: this should have been automatically generated by Heroku for you, but make sure it is populated already. Click add.
    - CLOUDINARY_URL: access this url from your cloudinary account and paste it in here. Click add.
    - SECRET_KEY: This should be a secret password, do not publish this anywhere. Click add.
    - PORT: add the number 8000 to this and click add.
    - ALLOWED_HOSTS: Optional to add here or in the settings.py of your project. Basically the name of your project with `.herokuapp.com` appended to it: example-app.herokuapp.com.
     - DISABLE_COLLECTSTATIC: Should have been set to 1 during development. You will REMOVE this for full deployment. Click the 'x' to remove it.

- After this, head to the Deploy tab and scroll down to the Deployment Method section and select "Github"
- Next, in the "App connected to GitHub" section, look up your account and repo to pair it to the heroku app (click connect).
- Head to the bottom of the page where you will see a section called "Manual Deploy". Select the 'main' branch in the drop down and click the 'Deploy Branch' button.
- Wait for the deployment to complete, and when prompted, click the "View/Open App" button to see the launched site.



# Credits

- Code Institute's Django Cheatsheet was used to help me get my workspace set up, including installing Django and how to create your project and app in the terminal: [C.I Django cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit)

- Similarly, the idea for a Rally Blog was inspired by a walkthrough called "I think, therefore I blog" by Code Insitute.

- I consolidated and learned much of how to use Python/Django with the Udemy course here, as a significant supplement to the C.I course: [Udemy Django course](https://www.udemy.com/course/django-and-python-full-stack-developer-masterclass/)

- There have been several sites that I have continuously returned to for help learning about or how to implement new concepts in Django. And whislt I will include specifics from sites below regarding exact pages I have learned from, I will detail the home pages of key sites here:
    - [W3Schools for Django](https://www.w3schools.com/django/index.php) 
    - [W3Schools for Bootstrap 5](https://www.w3schools.com/bootstrap5/index.php)
    - [GeeksforGeeks](https://www.geeksforgeeks.org/)
    - [Django Central](https://djangocentral.com/building-a-blog-application-with-django/)
    - [Bootstrap 5 Documentation](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
    - [Django 3.2 Documentation](https://docs.djangoproject.com/en/3.2/)
    - [MDN Web Docs (Mozilla)](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)


- I used Bootstrap's fantastic documentation to help me to create the main sections of my home page, and features on other pages such as the contact form:
    - [Bootstrap Navbars](https://getbootstrap.com/docs/4.1/components/navbar/)
    - [Bootstrap Forms](https://getbootstrap.com/docs/5.0/forms/validation/)
    - [Bootstrap Select](https://getbootstrap.com/docs/5.0/forms/select/)
    - [Bootstrap Cards](https://getbootstrap.com/docs/5.0/components/card/)

-  I learned about field validations for my app models from Geeksforgeeks: [geeksforgeeks](https://www.geeksforgeeks.org/default-django-built-in-field-validation/)

- All images are sourced from me or given to me with full permission to use. All the blog content is written by myself. 

- All icons used came from Font Awesome: [Fontawesome](https://fontawesome.com/)

- Favicons used were sourced from favicon.io: [Racing car Favicons](https://favicon.io/emoji-favicons/racing-car)

- I got inspiration for my follow-me page based on this code example from Bootsnipp: [Bootsnipp](https://bootsnipp.com/snippets/or33d)

- This superb page helped me to clear my migrations during development when I made too many migrations: [simpleisbetterthancomplex](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)

- Some great tutorials/sources used for inspiration for my contact form/page:
    - [A designer who codes](https://www.youtube.com/watch?v=aeNDvQi6O94)
    - [djangotutorials](https://www.youtube.com/watch?v=-qAf_Qx6Ygg)
    - [learningaboutelectronics](http://www.learningaboutelectronics.com/Articles/How-to-insert-data-into-a-database-from-an-HTML-form-in-Django.php)

- Colour codes:
    - Instagram purple: [Instagram colour](https://www.designpieces.com/palette/instagram-new-logo-2016-color-palette/)
    - Facebook: [Facebook colour](https://usbrandcolors.com/facebook-colors/)
    - Linkedin: [Linkedin colour](https://encycolorpedia.com/0e76a8#:~:text=The%20hexadecimal%20color%20code%20%230e76a8,%25%20green%20and%2065.88%25%20blue.)
    - Github: [Github colour](https://encycolorpedia.com/171515)

- Instructions on how to install Django Extensions: 
    - [Installation](https://django-extensions.readthedocs.io/en/latest/installation_instructions.html)
    - [Using AutoSlugField](https://django-extensions.readthedocs.io/en/latest/field_extensions.html)

- This site helped me to fix the footer to the bottom of the page no matter the height of the content in the block content: [radu](https://radu.link/make-footer-stay-bottom-page-bootstrap/)

- This site helped inspire my post detail view [Djangocentral](https://djangocentral.com/building-a-blog-application-with-django/)

- The Logic and Code for the Pagination in the index.html template came from this website: [Python in Plain English](https://python.plainenglish.io/how-to-implement-pagination-in-django-with-function-based-views-8f6462554930)

- This video by Codemy also helped me to understand how to implement pagination: [Codemy Pagination Youtube](https://www.youtube.com/watch?v=N-PB-HMFmdo&list=PLCC34OHNcOtqW9BJmgQPPzUpJ8hl49AGy&index=19)

- Django docs were reviewed for pagination requirements in the views.py file: [Django Pagination Docs](https://docs.djangoproject.com/en/4.1/topics/pagination/)

- Left and Right HTML arrows for Paginator: [Left Arrow](https://www.toptal.com/designers/htmlarrows/arrows/left-arrow/), [Right Arrow](https://www.toptal.com/designers/htmlarrows/arrows/right-arrow/)

- This youtube video helped guide me and give inspiration for the comments section: [Great Adib Youtuve vid](https://www.youtube.com/watch?v=MmLRE2fCcec)

- This youtube video showed me how to create a comments counter: [Selmi Tech](https://www.youtube.com/watch?v=QWNxscgCGfw)

- This is where I found the User model objects I needed for my Profile sections: [Django User model Docs](https://docs.djangoproject.com/en/4.1/ref/contrib/auth/#django.contrib.auth.models.User)

- All Images were hosted on Cloudinary: [Cloudinary](https://cloudinary.com/)

- Summernote was used to style my Post text areas in the admin page: [Summernote](https://summernote.org/)







## Personal Credits

There are a few people who have personally helped me through and guided me through this project, be it bugs and issues I was stuck on, to teaching me core concepts or explaining/running through why/how something works in Django. 

A special thanks to: 

- Daisy McGirr: My Code Institute Mentor, Daisy has guided me through Project 4 through mentor call sessions, advising me on my wireframes and scope at the start of the project, to helping me understand why code wasn't working as expected if I got stuck on a problem in 'In it together' slack group calls. Daisy has also been so kind and helpful with pep-talks when I was feeling down with issues regarding Django.

- Matt Bodden: Helped me learn how to delete a database and re-instate a new one if my database got corrupted or had conflicting issues. This has been an invaluable tool to know as I've had to delete and reinstate my database in order to make new migrations many times over the course of this project! Like Daisy, Matt has encouraged me when I felt low when struggling with Django and it has definitely got me back on my feet once or twice!

- Ian Meigh: Helped me to understand why there were url issues in my urls.py file in my rallyApp, and different ways I could go about resolving the issue. 

- Abubakar Shafique: Abubakar has been an incredible teacher of Django concepts to me. Through his lessons, I have picked up a much better confidence using the Django framework, and when I'm stuck he always sends me resources to look at that could help with a particular issue I'm stuck on.

---
## Final Thoughts:

Portfolio Project 4 proved a real challenge for me. It required me to go out and learn so much information and ask for help from friends, mentors and tutors as I really struggled with the initial learning curve of the Django frame-work. One thing I will say is that the take-away for me is that I can really see that when you start to become more profficient with Django, you can get fully functioning websites up and running very quickly compared to other means. 

On a more subjective level, seeing a website growing from the ground up to having full stack (front and back end) capabilities has been quite a satisfying experience, despite the struggles and issues. By no means do I feel that profficient with it yet, but it's safe to say I'm looking forward to using the Django frame-work again in future to see how things progress differently with the better understanding that I have now.

---

[Return to Top of Page](#rally-blog)