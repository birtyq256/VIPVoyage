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
> [An Internal Link](/file:///Users/lanakarout/Downloads/Ablauf_VIPVOYAGE.drawio.html)


[![](https://mermaid.ink/img/pako:eNrFVN1qgzAYfZWQ22mp1n_GYNAVel1hMISR1tQGNNqYlHWub7a7vdhSU4o_2cZgMG_Uc77zxXP8kgZuyhTDCG5yVNdzgjKGioQCebUIWNK9IOy4KFnRKByAG0I5IOn1dcUZoRmgqMBDrNqVdAQixsgB5UM4xRViXLCv6p85GS9wFfXZ8xeiohSUDwVrkWZ4hNYccVEr9KRu3RQ69jVsJ6P7ZtB5QXCe6qJRhC4fxehDUtw4qSXlOMPsItUZV5TWvaIY3gtc87rr73uz8T-Z1Sh1szGQ90v-PLBeVN2JAKb5dtdOEIjAA1tzcCgpeIzPSD0qj39XDm5Ns79aBOaIY1rIbZ3nYPvxzn4UxVoRNGCBWYFIKo-H9k8nkO-wzBBG8jHFWyRynsCEnmQpErxcHekGRpwJbEBRpbLj5UCB0RbltUQrRGHUwBcY2U44sQLPDn3Hdlzb9x0DHiXsTSzLcdxwZruWOw1c_2TA17KULaaTIPBmbhhY08AOLc_22n5PLXle9PQJ4ouIrA?type=png)](https://mermaid.live/edit#pako:eNrFVN1qgzAYfZWQ22mp1n_GYNAVel1hMISR1tQGNNqYlHWub7a7vdhSU4o_2cZgMG_Uc77zxXP8kgZuyhTDCG5yVNdzgjKGioQCebUIWNK9IOy4KFnRKByAG0I5IOn1dcUZoRmgqMBDrNqVdAQixsgB5UM4xRViXLCv6p85GS9wFfXZ8xeiohSUDwVrkWZ4hNYccVEr9KRu3RQ69jVsJ6P7ZtB5QXCe6qJRhC4fxehDUtw4qSXlOMPsItUZV5TWvaIY3gtc87rr73uz8T-Z1Sh1szGQ90v-PLBeVN2JAKb5dtdOEIjAA1tzcCgpeIzPSD0qj39XDm5Ns79aBOaIY1rIbZ3nYPvxzn4UxVoRNGCBWYFIKo-H9k8nkO-wzBBG8jHFWyRynsCEnmQpErxcHekGRpwJbEBRpbLj5UCB0RbltUQrRGHUwBcY2U44sQLPDn3Hdlzb9x0DHiXsTSzLcdxwZruWOw1c_2TA17KULaaTIPBmbhhY08AOLc_22n5PLXle9PQJ4ouIrA)


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

