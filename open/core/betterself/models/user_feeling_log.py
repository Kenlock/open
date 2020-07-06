from django.db.models import (
    CharField,
    TextField,
    DateTimeField,
    PositiveSmallIntegerField,
)

from open.core.betterself.constants import INPUT_SOURCES_TUPLES, WEB_INPUT_SOURCE
from open.utilities.date_and_time import get_utc_now
from open.utilities.models import BaseModelWithUserGeneratedContent


class WellBeingLog(BaseModelWithUserGeneratedContent):
    """
    Meant to capture both physical and mental well-being

    IE. Someone could be happy and tired, or sad and strong(?) less-likely

    Capture enough data to be helpful to diagnose chronic
    """

    time = DateTimeField(default=get_utc_now)

    # differentiate between feeling how a person may feel mentally versus physically
    # do as a score of 1-10
    mental_value = PositiveSmallIntegerField()
    physical_value = PositiveSmallIntegerField()

    source = CharField(
        max_length=50, choices=INPUT_SOURCES_TUPLES, default=WEB_INPUT_SOURCE
    )
    notes = TextField(default="")

    class Meta:
        unique_together = ("user", "time")
        ordering = ["user", "-time"]
        verbose_name = "Mood Log"
        verbose_name_plural = "Mood Logs"

    def __str__(self):
        return "User - {}, Mood - {} at {}".format(self.user, self.value, self.time)
