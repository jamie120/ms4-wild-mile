# Testing

[back to README.md](https://github.com/jamie120/ms4-wild-mile/blob/master/README.md)

## Contents

1. [Manual Testing](#manual-testing)
    * [Home Page](#home-page)
    * [Recipes Page](#recipes-page)
    * [Recipe Page](#recipe-page)
    * [Add Recipe Page](#add-recipe-page)
    * [Edit Recipe Page](#edit-recipe-page)
    * [Site Wide](#site-wide)
2. [DevTools](#devtools)
3. [Automated Testing](#automated-testing)
    * [Code Validation](#code-validation)
    * [Browser Validation](#browser-validation)
4. [User Stories](#user-stories)
5. [User Testing](#user-testing)
    * [My Mentor](#my-mentor)
    * [User review](#user-review)
6. [Post Review Changes](#post-review-changes)

## Manual Testing

### Testing completed using the following browsers: 

* Google Chrome (Version 87.0.4280.88) using MacOS on a monitor running at 1920 x 1080.
* Safari (Version 11.1.2 (13605.3.8)) using MacOS on a monitor running at 1920 x 1080.
* Apple iPad Pro 11" -  Safari and Google Chrome - latest build at 29/01/2021.
* Apple iPhone X - Safari and Google Chrome - latest build at 29/01/2021.

### **The following checks were completed on all browsers, any issues have been captured and documented below with screenshots.**

# **Home Page**
* Verify the page loads responsively on all device sizes. - :white_check_mark:
* Verify site-entry overlay only loads on the intital page and does NOT load if refreshed in the same browser tab. :white_check_mark:
* Verify When clicked the site-overlay fades (1500ms) and the element is removed - :white_check_mark:
* Verify the 'grow' animation on the logo in the site-overlay functions as expected - :white_check_mark:
* Check all links in index.html direct users to the correct routes - :white_check_mark:

# **Nabvar**
* Verify hover effect is present on all nav links - :white_check_mark:
* Check all links in the nav element direct users to expected pages - :white_check_mark:
* Check all links in the mobile nav element direct users to the expected pages - :white_check_mark:


# **Search Bar**
* Check an existing search term to achieve render the conversions template with search query applied - :white_check_mark:

- Search term = Mary
![Search - True](documentation/testing/img/search-true.png) 

* Check a non-existent search term to render the conversions template with search query applied - :white_check_mark:

- Search term = Tree
![Search - False](documentation/testing/img/search-false.png) 

----------------------------
----------------------------
----------------------------
----------------------------
----------------------------
CONTINUE BELOW - COMPLETED UP TO THIS POINT

----------------------------
----------------------------
----------------------------
----------------------------
----------------------------

### Not logged in

![CTA - Before](documentation/testing/img/home-cta-message.png) 

### Logged in

![CTA - Logged In](documentation/testing/img/home-cta-message-logged-in.png)


### **Home Page - Fixes**

* Incorrect font style on call to action button caption, when user not logged in to the site. 

# **Recipes Page**

* Verify the page loads responsively on all device sizes. - :white_check_mark:
* Verify all fonts are applied as expected - :white_check_mark:
* Verify the message and call to action button at the bottom of the page changes, if a user is logged in - :white_check_mark:
* Verify recipe cards render to the page correctly - :white_check_mark:
* Verify recipe cards redirect users to the individual recipe pages when clicked - :white_check_mark:
* Verify the four category buttons function correctly - re-rendering the page with only recipes from the selected category - :white_check_mark:
* Verify selected category has applied CSS outline and HTML page header indicates the category with text - :white_check_mark:

![missing image - recipes page](documentation/testing/img/missing-image-recipes.png)

### Category selection - Dinner

![Category-dinner](documentation/testing/img/category-dinner.png)


### Pagination 
* Verify page pagination functions correctly. At the time of testing there are 10 recipes - with a pagination setting of 6 recipes per page - :white_check_mark:
* Verify hover effect is present on recipe cards - :white_check_mark:


### Screenshots

![Pagination - 1](documentation/testing/img/pagination-test-1.png)
![Pagination - 2](documentation/testing/img/pagination-test-2.png)

### Search function

* Verify the search function operates as expected. Tested search term (avacado)  - :white_check_mark:
* Verify 'see all recipes' button functions correctly - rerenders the page with all recipes - :white_check_mark:

![Search](documentation/testing/img/avacado-search.png)


# **Recipe Page**


### General
* Verify the page loads responsively on all device sizes. - :white_check_mark:
* Verify all fonts are applied as expected - :white_check_mark:
* Verify all recipe info is rendered from the database correctly and in full - :white_check_mark:
* Verify the message and call to action button at the bottom of the page changes, if a user is logged in - :white_check_mark:

### Image
* Verify backup image renders if recipe IMG/URL path generates an error - :white_check_mark:
    * To test - the image URL was replaced with string 'testing' on the 'No fish and chips recipe.

![missing image - recipe page](documentation/testing/img/missing-image-recipe.png)

### Buttons
* Verify 'edit recipe' button is linked to the route 'edit-recipe' for the corresponding recipe - :white_check_mark:
* Verify 'delete recipe' button is linked to the route 'delete-recipe' for the corresponding recipe, and that the corresponding recipe is removed from the database if clicked - :white_check_mark:
* Verify 'delete' button in the comments section of the page - deletes the comment it corresponds to from the database - :white_check_mark:
* Verify buttons appear as required, based on authentication - :white_check_mark:
    * User logged in - viewing a recipe they are NOT author of - 
    ![missing image - recipe page](documentation/testing/img/recipe-buttons-not-author.png)
    * User logged in - viewing a recipe they ARE the author of - 
    ![missing image - recipe page](documentation/testing/img/recipe-buttons-author.png)
    * User logged in - viewing a comment/rating they ARE the author of -
    ![missing image - recipe page](documentation/testing/img/comment-author-button.png)

### Comments & rating
* Verify comments and ratings can only be added by users logged in with authentication - :white_check_mark:
* Verify users are not able to submit blank comments - :x:
* Verify the contents of the comments textarea is submitted to the database and renders to the page correctly once 'Add Comment & Rating' is clicked - :white_check_mark:


### **Recipe Page - Fixes**
* Add required attribute to ensure users cannot submit blank comments to the page.



# **Add Recipe Page**

### General

* Verify the page loads responsively on all device sizes. - :white_check_mark:
* Verify all fonts are applied as expected - :x:

### Form Fields
* Verify call categories are rendered from the database, into the select menu - :white_check_mark:
* Verify all labels are responsive, when a user focusses on corresponding input field - :white_check_mark:
* Verify all validation is present throughout the form as specified below:
    * Recipe Name - Minimum 5 characters :white_check_mark:
    * Short Description - Minimum 50 characters :white_check_mark:
    * Yield (Servings) - Maximum integer of 8 - must not be blank :white_check_mark:
    * Preptime - Integer - multiple of 5 - must not be blank :white_check_mark:
    * Cooktime - Integer - multiple of 5 - must not be blank :white_check_mark:
    * Ingredients - No maximum - must not be blank :white_check_mark:
    * Method - No maximum - must not be blank :white_check_mark:
    * Img URL - No maximum - must not be blank :white_check_mark:

### Form Buttons

#### Ingredients
* Add ingredient button - appends an empty input to the page, below the last ingredient input :white_check_mark:
* Remove ingredient button - removes the last input in the ingredients section, unless it is the only input present on the page :white_check_mark:
* Reset button - removes all but the first ingredient input field from the section and empties the first ingredient input field of any text :white_check_mark:

#### Method
* Add step button - appends an empty text area to the page, below the last step textarea :white_check_mark:
* Remove step button - removes the last textarea in the method section, unless it is the only textarea on the page :white_check_mark:
* Reset button - removes all but the first textarea from the section and empties the textarea field of any text :white_check_mark:

#### Add Recipe
* Verify if any form validation is not passed, the form will not submit, the user is indicated at field level of the criteria for the input field :white_check_mark:
* Verify if all validation is passed for the form, the data is submitted to the database 'Recipes' hosted with MongoDB :white_check_mark:


### **Add Recipe Page - Fixes**
* Style/font style missing from the call to action button and caption at the bottom of the page.


# **Edit Recipe Page**

* Verify the page loads responsively on all device sizes. - :white_check_mark:
* Verify all fonts are applied as expected - :white_check_mark:
* Verify all validation is in place as specified for the 'Add Recipe' page - detailed [HERE](#form-fields)- :white_check_mark:
* Verify all fields are automatically filled in from the database, with corresponding recipe information :white_check_mark:
* Verify all buttons function the same as the 'Add Recipe Page' - detailed [HERE](#form-buttons) :white_check_mark:
* Verify any changes are submitted to the database when the 'Submit Changes' button is clicked :white_check_mark:


# **Site Wide**

### Navbar
* Verify navbar is collapsed at all times -  :white_check_mark:
* Verify the scroll up arrow takes a user back to the top of the page when clicked (this is found bottom right of the viewport) - :white_check_mark:
* Verify the following links do NOT display in the navbar if logged out :
    * Logout :white_check_mark:
    * Add Recipe :white_check_mark:
* Verify the following links do NOT display in the navbar if logged in :
    * Register :white_check_mark:
    * Login :white_check_mark:
* Verify recipe categories are "display:none" class is toggled when 'Recipes' link is clicked :white_check_mark:
* Verify social icons link to the corresponding social media websites and that they open in a new window when clicked :white_check_mark:


### Footer
* Verify social icons link to the corresponding social media websites and that they open in a new window when clicked :white_check_mark:
* Verify the year is rendered as the current year in the copyright caption :white_check_mark:


# **DevTools**

Google DevTools was used within Google Chrome on macOS throughout the development process. 

* Testing responsiveness of the site across several device models. 
    * Media queries are written accordingly to support major devices available in dev tool testing environment.

* Target elements and style with CSS, to test potential changes before coding them into relevant HTML.

* Console used to support the development of JavaScript code.
    * console.log used at various points to check values of variables and function outputs, whilst developing logic for site.
    * Upon site completion - the console was checked for any errors
    * Once the site was completed, the console was checked for any errors on each page :white_check_mark:

# **Automated Testing**

## Validating the HTML, CSS and JS code

All of my code passed the following validation tests/services:
- HTML: [W3C Markup Validation Service](https://validator.w3.org/)
- CSS: [W3C Markup Validation Service](https://jigsaw.w3.org/css-validator/)
- HTML & CSS [Dead Link Checker](https://www.deadlinkchecker.com/website-dead-link-checker.asp)
- JS: [jshint](https://jshint.com/)

* There were various HTML and CSS validation issues to resolve. These mainly referred to formatting my code and were easily fixable across the site.

# **User Stories**


#### User Story 1
##### As a visitor to the site, I want to easily find a recipe for lunch and dinner. The recipe should have reviews.

* Upon visiting the site it was clear to me which recipes had been recommended most times, as there was a top recipe panel on the home page. It also indicated the type of meal it was. ie: lunch or dinner.
* The navbar was easily found and contained links to show only recipes from a certain category, this helped me find a recipe much quicker. 
* Each recipe had a comments section at the bottom of its page. This helped me decide if I should try to cook the recipe myself.

#### User Story 2
##### As a visitor to the site, I want to share one of my favourite vegan recipes with others.

* The home page indicates to me as a user, that the site is a place to share recipes. I am presented with a get started button upon visiting the site, which prompts me to make an account with 'Eat Vegan'. Upon signing up I am taken to the recipes page, at the bottom of which there is an 'add recipe' button.
* At the bottom of the home page, there is a message informing me as a user 'Sign up to Eat Vegan, to add and review our recipes', alongside a button to 'Get Started'.
* Once signing up, these buttons took me to an add-recipe form. The form was simple and easy to use, it was clear what information was required.

#### User Story 3
##### As a visitor to the site, I want to search for a light snack to make for some Vegan friends.

* Upon vising the site, I was presented with a link to see all recipes. This took me to a page full of different recipes.
* I was able to select lunch as a filter for the recipes, this made it easy to find a suitable meal. 
* I know that my friends enjoy avocado, I was able to search for a recipe containing avocado easily.


#### User Story 4
##### As a previous visitor to the site, I want to edit a recipe that I added to the site on a previous visit.

* Upon revisiting the site, I was able to search for the recipe I added easily.
* To edit the recipe, I had to be logged in. Although this was not clear initially.
* Once logged in, two buttons appeared below the recipe image, edit and delete the recipe.
* Once clicked, the edit recipe form appears with all the recipe information populated. I was able to easily edit the details and hit 'submit changes' at the bottom of the page. The recipe updated immediately.


#### User Story 5
##### As a previous visitor to the site, I want to review a recipe that I cooked last week. It would be good to be able to search for the recipe, as I remember the name of it.

* Upon visiting the site, I searched for the recipe I had cooked earlier in the week. 
* At the bottom of the page, a banner informed me that I should 'Sign up to add and review recipes'.
* I clicked the 'get started' button, which was next to this message.
* I easily signed up and relocated myself to the recipe, where I now found an 'add comment and rating' section at the bottom of the page. 
* I was easily able to rate the recipe out of 5 and leave a comment. Which was added to the page once I clicked 'Add Comment & Rating'. 
* I could also see a 'delete' button next to my newly added comment. It would be good if I could also edit this comment if I desired to do so.


# User Testing

## My-Mentor

A series of feedback and suggestions had been highlighted during a call on Saturday 30th January 2021. Action has been taken for all of these suggestions and changes to the site and code. 

All changes are documented in Section 6 of this document (Post Review Changes)

## **User Testing**

A fellow Code Institute student took the time to thoroughly review the site content and code. They provided me with several ideas to improve both the user experience and improve code efficiency.

All changes are documented in Section 6 of this document (Post Review Changes)

# Post Review Changes

* The following was addressed post-testing and feedback. (changes are detailed in commit history dated 30/01/2021 onwards) :
    1. Change image on the recipe page to occupy less page width ( change div class from container-fluid to a container ) - fixes image sharpness.
    2. Change ingredients and recipe info font style to match directions font style on the recipe page.
    3. Make the navbar menu button and scroll up button smaller on mobile.
    4. Adjust the spacing between 'search' and 'all recipes' buttons on the recipes page.
    5. Change the colour of the range, rating input on the recipes page, to match the track colour.
    6. Add page headers to add-recipe and edit-recipe pages - remove 'eat vegan' heading from both.
    7. Change all app routes to contain hyphens, not underscores.
    8. Sort recipes in app.py to display in ascending order of date added on the recipes template.
    9. Do not display image container on recipe page if 'image URL' entry is blank.
    10. Remove the required attribute from the 'image URL' field on both add and edit recipe forms.
    11. Add comment and rating made visible to all site visitors, redirect to login if attempt to add comment without authentication.
 