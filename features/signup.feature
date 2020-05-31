Feature: Sign Up

   Feature Description
   Scenario: Sign Up Test
    When I go to the link "http://127.0.0.1:5006/auth/register"
    Then there title should be "Document"
    When I write "idris2@gmail.com", "idris2", "12345678", "12345678" to the inputs and click the button
    Then I redirect to the link "http://127.0.0.1:5006/auth/login"
    
    # Scenario: Sign in test
    # When I go to the login page link "http://127.0.0.1:5006/auth/login"
    # Then there title should be "Document"
    # When I write "idris2@gmail.com", "12345678", to the inputs and click the button
    # Then I redirect to the link "http://127.0.0.1:5006"
    # Then there should be "Welcome idris2 !!!!" text in page