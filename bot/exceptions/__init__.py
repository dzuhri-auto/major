from aiohttp.client_exceptions import ClientResponseError


class InvalidSession(BaseException): ...


class CustomClientResponseError(ClientResponseError):
    def __str__(self) -> str:
        return "{}, message={!r}".format(
            self.status,
            self.message,
        )


class MissingLicenseKeyException(BaseException):
    pass


class InvalidLicenseKeyException(BaseException):
    pass


class ExpiredLicenseKeyException(BaseException):
    pass


class APIErrorException(BaseException):
    pass
