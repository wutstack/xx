#!/usr/bin/env python3
"""Static checks on the sample app (no Node required)."""

import json
import unittest
from pathlib import Path

APP = Path(__file__).resolve().parent.parent


def read(rel):
    return (APP / rel).read_text(encoding="utf-8")


class ProjectFiles(unittest.TestCase):
    def test_expected_files_exist(self):
        for rel in (
            "package.json",
            "index.html",
            "vite.config.js",
            "README.md",
            ".gitignore",
            "src/main.jsx",
            "src/App.jsx",
            "src/components/ThreeScene.jsx",
            "src/three/createScene.js",
        ):
            with self.subTest(rel=rel):
                self.assertTrue((APP / rel).is_file())

    def test_dependencies_and_scripts(self):
        pkg = json.loads(read("package.json"))
        for dep in ("react", "react-dom", "three"):
            self.assertIn(dep, pkg.get("dependencies", {}))
        self.assertIn("dev", pkg.get("scripts", {}))

    def test_readme_explains_how_to_run(self):
        readme = read("README.md")
        self.assertIn("npm", readme)
        self.assertIn("dev", readme)

    def test_gitignore_excludes_node_modules(self):
        self.assertIn("node_modules", read(".gitignore"))


class Separation(unittest.TestCase):
    def test_three_module_has_no_react(self):
        for line in read("src/three/createScene.js").splitlines():
            if line.lstrip().startswith("import"):
                self.assertNotIn("react", line.lower())

    def test_component_does_not_build_three_objects(self):
        src = read("src/components/ThreeScene.jsx")
        self.assertNotIn("from 'three'", src)
        self.assertNotIn("new THREE.", src)
        self.assertIn("createScene", src)


class Scene(unittest.TestCase):
    def test_scene_has_camera_light_and_mesh(self):
        src = read("src/three/createScene.js")
        for token in ("PerspectiveCamera", "Light", "Mesh", "WebGLRenderer"):
            self.assertIn(token, src)


class Cleanup(unittest.TestCase):
    def test_dispose_releases_resources(self):
        src = read("src/three/createScene.js")
        for token in (
            "cancelAnimationFrame",
            "geometry.dispose()",
            "material.dispose()",
            "renderer.dispose()",
            "removeChild",
            "removeEventListener",
        ):
            with self.subTest(token=token):
                self.assertIn(token, src)

    def test_component_disposes_in_effect_cleanup(self):
        src = read("src/components/ThreeScene.jsx")
        self.assertIn("useEffect", src)
        self.assertIn("handle.dispose()", src)

    def test_webgl_failure_is_handled(self):
        src = read("src/components/ThreeScene.jsx")
        self.assertIn("catch", src)


if __name__ == "__main__":
    unittest.main()
