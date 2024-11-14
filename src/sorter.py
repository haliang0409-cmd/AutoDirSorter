import os
import shutil
from pathlib import Path
from typing import Dict, List

class FileSorter:
    def __init__(self, config: Dict):
        self.rules = config['rules']
        self.settings = config['settings']
        
    def sort_directory(self, directory: str) -> None:
        """对指定目录进行文件排序"""
        directory = Path(directory)
        if not directory.exists():
            raise ValueError(f"目录不存在: {directory}")
            
        # 获取所有文件
        files = self._get_files(directory)
        
        # 处理每个文件
        for file_path in files:
            self._process_file(file_path)
    
    def _get_files(self, directory: Path) -> List[Path]:
        """获取目录下的所有文件"""
        files = []
        if self.settings.get('recursive', False):
            # 递归遍历
            for root, _, filenames in os.walk(directory):
                for filename in filenames:
                    files.append(Path(root) / filename)
        else:
            # 仅处理当前目录
            files.extend([f for f in directory.iterdir() if f.is_file()])
        return files
    
    def _process_file(self, file_path: Path) -> None:
        """处理单个文件"""
        # 获取文件扩展名
        extension = file_path.suffix.lower()
        
        # 查找匹配的规则
        for rule_name, rule in self.rules.items():
            if extension in rule['extensions']:
                target_dir = file_path.parent / rule['target_dir']
                
                # 创建目标目录
                if self.settings.get('create_dirs', True):
                    target_dir.mkdir(exist_ok=True)
                
                # 移动文件
                try:
                    shutil.move(str(file_path), str(target_dir / file_path.name))
                    print(f"已移动文件 {file_path.name} 到 {target_dir}")
                except Exception as e:
                    print(f"移动文件 {file_path.name} 时出错: {e}") 