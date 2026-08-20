# SauceDemo – Test Plan

## 1. Scope

The purpose of this testing is to check the main user flows of the SauceDemo e-commerce website.

The main areas covered are:

- Login and authentication
- Product browsing
- Product details
- Product sorting
- Add to Cart
- Shopping Cart
- Checkout
- Order completion
- Logout
- Negative and edge-case testing
- Testing different provided user accounts
- Performance observations

The testing also includes exploratory testing to identify unexpected behaviour that may not be found through normal functional testing.

---

# 2. Types of Testing

## 2.1 Functional Testing

Functional testing was performed to check whether the main features of the application work as expected.

The following were tested:
- Valid login
- Invalid/empty login
- Locked-out user login
- Product browsing
- Product details
- Product sorting
- Add to Cart
- Remove from Cart
- Checkout
- Order completion
- Logout

## 2.2 UI Testing

UI testing was performed to check the visibility and usability of important interface elements.

The following were checked:
- Username and password fields
- Login button
- Product names
- Product descriptions
- Product prices
- Product images
- Add to Cart buttons
- Sorting dropdown
- Cart icon
- Checkout fields
- Checkout buttons
- Navigation elements

## 2.3 Negative Testing

Negative testing was performed by entering invalid, empty, or unexpected data.

Examples include:
- Empty username
- Empty password
- Empty first name
- Empty last name
- Empty postal code
- Numbers in name fields
- Letters in postal code
- Special characters
- Very long input
- Single-character input
- Whitespace-only input

## 2.4 Edge Case Testing

Edge cases were tested using unusual input and actions.

Examples include:
- Extremely long first name
- Extremely long last name
- Extremely long postal code
- Special characters
- Single-character input
- Repeated add/remove actions
- Page refresh
- Back navigation
- Different user accounts
- Repeatedly opening product details

## 2.5 Cross-Browser Considerations

The actual testing for this assignment was performed using Google Chrome.
Firefox and Microsoft Edge were not tested during this test cycle.

For broader regression testing, the main workflows should also be tested on:
- Google Chrome
- Mozilla Firefox
- Microsoft Edge

This can help identify browser-specific functional or UI issues.

---

# 3. Test Environment

- Operating System: Windows 11
- Device: Dell Latitude 7420
- Browser: Google Chrome
- Browser Version: 151.0.7922.138
- Website: SauceDemo
- URL: https://www.saucedemo.com

The manual exploratory testing described in this document was performed using Windows 11 and Google Chrome.
No separate testing was performed on Firefox, Edge, Safari, mobile, or tablet devices.

---

# 4. Test Data

## Provided User Accounts

| Username | Purpose |
|---|---|
| `standard_user` | Normal application behaviour |
| `locked_out_user` | Locked account behaviour |
| `problem_user` | Intentional functional and UI issues |
| `performance_glitch_user` | Performance-related behaviour |

Password for the provided accounts: `secret_sauce`

## Negative Test Data

| Input Type | Example |
|---|---|
| Extremely long first name | Alexanderthegreatalexanderthegreatalexanderthegreat |
| Extremely long last name | Smithsmithsmithsmithsmithsmithsmithsmithsmithsmith |
| Extremely long postal code | 123456789012345678901234567890 |
| Special characters | @#$%^&*()! |
| Whitespace | Spaces only |
| Single character | A |
| Numeric value in name field | 1 |
| Alphabetic value in postal code | Letters |

---

# 5. Test Cases

## TC 1 — Valid Login
**Objective:** Verify that a valid user can successfully log in.
**Preconditions:** User is on the SauceDemo login page.
**Test Data:**
- Username: `standard_user`
- Password: `secret_sauce`

**Steps:**
1. Open SauceDemo.
2. Enter `standard_user`.
3. Enter `secret_sauce`.
4. Click Login.

**Expected Result:** The user should be successfully logged in and taken to the Products page.
**Actual Result:** The user was successfully logged in and the Products page was displayed.
**Status:** PASS

## TC 2 — Locked-Out User Login
**Objective:** Verify that a locked-out user cannot log in.
**Test Data:**
- Username: `locked_out_user`
- Password: `secret_sauce`

**Steps:**
1. Enter `locked_out_user`.
2. Enter `secret_sauce`.
3. Click Login.

**Expected Result:** The user should not be allowed to log in and an appropriate error should be displayed.
**Actual Result:** An error message indicating that the user has been locked out was displayed.
**Status:** PASS

## TC 3 — Product Browsing
**Objective:** Verify that products and their information are displayed correctly.
**Preconditions:** User is logged in as `standard_user`.

**Steps:**
1. Open the Products page.
2. Check product names.
3. Check descriptions.
4. Check prices.
5. Check images.
6. Check Add to Cart buttons.
7. Test the sorting dropdown.

**Expected Result:** Products should display the correct information and sorting should work when an option is selected.
**Actual Result:** Product names, descriptions, prices, images and Add to Cart buttons were displayed. Sorting was tested.
**Status:** PASS

## TC 4 — Product Details
**Objective:** Verify that clicking a product opens the corresponding product details.
**Preconditions:** User is logged in as `standard_user`.

**Steps:**
1. Open the Products page.
2. Select a product.
3. Observe the product details.
4. Compare the product information with the product card.
5. Navigate back.

