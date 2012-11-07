# -*- coding: utf-8

from django.test import TestCase
from django.db import IntegrityError
from datetime import datetime
from eventex.subscriptions.models import Subscription

class SubscriptionTest(TestCase):
  def setUp(self):
    self.obj = Subscription(
                  name='George Elias Ferreira da Silva',
                  cpf='12345678901',
                  email='mine@email.com',
                  phone='00-123456789'
                )

  def test_create(self):
    'Subscription must have name, cpf, email, phone.'
    self.obj.save()
    self.assertEqual(1, self.obj.id)

  def test_has_created_at(self):
    'Subscription must have automatic created_at.'
    self.obj.save()
    self.assertIsInstance(self.obj.created_at, datetime)

  def test_unide(self):
    self.assertEqual(u'George Elias Ferreira da Silva', unicode(self.obj))

class SubscriptionUniqueTest(TestCase):
  def setUp(self):
    # Create a first entry to force the colision
    Subscription.objects.create(
                  name='George Elias Ferreira da Silva',
                  cpf='12345678901',
                  email='mine@email.com',
                  phone='00-123456789'
                )

  def test_cpf_unique(self):
    'CPF must be unique.'
    s = Subscription(name='George Elias Ferreira da Silva', cpf='12345678901',
                      email='another@email.com', phone='00-123456789')
    self.assertRaises(IntegrityError, s.save)

  def test_email_unique(self):
    'Email must be unique.'
    s = Subscription(name='George Elias Ferreira da Silva', cpf='10987654321',
                      email='mine@email.com', phone='00-123456789')
    self.assertRaises(IntegrityError,s.save)
    