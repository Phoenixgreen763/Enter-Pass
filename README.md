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
        ![Categroy Filter](/static/images/category-filter.png)
        * Dropdown Filter: this feature lets users sort events by date or price. The dropdown allows for both ascending and descending order, offering flexibility in how events are displayed.
        ![Dropdown Filter](/static/images/dropdown-filter.png)
    * Admin users have additional controls with edit and delete buttons available under each event, enabling them to easily manage event listings.

    ![Admin Event Buttons](/static/images/admin-events.png)

![Events Page](/static/images/events.png)


* Event Detail Page
    * When a user clicks on any event, they are taken to the Event Detail Page, which provides detailed information about that specific event.
    * Similar to the Events page, this page displays key details such as the event title, location, available tickets, and pricing. Additionally, this page includes a more comprehensive event description, giving users deeper insight into the event.
    * The page features two key buttons:
        * Booking Button: this allows users to add the event to their shopping bag, making it easy to proceed with booking.
        * Back Button: This provides a convenient way to return to the previous Events page, helping users seamlessly navigate back to continue browsing.

![Event Detail](/static/images/event-detail.png)


* Bag 
    * If a user clicks the bag icon on the navbar, the toast messages that appear. They will be redirected to the bag page.
    * If the shopping bag is empty, the user will receive a notification message indicating this, along with a button that redirects them to the Events page to browse available tickets.

        ![Empty Bag](/static/images/empty-bag.png)

    * When a user adds an event to the shopping bag, the event will be displayed on the bag page, including key information and the total price of all items in the bag.
    * Each item will display a subtotal, along with a grand total for all items in the shopping bag.

        ![Bag Items](/static/images/bag-items.png)

    * Users have the ability to adjust the number of tickets for each specific event, and can either update that item or delete it entirely from the bag.

        ![Bag Buttons](/static/images/bag-buttons.png)

    * Additionally, users will see options to either continue shopping or proceed to a secure bag page.

![Bag](/static/images/bag.png)


* Checkout 
    * If users are satisfied with the items in their bag, they can proceed to a secure checkout.
    * The checkout page provides a summary of the order, allowing users to review their selected items.
    * Users will find a form to fill out their details, such as email and phone number, to ensure they receive their tickets.
    * The form will also prompt users to enter their card details to complete the purchase. Below the form, a warning message will inform users that their card will be charged, along with the total amount.
    * At the bottom of the form, users have two options:
        * Complete Payment - Finalize their order and proceed with the purchase.
        * Adjust Bag - Redirect them back to their shopping bag, allowing them to make any necessary changes to their items.
    * Additionally, there is an option on the form to save your information to your profile for future transactions, providing convenience for repeat users.

![Checkout](/static/images/checkout.png)


* Checkout Confirmation 
    * Upon successful payment, the user will be redirected to a success page.
    * This page will display an order summary, including a unique order ID that confirms the transaction.
    * The summary will show the user information entered into the checkout form, ensuring accuracy and transparency.
    * Additionally, the user will receive a confirmation message indicating that the order details will be sent to the email address provided during checkout.

![Checkout Confirmation](/static/images/order-confirmation.png)

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

* Advanced Search and Filtering Options
    * Enhance the search functionality to include more filtering options, such as date ranges, price ranges, and location-specific filters, making it easier for users to find events that suit their preferences.

* Social Media Integration
    * Integrate social media sharing options, allowing users to share their favorite events on platforms like Facebook, Twitter, and Instagram to increase visibility and engagement.

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

* Multiple testing methods were employed to ensure the site functions as intended and that users do not encounter errors or potential bugs that could impact their experience. 

## Manual Testing

* Manual testing was conducted to ensure that all features of the application function as intended. The following steps were taken during the testing process:

* Functional Testing
    * Each feature was tested for functionality, including user registration, login/logout, event browsing, ticket booking, and payment processing. All functionalities performed as expected without errors.

* User Interface Testing
    * The website’s layout and design were reviewed across different devices and screen sizes to ensure responsiveness and usability. Elements such as buttons, images, and text were checked for clarity and proper alignment.

* Input Validation Testing
    * User input fields (e.g., registration forms, search bars) were tested with valid and invalid data to ensure proper validation messages are displayed. This confirmed that users receive appropriate feedback for incorrect inputs.

* Navigation Testing
    * The navigation flow was tested by clicking through various links and buttons to ensure that all pages load correctly and that users can navigate seamlessly throughout the site.

* Performance Testing
    * The loading speed of the website was assessed to ensure that pages load quickly and efficiently, providing a positive user experience.

* Cross-Browser Testing
    * The application was tested across multiple web browsers (e.g., Chrome, Firefox, Safari) to ensure consistent performance and appearance.

* Accessibility Testing
    * Accessibility features were evaluated to ensure the website is usable for individuals with disabilities, including proper use of alt text for images and keyboard navigability.

* By performing these manual tests, we ensured that the application meets the required quality standards and provides a seamless experience for users.

## Code testing

* Code testing was conducted during the build process of the project to ensure that the application is robust, reliable, and free from critical bugs. The following methodologies and tools were employed during the testing process:

* Unit Testing
    * Unit tests were created to verify the functionality of individual components and functions within the codebase. These tests check specific logic and ensure that each unit behaves as expected.

* Integration Testing
    * Integration tests were performed to verify that different modules of the application work together correctly. These tests ensure that data flows as expected between various parts of the application, such as user authentication and event management features.

* Static Code Analysis
    * Static code analysis tools were used to detect potential issues in the code without executing it. Tools like Pylint or Flake8 were employed to identify code smells, style violations, and potential bugs, enhancing code quality.

* Through these testing methods, we ensured that the codebase is reliable, maintainable, and performs well under various conditions.

## Validator Testing 

* Static code analysis tools were used to check for coding standards, potential errors, and code quality. These tools help maintain a clean codebase and prevent common pitfalls in development.

* CSS Validator 
    ![CSS results]()
    
* HTML Validator
    ![HTML results]()
    
* Light House Testing
    ![LightHouse results]()

## All Known Bugs

* No known bugs have been found present at this point.

## Design

* Fonts
    * All fonts were sourced from Google Fonts.

* Color 
    * The majority of the pages and text are in black and white, providing a clean and minimalist look.
    * Colorful images are used for events to create visual interest, as a contrast to the minimalist desgin everwhere else.
    * Buttons are styled in red and blue for emphasis and interaction.
    * Green text is used for pricing information, making it stand out for users.
    
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
    * Templates for some HTML, such as the allauth templates, were utilized from the Boutique Ado module.

* Content
    * All content was written by the developer

* Imagery
    * All images were sourced from shuttershock.

* Icons
    * All icons were sourced from fontawesome. 
    