**Expected Result:** The selected product's corresponding details should be displayed.
**Actual Result:** The product details were displayed. Back navigation worked, although returning to the Products page moved the page to the top.
**Status:** PASS

## TC 5 — Add and Remove Product from Cart
**Objective:** Verify that products can be added to and removed from the cart.

**Steps:**
1. Open the Products page.
2. Select a product.
3. Click Add to Cart.
4. Open the Cart.
5. Verify the product.
6. Remove the product.
7. Verify the cart.

**Expected Result:** The product should be added to the cart and should be removable.
**Actual Result:** Products could be added and removed during standard-user testing.
**Status:** PASS

## TC 6 — Complete Checkout
**Objective:** Verify that a user can successfully complete an order.

**Steps:**
1. Add a product to the cart.
2. Open the Cart.
3. Click Checkout.
4. Enter first name.
5. Enter last name.
6. Enter postal code.
7. Click Continue.
8. Review the order.
9. Click Finish.

**Expected Result:** The order should be completed successfully.
**Actual Result:** The prices, tax, total cost and order details were displayed correctly. The order was completed and the cart became empty.
**Status:** PASS

## TC 7 — Required Checkout Fields
**Objective:** Verify that required checkout fields are validated.
**Preconditions:** User is logged in as `standard_user`.

**Steps:**
1. Leave First Name empty.
2. Click Continue.
3. Leave Last Name empty.
4. Click Continue.
5. Leave Postal Code empty.
6. Click Continue.
7. Leave all fields empty.
8. Click Continue.

**Expected Result:** Appropriate required-field validation messages should appear.
**Actual Result:** Required-field error messages were displayed.
**Status:** PASS

## TC 8 — Unusual Checkout Input
**Objective:** Check how checkout fields handle unusual input.

**Test Data:**
- Extremely long first name
- Extremely long last name
- Extremely long postal code
- Special characters
- Single-character values
- Numbers in name fields
- Letters in postal code

**Steps:**
1. Enter the test value.
2. Complete the remaining fields.
3. Click Continue.
4. Observe the result.

**Expected Result:** The fields should apply appropriate validation for the expected type and reasonable length of information.
**Actual Result:** The tested unusual inputs were accepted and the application allowed the user to continue. Whitespace-only input was tested separately and was not accepted.
**Status:** FAIL

## TC 9 — Problem User Testing
**Objective:** Compare the behaviour of `problem_user` with normal user behaviour.

**Steps:**
1. Log in as `problem_user`.
2. Check product images.
3. Open different products.
4. Test sorting.
5. Test Add to Cart.
6. Open the Cart.
7. Test checkout.

**Expected Result:** Product information, navigation, sorting, cart and checkout should work normally.
**Actual Result:** Several functional and UI issues were observed.
**Status:** FAIL

**Related Bugs:**
- BUG-01
- BUG-02
- BUG-03
- BUG-04

## TC 10 — Performance Glitch User
**Objective:** Observe where performance delays occur for `performance_glitch_user`.

**Steps:**
1. Log in.
2. Navigate between products.
3. Test sorting.
4. Use Continue Shopping.
5. Continue through checkout.
6. Navigate back home.
7. Log out.

**Expected Result:** The application should respond within a reasonable and consistent time.
**Actual Result:** Delays were observed during login, product navigation, sorting, Continue Shopping, navigation after checkout, and logout.
**Status:** PERFORMANCE OBSERVATION

---

# 6. Risk Assessment

| Area | Risk | Reason |
|---|---|---|
| Authentication | High | Login problems can prevent users from accessing the application. |
| Product information | High | Incorrect information or images can mislead customers. |
| Product navigation | High | Opening the wrong product can lead to incorrect product selection. |
| Product sorting | Medium | Users may have difficulty finding products efficiently. |
| Cart functionality | High | Products that cannot be added cannot be purchased. |
| Checkout validation | Medium | Invalid information may enter the order flow. |
| Price calculation | High | Incorrect prices or totals directly affect purchases. |
| Order completion | High | Failure can prevent customers from completing purchases. |
| Performance | Medium | Delays can negatively affect the user experience. |
| UI/navigation | Low–Medium | Poor visibility or navigation can make the application harder to use. |

---

# 7. Exit Criteria

Testing is considered complete when:
- Login workflows have been tested.
- Product browsing has been tested.
- Cart functionality has been tested.
- Checkout has been tested.
- Negative and edge cases have been explored.
- Provided user accounts have been tested where applicable.
- At least five distinct bugs have been documented.
- Evidence has been captured.
- Required automation tests have been implemented and executed.

---

# 8. Test Summary

- The testing covered the main SauceDemo shopping workflow from login through order completion.
- Exploratory testing was also performed using the provided user accounts, especially `problem_user` and `performance_glitch_user`.
- Five distinct bugs were selected based on reproducibility and potential user impact:
  1. Incorrect product images for `problem_user`
  2. Product sorting does not work for `problem_user`
  3. Product links open incorrect product details
  4. Sauce Labs Fleece Jacket cannot be added to the cart
  5. Checkout fields accept unusually long and unexpected input without apparent validation
- The manual testing was performed on Windows 11 using Google Chrome.
- Cross-browser testing was considered but was not performed during this test cycle.