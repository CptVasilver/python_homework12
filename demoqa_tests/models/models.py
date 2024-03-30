from selene import browser, be, have, command

from demoqa_tests.models.data import User
from tests import conftest


class RegistrationPage:

    def open(self):
        browser.open('/automation-practice-form')

    def fill_first_name(self, value):
        browser.element('#firstName').should(be.blank).type(value)

    def fill_second_name(self, second_name):
        browser.element('#lastName').should(be.blank).type(second_name)

    def fill_email(self, email):
        browser.element('#userEmail').should(be.blank).type(email)

    def choose_gender(self, gender):
        browser.all('[name=gender]').element_by(have.value_containing(gender)).with_(click_by_js=True).click()

    def fill_phone_number(self, phone_number):
        browser.element('#userNumber').should(be.blank).type(phone_number)

    def fill_date_of_birth(self, year, month, day):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type(month)
        browser.element('.react-datepicker__year-select').type(year)
        browser.element(f'.react-datepicker__day--0{day}').click()

    def fill_subjects(self, subject):
        browser.element('#subjectsInput').type(subject).press_enter()

    def fill_hobbies(self, hobbies):
        for hobby in hobbies:
            browser.all('.custom-checkbox').element_by(have.exact_text(hobby)).click()

    def upload_picture(self, pic):
        browser.element('#uploadPicture').type(conftest.path(pic))

    def fill_address(self, address):
        browser.element('#currentAddress').should(be.blank).type(address)

    def fill_state(self, state):
        browser.element('#react-select-3-input').should(be.blank).type(state).press_enter()

    def fill_city(self, city):
        browser.element('#react-select-4-input').should(be.blank).type(city).press_enter()

    def submit(self, value):
        browser.element(f'#{value}').click()

    def scroll(self, tag):
        browser.element(f'#{tag}').perform(command.js.scroll_into_view)

    def assert_user_data(self, full_name, email, gender,
                         phone_number, birthday, subjects, hobbies,
                         picture, address, state_city):
        hobbiess = ''
        for hobby in hobbies:
            if hobbiess == '':
                hobbiess += hobby
            else:
                hobbiess += ', ' + hobby
        browser.all('.table').all('td').even.should(
            have.exact_texts(
                full_name,
                email,
                gender,
                str(phone_number),
                birthday,
                subjects,
                hobbiess,
                picture,
                address,
                state_city))

    def assert_filled_table(self):
        browser.element('.modal-header').should(have.text('Thanks for submitting the form'))

    def register(self, user: User):
        self.fill_first_name(user.first_name)
        self.fill_second_name(user.second_name)
        self.fill_email(user.email)
        self.choose_gender(user.gender)
        self.fill_phone_number(user.phone_number)
        self.fill_date_of_birth(user.year_of_birth, user.month_of_birth, user.day_of_birth)
        self.fill_subjects(user.subjects)
        self.fill_hobbies(user.hobbies)
        self.upload_picture(user.picture)
        self.fill_address(user.address)
        self.fill_state(user.state)
        self.fill_city(user.city)

    def should_have_registered(self, user: User):
        self.scroll('submit')
        self.submit('submit')
        self.assert_filled_table()
        self.assert_user_data(
            f'{user.first_name} {user.second_name}',
            user.email,
            user.gender,
            user.phone_number,
            f'{user.day_of_birth} {user.month_of_birth},{user.year_of_birth}',
            user.subjects,
            user.hobbies,
            user.picture,
            user.address,
            f'{user.state} {user.city}')
        self.scroll('closeLargeModal')
        self.submit('closeLargeModal')