---
title: Reference
parent: Technical Docs
nav_order: 4
---

{: .label }
Lana

# Reference documentation
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details> 

## Home Page

### `home()`

**Route:** `/`

**Methods:** `GET`

**Purpose:** Renders the home page of VIP Voyage.

**Sample output:**

![Home Page](../assets/images/Homepage.png)

---

## Login

### `login()`

**Route:** `/login`

**Methods:** `GET`, `POST`

**Purpose:** Renders the login page and processes login attempts. On successful login, redirects to the booking overview page. On failure, flashes an error message.

**Sample output:**

![Login Page](../assets/images/LoginPage.png)


---

## Inquiry Option

### `inquiry_option()`

**Route:** `/inquiryoption`

**Methods:** `GET`

**Purpose:** Renders the inquiry option page.

**Sample output:**

![Inquiry Option Page](../assets/images/InquiryOption.png)

---

## Inquiry Form (Accommodation)

### `inquiryform_a()`

**Route:** `/inquiryform-a`

**Methods:** `GET`

**Purpose:** Renders the inquiry form Accommodation.

**Sample output:** ![Accommodation Form](../assets/images/InquiryFormA.png)



---

## Inquiry Form (Transportation)

### `inquiryform_t()`

**Route:** `/inquiryform-t`

**Methods:** `GET`

**Purpose:** Renders the inquiry form Transportation.

**Sample output:**

---

## Overview

### `overview()`

- **Route:** `/overview`
- **Methods:** `GET`
- **Purpose:** Displays an overview of all inquiries submitted, available only to admin users after successful login.
- **Sample output:** ![Overview Page](../assets/images/OverviewPage.png)

---

## Update Status

### `update_status(inquiry_id)`

- **Route:** `/update_status/<int:inquiry_id>`
- **Methods:** `POST`
- **Purpose:** Allows the admin to update the status of an inquiry. Redirects to the overview page after the update.
- **Sample output:** ![ Update](../assets/images/Update.png)

---

## Delete Inquiry

### `delete_inquiry(inquiry_id)`

- **Route:** `/delete_inquiry/<int:inquiry_id>`
- **Methods:** `POST`
- **Purpose:** Allows the admin to delete an inquiry. Redirects to the overview page after deletion.
- **Sample output:** ![Delete Conf](../assets/images/DeleteModal.png)

---

## Thank You Page

### `thank_you()`

- **Route:** `/thank_you`
- **Methods:** `GET`
- **Purpose:** Displays a thank you message to users after submitting an inquiry.
- **Sample output:** ![Thank You Page](../assets/images/ThankYouPage.png)

---