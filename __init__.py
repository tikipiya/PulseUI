"""
PulseUI - Reactライクなコンポーネントとユーティリティファーストスタイリングを備えたモダンなPython GUIライブラリ

特徴:
- Reactライクなコンポーネントアーキテクチャ
- TailwindCSS風ユーティリティクラス
- GPU加速レンダリング（OpenGL/Vulkan）
- 科学的可視化機能
- アニメーションとマルチタッチサポート
- クロスプラットフォーム対応（Windows、macOS、Linux）
"""

from .core.application import Application
from .core.window import Window
from .core.component import Component
from .core.renderer import Renderer
from .components.basic import Button, Text, Input, Container
from .styling.styles import Style, Theme
from .animation.animator import Animator
from .visualization.charts import Chart, LineChart, BarChart

__version__ = "1.0.0"
__author__ = "tikisan"

# Main exports
__all__ = [
    "Application",
    "Window", 
    "Component",
    "Renderer",
    "Button",
    "Text",
    "Input",
    "Container",
    "Style",
    "Theme",
    "Animator",
    "Chart",
    "LineChart",
    "BarChart"
]