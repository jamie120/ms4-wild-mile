
# Wild Mile Conversions
## Code Institute: Milestone Project 4 - Jamie Rolls - 
A live version of the site is available [here.](https://wild-mile-ms4.herokuapp.com/)
---
![Desktop](insert - responsive screenshots here)

Wild Mile Conversions is a site dedicated to the advertisement of bespoke vehicle conversions for leisure and business. Listings are added by site users, with the aim to attract buyers and complete a selling transaction off-site. Users purchase a listing fee to advertise on the site. Wild Mile merchansise is also available for purchase. The site is designed to be easy to navigate, promotes ease of use and have intuitive features for both buyers and sellers to enhance the user experience.

#### **Project Requirements:**
Build a full-stack site based around business logic used to control a centrally-owned dataset. Set up an authentication mechanism and provide paid access to the site's data and/or other activities based on the dataset, such as the purchase of a product/service.

Required Technologies : 
* HTML, CSS, JavaScript, Django + Django
* Relational database (MySQL or Postgres)
* Stripe Payments

Optional: Include use of additional libraries and external APIs.

#### Mandatory Requirements

1. Django Full Stack Project: Build a Django project backend by a relational database to create a website that allows users to store and manipulate data records about a particular domain.
2. Multiple Apps: The project must be a brand new Django project, composed of multiple apps (an app for each potentially reusable component in your project).
3. Data Modeling: Put some effort into designing a relational database schema well-suited for your domain. Make sure to put some thought into the relationships between entities. Create at least 2 custom django models beyond the examples shown on the course
4. User Authentication: The project should include an authentication mechanism, allowing a user to register and log in, and there should be a good reason as to why the users would need to do so. e.g., a user would have to register to persist their shopping cart between sessions (otherwise it would be lost).
5. User Interaction: Include at least one form with validation that will allow users to create and edit models in the backend (in addition to the authentication mechanism).
6. Use of Stripe: At least one of your Django apps should contain some e-commerce functionality using Stripe. This may be a shopping cart checkout or single payments, or donations, etc. After paying successfully, the user would then gain access to additional functionality/content on the site. Note that for this project you should use Stripe's test functionality, rather than actual live payments.
7. Structure and Navigation: Incorporate a main navigation menu and structured layout (you might want to use Bootstrap to accomplish this).
8. Use of JavaScript: The frontend should contain some JavaScript logic you have written to enhance the user experience.
9. Documentation: Write a README.md file for your project that explains what the project does and the value that it provides to its users.
10. Version Control: Use Git & GitHub for version control.
11. Attribution: Maintain clear separation between code written by you and code from external sources (e.g. libraries or tutorials). Attribute any code from external sources to its source via comments above the code and (for larger dependencies) in the README.
12. Deployment: Deploy the final version of your code to a hosting platform such as Heroku.
13. Security: Make sure to not include any passwords or secret keys in the project repository. Make sure to turn off the Django DEBUG mode, which could expose secrets.

# Table of Contents

1.  [Strategy & Scope](#strategy-and-scope)
    * [UX](#ux)
        * [Business Objectives](#business-objectives)
        * [User Objectives](#user-objectives)
        * [Project goals](#project-goals)
        * [User Stories](#user-stories)
2.  [Structure](#structure)
    * [Design Process](#design-process)
        * [Page Structure](#page-structure)
            * [Home](#home-landing-page)
            * [Conversions](#conversions-page)
                * [Conversion Detail](#conversion-detail-page)
            * [Add Conversion](#add-conversion-page)
            * [Add Conversion Pricing](#add-conversion-pricing-page)
            * [Merchandise](#merchandise-page)
                * [Product Detail](#product-detail-page)
            * [Shopping Bag](#shopping-bag-page)
            * [Checkout](#checkout-page)
                * [Checkout Success](#checkout-success-page)
            * [About Us](#about-us-page)
            * [Faq](#faq-page)
            * [Profile](#profile-page)
                * [Order History](#order-history-page)
                * [My Listings](#my-listings-page)
                * [Saved Listings](#saved-listings-page)
                * [Message Portal](#message-portal-page)
            * [Conversion Management](#conversion-management-page)
                * [Approve Conversions](#approve-conversions-page)
            * [Add Product](#add-product-page)
            * [Authentication](#auth-pages)

3.  [Surface](#surface)
    * [Colors](#colours)
    * [Fonts](#font-choice)
4.  [Skeleton](#skeleton)
    * [Wireframe Designs](#wireframe-designs)
    * [Final Project Design Differences](#wireframe-and-final-project-differences)
    * [Responsive Design](#responsive-design)
    * [Database Design & Structure](#database-design-and-structure)
5.  [Features](#features)
    * [Sitewide](#sitewide)
        * [Navbar](#nav-bar)
        * [Footer](#footer)
    * [Homepage](#home)
        * [Header](#header)
        * [Top Recipes](#top-recipes)
        * [Recipe Links](#recipe-links)
        * [Call to action buttons](#call-to-action-button)
    * [Recipes Page](#recipes-page)
        * [Search and Filter Function](#search-and-filter-functionality)
        * [Recipe Cards](#recipe-cards)
        * [Pagination](#pagination)
        * [Call to action buttons](#call-to-action-button)
    * [Recipe Page](#recipe-page)
        * [Image & Buttons](#image-and-buttons)
        * [Recipe Information](#recipe-information)
        * [Comments](#comments)
        * [Call to action buttons](#call-to-action-buttons)
    * [Add Recipe Page](#add-recipe-page)
        * [Categories](#categories)
        * [Form Design](#form-design)
        * [Ingredients Input](#ingredients-input)
        * [Method Input](#method-input)
    * [Edit Recipe Page](#edit-recipe-page)
    * [Authentication](#authentication)
6.  [Future Features](#future-features)
7.  [Technologies Used](#technologies-used)
    * [Languages](#languages)
    * [Libraries](#libraries)
    * [Tools](#tools)
8.  [Testing](#testing)
9. [Deployment](#deployment)
    * [Hosting on Heroku](#hosting-on-heroku)
    * [Cloning](#cloning)
10. [Credits](#credits)
    * [Content](#content)
    * [Media](#media)
        * [Images](#images)
    * [Acknowledgements](#acknowledgements)
        * [Sites used](#sites-used-for-information-and-support)
        * [Advice & Support](#i-received-advice-and-support-from)


# Strategy and Scope
## UX

#### Business Objectives
- The aim of Wild Mile Conversions is to create a web-based platform that enables the buying and selling of all sorts of unique, interesting and alternative conversions such as (but not limited to!) campervans, mobile bars and catering. 
- The site will generate revenue from people that wish to list/advertise their converted vehicle on the platform. Revenue will also be generated from selling Wild Mile merchandise.
- The site will only allow self- converted and vintage vehicles, or unique base vehicles ready for conversion - to be listed. This will be managed by an approval process before listings become live on the site.
- The site will provide sellers, with a unique opportunity to advertise to a large group of a specific target audience.
- The site will be easy to navigate, all features will be clear to a user.
- Social media channels will be present on the footer, to attract site visitors to join the growing community of 'Wild Mile' enthusiasts.

#### User Objectives

- Users may be using the site to find bespoke conversions, as potential buyers.
- Users may like to list/advertise a conversion for sale on the site, this should be easily acheived with a clear, straightforward method.
- Users may like to purchase 'Wild Mile' merchandise using the site. The store should make this easy, with clear pricing and checkout functionality.

#### Project Goals

- Create a clear, well-designed website for the user to navigate with ease.
- Use a consistent, clear theme throughout the site.
- Consider appropriate pages/layout and content to fulfil business/user objectives/user stories.
- Design models and integrate a relational database into the web app using SQlite + Django, transfer this to Postgres during deployment. The database will store conversion listings, merchandise products, user profiles.
- Consider user authentication, to allow/enable the following actions & features: -
    * Creation of a user profile
    * Save Default delivery information
    * View order history
    * Add/Edit a conversion listing
    * Save/Favorite listings to profile
    * Admin features
        * Edit, delete, approve conversion listings
        * Edit, delete and add merchandise products

- Fulfil all mandatory project minimum requirements. (these are listed [HERE](#mandatory-requirements))

 

#### User Stories

A detailed list of user stories has been complied to help steer the design process.
 * The list can be viewed using this link to a Google Drive Sheets file - [User Stories](https://docs.google.com/spreadsheets/d/1g_SrmtPI9fuqDBbD-NZnR5lpJLmGJHU5aqLjB80KybA/edit?usp=sharing)


# Structure

## Design Process

#### Page Structure

* The site is designed to feel familar throughout it's pages in style and functionality. It contains straight-forward navigation elements, further filtering/manipulation of site content can be completed within individual pages by utilising features such as search, filter and multiple pages. This design allows users to quickly and easily engage with and locate relevant content from within the site.

* The site theme and code was developed from the ground up, with elements of the site layout inspired from 'boutique-ado' mini project that was put together during the teaching/learning of the 'Code Institute - Software Developer' course.
            
* To maintain familarity between pages and improve site usability, the filter and sort elements implemented accross the site are displayed and work in the same way throughout the site.

* Research into optimal page layouts was conducted accross various sites/businesses which advertise/list products. The research helped to develop page layouts which present information clearly to the user accross multiple devices sizes with success.

* To support [User Stories](https://docs.google.com/spreadsheets/d/1g_SrmtPI9fuqDBbD-NZnR5lpJLmGJHU5aqLjB80KybA/edit?usp=sharing) and taking input from research, the following pages were chosen to be created:

    ##### Home - Landing Page

    ##### Conversions Page ----- Conversion Detail Page

    ##### Add Conversion Page

    ##### Edit Conversion Page

    ##### Conversion Listing Prices Page

    ##### Merchandise Page ----- Product Detail Page

    ##### Shopping Bag Page ----- Checkout Page ----- Checkout Success Page

    ##### About Page

    ##### FAQ Page

    ##### Profile Page ----- Order History Page ----- My Listings Page ----- Saved Listings ----- Message Portal

    ##### Conversion Management Page ----- Approve Conversions Page

    ##### Add Product Page

    ##### Edit Product Page

    ##### Authentication Pages (allauth templates - styled)
    
* The navbar, present on all pages will contain the following navigation links :
    * Home
    * Buy a conversion (dropdown) ----- All conversions ----- Campervans ----- Mobile Bars and Catering Vans
    * Sell a conversion (dropdown) ----- View Pricing ----- Add a conversion
    * Merchandise (dropdown) ----- All Products ----- Clothing ----- Stickers ------ Mugs
    * About Us
    * Faq

* Accompanying the navbar, a 'My Account' and 'Shopping Bag' button will be present on all pages:
    * My Account (dropdown) ----- Register ----- Login / My Profile ----- Logout

    * My Account for admin/superuser with contain addition navlinks when logged in:
        * Product Management
        * Conversion Listing Management
    
    * Shopping Bag is a direct link to the shopping bag template

* A search bar will be present on all pages - this takes a user query and returns the conversions template displaying only relevant matches. The specified search query is used as a filter against the title and description of all live listings.

* The site footer will contain social media icons, which link the user to the relevant social platform in a new browser/tab.

#### Home Landing Page

* The home page will contain a button to view all conversions with the company name and business summary.

#### Conversions Page

* The all conversions page (conversions.html) will dynamically show conversions from the database, based on search terms or filters which have been applied.

#### Conversion Detail Page

* The conversion detail page will display the content/data for one listing, including contact information for the seller.
#### Add Conversion Page

* The add conversion page will render a form, which can be filled in to submit a listing to the site including photo file upload. The page will also contain directions for the user to support the user experience.

#### Edit Conversion Page

* The edit conversion page will render the same form as 'add conversion', but it will be populated with an instance of a specified listing. The user will be able to update the content, clear or update photo file content.

#### Add Conversion Pricing Page

* The conversion pricing page will outline the different listing tokens which can be purchased. The elements displaying this information will link to their respective product page, so that a user may add it to their shopping bag and checkout to purchase a listing token.

#### Merchandise Page

* The merchandise page (products.html) will dynamically show products from the database, based on category filters which have been applied.

#### Product Detail Page

* The product detail page will display the content/data for one product, including the functionality to add the product to the shopping bag so that a user may checkout and purchase the item.

#### Shopping Bag Page

* The shopping bag will render all products in the session bag. It will contain links to checkout - to allow the user to complete purchase of bag items.

#### Checkout Page

* The checkout page will allow users to review and complete the order, add delivery and payment details.

#### Checkout Success Page

* The checkout success page will render the completed order information and provide user feedback.

#### About Us Page

* The about us page will display information about the business and its owners.

#### FAQ Page

* The FAQ page will render some questions and answers which are most common to site users.

#### Profile Page

* The profile page will contain a host of links to other registered site features, as well as the users default delivery information which can be updated.

#### Order History Page

* This page will display all previous orders associated with the logged in user profile.

#### My Listings Page

* The My listings page will display any listings that the user has added to the platform, allowing users to edit or delete listings as required.

#### Saved Listings Page

* The saved listings page will render any listings the user has chosed to save/favorite whilst browsing the site.

#### Message Portal Page

* The message portal is a future feature that will allow users to communicate between themselves using the 'Wild Mile' platform.

#### Conversion Management Page

* This page will render a summary of all active listings and allow the ability to view, edit, delete, unlist as required.

#### Approve Conversion Page

* This page will render a summary of all inactive listings and allow the ability to view, edit, delete, make active as required.

#### Add Product Page

* The add product page will render a form, the form allows products to be added to the merchandise section of the site.

#### Authentication Pages

* Various authentication pages, login, logout, register ... and other associated will be provided from the allauth library.


# Surface

## Colours

Colour Palette - Three main colours that compliment the design of the site are:

 - ![#363E46](https://via.placeholder.com/15/363E46/000000?text=+) - `#363E46` - Main Site Body
 - ![#263d41](https://via.placeholder.com/15/263d41/000000?text=+) - `#263d41` - Information Banner
 - ![#627072](https://via.placeholder.com/15/627072/000000?text=+) - `#627072` - Page buttons, card background

* Other various shades of grey are used with white to highlight, surround and drop shadows on elements throughout the site.
* The main colour was chosen to represent the road and take some relvance to the company name.


## Font Choice

The following fonts were applied to the site. 

- pwscratchedfont - Used for conversion listing titles and home page brand title.
    - The hand drawn style of the font works well to bring the concept of creativity forward.
- Raleway - Used throughout the site as main parent font.
    - The clean, modern look compliments the dark backgrounds and theme of the site.

# Skeleton

## Wireframe designs

Wireframes were designed using Figma, for three primary breakpoints - Desktop, Tablet and Mobile.

- [Figma Wireframes](https://www.figma.com/file/UHdbvOVwqO7qNSWGQC7sWG/MS4-WILD-MILE?node-id=0%3A1)

![Home & Profile](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/home_&_profile.png "Home & Profile screenshot")
![About & FAQ](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/about_&_faq.png "About & FAQ screenshot")
![Conversions & Conversion Detail](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/conversions_&_conversion_detail.png "Conversions & Conversion Detail screenshot")
![Merchandise & Product Detail](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/merch_&_product_detail.png "Merchandise & Product Detail screenshot")
![Add Conversion & Listing Pricing](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/add_conversion_&_listing_pricing.png "Add Conversion & Listing Pricing screenshot")
![My Listings & Saved Listings](https://github.com/jamie120/ms3-eat-vegan-recipes/blob/master/documentation/wireframes/saved_listings_&_my_listings.png "My Listings & Saved Listings screenshot")

## Wireframe and Final Project Differences

- Home Page
    
- Recipes
   
- Recipe Page
  
- Add Recipe form
    
- Navbar
   
- Call to action buttons
   
## Responsive Page Design

The site has been designed to operate well on all screen sizes. As a core purpose of the site is to host recipes, it is expected that the site will be viewed on tablet and mobile devices often, whilst in the kitchen. With that in mind, the site content and layouts have been designed to support a positive user experience.

- Home page

## Database Design and structure

* The database 

### Recipe Structure
1. _id - ObjectId - (generated by mongoDB)
2. name - str
3. category - str 
4. short_description - str
5. recipe_info - array
6. ingredients - array
7. method - str
8. img_url - str
9. votes - int
10. added_by - str

### Categories Structure
1. _id - ObjectId - (generated by mongoDB)
2. name - str

### Reviews Structure
1. _id - ObjectId - (generated by mongoDB)
2. recipe_review - str
3. recipe_rating - str
4. recipe_id - str
5. added_by - str

### Users

1. _id - ObjectId - (generated by mongoDB)
2. username - str
3. password - str - (password hash generated by werkzeug.security)

# Features

## Sitewide

### Nav Bar

### Banner

### Footer


## Home

## Conversions Page

## Conversion Detail Page

## Add Conversion Page

## Add Conversion Pricing Page

## Merchandise Page

## Product Detail Page

## Shopping Bag Page

## Checkout Page

## Checkout Success Page

## About Us Page

## FAQ Page

## Profile Page

## Order History Page

## My Listings Page

## Saved Listings Page

## Message Portal

## Conversion Management

## Approve Conversion 

## Add Product Page

## Authentication Pages


## Authentication
The site uses authentication. Users that have signed up to the site have the privilege to conduct the following actions:

1. add recipes to the site / Edit & Delete recipes added by themselves.
2. Like other users recipes.
3. Leave comments and ratings on recipes from other users / Delete comments added by themselves.

# Future Features

# Technologies Used

## Languages

* HTML - the base language used for this project.
* CSS - used for styling HTML code sitewide.
* Python & Flask - Used to produce the backend code running the site.
    * OS - This project used OS to provide functions for interacting with the site.
    * Bson.objectid - Used to enable the use of ObjectID when referring to the _id data names within the MongoDB database.
    * Werkzeug - Werkzeug.security is used to provide password authentication for the site.
* JavaScript - used to make elements of the site interactive and support HTML & CSS styling.

## Libraries

* [Bootstrap](https://getbootstrap.com/) (4.5.2) - with supporting JS Script and tooltips. Used for the responsive grid system, styling elements and navbar creation.
* [FontAwseome](https://fontawesome.com/) (5.15.1) - used for all icons on the site.
* [Google Fonts](https://fonts.google.com/) - used for the Roboto fonts.
* [JQuery](https://jquery.com/) (3.5.1) - used throughout the site to target and manipulate HTML elements and also in conjunction with the Bootstrap library.

## Tools

* [Gitpod](https://www.gitpod.io) - used as IDE for this project.
* [Git](https://git-scm.com/) - used for version control.
* [Github](https://github.com/) - used to host repository.
* [Heroku](https://dashboard.heroku.com/) - 
* [Figma](https://www.figma.com/) - used for creation of website theme/wireframe.
* [Am I Responsive](http://ami.responsivedesign.is/) - used for testing purposes and for the screenshot at the top of my README filed to display the web pages on different devices.
* [Google Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - used for testing and debugging the site.
* [w3 html validator](https://validator.w3.org/) - used to test and validate my html code.
* [w3 css validator](https://jigsaw.w3.org/) - used to test and validate my CSS code.
* [jshint](https://jshint.com/) - used to test and validate all JS code.
* [Dead Link Checker](https://www.deadlinkchecker.com/website-dead-link-checker.asp)

# Testing

All-testing has been documented [testing.md](insert link here)

# Deployment

<!-- * The site was developed in GitPod and pushed to the following remote GitHub repository - [REPO](https://github.com/jamie120/ms3-eat-eat_vegan_recipes) -->
    * The following GIT commands were used throughout deployment:
        * **git status** ------ used to check the status of files and any changes made / untracked.
        * **git add**   ------ to stage files ready to commit.
        * **git commit -m " "**  ------ to commit the files.
        * **git push** ------ to push the files to the master branch of the GitHub repo.

### Hosting on Heroku
<!-- 
* This site is hosted using Heroku, deployed directly from the master branch via GitHub. - [LIVE SITE](https://ms3-eat-vegan-recipes.herokuapp.com/) -->
    * The following steps were taken to complete the hosting process.
       
    1. Set **_debug=False_** in the app.py file.
    2. Created a requirements.txt file from the terminal, using **_pip3 freeze --local > requirements.txt_**, to allow Heroku to detect this project as a python app and any required package dependencies.
    3. Created a Procfile using **_echo web: python app.py > Procfile_** from the Gitpod terminal so Heroku would be informed on which file runs the app and how to run this project.
    4. Created a new Heroku app, **_ms3_eat-vegan-recipes** and set its region to Europe.
    5. Automatic deployment was set up on Heroku - On the app dashboard, in the deploy menu. Connect to GitHub section. The GitHub repository was searched for and connected to the app.
    6. In the settings tab on the app dashboard, 'Reveal Config Vars' was used to tell Heroku which variableS are required to run the app. The following config vars were added: 
        *  **_IP_** 
        *  **_PORT_**
        * **_SECRET_KEY_**
        * **_MONGO_URI_**
    7. In GitPod, a check was completed to ensure the master branch was up to date and all commits had been pushed to GitHub, ready for Heroku to deploy.
    8. Clicked the **_Enable Automatic Deploys_** button located in the **_Deploy_** section of Heroku to allow for automatic deploys.
    13. Clicked the **_Deploy Branch_** button located in the **_Deploy_** section of Heroku to finally deploy this project.
    14. Clicked the **_View_** button to launch this project's app.

    <!-- * The deployed site on Heroku will update automatically upon new commits to the master branch in the GitHub Repo : [REPO](https://github.com/jamie120/ms3-eat-eat_vegan_recipes). -->


### Cloning

To run this code locally, you can clone this repository directly into the editor of your choice by following the steps below:

1. Open Terminal.
2. Change the current working directory to the location when you want the cloned directory.
3. Type the following into your Terminal:  
    <!-- git clone https://github.com/jamie120/ms3-eat-vegan-recipes.git -->
4. Press Enter to create a local clone.

* To cut ties with this GitHub repository, type git remote rm origin into the terminal.

##### For more information regarding cloning of a repository click [here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository).


# Credits

## Content

All the written content of the website has been written by myself. 

## Media

### Images

The following images used for this app/website were taken from Unsplash:


All other images were contributed from personal sources, of which no acknowledgement is required.

## Acknowledgements
   
### Sites used for information and support

* [W3C](https://www.w3.org/)
* [Stack overflow](https://stackoverflow.com/)
* [W3schools](https://www.w3schools.com/)
* [CSS Tricks](#https://css-tricks.com)
* [JQuery Documentation](https://api.jquery.com/)
* [Start Bootstrap](#https://startbootstrap.com/)
* [Bootstrap Documentation](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
* [JS Commenting](https://jsdoc.app/about-getting-started.html)
* [Python Documentation](https://docs.python.org/3/)

#### I received advice and support from
   * Oluwafemi Medale (mentor)
   * Code Institute - Slack Community (various students, tutors and mentors)