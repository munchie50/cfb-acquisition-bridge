"""Extract the CBS odds table schema for the isolated Actions rehearsal."""
import html
import re
from urllib.parse import urljoin

from cfb_cbs_full_board_normalizer import WEEK11_URL


def text(markup):
    return ' '.join(html.unescape(re.sub(r'<[^>]*>', ' ', markup)).split())


def extract(document):
    output = []
    for table in re.findall(r'<table\b[^>]*\bdata-game-abbrev=[^>]*>.*?</table>', document, re.S):
        rows = [re.findall(r'<t[dh]\b[^>]*>.*?</t[dh]>', row, re.S)
                for row in re.findall(r'<tr\b[^>]*>.*?</tr>', table, re.S)
                if not row.startswith('<tr class="OddsBlock-linksRow">')]
        if len(rows) != 3 or any(len(row) != 6 for row in rows):
            raise ValueError('unexpected CBS table shape')
        header = rows[0]
        if [text(cell) for cell in header[1:]] != ['Final', 'Open', 'Spread', 'ML Moneyline', 'Total']:
            raise ValueError('unexpected CBS column labels')
        kickoff, = re.findall(r'<span\b[^>]*OddsBlock-timeText--desktop[^>]*>(.*?)</span>', header[0], re.S)
        output.append([text(kickoff), 'Final', 'Open', 'Spread', 'MLMoneyline', 'Total'])
        for team, _final, _opening, *markets in rows[1:]:
            long_name, = re.findall(r'<span\b[^>]*OddsBlock-teamText--long[^>]*>(.*?)</span>', team, re.S)
            link, = re.findall(r'<a\b[^>]*href="(/college-football/teams/[^"]+)"[^>]*>', long_name, re.S)
            cells = [f'[{text(long_name)}]({urljoin(WEEK11_URL, link)})', '', '']
            for market in markets:
                value = text(market)
                icons = re.findall(r'https://sports\.cbsimg\.net/[^"\s]*/books-icons/\d+\.svg', market)
                cells.append(value + ''.join(f' ![book logo]({icon})' for icon in icons))
            output.append(cells)
    if not output or any('|' in cell or '\n' in cell for row in output for cell in row):
        raise ValueError('CBS capture cannot be represented as odds tables')
    return ''.join('| ' + ' | '.join(row) + ' |\n' for row in output)
