from django.contrib.auth import get_user_model
from django.test import TestCase

from open.core.betterself.constants import (
    BetterSelfResourceConstants,
    BetterSelfTestContants as CONSTANTS,
)
from open.core.betterself.factories import (
    SupplementFactory,
    IngredientCompositionFactory,
)
from open.core.betterself.models.supplement import Supplement
from open.core.betterself.tests.mixins.resource_mixin import (
    BetterSelfResourceViewTestCaseMixin,
    DeleteTestsMixin,
)
from open.core.betterself.utilities.serializer_utilties import iterable_to_uuids_list

User = get_user_model()

"""
python manage.py test --pattern="*test_supplement_views.py" --keepdb
"""


class TestSupplementsView(BetterSelfResourceViewTestCaseMixin, TestCase):
    url_name = BetterSelfResourceConstants.SUPPLEMENTS
    model_class_factory = SupplementFactory
    model_class = Supplement

    def test_create_view(self):
        post_data = {"name": CONSTANTS.NAME_1, "notes": CONSTANTS.NOTES_1}

        response = self.client_1.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200, response.data)

        data = response.data

        self.assertEqual(data["name"], CONSTANTS.NAME_1)
        self.assertEqual(data["notes"], CONSTANTS.NOTES_1)

    def test_create_view_with_ingredient_compositions(self):
        ind_comps = IngredientCompositionFactory.create_batch(3, user=self.user_1)
        ingredient_composition_uuids = iterable_to_uuids_list(ind_comps)

        post_data = {
            "name": CONSTANTS.NOTES_1,
            "notes": CONSTANTS.NOTES_1,
            "ingredient_composition_uuids": ingredient_composition_uuids,
        }

        response = self.client_1.post(self.url, data=post_data)
        self.assertEqual(response.status_code, 200, response.data)

    def test_create_view_with_conflicting_ingredient_compositions(self):
        post_data = {
            "name": CONSTANTS.NOTES_1,
            "notes": CONSTANTS.NOTES_1,
            "ingredient_composition_uuids": [CONSTANTS.INVALID_UUID],
        }

        response = self.client_1.post(self.url, data=post_data)

        # error out and say the reason is
        self.assertEqual(response.status_code, 400, response.data)
        self.assertIn("ingredient_composition_uuids", response.data)


class TestSupplementGetUpdateDelete(
    BetterSelfResourceViewTestCaseMixin, DeleteTestsMixin, TestCase
):
    url_name = BetterSelfResourceConstants.SUPPLEMENTS
    model_class_factory = SupplementFactory
    model_class = Supplement

    def test_get_singular_resource(self):
        instance = self.model_class_factory(user=self.user_1)
        url = instance.get_update_url()

        response = self.client_1.get(url)
        self.assertEqual(response.status_code, 200, response.data)
        data = response.data

        for key, value in data.items():
            instance_value = getattr(instance, key)
            if isinstance(instance_value, (str, bool)):
                # if the field stored on the db level is the right noe
                self.assertEqual(instance_value, value)
