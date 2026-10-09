"""Validate this collection's string-only metadata, paths, and Day mapping."""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

def scalar(value):
    if value.startswith('"'):
        result = json.loads(value)
        if not isinstance(result, str):
            raise ValueError('Metadata value must be a string')
        return result
    if not value or any(c in value for c in '{}[]') or ': ' in value:
        raise ValueError('Unsupported YAML scalar; use a quoted string')
    return value

def main():
    errors = []
    skill_files = sorted((ROOT/'skills').glob('*/SKILL.md'))
    if not skill_files:
        errors.append('No skills found')
    for path in skill_files:
        try:
            text = path.read_text(encoding='utf-8')
            match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
            if not match:
                raise ValueError('Missing frontmatter')
            fields = {}
            for line in match.group(1).splitlines():
                key, value = line.split(': ', 1)
                if key in fields:
                    raise ValueError('Duplicate frontmatter key')
                fields[key] = scalar(value)
            if set(fields) != {'name','description'}:
                raise ValueError('Expected name and description')
            name = fields['name']
            if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*',name) or len(name)>64 or name!=path.parent.name:
                raise ValueError('Invalid skill name or folder mismatch')
            if not 0<len(fields['description'])<=1024 or any(c in fields['description'] for c in '<>'):
                raise ValueError('Invalid description')
            if re.search(r'\[TODO:',text):
                raise ValueError('Unfinished scaffold')
            ui_path = path.parent/'agents'/'openai.yaml'
            lines = ui_path.read_text(encoding='utf-8').splitlines()
            if lines[0]!='interface:':
                raise ValueError('Missing interface metadata')
            ui = {}
            for line in lines[1:]:
                if not line.startswith('  '):
                    raise ValueError('Invalid UI indentation')
                key,value = line.strip().split(': ',1)
                if key in ui:
                    raise ValueError('Duplicate interface field')
                ui[key]=scalar(value)
            if set(ui)!={'display_name','short_description','default_prompt'}:
                raise ValueError('Unexpected interface fields')
            if not 25<=len(ui['short_description'])<=64 or '$'+name not in ui['default_prompt']:
                raise ValueError('Invalid UI length or invocation')
        except (ValueError,KeyError,IndexError,OSError) as exc:
            errors.append(f'{path.relative_to(ROOT)}: {exc}')

    markdown = list((ROOT/'days').glob('*/TASK.md')) + list((ROOT/'docs').glob('*.md')) + list((ROOT/'skills').rglob('*.md')) + [ROOT/'README.md']
    for path in markdown:
        text=path.read_text(encoding='utf-8')
        for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)',text):
            if target.startswith(('https://','http://','#')):
                continue
            if not (path.parent/target.split('#',1)[0]).exists():
                errors.append(f'{path.relative_to(ROOT)}: missing link {target}')
    day_paths=sorted((ROOT/'days').glob('Day*/TASK.md'))
    numbers=[int(re.match(r'Day(\d+)-',p.parent.name).group(1)) for p in day_paths]
    if numbers!=list(range(1,31)):
        errors.append('Expected exactly Day01 through Day30')
    for path in day_paths:
        text=path.read_text(encoding='utf-8')
        for section in ['## AI 主动完成','## 用户负责决定','## 今天的产出','## 启动提示词']:
            if section not in text:
                errors.append(f'{path.relative_to(ROOT)}: missing {section}')
    if errors:
        print('\n'.join(errors))
        return 1
    print(f'Checked {len(skill_files)} skills, {len(day_paths)} Day tasks and local references.')
    print('Format checks only; market conclusions and agent behavior are not verified by this script.')
    return 0

if __name__ == '__main__':
    sys.exit(main())
