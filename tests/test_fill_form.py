from demoqa_tests.models.data import User
from demoqa_tests.models.models import RegistrationPage
import allure

@allure.story('Filling registration form')
def test_fill():
    registration_page = RegistrationPage()

    user = User(first_name='Yashaka', second_name='Selenium', email='Examplum@mulpmaxe.com',
                gender='Male', phone_number=8005553535, day_of_birth=19,
                month_of_birth='November', year_of_birth=1900,
                subjects='Maths', hobbies=['Reading', 'Music'], picture='pic.png',
                address='Colorado-Springs', state='NCR', city='Noida')
    with allure.step('Open registration form'):
        registration_page.open()
    with allure.step('Fill registration form with user data'):
        registration_page.register(user)
    with allure.step('Check for correct filling'):
        registration_page.should_have_registered(user)
