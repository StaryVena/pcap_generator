import unittest
from http_client import HttpClient


class HttpClientTest(unittest.TestCase):

    def test_link_checker(self):
        valid_urls = ['http://domain.com',
                      'http://example.com/path/to/page?name=ferret&color=purple',
                      'https://docs.python.org/2/library/unittest.html',
                      'http://127.0.0.1:8080',
                      'http://localhost:8080',
                      'http://web-nginx.example.com:80'
                      ]
        invalid_urls = ['domain.com',
                        'http://domain',
                        'http://.com',
                        'file:///etc/fstab,'
                        ]
        # test valid urls
        for url in valid_urls:
            self.assertTrue(HttpClient.is_link_ok(url))
        # test invalid urls
        for url in invalid_urls:
            self.assertFalse(HttpClient.is_link_ok(url))


if __name__ == '__main__':
    unittest.main()
