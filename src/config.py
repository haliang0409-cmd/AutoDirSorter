import yaml
from pathlib import Path
from typing import Dict

def load_config(config_path: str = None) -> Dict:
    """加载配置文件"""
    if config_path is None:
        # 使用默认配置文件
        config_path = Path(__file__).parent.parent / 'config' / 'rules.yaml'
    
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f) 