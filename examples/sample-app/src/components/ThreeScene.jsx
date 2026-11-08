import { useEffect, useRef, useState } from 'react';
import { createScene } from '../three/createScene.js';

// React side only: owns the container, calls createScene, and disposes on cleanup.
export default function ThreeScene() {
  const containerRef = useRef(null);
  const [error, setError] = useState(null);

  useEffect(() => {
    let handle;
    try {
      handle = createScene(containerRef.current);
    } catch (e) {
      setError('WebGL is not available in this browser.');
      return undefined;
    }
    // Cleanup also runs between StrictMode's double-invoked effects,
    // so no duplicate canvas or render loop is left behind.
    return () => handle.dispose();
  }, []);

  if (error) {
    return <p style={{ padding: 16 }}>{error}</p>;
  }
  return <div ref={containerRef} style={{ width: '100%', height: '100%' }} />;
}
