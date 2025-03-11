from selene import browser, have, be, command


def test_submit_practice_form_by_using_send_keys():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').send_keys('Sponge')
    browser.element('#lastName').send_keys('Bob')
    browser.element('#userEmail').send_keys('sponge.bob@bbottom.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').send_keys('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1986"]').click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').send_keys('Biology').press_enter()

    browser.all('.custom-control-label').element_by(have.text('Sports')).click()

    browser.element('#currentAddress').type('24 Conch Street, Bikini Bottom, Marshall Islands 96970')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click().element('div[id^="react-select-3-option"]').click()
    browser.element('#city').click().element('div[id^="react-select-4-option"]').click()

    browser.element('#submit').press_enter()

    browser.element('.modal-content').should(be.visible)
    browser.element('.table').should(have.text('Sponge Bob'))
    browser.element('.table').should(have.text('sponge.bob@bbottom.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('1234567890'))
    browser.element('.table').should(have.text('15 July,1986'))
    browser.element('.table').should(have.text('Biology'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('24 Conch Street, Bikini Bottom, Marshall Islands 96970'))
    browser.element('.table').should(have.text('NCR Delhi'))

def test_submit_practice_form_by_using_type():
    browser.open('https://demoqa.com/automation-practice-form')

    browser.element('#firstName').type('Sponge')
    browser.element('#lastName').type('Bob')
    browser.element('#userEmail').type('sponge.bob@bbottom.com')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('#userNumber').type('1234567890')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="6"]').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1986"]').click()
    browser.element('.react-datepicker__day--015').click()

    browser.element('#subjectsInput').type('Biology').press_enter()

    browser.all('.custom-control-label').element_by(have.text('Sports')).click()

    browser.element('#currentAddress').type('24 Conch Street, Bikini Bottom, Marshall Islands 96970')

    browser.element('#state').perform(command.js.scroll_into_view)
    browser.element('#state').click().element('div[id^="react-select-3-option"]').click()
    browser.element('#city').click().element('div[id^="react-select-4-option"]').click()

    browser.element('#submit').press_enter()

    browser.element('.modal-content').should(be.visible)
    browser.element('.table').should(have.text('Sponge Bob'))
    browser.element('.table').should(have.text('sponge.bob@bbottom.com'))
    browser.element('.table').should(have.text('Male'))
    browser.element('.table').should(have.text('1234567890'))
    browser.element('.table').should(have.text('15 July,1986'))
    browser.element('.table').should(have.text('Biology'))
    browser.element('.table').should(have.text('Sports'))
    browser.element('.table').should(have.text('24 Conch Street, Bikini Bottom, Marshall Islands 96970'))
    browser.element('.table').should(have.text('NCR Delhi'))

