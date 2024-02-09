---
title: Data Model
parent: Technical Docs
nav_order: 3
---

{: .label }
Birte

# Data model
{: .no_toc }

<details open markdown="block">
{: .text-delta }
<summary>Table of contents</summary>
+ ToC
{: toc }
</details>

{: .download }
> Unter diesem Link befindet sich das Ablaufdiagram.
>file:///Users/lanakarout/Downloads/Ablauf_VIPVOYAGE.drawio.html



```mermaid
classDiagram
    class InquiryForm{
      +int id
      +String name
      +String phone
      +String arrival
      +String departure
      +String arrival_time
      +String departure_time
      +int amount
      +String budget
      +String status
    }
    
    class Form{
    }
    
    class InquiryFormA{
      +StringField name
      +StringField phone
      +StringField arrival
      +StringField departure
      +IntegerField amount
      +StringField budget
      +StringField requests
    
    }
    
    class InquiryFormT{
      +StringField name
      +StringField phone
      +StringField arrival
      +StringField departure
      +StringField arrival_time
      +StringField departure_time
      +IntegerField amount
      +StringField budget
      +StringField requests
    }
    
    InquiryFormA --|> Form : Erbt von WTForms
    InquiryFormT --|> Form : Erbt von WTForms
    InquiryForm <-- InquiryFormA : Datenmodell für
    InquiryForm <-- InquiryFormT : Datenmodell für
```

