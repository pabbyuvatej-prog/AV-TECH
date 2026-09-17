# AV Impacttetur — Interactive Simulation Game

A repository-ready, game-style engineering simulation. The browser version is the primary "wooosh" experience: launch the vehicle, control pitch, watch altitude/velocity/angle, thermal load, shock stand-off, actuator state, and structural deformation update in real time.

## Run

### Easiest
Open `web/index.html` in a modern browser.

### Local server
```bash
python -m http.server 8000 --directory web
```
Then open `http://localhost:8000`.

## Controls
- W / Up: pitch up
- S / Down: pitch down
- A / Left and D / Right: roll input
- Space: boost
- R: reset
- P: pause

The simulation is deliberately a reduced-order interactive model. It is intended for exploration and software integration, not real-world vehicle control or physical certification.

## Repository layout
- `web/` — self-contained playable simulator
- `python/` — lightweight numerical reference model
- `docs/` — equations and model-status notes
- `outputs/` — runtime output location
