import csv
import datetime as dt
from pathlib import Path

BASE_DIR = Path.cwd()
DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'


class PepParsePipeline:
    def __init__(self):
        self.status_summary = {}
        self.total = 0

    def process_item(self, item, spider):

        status = item.get('status', 'Unknown')
        self.status_summary[status] = self.status_summary.get(status, 0) + 1
        self.total += 1
        return item

    def open_spider(self, spider):
        pass

    def close_spider(self, spider):
        self.create_file_with_status()

    def create_file_with_status(self):

        results = [('Статус', 'Количество')]
        results.extend(tuple(self.status_summary.items()))
        results.append(('Total', self.total))

        results_dir = BASE_DIR / 'results'
        results_dir.mkdir(exist_ok=True)

        now_formatted = dt.datetime.now().strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect='unix')
            writer.writerows(results)
