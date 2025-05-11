from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp

class RegistrationForm(FlaskForm):
    fname = StringField(
        "First Name", validators=[DataRequired(), Length(min=2, max=25)]
    )
    lname = StringField("Last Name", validators=[DataRequired(), Length(min=2, max=25)])
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=25)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])

    role = SelectField('Register As', choices=[('Student', 'Student'), ('Instructor', 'Instructor')], validators=[DataRequired()])
    
    password = PasswordField(
        "Password",
        validators=[
            DataRequired(),
            Regexp(
               r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&#_])[A-Za-z\d@$!%*?&#_]{8,32}$"
            ),
        ],
    )
    confirm_password = PasswordField(
        "Confirm Password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign Up")

class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember Me?")
    submit = SubmitField("Login")

class contactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=25)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    message = TextAreaField('How can we help you?', validators=[DataRequired(), Length(min=5)])
    submit = SubmitField("Send Message")

class CourseForm(FlaskForm):
    title = StringField('عنوان الكورس', validators=[DataRequired()])
    description = TextAreaField('وصف الكورس', validators=[DataRequired()])
    category = SelectField('الفئة', choices=[('Programming', 'برمجة'), ('Design', 'تصميم'), ('Marketing', 'تسويق')], validators=[DataRequired()])
    price = StringField('السعر', validators=[DataRequired()])
    submit = SubmitField('إضافة')

class DeleteForm(FlaskForm):
    pass    

class EnrollmentForm(FlaskForm):
    submit = SubmitField('تأكيد التسجيل')