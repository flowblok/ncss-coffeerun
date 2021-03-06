# vim: set et nosi ai ts=2 sts=2 sw=2:
# coding: utf-8

import unittest

from coffeespecs import Coffee, get_all_tokens


class TestCoffeeValidation(unittest.TestCase):
  def test_minimal_spec(self):
    c = Coffee('')
    self.assertFalse(c.validate())
    self.assertTrue(c.add_spec('type', 'C'))
    self.assertTrue(c.validate())
    self.assertTrue(c.add_spec('size', 'l'))
    self.assertTrue(c.validate())

    # Still valid if we add more.
    self.assertTrue(c.add_spec('milk', 'soy'))


class TestParser(unittest.TestCase):
  def test_get_tokens(self):
    tokens = get_all_tokens()
    self.assertEqual('2 extra-shots', tokens[0])

  def test_parse(self):
    c = Coffee('Large Cap')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Large')

    c = Coffee('LC')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Large')

    c = Coffee('SC')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Small')

    c = Coffee('Large Cap 2 Sugars')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Large')
    self.assertEquals(c.specs['sugar'], '2 Sugars')

    c = Coffee('Small strong cap')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Small')
    self.assertEquals(c.specs['strength'], 'Extra-shot')

    c = Coffee('Small doubleshot cap')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Small')
    self.assertEquals(c.specs['strength'], 'Extra-shot')

    c = Coffee('Small Latte')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['size'], 'Small')

    c = Coffee('SL')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['size'], 'Small')

    c = Coffee('RegL')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['size'], 'Regular')

    c = Coffee('LL')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['size'], 'Large')

    c = Coffee('CL')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Large')

    c = Coffee('CL 2S')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Cappuccino')
    self.assertEquals(c.specs['size'], 'Large')
    self.assertEquals(c.specs['sugar'], '2 Sugars')

    c = Coffee('Large Iced Latte')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['size'], 'Large')
    self.assertEquals(c.specs['iced'], 'Iced')

    c = Coffee('Large Flat white')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Flat White')
    self.assertEquals(c.specs['size'], 'Large')

    c = Coffee('Large FW 3 Sugars')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Flat White')
    self.assertEquals(c.specs['size'], 'Large')
    self.assertEquals(c.specs['sugar'], '3 Sugars')

    c = Coffee('Regular Flat White')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Flat White')
    self.assertEquals(c.specs['size'], 'Regular')

    c = Coffee('Soy decaf latte with 2 sugars')
    self.assertTrue(c.validate())
    self.assertEquals(c.specs['type'], 'Latte')
    self.assertEquals(c.specs['sugar'], '2 Sugars')
    self.assertEquals(c.specs['decaf'], 'Decaf')
    self.assertEquals(c.specs['milk'], 'Soy')


class TestPrettyPrint(unittest.TestCase):

  def testPrint(self):
    c = Coffee('Large Cap')
    self.assertEquals('Large Cappuccino', str(c))

    c = Coffee('SC')
    self.assertEquals('Small Cappuccino', str(c))

    c = Coffee('Large Cap 2 Sugars')
    self.assertEquals('Large Cappuccino with 2 Sugars', str(c))

    c = Coffee('Small strong cap')
    self.assertEquals('Small Extra-shot Cappuccino', str(c))

    c = Coffee('Small Latte')
    self.assertEquals('Small Latte', str(c))

    c = Coffee('RegL')
    self.assertEquals('Regular Latte', str(c))

    c = Coffee('LL')
    self.assertEquals('Large Latte', str(c))

    c = Coffee('Large Iced Latte')
    self.assertEquals('Large Iced Latte', str(c))

    c = Coffee('Large Flat white')
    self.assertEquals('Large Flat White', str(c))

    c = Coffee('Large FW 3 Sugars')
    self.assertEquals('Large Flat White with 3 Sugars', str(c))

    c = Coffee('Regular Flat White')
    self.assertEquals('Regular Flat White', str(c))

    c = Coffee('Soy decaf latte with 2 sugars')
    self.assertEquals('Regular Soy Decaf Latte with 2 Sugars', str(c))
