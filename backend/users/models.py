from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models
from django.db.models import F, Q, UniqueConstraint


class User(AbstractUser):
    """Модель пользователя."""
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username', 'first_name', 'last_name')

    first_name = models.CharField(
        verbose_name='Имя',
        max_length=settings.LENGTH_OF_FIELDS_USER_1
    )
    last_name = models.CharField(
        max_length=settings.LENGTH_OF_FIELDS_USER_1,
        verbose_name='Фамилия',
    )
    email = models.EmailField(
        max_length=settings.LENGTH_OF_FIELDS_USER_1,
        verbose_name='email',
        unique=True
    )
    username = models.CharField(
        verbose_name='username',
        max_length=settings.LENGTH_OF_FIELDS_USER_2,
        unique=True,
        validators=(UnicodeUsernameValidator(), )
    )

    class Meta:
        ordering = ('username', )
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        constraints = (
            UniqueConstraint(
                fields=('username', 'email'),
                name='unique_username_email'
            ),
        )

    def __str__(self):
        return self.username


class Follow(models.Model):
    """Модель подписки на автора."""
    user = models.ForeignKey(
        User,
        verbose_name='Пользователь',
        on_delete=models.CASCADE,
        related_name='follower'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='following'
    )

    class Meta:
        ordering = ('-id',)
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        constraints = (
            UniqueConstraint(
                fields=('user', 'author'),
                name='unique_subscription'
            ),
            models.CheckConstraint(
                check=~Q(user=F('author')),
                name='no_self_follow'
            )
        )

    def __str__(self) -> str:
        return f'{self.user} подписан на {self.author}'
