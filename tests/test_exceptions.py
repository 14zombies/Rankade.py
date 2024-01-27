import unittest

from rankade import RankadeExceptions


class TestExceptions(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.default_message = "an error occured"
        cls.default_url = "https://example.com/"
        cls.default_verb = "GET"
        cls.default_status = 418
        cls.default_code = "A001"

    def test_rankadeexception(self):
        exception = RankadeExceptions.RankadeException(message=TestExceptions.default_message)
        self.assertEqual(exception.message, TestExceptions.default_message)

    def test_searchtooshort(self):
        exception = RankadeExceptions.SearchTooShort(search="aa")
        self.assertEqual(exception.message, "Search must be at least 2 characters (got 'aa').")

    def test_novalidcredentials(self):
        exception = RankadeExceptions.NoValidCredentials()
        self.assertEqual(exception.message, "No Credentials Supplied")

    def test_apierrorresponse(self):
        exception = RankadeExceptions.ApiErrorResponse(
            url=TestExceptions.default_url,
            verb=TestExceptions.default_verb,
            status=TestExceptions.default_status,
            code=TestExceptions.default_code,
            message=TestExceptions.default_message,
        )
        self.check_api_based_exception(exception)

    def test_authcredentials(self):
        exception = RankadeExceptions.AuthCredentials(
            url=TestExceptions.default_url,
            verb=TestExceptions.default_verb,
            status=TestExceptions.default_status,
            code=TestExceptions.default_code,
            message=TestExceptions.default_message,
        )
        self.check_api_based_exception(exception)

    def test_matchvalidation(self):
        exception = RankadeExceptions.MatchValidation(
            url=TestExceptions.default_url,
            verb=TestExceptions.default_verb,
            status=TestExceptions.default_status,
            code=TestExceptions.default_code,
            message=TestExceptions.default_message,
        )
        self.check_api_based_exception(exception)

    def test_quotas(self):
        exception = RankadeExceptions.Quotas(
            url=TestExceptions.default_url,
            verb=TestExceptions.default_verb,
            status=TestExceptions.default_status,
            code=TestExceptions.default_code,
            message=TestExceptions.default_message,
        )
        self.check_api_based_exception(exception)

    def check_api_based_exception(self, exception: RankadeExceptions.ApiErrorResponse):
        self.assertEqual(exception.message, TestExceptions.default_message)
        self.assertEqual(exception.url, TestExceptions.default_url)
        self.assertEqual(exception.verb, TestExceptions.default_verb)
        self.assertEqual(exception.status, TestExceptions.default_status)
        self.assertEqual(exception.code, TestExceptions.default_code)


if __name__ == "__main__":
    unittest.main()
