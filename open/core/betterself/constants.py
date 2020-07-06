from open.utilities.fields import create_django_choice_tuple_from_list


class BetterSelfResourceConstants:
    """
    RESTful constants used in URLs, useful for URL lookups
    """

    MEASUREMENTS = "measurements"
    INGREDIENTS = "ingredients"
    INGREDIENT_COMPOSITIONS = "ingredient_compositions"
    SUPPLEMENTS = "supplements"
    # note - changed the plural of this, before it was called supplements_stacks and that felt stupid
    SUPPLEMENT_STACKS = "supplement_stacks"
    SUPPLEMENT_STACK_COMPOSITIONS = "supplement_stack_compositions"
    SUPPLEMENT_LOGS = "supplement_logs"
    DAILY_PRODUCTIVITY_LOGS = "productivity_logs"
    SLEEP_LOGS = "sleep_logs"
    ACTIVITIES = "activities"
    ACTIVITY_LOGS = "activity_logs"
    WELL_BEING_LOG = "well_being_logs"


WEB_INPUT_SOURCE = "web"
TEXT_MSG_SOURCE = "text_message"
BETTERSELF_LOG_INPUT_SOURCES = [
    "api",
    "ios",
    "android",
    "mobile",
    WEB_INPUT_SOURCE,
    "user_excel",
    TEXT_MSG_SOURCE,
]

INPUT_SOURCES_TUPLES = create_django_choice_tuple_from_list(
    BETTERSELF_LOG_INPUT_SOURCES
)
