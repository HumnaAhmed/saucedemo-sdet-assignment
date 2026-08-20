# SauceDemo – Bug Reports

## Test Environment

- OS: Windows 11
- Device: Dell Latitude 7420
- Browser: Google Chrome
- Browser Version: 151.0.7922.138
- Website: SauceDemo
- URL: https://www.saucedemo.com

---

# BUG 1 — Incorrect Product Images for `problem_user`

## Severity

Medium

## Priority

High

## Environment

- OS: Windows 11
- Browser: Google Chrome
- User: `problem_user`

## Preconditions

User is logged in using `problem_user` and is on the Products page.

## Steps to Reproduce

1. Open SauceDemo.
2. Log in using `problem_user` and `secret_sauce`.
3. Open the Products page.
4. Observe the product images displayed on the product cards.

## Expected Result

Each product should display its corresponding product image.

## Actual Result

Multiple product cards display the same dog image instead of their corresponding product images.

## Impact

Incorrect product images can make it difficult for customers to identify products correctly and may reduce trust in the product catalogue.

## Evidence

Demonstrated in Video 2 Manual Bug Discovery Demo.

## Notes

This issue was reproduced while testing the `problem_user` account.

# BUG 2 — Product Sorting Does Not Work for `problem_user`

## Severity

Medium

## Priority

Medium

## Environment

- OS: Windows 11
- Browser: Google Chrome
- User: `problem_user`

## Preconditions

User is logged in using `problem_user` and is on the Products page.

## Steps to Reproduce

1. Log in using `problem_user` and `secret_sauce`.
2. Open the Products page.
3. Open the sorting dropdown.
4. Try to select a different sorting option.
5. Observe the sorting dropdown and the product order.

## Expected Result

The selected sorting option should be applied and the products should be reordered accordingly.

## Actual Result

The sorting option does not get applied when selected, and the product list remains in the default order.

## Impact

Users cannot use the available sorting options to arrange products by name or price, which makes it harder to find products efficiently.

## Evidence

Demonstrated in Video 2 Manual Bug Discovery Demo.

## Notes

The sorting functionality was re-tested with different sorting options, but the options did not work and the product order remained unchanged.

# BUG 3 — Product Link Opens Incorrect Product Details

## Severity

High

## Priority

High

## Environment

- OS: Windows 11
- Browser: Google Chrome
- User: `problem_user`

## Preconditions

User is logged in using `problem_user` and is on the Products page.

## Steps to Reproduce

1. Log in using `problem_user` and `secret_sauce`.
2. Open the Products page.
3. Locate "Sauce Labs Backpack".
4. Click on the "Sauce Labs Backpack" product.
5. Observe the product details page.

## Expected Result

The Sauce Labs Backpack product details should open.

## Actual Result

The Sauce Labs Fleece Jacket product details open instead.

## Impact

Opening the details of a different product can mislead customers and may result in them viewing or attempting to purchase the wrong product.

## Evidence

Demonstrated in Video 2 Manual Bug Discovery Demo.

## Reproducibility

The Backpack product was clicked multiple times, and the Fleece Jacket product details opened each time.

# BUG 4 — Sauce Labs Fleece Jacket Cannot Be Added to Cart

## Severity

High

## Priority

High

## Environment

- OS: Windows 11
- Browser: Google Chrome
- User: `problem_user`

## Preconditions

User is logged in using `problem_user` and is on the Products page.

## Steps to Reproduce

1. Log in using `problem_user` and `secret_sauce`.
2. Open the Products page.
3. Locate "Sauce Labs Fleece Jacket".
4. Click the "Add to Cart" button.
5. Open the shopping cart.
6. Check whether the Fleece Jacket has been added.

## Expected Result

The Sauce Labs Fleece Jacket should be added to the cart and should appear in the cart.

## Actual Result

The Fleece Jacket is not added to the cart.

## Impact

Customers cannot add the affected product to the cart and therefore cannot purchase it through the normal shopping flow.

## Evidence

Demonstrated in Video 2 Manual Bug Discovery Demo.

## Reproducibility

The Add to Cart action was re-tested for the Fleece Jacket, but the product still did not appear in the cart.

# BUG 5 — Checkout Fields Accept Unusually Long and Unexpected Input

## Severity

Medium

## Priority

Medium

## Environment

- OS: Windows 11
- Browser: Google Chrome
- User: `standard_user`

## Preconditions

User is logged in as `standard_user` and has reached the checkout information page.

## Steps to Reproduce

1. Log in using `standard_user` and `secret_sauce`.
2. Add a product to the cart.
3. Open the cart.
4. Proceed to checkout.
5. Enter an extremely long value in the First Name field.
6. Enter an extremely long value in the Last Name field.
7. Enter an extremely long value in the Postal Code field.
8. Repeat the test using special characters.
9. Repeat the test using a single-character value.
10. Click Continue.

## Test Data

### Extremely long first name

`Alexanderthegreatalexanderthegreatalexanderthegreat`

### Extremely long last name

`Smithsmithsmithsmithsmithsmithsmithsmithsmithsmith`

### Extremely long postal code

`123456789012345678901234567890`

### Special characters

`@#$%^&*()!`

### Single character

`A`

## Expected Result

The checkout fields should apply appropriate validation and reasonable length constraints for the type of information expected in each field. Clearly inappropriate input should not be accepted without validation.

## Actual Result

The checkout form accepted the tested extremely long values, special-character input, and single-character values and allowed the user to continue to the next checkout step. No apparent format or length validation was applied to these tested inputs.

## Impact

Accepting unusually long or unexpected customer information may result in invalid or inconsistent order data and can create data-quality issues.

## Evidence

Demonstrated in Video 2 Manual Bug Discovery Demo.

## Notes

Whitespace-only input was also tested, but it was not accepted. Therefore, whitespace-only input is not included as part of this bug.