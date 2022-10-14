# Manual and Automated Testing 

This section comprises of Automated and Manual tests conducted towards the end of development of the website.

---

## Automated Tests



---
## Manual Tests 

 ### Registration Form Submission (Register Page)

| Test | Method | Expected Outcome | Result |
| - | - | - | - |
| Registration Form | Try to submit empty form | Form doesn't submit, and points to first field not filled in | Pass |
| Registration Form | Try to submit a form where a username already exists | Username is taken message will appear and reload register page | Pass |
| Remember me check box | Click on check box more than once | Blue tick shows when it is selected | Pass |
| Remember me check box | Remember me check box selected, close site and revisit | User is kept signed in on return | Pass |
| Email input | Try to enter an invalid email address or random numbers, words etc. | Email invalid message appears | Pass |
| Forget Password Link | Click on link | User is redirected to Reset Password page | Pass |
| Login link | Click on link | User is redirected to Login Page | Pass |
| Registration Form | Create a new user | Success message displays as user is redirected to Login Page | Pass |

&nbsp;


### Login Form Submission

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Login Form | Submit empty form | Form doesn't submit, and points to first field not filled in | Pass |
| Login Form | Enter invalid Username | Return to login page with User not found message | Pass |
| Login Form | Enter User login credentials | Redirect to Home Page, logged in | Pass |
| Remember me check box | Click on check box more than once | Blue tick shows when it is selected | Pass |
| Remember me check box | Remember me check box selected, close site and revisit | User is kept signed in on return | Pass |
| Forget Password Link | Click on link | User is redirected to Reset Password page | Pass |
| Login link | Click on link | User is redirected to Login Page | Pass |

&nbsp;
### Password Reset Form Submission

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Form Submit | Test with false username | Return to Reset page with No user found message | Pass |
| Form Submit | Submit form with Username on file | Redirects with message stating an email has been sent  |   |
| Login link | Click on link | User is redirected to Login Page | Pass |
| Register link | Click on link | User is redirected to Register Page | Pass |

&nbsp;
### Contact Form Submission

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Form Submit | Attempt to submit empty form | Doesn't submit, points to first field not filled in | Pass |
| Form Submit | Attempt to submit with some but not all fields filled in | Specific fields not filled in inform the user that they are required | Pass |
| Form Submit | Submit a complete contact form | Form is sent and shows success message | Pass |
| Email input | Try to enter an invalid email address or random numbers, words etc. | Email invalid message appears | Pass |

&nbsp;
### Comment Form Submission

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |

&nbsp;
---
## Updating 

### Update Profile

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |

&nbsp;
### Update Comment

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
| Content | Content | Content | Content |


&nbsp;
---
## Deleting 

### Deleting Comment

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Delete Comment | Try to delete comment when not signed in | Not possible as only delete button available when Logged in | Pass |
| Delete Comment | Try to delete another user's comment | Not possible to delete another user's comment | Pass |
| Delete Comment | Delete your own comment | User Comment is removed | Pass |
| Comment counter (Delete) | Delete comment and view counter | Counter should subtract each time a comment is deleted | Pass |

&nbsp;
---
## Posts and Post-Details

### Post-List

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Add Post | Content | Content | Content |
| Delete Post | Content | Content | Content |
| Edit Post | Content | Content | Content |
| Draft Post | Content | Content | Content |
| Post Shows when set to "Published" | Content | Content | Content |
| Post hidden when set to "Draft" | Content | Content | Content |

&nbsp;
### Pagination

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Pagination | Create 7 Blog Posts (Pagination number set to 6) | When number of Posts exceeds 6, pagination will occur | Pass |
| Left-Right Buttons | Click Left and Right Buttons on Paginator | Left button will move back one page, where as right button will move forward one page | Pass |
| Page Number Buttons | Click Page number buttons | Shows specific page number matching the number in the paginator | Pass |

&nbsp;
### Post-Detail

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Content | Content | Content | Content |
| Content | Content | Content | Content |
&nbsp;

## Social Media Page and Footer Links:

### Social Media Page

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Facebook Link/Icon | Click Link/Icon | Opens my Facebook Page in a new tab | Pass |
| Instagram Link/Icon | Click Link/Icon | Opens my Instagram Page in a new tab  | Pass |
| Github Link/Icon | Click Link/Icon | Opens my Github Page in a new tab  | Pass |
| Linkedin Link/Icon | Click Link/Icon | Opens my Linkedin Page in a new tab  | Pass |

&nbsp;

### Footer Icons

| Test | Method | Expected Outcome | Result |
| ---- | ------ | ---------------- | ------ |
| Facebook Link/Icon | Click Link/Icon | Opens my Facebook Page in a new tab  | Pass |
| Instagram Link/Icon | Click Link/Icon | Opens my Instagram Page in a new tab  | Pass |
| Github Link/Icon | Click Link/Icon | Opens my Github Page in a new tab  | Pass |
| Linkedin Link/Icon | Click Link/Icon | Opens my Linkedin Page in a new tab  | Pass |

&nbsp;

---
## HTML Validation:
- 
- 

---
## CSS Validation:
- 
- 

---
## JS Validation:
- 
- 

---
## Python Validation:
- 
- 

---
## Lighthouse Performance Testing:
- 
- 


---
### Return to README: 

[README.md](README.md)

