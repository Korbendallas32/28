from faker import Faker

URL = 'https://b2c.passport.rt.ru'

PATH = "drivers/chromedriver"

valid_email = 'TEST_VALID_EMAIL'
valid_phone = 'TEST_VALID_PHONE (+79106174688)'
valid_password = 'TEST_VALID_PASSWORD'

fake = Faker()
fake_password = fake.password()