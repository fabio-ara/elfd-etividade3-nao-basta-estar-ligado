"""Confere os bytes do website público com a versão guardada no Git."""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from hashlib import sha256
import json
from pathlib import Path
import subprocess
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://fabio-ara.github.io/elfd-etividade3-nao-basta-estar-ligado/'


def git(*args):
    return subprocess.check_output(['git', *args], cwd=ROOT)


def check(path):
    expected = git('show', 'HEAD:' + path)
    relative = path.removeprefix('website/')
    request = Request(BASE + relative, headers={'Cache-Control': 'no-cache'})
    with urlopen(request, timeout=25) as response:
        actual = response.read()
        status = response.status
        resolved = response.url
    assert status == 200, (relative, status)
    assert actual == expected, f'Conteúdo público diferente: {relative}'
    return {'path': relative, 'status': status, 'url': resolved,
            'bytes': len(actual), 'sha256': sha256(actual).hexdigest(),
            'same_git_bytes': True}


if __name__ == '__main__':
    paths = [path for path in git('ls-tree', '-r', '--name-only', 'HEAD', 'website').decode().splitlines()
             if not any(part.startswith('.') for part in Path(path).parts)]
    with ThreadPoolExecutor(max_workers=6) as pool:
        files = list(pool.map(check, paths))
    report = {'checked_at': datetime.now(timezone.utc).isoformat(),
              'base': BASE, 'commit': git('rev-parse', 'HEAD').decode().strip(),
              'files_checked': len(files), 'authentication': 'sem credenciais',
              'comparison': 'bytes públicos iguais aos ficheiros website no Git',
              'excluded': ['.nojekyll: controlo da publicação, não é um recurso utilizado pelas páginas'],
              'files': files}
    (ROOT / 'validacao/publicacao-revisada-http.json').write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f'{len(files)} ficheiros públicos: HTTP 200 e bytes confirmados.')
