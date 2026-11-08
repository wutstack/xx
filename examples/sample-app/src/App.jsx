import ThreeScene from './components/ThreeScene.jsx';

// Placeholder copy: confirm the final wording with the requester.
const TITLE = 'Three.js 3D Example';
const SUBTITLE = 'React + Three.js';

export default function App() {
  return (
    <div style={{ position: 'relative', width: '100%', height: '100%' }}>
      <ThreeScene />
      <div
        style={{
          position: 'absolute',
          top: 16,
          left: 16,
          color: '#fff',
          fontFamily: 'system-ui, sans-serif',
          lineHeight: 1.5,
          pointerEvents: 'none',
        }}
      >
        <h1 style={{ margin: 0, fontSize: 20 }}>{TITLE}</h1>
        <p style={{ margin: 0, fontSize: 14, opacity: 0.8 }}>{SUBTITLE}</p>
      </div>
    </div>
  );
}
