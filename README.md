# 01---TESTRUN

Simple drag-a-point test app with both a browser canvas version and a Tkinter
desktop fallback, used to confirm local UI input and basic hosting work.

## Features
- 1500x1500 canvas with click-to-add points and a polyline
- Simple local Node.js static server
- Tkinter desktop version for quick testing
 - Clear button to remove all points and lines

## Getting started
1. Open a terminal in this folder: `C:\AI\01 - TestRun`
2. Install Node.js (if not already installed)
3. Run the server:
   - `npm start`
4. Open `http://localhost:3000` in a browser

## Controls
- Left click to add points
- Clear button removes all points and lines

## GitHub Pages
1. Go to the repo Settings → Pages
2. Set Source to "GitHub Actions"
3. Push to `main` and wait for the "Deploy to GitHub Pages" workflow
4. Your site will be live at `https://mppxrb.github.io/01---TESTRUN/`
