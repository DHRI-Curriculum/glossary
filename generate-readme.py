from pathlib import Path

file_list = [x for x in Path('terms').glob('*.md')]
file_list.sort(key=lambda v: v.name.upper())

README = '# Digital Humanities Research Institute Glossary\n\n'

README += 'This glossary contains definitions and explanations of core concepts introduced in the early sections of the Digital Humanities Research Institute. To see the live glossary, go to https://curriculum.dhinstitutes.org/glossary/\n\n'

for file in file_list:
    lines = (x for x in file.read_text().splitlines() if x)
    line = ''
    while not line.startswith('#'):
        try:
            line = next(lines)
            header = line.replace('#', '')
            header = header.strip()
        except StopIteration:
            raise RuntimeError(f'Could not find term in file {file}. Verify the contents of it first.')

    README += f'- [{header}]({file})\n'

README += '\n\n-----\n\n[![Creative Commons License](https://i.creativecommons.org/l/by-sa/4.0/88x31.png)](http://creativecommons.org/licenses/by-sa/4.0/)\n\n[Digital Research Institute (DRI) Curriculum](http://purl.org/dc/terms/) by [Graduate Center Digital Initiatives](https://gcdi.commons.gc.cuny.edu/) is licensed under a [Creative Commons Attribution-ShareAlike 4.0 International License](http://creativecommons.org/licenses/by-sa/4.0/). Based on a work at <https://github.com/DHRI-Curriculum>. When sharing this material or derivative works, preserve this paragraph, changing only the title of the derivative work, or provide comparable attribution.\n'

Path('README.md').write_text(README)