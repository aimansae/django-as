from django.test import TestCase
from forms import ItemForm


class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = Itemform({"name": " "})
        self.assertFalse(form_is_valid())
        self.assertIn('name', form.errors.keys)
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        form = Itemform({"name": "Test To do Items "})
        self.assertTrue(form_is_valid())

    def test_fields_is_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])
