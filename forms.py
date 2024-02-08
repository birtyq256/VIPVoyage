from wtforms import Form, StringField, IntegerField, validators



class InquiryFormA(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    phone = StringField('Phone Number', [validators.Length(min=1, max=20)])  
    arrival = StringField('Arrival', [validators.Length(min=1, max=100)])
    departure = StringField('Departure', [validators.Length(min=1, max=100)])
    amount = IntegerField('Amount of people', [validators.NumberRange(min=1)])
    budget = StringField('Budget', [validators.Length(min=1, max=100)])
    requests = StringField('Special Requests', [validators.Length(max=200)])

class InquiryFormT(Form):
    name = StringField('Name', [validators.Length(min=1, max=100)])
    phone = StringField('Phone Number', [validators.Length(min=1, max=20)])  
    arrival = StringField('Arrival', [validators.Length(min=1, max=100)])
    departure = StringField('Departure', [validators.Length(min=1, max=100)])
    arrival_time = StringField('Arrival Time', [validators.Length(min=1, max=100)])
    departure_time = StringField('Departure Time', [validators.Length(min=1, max=100)])
    amount = IntegerField('Amount of people', [validators.NumberRange(min=1)])
    budget = StringField('Budget', [validators.Length(min=1, max=100)])
    requests = StringField('Special Requests', [validators.Length(max=200)])
