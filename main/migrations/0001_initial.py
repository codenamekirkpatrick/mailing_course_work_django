# Generated by Django 4.2.2 on 2024-08-24 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.CharField(max_length=250, verbose_name="Почта")),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=200, null=True, verbose_name="Фамилия"
                    ),
                ),
                (
                    "comment",
                    models.TextField(blank=True, null=True, verbose_name="Комментарий"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
                "ordering": ("email",),
            },
        ),
        migrations.CreateModel(
            name="Mailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "send_date",
                    models.CharField(
                        blank=True,
                        default="Дата не указана",
                        max_length=200,
                        null=True,
                        verbose_name="Дата отправки",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата создания рассылки"
                    ),
                ),
                (
                    "updated_at",
                    models.DateTimeField(
                        auto_now=True, verbose_name="Дата последнего изменения рассылки"
                    ),
                ),
                (
                    "interval",
                    models.CharField(
                        choices=[
                            ("once a day", "once a days"),
                            ("once a week", "once a week"),
                            ("once a month", "once a months"),
                        ],
                        default="once a week",
                        verbose_name="Интервал",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("completed", "completed"),
                            ("created", "created"),
                            ("started", "started"),
                        ],
                        default="created",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "email",
                    models.ManyToManyField(
                        related_name="emails", to="main.client", verbose_name="Почта"
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
                "ordering": ("interval",),
            },
        ),
        migrations.CreateModel(
            name="Message",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=200, verbose_name="Тема")),
                ("body", models.TextField(verbose_name="Содержание")),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
                "ordering": ("subject",),
            },
        ),
        migrations.CreateModel(
            name="TryMailing",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "last_try",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="Дата последней попытки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[("success", "success"), ("failure", "failure")],
                        default="success",
                        verbose_name="Статус",
                    ),
                ),
                (
                    "response",
                    models.TextField(blank=True, null=True, verbose_name="Ответ"),
                ),
                (
                    "mailing",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="emails",
                        to="main.mailing",
                        verbose_name="Рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка рассылки",
                "verbose_name_plural": "Попытки рассылок",
                "ordering": ("status",),
            },
        ),
        migrations.AddField(
            model_name="mailing",
            name="message",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="Сообщение",
                to="main.message",
                verbose_name="massage",
            ),
        ),
    ]