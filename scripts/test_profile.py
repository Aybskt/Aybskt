from datetime import date, timedelta
import unittest
import xml.etree.ElementTree as ET
from update_profile import CalendarParser, render


class CalendarTests(unittest.TestCase):
    def fixture(self):
        return ''.join(
            f'<td id="d{i}" data-date="{date(2025, 1, 1)+timedelta(days=i)}" data-level="{1 if i == 0 else 0}"></td>'
            f'<tool-tip for="d{i}">{"1,234 contributions" if i == 0 else "No contributions"} on date.</tool-tip>'
            for i in range(365))

    def test_counts_and_svg(self):
        parser = CalendarParser()
        parser.feed(self.fixture())
        days = parser.days()
        self.assertEqual(sum(d['count'] for d in days), 1234)
        root = ET.fromstring(render(days))
        self.assertEqual(len(root.findall('.//{*}rect[@class="day"]')), 365)

    def test_changed_markup_fails_without_fake_data(self):
        parser = CalendarParser()
        parser.feed(self.fixture().replace('No contributions', 'Unknown'))
        with self.assertRaises(ValueError):
            parser.days()

    def test_incomplete_response_fails(self):
        parser = CalendarParser()
        parser.feed('<html>Rate limited</html>')
        with self.assertRaises(ValueError):
            parser.days()


if __name__ == '__main__':
    unittest.main()
