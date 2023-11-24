from abc import abstractmethod
from typing import Protocol, cast

from django.contrib.auth.models import AnonymousUser
from django.http import HttpRequest

from authuser.models import User

class PUserService(Protocol):
    @abstractmethod
    def get_current_user(self, request: HttpRequest) -> User:
        raise NotImplementedError

    @abstractmethod
    def create_user(self, email: str, password: str) -> User:
        raise NotImplementedError


class UserService(PUserService):
    def get_current_user(self, request: HttpRequest) -> User:
        if not request.user or isinstance(request.user, AnonymousUser):
            raise ValueError('Request is not authenticated')

        return cast(User, request.user)

    def create_user(self, email: str, password: str) -> User:
        return User.objects.create_user(email=email, password=password)
