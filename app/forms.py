from wtforms import Form, StringField, PasswordField,TextAreaField, validators

class RegistrationForm(Form):
    name = StringField('Name', [validators.Length(min=4, max=16), validators.DataRequired()])
    email = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=20), validators.DataRequired()])
    confirm = PasswordField('Confirm Password', [validators.DataRequired(), validators.EqualTo('password', message='Passwords are not a match')])

class LoginForm(Form):
    email = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired(), validators.Email()])
    password = PasswordField('Password', [validators.Length(min=6, max=20), validators.DataRequired()])

class AddEventForm(Form):
    name = StringField('Name', [validators.Length(min=6, max=32), validators.DataRequired()])
    category = PasswordField('Category', [validators.Length(min=6, max=20), validators.DataRequired()])
    location = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired()])
    date = StringField('Date', [validators.DataRequired()])
    description = TextAreaField ('Description', [validators.Length(min=6, max=300), validators.DataRequired()])

class EditEventForm(Form):
    name = StringField('Name', [validators.Length(min=6, max=32), validators.DataRequired()])
    category = PasswordField('Category', [validators.Length(min=6, max=20), validators.DataRequired()])
    location = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired()])
    date = StringField('Date', [validators.DataRequired()])
    description = TextAreaField ('Description', [validators.Length(min=6, max=300), validators.DataRequired()])

class DeleteEventForm(Form):
    name = StringField('Name', [validators.Length(min=6, max=32), validators.DataRequired()])
    location = StringField('Email', [validators.Length(min=6, max=32), validators.DataRequired()])
    description = TextAreaField ('Description', [validators.Length(min=6, max=300), validators.DataRequired()])
