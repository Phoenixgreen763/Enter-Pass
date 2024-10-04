# Enter-Pass

## Summary

EnterPass is an event management and ticketing platform designed to simplify the process of discovering, organizing, and attending events. The platform provides a streamlined experience for both event organizers and attendees, offering robust features like event creation, ticket sales, and user profiles. EnterPass allows event hosts to create and manage events, set ticket prices, and monitor sales through a dedicated organizer dashboard.

View the live website here - https://enter-pass-37670ea809e0.herokuapp.com

![UX Mockup](/static/images/UX.jpg)

## Features 


### Existing features

* Home Page
    * The homepage is the first point of interaction for users and sets the tone for the rest of the website. It features a dynamic navbar, present on all pages, offering easy navigation to various sections of the site.
    * The background is dominated by a vibrant, full-width concert image, creating an immersive visual experience for the user. Overlaid on this image is a welcoming message, designed to inspire users to explore the site further.
    * A prominent "SHOP NOW!" button accompanies the text, providing a direct call to action. Clicking this button immediately redirects users to the product page, allowing them to start shopping with just one click.

![Home Page](/static/images/homepage.png)

* Navbar 
    * The navbar is present on all pages of the site, and includes a number of features for users, and admins.
    * It includes the site heading, clicking on the site title instantly redirects users back to the homepage, providing a quick way to return.
    * The navbar also has a searchbar, users can search for events effortlessly by entering keywords or specific references. The search bar dynamically returns results that match the user's input, streamlining the browsing experience.

    ![Search Bar](/static/images/searchbar.png)

    * The account management section handles multiple functions. This section offers comprehensive user controls, including options to sign up, sign in, and sign out. Users can also view and update their profiles. For admin users, this section expands to include event management tools, allowing them to create, edit, or remove events.

    ![Account Management](/static/images/account-management.png)

    * A checkout bag icon displays the user's current total, and upon clicking, it takes them to a detailed view of their selected items, providing a seamless shopping experience.

![Navbar](/static/images/navbar.png)

* Events
    * The Events page showcases all available events and provides users with powerful filtering options to refine their search.
    * Each event is displayed with key details, including a category banner image, the event title, location, available tickets, and pricing, giving users a comprehensive overview at a glance.
    * Users can refine their search using two filtering options:
        * Category Filter: located at the top of the event list, this filter allows users to narrow down their results by selecting specific categories, ensuring they find events that match their interests.
        * Dropdown Filter: this feature lets users sort events by date or price. The dropdown allows for both ascending and descending order, offering flexibility in how events are displayed.
    * Admin users have additional controls with edit and delete buttons available under each event, enabling them to easily manage event listings.

![Events Page](/static/images/events.png)

* Event Detail Page
    * When a user clicks on any event, they are taken to the Event Detail Page, which provides detailed information about that specific event.
    * Similar to the Events page, this page displays key details such as the event title, location, available tickets, and pricing. Additionally, this page includes a more comprehensive event description, giving users deeper insight into the event.
    * The page features two key buttons:
        * Booking Button: this allows users to add the event to their shopping bag, making it easy to proceed with booking.
        * Back Button: This provides a convenient way to return to the previous Events page, helping users seamlessly navigate back to continue browsing.

![Event Detail](/static/images/event-detail.png)

### Core features

* Event creation and management functionality for organizers
* Secure online payments using Stripe
* User authentication and profile management
* Role-based access control for event management
* Dashboards for both organizers and attendees
* Real-time updates on ticket availability
* Browsing and filtering of events
* Responsive UI using Bootstrap and JavaScript for enhanced user interaction

### Features to Implement


## User Stories

* User A: teenager looking for a birthday event
    * "As a teenager, I want to quickly browse through a variety of fun events, filter by categories like concerts or festivals, and easily find affordable events for my birthday party so I can celebrate with my friends."

* User B: busy parent planning a family outing.
    * "As a parent, I want to be able to search for family-friendly events and sort them by date, so I can quickly find activities that fit within our schedule."

* User C: A concert enthusiast interested in discovering new shows.
    * "As a music lover, I want to be able to search for concerts based on specific bands or genres, and read detailed event descriptions, so I can decide which shows to attend."

* User D: admin user managing events for the platform.
    * "As an admin, I want to easily update event information, add new events, and remove outdated ones directly from the Events page so that the website stays current and accurate for users."

## Testing


## Manual Testing


## Code testing


## Validator Testing 

* CSS Validator 
    
* HTML Validator

* Light House Testing

## All Known Bugs


## Design

* Fonts
    * All fonts were from google.

* Color 
    
* Images
    * A background image of an event was used on the homepage to set the tone and theme of the site, creating an immersive visual experience.
    * Category images were assigned to each event category. These are displayed as banners on the main Events page and are also featured on the individual Event Details pages, providing visual consistency throughout the site.

## Deployment Of The Website

* The website was deployed to Heroku. The steps to deploy are shown, as follows:
    * Go to your Heroku Dashboard, open your app, and navigate to the Deploy tab.
    * Select GitHub as the deployment method and connect your GitHub account.
    * Choose your repository and branch, then click Deploy Branch.
    * Enable automatic deploys for continuous deployment when new changes are pushed to GitHub.
    * Set environment variables in the Settings tab by clicking Reveal Config Vars.
    * Ensure the app is running properly, including performing all necessary migrations and installing dependencies.

The live link can be found here - https://enter-pass-37670ea809e0.herokuapp.com

## Technologies Used

* HTML5
* CSS
* JavaScript
* Python
* Django

## Credits

* Code
    * Templates for some html, such as allauth templates were used from the Boutique Ado module.

* Content
    * All content was written by the developer

* Imagery
    * All images were sourced from shuttershock.

* Icons
    * All icons were sourced from fontawesome. 
    

