import unittest, os
from app import run

def test_atbash():
    assert run.atbash('Hello') == 'Svool'
