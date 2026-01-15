from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    ACCOUNT_TYPES = [
        ("student", "Student"),
        ("educator", "Educator"),
        ("researcher", "Researcher"),
    ]
    account_type = models.CharField(max_length=20, choices=ACCOUNT_TYPES, default="student")

    bio = models.TextField(blank=True, null=True)
    avatar_url = models.URLField(blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email


class UserInterest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="interests")
    interest_domain = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "interest_domain")

    def __str__(self):
        return f"{self.user.email} -> {self.interest_domain}"


class Item(models.Model):
    SOURCE_TYPES = [
        ("video", "Video"),
        ("news", "News"),
        ("article", "Article"),
        ("research_paper", "Research Paper"),
    ]

    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    source_url = models.URLField()
    thumbnail_url = models.URLField(blank=True, null=True)

    channel_or_source = models.CharField(max_length=255, blank=True, null=True)
    authors = models.CharField(max_length=255, blank=True, null=True)

    published_date = models.DateTimeField(blank=True, null=True)
    duration = models.IntegerField(blank=True, null=True)  # seconds for video

    view_count = models.IntegerField(default=0)
    like_count = models.IntegerField(default=0)
    save_count = models.IntegerField(default=0)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.source_type})"


class UserSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="searches")
    query = models.TextField()
    results_count = models.IntegerField(default=0)
    searched_at = models.DateTimeField(auto_now_add=True)


class UserView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="views")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="views")
    view_duration = models.IntegerField(default=0)
    viewed_at = models.DateTimeField(auto_now_add=True)


class UserLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="likes")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="liked_by")
    liked_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "item")


class UserSave(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="saves")
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="saved_by")
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "item")


class UserSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="settings")

    theme = models.CharField(max_length=10, default="auto")  # light/dark/auto
    notifications_enabled = models.BooleanField(default=True)
    notification_frequency = models.CharField(max_length=10, default="weekly")

    language = models.CharField(max_length=10, default="en")
    items_per_page = models.IntegerField(default=20)

    relevance_weight = models.FloatField(default=0.4)
    popularity_weight = models.FloatField(default=0.3)
    recency_weight = models.FloatField(default=0.3)

    updated_at = models.DateTimeField(auto_now=True)
