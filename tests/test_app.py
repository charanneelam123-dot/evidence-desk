import unittest
from unittest.mock import patch
from app import Chunk, answer, load_documents, retrieve

class RetrievalTests(unittest.TestCase):
    def setUp(self):
        self.chunks = load_documents('data')
    def test_vacation_retrieval(self):
        self.assertIn('20 days', retrieve('vacation allowance', self.chunks)[0][1].text)
    def test_out_of_domain_abstention(self):
        self.assertEqual(answer('quantum zebras', self.chunks)['sources'], [])
    def test_empty_index(self):
        self.assertEqual(retrieve('hello', []), [])
    def test_tie_order_is_stable(self):
        self.assertEqual(retrieve('hello', [Chunk('b','b','hello'), Chunk('a','a','hello')])[0][1].id, 'a')
    @patch('app.complete', return_value=({'content': '20 days [invented]'}, {}))
    def test_invalid_citation_blocked(self, mock):
        self.assertIn('failed citation', answer('vacation', self.chunks, True)['answer'])
    @patch('app.complete', return_value=({'content': '20 days [handbook.md:1:0]'}, {}))
    def test_valid_citation(self, mock):
        self.assertIn('20 days', answer('vacation', self.chunks, True)['answer'])

if __name__ == '__main__':
    unittest.main()
