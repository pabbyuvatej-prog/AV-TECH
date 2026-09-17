from pathlib import Path
import webbrowser
p=(Path(__file__).parent/'web'/'index.html').resolve()
webbrowser.open(p.as_uri())
print('Opened AV Impacttetur Simulation Game:', p)
