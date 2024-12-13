# Юнит-тесты

import unittest
from domains_checker import is_valid_domain

class TestDomainValidation(unittest.TestCase): #
    def test_valid_domains(self):
        valid_domains = [
            "example.com",
            "sub-domain.example.org",
            "another-example.co.uk",
            "example123.biz"
        ]
        for domain in valid_domains:
            self.assertTrue(is_valid_domain(domain))

    def test_invalid_domains(self):
        invalid_domains = [
            "-example.com",
            "example-.com",
            "example..com",
            "example_123.com",
            "123.456.789.012",
            "example.c",
            "example@domain.com"
        ]
        for domain in invalid_domains:
            self.assertFalse(is_valid_domain(domain))