"""Validate the distributable package using Python's standard library."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'ai-career-copilot'


def validate(root=ROOT, skill=SKILL):
    required = [root/'README.md', root/'LICENSE', skill/'SKILL.md',
                skill/'agents/openai.yaml', skill/'references/evidence.md',
                skill/'references/workflows.md', skill/'templates/profile.example.json']
    for path in required:
        if not path.is_file():
            raise ValueError(f'Missing required file: {path.relative_to(root)}')
    content = (skill/'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'^---\n(.*?)\n---\n', content, re.S)
    if not front:
        raise ValueError('Invalid frontmatter delimiters')
    if not re.search(r'^name: ai-career-copilot$', front[1], re.M):
        raise ValueError('Skill name must match its directory')
    if not re.search(r'^description: .+', front[1], re.M):
        raise ValueError('Missing description')
    metadata = (skill/'agents/openai.yaml').read_text(encoding='utf-8')
    if '$ai-career-copilot' not in metadata:
        raise ValueError('Invocation metadata must name the skill')
    for path in root.rglob('*'):
        if '.git' in path.relative_to(root).parts or '__pycache__' in path.parts:
            continue
        if path.is_file() and path.suffix.lower() in {'.pdf', '.docx', '.jpg', '.jpeg', '.png'}:
            raise ValueError(f'Unexpected personal/document asset: {path.relative_to(root)}')
        if path.is_file() and path.suffix in {'.md', '.yaml', '.json', '.py', '.yml'}:
            text = path.read_text(encoding='utf-8')
            if '\ufffd' in text or (path.suffix != '.py' and '[TODO:' in text):
                raise ValueError(f'Invalid text or unfinished scaffold: {path.relative_to(root)}')
            if path.suffix == '.md':
                for target in re.findall(r'\]\(([^)]+)\)', text):
                    if '://' not in target and not target.startswith('#'):
                        resolved = (path.parent/target.split('#')[0]).resolve()
                        if not resolved.is_relative_to(root.resolve()) or not resolved.exists():
                            raise ValueError(f'Broken or external local link in {path.relative_to(root)}')
    profile = json.loads((skill/'templates/profile.example.json').read_text(encoding='utf-8'))
    for key in ['education', 'experience', 'projects', 'private_source_paths']:
        if profile.get(key) != []:
            raise ValueError(f'Public profile template must leave {key} empty')
    if profile.get('updated_at') is not None:
        raise ValueError('Public template must not assert a profile update date')
    return 'OK: package metadata, links, UTF-8, empty profile, and asset exclusions'


if __name__ == '__main__':
    print(validate())
