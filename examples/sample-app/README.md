# React + three.js example

A small app showing a rotating 3D cube rendered with three.js inside a React component.

## Run

Requires Node.js 18 or newer.

```
cd examples/sample-app
npm install
npm run dev
```

Open the URL printed by Vite (usually http://localhost:5173).

## How three.js connects to React

- `src/three/createScene.js` — plain three.js (scene, camera, lights, mesh, renderer, render loop). It has no React code and returns `{ dispose }`.
- `src/components/ThreeScene.jsx` — React component. A `useEffect` calls `createScene(container)` and returns a cleanup that calls `dispose()`, which cancels the animation frame, removes the resize listener, disposes geometry, material and renderer, and removes the canvas. This keeps React StrictMode (double effect invocation) from leaving duplicate canvases or loops.
- If WebGL is unavailable, the component shows a message instead of crashing.

## Assumptions (unconfirmed)

Direct three.js (not `@react-three/fiber`), JavaScript, Vite, one scene with a simple rotating cube, no user interaction, pixel ratio capped at 2.

## Not verified

Dependencies were not installed and the app was not run in a browser in this session.
