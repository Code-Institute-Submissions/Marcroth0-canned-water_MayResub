# Testing

Coverage report automated testing resulted in 72% which you can see below:

<details><summary>Coverage</summary>

![coverage](/readme-files/readme/coverage-report-readme.png)

</details>
<br>

Testing user stories:

1. As a shopper I can filter on category/product so that I can find what i'm searching for

- The user is able to navigate through the navbar, and choose by category.
  <br>

![userstories1](/readme-files/readme/user-stories-navigation.png)

- Via the footer the user has the ability of finding their way to products.
  <br>

![userstories2](/readme-files/readme/user-stories-navigation2.png)

- Via the sidebar the user has the ability of finding their way to products
  <br>

![userstories3](/readme-files/readme/user-stories-navigation3.png)

2. As a shopper I can search the website so that i can easily find what I'm looking for.

Including the above, the user has the ability of using the search-bar, as well as through the spread breadcrumbs.
<br>
Product Detail:

![userstories4](/readme-files/readme/user-stories-navigation4.png)

Bag:
<br>

![userstories5](/readme-files/readme/user-stories-navigation-5.png)

Profile:
<br>

![userstories6](/readme-files/readme/user-stories-navigation-6.png)

3. As a user I can login or logout so that I can manage my account login/As a user I can register for an account so that I can have a personal account:

Sign in:
<br>

![userstories8](/readme-files/readme/signed-in-readme.png)

Sign out:
<br>

![userstories9](/readme-files/readme/signed-out-readme.png)

4. As a shopper I can select quantity of product so that add it to cart

The user has the ability of incrementing, or decrementing, to how many products they want:

![userstories10](/readme-files/readme/amount-readme.png)

5. As a shopper I can view product details so that I can read the price, description, see image

![userstories11](/readme-files/readme/user-stories-details-readme.png)

6. As a user I can access my personal user profile so that I can privately view my order, save payment information

![userstories12](/readme-files/readme/profile-readme.png)

7. As a shopper I can view a list of products so that i can select one to purchase

![userstories13](/readme-files/readme/products-mobile-readme.png)

8. As a shopper I can get live feedback of products added so that I can keep track of my shopping bag

9. As a user I can "forgot password?" so that I can get it back

Not achieved.

10. As a shopper I can view my shopping bag so that I can see what's in it

![userstories14](/readme-files/readme/userstories-bag-readme.png)

11. As a user I can read articles so that I can learn more about environmental impact

![userstories15](/readme-files/readme/view-articles-readme.png)

## SuperUser

As a superUser I have the ability to via the frontend edit, add, delete, these following things:

- Products

![userstories16](/readme-files/readme/superuser-articles-readme.png)

- Reviews

![userstories17](/readme-files/readme/superuser-reviews-readme.png)

- Products

![userstories18](/readme-files/readme/superuser-products-readme.png)

# Manual Testing

![testin1](/readme-files/readme/testing-bag-readme.png)
![testing2](/readme-files/readme/testing-checkout-readme.png)
![testing3](/readme-files/readme/testing-checkout-success-readme.png)
![testing4](/readme-files/readme/testing-bag-readme.png)
![testing5](/readme-files/readme/testing-checkout-readme.png)
![testing6](/readme-files/readme/testing-contact-readme.png)
![testing7](/readme-files/readme/testing-footer-navbar.png)
![testing8](/readme-files/readme/testing-home-readme.png)
![testing9](/readme-files/readme/testing-products-readme.png)
![testing10](/readme-files/readme/testing-profile-readme.png)
![testing11](/readme-files/readme/testing-superuser-readme.png)

## Validators

My Python code has ran through pep8 and is deemed "All right"
My Html-code has ran through wc3 validator and has received no errors.
W3 CSS Validator came back appproved.

# Lighthouse

Lighthouse returned high in Best Practices, as well as SEO. However, performance is lacking which was anticipated. Due to the brand being in the light I deemed it to be worth it. The SVG-files are heavy, but sell the brand, sell the product.

## Unfixed Bugs

1. Through Ajax Code I was able to cause the quickview to gather the product details of my featured products on the index.html. However, sometimes, the footer loses its position(even though I've added code to constantly pushes it down no matter what) However, considering the model "freezes" whatever is behind it it manages to sneak up. I have no solution for it right now, but deemed the function to be cool enough to let it be there.
2. Between width 885 and width 767 the account-button and bag overlap. Sometimes my fix works, which was to override the bootstrap class of navbar-expand-md. However, sometimes it still happens and I caught it too late to look further into it. Easily fixed whenever the above mentioned css override will work.
3. An issue has occured with the confirmation email sent upon a successful payment. Every purchase goes through, however an issue remains where the confirmation email doesn't get sent. I chose to keep the functionality due to the fix is not far off.
